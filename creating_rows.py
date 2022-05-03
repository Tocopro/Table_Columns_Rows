
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

df = pd.read_csv("C:\\Users\\NEAK\\Downloads\\survey_results_public.csv")
df = df[['ResponseId', 'MainBranch', 'Employment', 'EdLevel', 'LearnCode', 'YearsCode', 'YearsCodePro']]

result = df.head(10)
print(result)
