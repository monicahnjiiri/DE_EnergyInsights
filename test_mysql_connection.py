from sqlalchemy import create_engine

# Intentionally simple
url = "mysql+pymysql://root:LiebeKinder%40123@127.0.0.1:3306/energy_insights"
print("Attempting to connect with URL:", url)

engine = create_engine(url)
print("✅ Engine created successfully")
