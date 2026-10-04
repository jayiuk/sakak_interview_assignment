import pytest

from service.preprocessing.DataPreprocessing import only_overview, get_data_part, only_unit, only_normal_A, only_normal_B, only_suspected, only_result_list, get_name, get_specific_result

expected_overview = {
        "checkupDate": "2025-08-15",
        "height": "175",
        "weight": "72",
        "waists": "85",
        "BMI": "23.5",
        "vision": "1.0/0.8",
        "hearing": "정상/정상",
        "bloodPressure": "125/82",
        "proteinuria": "음성",
        "hemoglobin": "15.0",
        "fastingBloodGlucose": "95",
        "totalCholesterol": "190",
        "HDLCholesterol": "60",
        "triglyceride": "120",
        "LDLCholesterol": "115",
        "serumCreatinine": "1.2",
        "GFR": "90",
        "AST": "30",
        "ALT": "28",
        "yGPT": "25",
        "chestXrayResult": "정상, 비활동성",
        "osteoporosis": "T-score -0.8",
        "evaluation": "전체적으로 정상 범위 내 건강 상태입니다."
      }

original = {
  "status": "success",
  "data": {
    "patientName": "홍길동",
    "overviewList": [
      {
        "checkupDate": "2025-08-15",
        "height": "175",
        "weight": "72",
        "waists": "85",
        "BMI": "23.5",
        "vision": "1.0/0.8",
        "hearing": "정상/정상",
        "bloodPressure": "125/82",
        "proteinuria": "음성",
        "hemoglobin": "15.0",
        "fastingBloodGlucose": "95",
        "totalCholesterol": "190",
        "HDLCholesterol": "60",
        "triglyceride": "120",
        "LDLCholesterol": "115",
        "serumCreatinine": "1.2",
        "GFR": "90",
        "AST": "30",
        "ALT": "28",
        "yGPT": "25",
        "chestXrayResult": "정상, 비활동성",
        "osteoporosis": "T-score -0.8",
        "evaluation": "전체적으로 정상 범위 내 건강 상태입니다."
      }
    ],
    "referenceList": [
      {
        "refType": "단위",
        "height": "Cm",
        "weight": "Kg",
        "waists": "Cm",
        "BMI": "kg/m2",
        "vision": "",
        "hearing": "",
        "bloodPressure": "mmHg",
        "proteinuria": "",
        "hemoglobin": "g/dL",
        "fastingBloodGlucose": "mg/dL",
        "totalCholesterol": "mg/dL",
        "HDLCholesterol": "mg/dL",
        "triglyceride": "mg/dL",
        "LDLCholesterol": "mg/dL",
        "serumCreatinine": "mg/dL",
        "GFR": "mL/min",
        "AST": "U/L",
        "ALT": "U/L",
        "yGPT": "U/L",
        "chestXrayResult": "",
        "osteoporosis": ""
      },
      {
        "refType": "정상(A)",
        "height": "",
        "weight": "",
        "waists": "",
        "BMI": "18.5-24.9",
        "vision": "",
        "hearing": "",
        "bloodPressure": "120미만 이며/80미만",
        "proteinuria": "음성",
        "hemoglobin": "남: 13-16.5 / 여: 12-15.5",
        "fastingBloodGlucose": "100미만",
        "totalCholesterol": "200미만",
        "HDLCholesterol": "60이상",
        "triglyceride": "150미만",
        "LDLCholesterol": "130미만",
        "serumCreatinine": "1.6이하",
        "GFR": "60이상",
        "AST": "40이하",
        "ALT": "35이하",
        "yGPT": "남:11-63 / 여:8-35",
        "chestXrayResult": "정상, 비활동성",
        "osteoporosis": "T-score -1 이상"
      },
      {
        "refType": "정상(B)",
        "BMI": "18.5미만/25~29.9",
        "bloodPressure": "120-139 또는 /80-89",
        "proteinuria": "약양성±",
        "hemoglobin": "남: 12-12.9 / 여: 10-11.9",
        "fastingBloodGlucose": "100-125",
        "totalCholesterol": "200-239",
        "HDLCholesterol": "40-59",
        "triglyceride": "150-199",
        "LDLCholesterol": "130-139",
        "serumCreatinine": "",
        "GFR": "",
        "AST": "41-50",
        "ALT": "36-45",
        "yGPT": "남:64-77 / 여:36-45",
        "osteoporosis": "-1~-2.5 초과"
      },
      {
        "refType": "질환의심",
        "waists": "남 90이상 / 여 85이상",
        "BMI": "30이상",
        "bloodPressure": "140이상 또는 /90이상",
        "proteinuria": "양성(+1)이상",
        "hemoglobin": "남:12.0미만 / 여:10.0미만",
        "fastingBloodGlucose": "126이상",
        "totalCholesterol": "240이상",
        "HDLCholesterol": "40미만",
        "triglyceride": "200이상",
        "LDLCholesterol": "160이상",
        "serumCreatinine": "1.6초과",
        "GFR": "60미만",
        "AST": "51이상",
        "ALT": "46이상",
        "yGPT": "남:78이상 / 여:46이상",
        "chestXrayResult": "정상 및 비활동성이외의자",
        "osteoporosis": "-2.5이하"
      }
    ],
    "resultList": [
      {
        "caseType": "0",
        "checkupType": "일반",
        "checkupDate": "2025-08-15",
        "organizationName": "서울병원",
        "pdfData": "example.pdf",
        "questionnaire": []
      }
    ]
  }
}

