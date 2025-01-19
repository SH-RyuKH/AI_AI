import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_data(data):
    # 간단한 분석 예시
    return data.describe()
