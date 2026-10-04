from pydantic import BaseModel, ConfigDict
from typing import Any, Literal

class SchemaBase(BaseModel):
    model_config = ConfigDict(extra="forbid")


class OverviewResponse(SchemaBase):
    checkupDate : str
    height : str
    weight : str
    waists : str
    BMI : str
    vision : str
    hearing : str
    bloodPressure : str
    proteinuria : str
    hemoglobin : str
    fastingBloodGlucose : str
    totalCholesterol : str
    HDLCholesterol : str
    triglyceride : str
    LDLCholesterol : str
    serumCreatinine : str
    GFR : str
    AST : str
    ALT : str
    yGPT : str
    chestXrayResult : str
    osteoporosis : str
    evaluation : str


class ReferenceResponse(SchemaBase):
    refType : Literal["단위", "정상(A)", "정상(B)", "질환의심"]
    height : str = ""
    weight : str = ""
    waists : str = ""
    BMI : str = ""
    vision : str = ""
    hearing : str = ""
    bloodPressure : str = ""
    proteinuria : str = ""
    hemoglobin : str = ""
    fastingBloodGlucose : str = ""
    totalCholesterol : str = ""
    HDLCholesterol : str = ""
    triglyceride : str = ""
    LDLCholesterol : str = ""
    serumCreatinine : str = ""
    GFR : str = ""
    AST : str = ""
    ALT : str = ""
    yGPT : str = ""
    chestXrayResult : str = ""
    osteoporosis : str = ""


class ResultResponse(SchemaBase):
    caseType : str
    checkupType : str
    checkupDate : str
    organizationName : str
    pdfData : str
    questionnaire : list[Any]


class DataResponse(SchemaBase):
    patientName : str
    overviewList : list[OverviewResponse]
    referenceList : list[ReferenceResponse]
    resultList : list[ResultResponse]


class MockAPIResponse(SchemaBase):
    status : Literal["success"]
    data : DataResponse