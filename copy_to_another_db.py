from sqlalchemy import create_engine
import pandas as pd

# Copy from sakila → sakila_backup
source = create_engine("mysql+mysqlconnector://root:@localhost/sakila")
target = create_engine("mysql+mysqlconnector://root:@localhost/sakila_backup")

# Get all table names
tables = pd.read_sql("SHOW TABLES", source).iloc[:, 0].tolist()

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", source)
    df.to_sql(table, target, if_exists='replace', index=False)

print("✅ All tables copied to 'sakila_backup'.")