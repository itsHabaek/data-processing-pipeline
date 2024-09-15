import pandas as pd

def identify_missing_values(df: pd.DataFrame, params: dict) -> dict:
    columns_to_check = params.get('columns', [])
    thresholds = params.get('thresholds', {})
    report = {}
    for column in columns_to_check:
        if column in df.columns:
            missing_percentage = df[column].isna().mean() * 100
            threshold = thresholds.get(column, 0)
            if missing_percentage > threshold:
                report[column] = {
                    "missing_percentage": missing_percentage,
                    "status": "Exceeds threshold"
                }
            else:
                report[column] = {
                    "missing_percentage": missing_percentage,
                    "status": "Within threshold"
                }
        else:
            report[column] = "Column not found in dataset"
    return report
