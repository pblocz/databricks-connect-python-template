# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Setup spark and dbutils. Some shortcuts are in library.config

# %%
from library import config

spark, dbutils = config.setup_environment()


# %%
def displaydf(df):
   display(df.limit(1000).toPandas()) 


# %%
# It works!

displaydf(
    spark.sql("select 1")
)

# %% [markdown]
# ## Use part of the dbutils library

# %%
# Use dbutils.fs
dbutils.fs.ls("/")


# %%
# Use dbutils.secrets. First time you will need to follow the steps.
dbutils.secrets.get("secret-scope", "secret")

# %% [markdown]
# ## Use custom transformations defined in library

# %%
df = spark.createDataFrame([[1, 2], [3, 4]]).toDF("x", "y")

displaydf(df)


# %%
from library import transformations

displaydf(
   df.transform(transformations.add)
)

# %%
