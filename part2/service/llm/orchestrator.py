from langgraph.graph.message import add_messages
from service.llm.StartNode import start_node
from service.llm.chat import Chat
from service.llm.Mapping import MappingNode
from service.llm.total_explain import TotalExplain
from service.llm.is_normal import IsNormal

from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Any, Dict, List

class GraphState(TypedDict):
    query : str
    execution_plan: List[Dict[str, Any]]
    step: int
    results: Dict[str, Any]
    specific_list : Dict[str, Any]


class AIGraph:
    def __init__(self, llm):
        self.start = start_node(llm)
        self.chat = Chat(llm)
        self.mapping = MappingNode(llm)
        self.explain = TotalExplain(llm)
        self.normal = IsNormal(llm)
        self.tasks = {
                    "chat_node" : self._run_chat,
                    "mapping_node" : self._run_mapping,
                    "total_explain_node" : self._run_total_explain,
                    "is_normal_node" : self._run_is_normal
                }
        self.graph = self._build_graph()
        
        
    async def _start(self, state : GraphState):
        result = await self.start.generate(state['query'])
        plan = result["execution_plan"]
        
        for item in plan:
            if item["node"] not in self.tasks:
                raise ValueError(f"등록되지 않은 노드입니다. : {item["node"]}")
        
        return {
            "execution_plan" : plan,
            "step" : 0,
            "results" : []
        }
        
    def _route(self, state : GraphState):
        step = state["step"]
        plan = state["execution_plan"]
        
        if step >= len(plan):
            return END
        
        return plan[step]["node"]
    
    async def _run_is_normal(self, state : GraphState):
        result = await self.normal.generate(state["specific_list"], state["query"])
        return self._save_result(state, "is_normal_node", result)
    
    async def _run_mapping(self, state : GraphState):
        result = await self.mapping.generate(state["query"])
        saving = self._save_result(state, "mapping_node", result)
        saving["specific_list"] = result
        return saving
    
    async def _run_total_explain(self, state : GraphState):
        result = await self.explain.generate(state["query"])
        return self._save_result(state, "total_explain_node", result)
    
    async def _run_chat(self, state : GraphState):
        result = await self.chat.generate(state["query"])
        return self._save_result(state, "chat_node", result)
    
    def _save_result(self, state, node_name : str, result):
        return {
            "results" : [
                *state["results"],
                {"node" : node_name, "result" : result}
            ],
            "step" : state["step"] + 1
        }
        
    def _build_graph(self):
        builder = StateGraph(GraphState)
        
        builder.add_node("start", self._start)
        
        
        for node_name, func in self.tasks.items():
            builder.add_node(node_name, func)
        
        destinations = {node_name : node_name for node_name in self.tasks}
        
        destinations[END] = END
        
        builder.add_edge(START, "start")
        
        builder.add_conditional_edges("start", self._route, destinations)
        
        for node_name in self.tasks:
            builder.add_conditional_edges(node_name, self._route, destinations)
        
        return builder.compile()
    
    async def generate(self, query : str, specific_list : Dict[str, Any] | None = None):
        initial_state : GraphState = {
            "query" : query,
            "execution_plan" : [],
            "step" : 0,
            "results" : {},
            "specific_list" : specific_list if specific_list is not None else {} 
        }
        
        final_state = await self.graph.ainvoke(initial_state)
        
        return final_state["results"]