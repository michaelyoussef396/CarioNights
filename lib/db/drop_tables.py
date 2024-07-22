from models import engine, Base
from sqlalchemy import MetaData

meta = MetaData()

# Reflect the tables
meta.reflect(bind=engine)

# Drop the tables if they exist
tables_to_drop = ['waiting_list']

for table_name in tables_to_drop:
    if table_name in meta.tables:
        table = meta.tables[table_name]
        table.drop(engine)
        print(f"Dropped '{table_name}' table.")