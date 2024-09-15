import pandas as pd
from typing import Dict, Any

def check_column_limit(df: pd.DataFrame, params: Dict[str, Any]) -> Dict[str, Any]:
    column_count = df.shape[1]
    warning_message = ""

    if column_count == 255:
        warning_message = (
            "Warning: The dataset contains exactly 255 columns. "
            "This might indicate that the file was opened or converted using Apple's Numbers app, "
            "which truncates files with more than 255 columns without warning."
        )
    
    return {
        "column_count": column_count,
        "warning_message": warning_message
    }
