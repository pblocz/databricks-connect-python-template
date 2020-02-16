# Installation Steps

1. Create a virtual environment with the same python version as the databricks runtime
`virtualenv .venv`
2. In setup.py change the databricks runtime version in install_requires from `databricks-connect==6.2.*` to the one you are using. For example if using 5.5 then change it to `==5.5.*`
3. Install the current directory with setup.py in the virtual environment `pip install -e .`

Follow the steps in [the official guide](https://docs.databricks.com/dev-tools/databricks-connect.html#step-2-configure-connection-properties) to finish configuring the client.

Follow the steps in the guide for VS Code or Jupyter to configure the IDE.

> *Note*: Check that you don't have SPARK_HOME set to your local spark installation. If set, then unset it or use `python.envFile` to set SPARK_HOME to the path returned by `databricks-connect get-spark-home`

# Deployment

Once you have code you want to deploy to databricks.

1. Import notebooks directly to databricks from the `.ipynb` or `.py` files.
2. For the libraries in src/ you will need to build a library and upload it

## Build python library
Use `python setup.py bdist_spark` or `python setup.py bdist_egg` to build a library in `dist/`. Import this library into databricks and install into the databricks cluster.