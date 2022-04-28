import sys
sys.path.append('./')
import pickle
from serializers.objectPack.objectPack import convert, deconvert

class Pickle:
    def dump(self, obj, fp):
        with open(fp, 'wb+') as f:
            return pickle.dump(convert(obj), f)

    def dumps(self, obj):
        return pickle.dumps(convert(obj))

    def load(self, fp):
        with open(fp, 'rb') as f:
            return deconvert(pickle.load(f))

    def loads(self, s):
        return deconvert(pickle.loads(s))