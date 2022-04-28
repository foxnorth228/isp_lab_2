import sys
sys.path.append('./')
from serializers.json_serializer.json_serializer import Json
from serializers.pickle_serializer.pickle_serializer import Pickle
from serializers.toml_serializer.toml_serializer import Toml
from serializers.yaml_serializer.yaml_serializer import Yaml

class Factory:
    def create_serializer(format):
        if format == ".json":
            return Json()
        elif format == ".pickle":
            return Pickle()
        elif format == ".toml":
            return Toml()
        elif format == ".yaml":
            return Yaml()
        else:
            raise ValueError("Unacceptable value")