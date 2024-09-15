import pandas as pd

def identify_duplicate_rows(df: pd.DataFrame, params: dict) -> dict:
    columns_to_check = params.get('columns', df.columns.tolist())
    duplicate_rows = df[df.duplicated(subset=columns_to_check, keep=False)]
    return {
        "total_duplicates": len(duplicate_rows),
        "duplicate_rows": duplicate_rows.to_dict(orient='records')
    }
