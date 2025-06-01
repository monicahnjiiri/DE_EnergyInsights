import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:LiebeKinder%40123@127.0.0.1:3306/energy_insights")

# Load CSVs
load_df = pd.read_csv(r'C:/Users/admin/Desktop/BI.Final.Project/LoadCleaned.csv')
gen_df = pd.read_csv(r'C:/Users/admin/Desktop/BI.Final.Project/GenerationCleaned.csv')

print("LoadCleaned shape:", load_df.shape)
print("GenerationCleaned shape:", gen_df.shape)

# Upload
load_df.to_sql('load_cleaned', con=engine, if_exists='replace', index=False)
gen_df.to_sql('generation_cleaned', con=engine, if_exists='replace', index=False)

print("✅ Data upload successful.")
