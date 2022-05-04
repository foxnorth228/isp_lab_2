from setuptools import setup

setup(
    name = "lb2",
    version = "1.0",
    author = "Alexandr Khitrii",
    author_email = "khitrii03@gmail.com",
    packages = ["serializers", "factory", "serializers/json_serializer",
    "serializers/yaml_serializer", "serializers/toml_serializer",
    "serializers/pickle_serializer", "serializers/objectPack"],
    scripts = ["serializer.py"]
)