expected_unit = {
        "refType": "단위",
        "height": "Cm",
        "weight": "Kg",
        "waists": "Cm",
        "BMI": "kg/m2",
        "vision": "",
        "hearing": "",
        "bloodPressure": "mmHg",
        "proteinuria": "",
        "hemoglobin": "g/dL",
        "fastingBloodGlucose": "mg/dL",
        "totalCholesterol": "mg/dL",
        "HDLCholesterol": "mg/dL",
        "triglyceride": "mg/dL",
        "LDLCholesterol": "mg/dL",
        "serumCreatinine": "mg/dL",
        "GFR": "mL/min",
        "AST": "U/L",
        "ALT": "U/L",
        "yGPT": "U/L",
        "chestXrayResult": "",
        "osteoporosis": ""
      }

expected_data = {
    "patientName": "홍길동",
    "overviewList": [
      {
        "checkupDate": "2025-08-15",
        "height": "175",
        "weight": "72",
        "waists": "85",
        "BMI": "23.5",
        "vision": "1.0/0.8",
        "hearing": "정상/정상",
        "bloodPressure": "125/82",
        "proteinuria": "음성",
        "hemoglobin": "15.0",
        "fastingBloodGlucose": "95",
        "totalCholesterol": "190",
        "HDLCholesterol": "60",
        "triglyceride": "120",
        "LDLCholesterol": "115",
        "serumCreatinine": "1.2",
        "GFR": "90",
        "AST": "30",
        "ALT": "28",
        "yGPT": "25",
        "chestXrayResult": "정상, 비활동성",
        "osteoporosis": "T-score -0.8",
        "evaluation": "전체적으로 정상 범위 내 건강 상태입니다."
      }
    ],
    "referenceList": [
      {
        "refType": "단위",
        "height": "Cm",
        "weight": "Kg",
        "waists": "Cm",
        "BMI": "kg/m2",
        "vision": "",
        "hearing": "",
        "bloodPressure": "mmHg",
        "proteinuria": "",
        "hemoglobin": "g/dL",
        "fastingBloodGlucose": "mg/dL",
        "totalCholesterol": "mg/dL",
        "HDLCholesterol": "mg/dL",
        "triglyceride": "mg/dL",
        "LDLCholesterol": "mg/dL",
        "serumCreatinine": "mg/dL",
        "GFR": "mL/min",
        "AST": "U/L",
        "ALT": "U/L",
        "yGPT": "U/L",
        "chestXrayResult": "",
        "osteoporosis": ""
      },
      {
        "refType": "정상(A)",
        "height": "",
        "weight": "",
        "waists": "",
        "BMI": "18.5-24.9",
        "vision": "",
        "hearing": "",
        "bloodPressure": "120미만 이며/80미만",
        "proteinuria": "음성",
        "hemoglobin": "남: 13-16.5 / 여: 12-15.5",
        "fastingBloodGlucose": "100미만",
        "totalCholesterol": "200미만",
        "HDLCholesterol": "60이상",
        "triglyceride": "150미만",
        "LDLCholesterol": "130미만",
        "serumCreatinine": "1.6이하",
        "GFR": "60이상",
        "AST": "40이하",
        "ALT": "35이하",
        "yGPT": "남:11-63 / 여:8-35",
        "chestXrayResult": "정상, 비활동성",
        "osteoporosis": "T-score -1 이상"
      },
      {
        "refType": "정상(B)",
        "BMI": "18.5미만/25~29.9",
        "bloodPressure": "120-139 또는 /80-89",
        "proteinuria": "약양성±",
        "hemoglobin": "남: 12-12.9 / 여: 10-11.9",
        "fastingBloodGlucose": "100-125",
        "totalCholesterol": "200-239",
        "HDLCholesterol": "40-59",
        "triglyceride": "150-199",
        "LDLCholesterol": "130-139",
        "serumCreatinine": "",
        "GFR": "",
        "AST": "41-50",
        "ALT": "36-45",
        "yGPT": "남:64-77 / 여:36-45",
        "osteoporosis": "-1~-2.5 초과"
      },
      {
        "refType": "질환의심",
        "waists": "남 90이상 / 여 85이상",
        "BMI": "30이상",
        "bloodPressure": "140이상 또는 /90이상",
        "proteinuria": "양성(+1)이상",
        "hemoglobin": "남:12.0미만 / 여:10.0미만",
        "fastingBloodGlucose": "126이상",
        "totalCholesterol": "240이상",
        "HDLCholesterol": "40미만",
        "triglyceride": "200이상",
        "LDLCholesterol": "160이상",
        "serumCreatinine": "1.6초과",
        "GFR": "60미만",
        "AST": "51이상",
        "ALT": "46이상",
        "yGPT": "남:78이상 / 여:46이상",
        "chestXrayResult": "정상 및 비활동성이외의자",
        "osteoporosis": "-2.5이하"
      }
    ],
    "resultList": [
      {
        "caseType": "0",
        "checkupType": "일반",
        "checkupDate": "2025-08-15",
        "organizationName": "서울병원",
        "pdfData": "example.pdf",
        "questionnaire": []
      }
    ]
  }

