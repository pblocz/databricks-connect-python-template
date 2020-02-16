from pyspark.sql.functions import col

def add(df):
    return (
        df.withColumn("z", col("x") + col("y"))
    )