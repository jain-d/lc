# Employees earning more than their Managers
import pandas as pd

def find_employees(employee_table: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee_table, employee_table.loc[:, ["id", "salary"]], left_on="managerId", right_on="id")
    return merged_df[merged_df["salary_x"] > merged_df["salary_y"]].loc[:, ["name"]].rename({"name":"Employee"}, axis=1)
    
data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})

good_job = find_employees(employee)
print(good_job)
