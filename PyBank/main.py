
import pandas as pd
from pathlib import Path

budget_file = Path("PyBank","Resources", "budget_data.csv")


months = budget_df["Date"].unique()
months_count=len(months)
total = budget_df["Profit/Losses"].sum()
print(total)