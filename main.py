import geopandas as gpd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

db_connection_url = "postgresql://Grupo1:IFSP2023!@grupo1-postgresql.crys2li8ehue.us-east-1.rds.amazonaws.com:5432/Grupo1_PostgreSQL_DB"
con = create_engine(db_connection_url)


df = gpd.read_file('Dataframe/CET-data/ZonaAzulVagas.shp')


# Push the geodataframe to postgresql
df.to_postgis("Vagas", con, index=True, if_exists='replace')