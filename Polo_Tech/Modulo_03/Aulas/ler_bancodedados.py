from sqlalchemy import create_engine
import pandas as pd
# from pandassql import PandasSQL

engine = create_engine('postgresql+psycop2://admin:admin@hotname/postgres')
connection = engine.connect()

query = "SELECT * FROM sales"
df = pd.read_sql(query, connection)
print(df)