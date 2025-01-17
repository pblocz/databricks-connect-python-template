from pyspark.sql import SparkSession


def get_spark():
    spark = SparkSession.builder.getOrCreate()

    return spark


def get_dbutils(spark):
    try:
        from pyspark.dbutils import DBUtils
        dbutils = DBUtils(spark)
    except ImportError:
        import IPython
        dbutils = IPython.get_ipython().user_ns["dbutils"]
    return dbutils


def setup_environment():
    "Shortcut to setup spark and dbutils"

    spark = get_spark()
    dbutils = get_dbutils(spark)

    return spark, dbutils