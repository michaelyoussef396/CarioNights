from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///cario_nights.db"

engine = create_engine(DATABASE_URL)
meta = MetaData()

# Reflect the tables
meta.reflect(bind=engine)

# Drop the tables if they exist
if 'shisha' in meta.tables:
    table = meta.tables['shisha']
    table.drop(engine)
    print("Dropped 'shisha' table.")

if 'flavors' in meta.tables:
    table = meta.tables['flavors']
    table.drop(engine)
    print("Dropped 'flavors' table.")
