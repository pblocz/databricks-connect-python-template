from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg

from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from pathlib import Path

import yaml

config = yaml.load(Path("config.yaml").open("r"))

class bdist_spark(bdist_egg):
      description = "create an egg and prepare driver and config"

      user_options = bdist_egg.user_options + [
              ('conf-environment=', 'e',
               "environment to distribute configuration"),
              ('spark-entry-point=', None,
               "python script to run in spark-submit"),
              ('conf-subdir=', None,
               "configuration subdir where to find configuration"),

      ]

      def initialize_options(self):
            self.conf_environment = 'dev'
            self.spark_entry_point = "jobs/main.py"
            self.conf_subdir = "config"

            super().initialize_options()

      def finalize_options(self):
            super().finalize_options()

      def run(self):
            print(vars(self))
            super().run()

            source_dir = Path("src")
            dist_dir = Path(self.dist_dir)

            driver = source_dir / self.spark_entry_point 
            copy_file(driver, self.dist_dir)

            conf_dir = source_dir / self.conf_subdir / self.conf_environment
            copy_tree(str(conf_dir), str(dist_dir / "config"))


setup(name=config["name"],
      version=config["version"],
      description='Some interesting description',
      url=config["url"],
      author=config["author"],
      author_email=config["author_email"],
      packages=config["packages"],
      package_dir={'': "src"},
      zip_safe=False,
      cmdclass={
            'bdist_spark': bdist_spark,
      },
      install_requires = [
          'databricks-connect=={runtime}.*'.format(runtime=config["databricks-runtime"]),
          'pandas'
      ]
)