expected_normal_a = {
        "refType": "정상(A)",
        "height": "",
        "weight": "",
        "waists": "",
        "BMI": "18.5-24.9",
        "vision": "",
        "hearing": "",
        "bloodPressure": "120미만 이며/80미만",
        "proteinuria": "음성",
        "hemoglobin": "남: 13-16.5 / 여: 12-15.5",
        "fastingBloodGlucose": "100미만",
        "totalCholesterol": "200미만",
        "HDLCholesterol": "60이상",
        "triglyceride": "150미만",
        "LDLCholesterol": "130미만",
        "serumCreatinine": "1.6이하",
        "GFR": "60이상",
        "AST": "40이하",
        "ALT": "35이하",
        "yGPT": "남:11-63 / 여:8-35",
        "chestXrayResult": "정상, 비활동성",
        "osteoporosis": "T-score -1 이상"
      }

expected_normal_b = {
        "refType": "정상(B)",
        "BMI": "18.5미만/25~29.9",
        "bloodPressure": "120-139 또는 /80-89",
        "proteinuria": "약양성±",
        "hemoglobin": "남: 12-12.9 / 여: 10-11.9",
        "fastingBloodGlucose": "100-125",
        "totalCholesterol": "200-239",
        "HDLCholesterol": "40-59",
        "triglyceride": "150-199",
        "LDLCholesterol": "130-139",
        "serumCreatinine": "",
        "GFR": "",
        "AST": "41-50",
        "ALT": "36-45",
        "yGPT": "남:64-77 / 여:36-45",
        "osteoporosis": "-1~-2.5 초과"
      }

suspected = {
        "refType": "질환의심",
        "waists": "남 90이상 / 여 85이상",
        "BMI": "30이상",
        "bloodPressure": "140이상 또는 /90이상",
        "proteinuria": "양성(+1)이상",
        "hemoglobin": "남:12.0미만 / 여:10.0미만",
        "fastingBloodGlucose": "126이상",
        "totalCholesterol": "240이상",
        "HDLCholesterol": "40미만",
        "triglyceride": "200이상",
        "LDLCholesterol": "160이상",
        "serumCreatinine": "1.6초과",
        "GFR": "60미만",
        "AST": "51이상",
        "ALT": "46이상",
        "yGPT": "남:78이상 / 여:46이상",
        "chestXrayResult": "정상 및 비활동성이외의자",
        "osteoporosis": "-2.5이하"
      }

result_part = {
        "caseType": "0",
        "checkupType": "일반",
        "checkupDate": "2025-08-15",
        "organizationName": "서울병원",
        "pdfData": "example.pdf",
        "questionnaire": []
      }

mapping_input = ["AST", "ALT", "yGPT"]
mapping_expected = {
  "AST" : 30,
  "ALT" : 28,
  "yGPT" : 25
}

patient_name = "홍길동"

@pytest.mark.parametrize("before, after", [(original, expected_data)])
def test_get_data(before, after):
    assert get_data_part(before) == after

@pytest.mark.parametrize("before, after", [(original, expected_overview)])
def test_get_overview(before, after):
    assert only_overview(before) == after
    
@pytest.mark.parametrize("before, after", [(original, expected_unit)])
def test_get_unit(before, after):
    assert only_unit(before) == after

@pytest.mark.parametrize("before, after", [(original, expected_normal_a)])
def test_get_normal_a(before, after):
    assert only_normal_A(before) == after
    
def test_get_normal_b():
    assert only_normal_B(original) == expected_normal_b
    
def test_get_suspected():
    assert only_suspected(original) == suspected

def test_get_result_list():
    assert only_result_list(original) == result_part

def test_get_name():
    assert get_name(original) == patient_name
    
def test_get_specific_result():
  assert get_specific_result(original, mapping_input) == mapping_expected