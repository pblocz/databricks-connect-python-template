# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from library import config

spark = config.get_spark()
dbutils = config.get_dbutils(spark)

# %%

def displaydf(df):
   display(df.limit(1000).toPandas()) 

# %%

displaydf(
   spark.sql("select 1")
)

# %%

# Use dbutils.fs
dbutils.fs.ls("/")

# %%

# Use dbutils.secrets. First time you will need to follow the steps.
dbutils.secrets.get("secret-scope", "secret")

#%%