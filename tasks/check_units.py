import pandas as pd
from typing import Dict, Any

def check_units(df: pd.DataFrame, params: Dict[str, Any]) -> Dict[str, Any]:
    columns_to_check = params.get('columns', df.columns.tolist())
    unit_info = params.get('unit_info', {})
    
    missing_units = {}
    
    for column in columns_to_check:
        if column in df.columns:
            if column not in unit_info or not unit_info[column]:
                missing_units[column] = "Unit information is missing"
            else:
                missing_units[column] = f"Unit specified: {unit_info[column]}"
        else:
            missing_units[column] = "Column not found in dataset"
    
    return {
        "missing_units": missing_units
    }
