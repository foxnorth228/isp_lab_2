import sys
sys.path.append('./')
import unittest
from factory.factory import Factory
import test.test_objects as test_objects

class SerializeTester(unittest.TestCase):
#---------JSON---------
    json = Factory.create_serializer('.json')
    yaml = Factory.create_serializer('.yaml')
    toml = Factory.create_serializer('.toml')
    pickle = Factory.create_serializer('.pickle')

    def test_json_int(self):
        ser = SerializeTester.json
        old_obj = test_objects.int_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)
        
    def test_json_float(self):
        ser = SerializeTester.json
        old_obj = test_objects.float_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_str(self):
        ser = SerializeTester.json
        old_obj = test_objects.str_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_boolean(self):
        ser = SerializeTester.json
        old_obj = test_objects.boolean_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_none(self):
        ser = SerializeTester.json
        old_obj = test_objects.none_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_list(self):
        ser = SerializeTester.json
        old_obj = test_objects.list_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_tuple(self):
        ser = SerializeTester.json
        old_obj = test_objects.tuple_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_set(self):
        ser = SerializeTester.json
        old_obj = test_objects.set_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_frozenset(self):
        ser = SerializeTester.json
        old_obj = test_objects.frozenset_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_dict(self):
        ser = SerializeTester.json
        old_obj = test_objects.dict_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj['Name'], new_obj['Name'])

    def test_json_lambda(self):
        ser = SerializeTester.json
        old_obj = test_objects.simple_lambda
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_json_simple_func(self):
        ser = SerializeTester.json
        old_obj = test_objects.simple_func
        ser.dump(old_obj, '.\\test\\test.json')
        new_obj = ser.load('.\\test\\test.json')
        self.assertEqual(old_obj(4), new_obj(4))

    def test_json_cmplx_func(self):
        ser = SerializeTester.json
        old_obj = test_objects.cmplx_func
        old_obj_2 = test_objects.simple_lambda
        new_obj = ser.loads(ser.dumps(old_obj))
        new_obj_2 = ser.loads(ser.dumps(old_obj_2))
        self.assertEqual(old_obj(4), new_obj(4))
        self.assertEqual(old_obj_2(4), new_obj_2(4))

    def test_json_simple_class_obj(self):
        ser = SerializeTester.json
        old_obj = test_objects.SimpleClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_json_cmplx_class_obj(self):
        ser = SerializeTester.json
        old_obj = test_objects.ComplexClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_test(), new_obj.func_with_test(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))

#---------YAML---------
    def test_yaml_int(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.int_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_float(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.float_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_str(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.str_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_boolean(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.boolean_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_none(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.none_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_list(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.list_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_tuple(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.tuple_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_set(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.set_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)
    def test_json_frozenset(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.frozenset_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_lambda(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.simple_lambda
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_yaml_simple_func(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.simple_func
        ser.dump(old_obj, '.\\test\\test.yaml')
        new_obj = ser.load('.\\test\\test.yaml')
        self.assertEqual(old_obj(4), new_obj(4))

    def test_yaml_cmplx_func(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.cmplx_func
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_yaml_simple_class_obj(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.SimpleClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_yaml_dict(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.dict_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_cmplx_class_obj(self):
        ser = SerializeTester.yaml
        old_obj = test_objects.ComplexClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_test(), new_obj.func_with_test(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))
    
#---------TOML---------
    def test_toml_int(self):
        ser = SerializeTester.toml
        old_obj = test_objects.int_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_float(self):
        ser = SerializeTester.toml
        old_obj = test_objects.float_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_str(self):
        ser = SerializeTester.toml
        old_obj = test_objects.str_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_boolean(self):
        ser = SerializeTester.toml
        old_obj = test_objects.boolean_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_none(self):
        ser = SerializeTester.toml
        old_obj = test_objects.none_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_list(self):
        ser = SerializeTester.toml
        old_obj = test_objects.list_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_tuple(self):
        ser = SerializeTester.toml
        old_obj = test_objects.tuple_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_set(self):
        ser = SerializeTester.toml
        old_obj = test_objects.set_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_dict(self):
        ser = SerializeTester.toml
        old_obj = test_objects.dict_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj['Name'], new_obj['Name'])

    def test_json_frozenset(self):
        ser = SerializeTester.toml
        old_obj = test_objects.frozenset_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_lambda(self):
        ser = SerializeTester.toml
        old_obj = test_objects.simple_lambda
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_toml_simple_func(self):
        ser = SerializeTester.toml
        old_obj = test_objects.simple_func
        ser.dump(old_obj, '.\\test\\test.toml')
        new_obj = ser.load('.\\test\\test.toml')
        self.assertEqual(old_obj(4), new_obj(4))

    def test_toml_cmplx_func(self):
        ser = SerializeTester.toml
        old_obj = test_objects.cmplx_func
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_toml_simple_class_obj(self):
        ser = SerializeTester.toml
        old_obj = test_objects.SimpleClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_toml_cmplx_class_obj(self):
        ser = SerializeTester.toml
        old_obj = test_objects.ComplexClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_test(), new_obj.func_with_test(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))

#---------PICKLE---------
    def test_pickle_int(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.int_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_float(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.float_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_str(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.str_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_boolean(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.boolean_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_none(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.none_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_list(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.list_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_tuple(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.tuple_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_pickle_set(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.set_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)
        
    def test_pickle_dict(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.dict_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_frozenset(self):
        ser = SerializeTester.json
        old_obj = test_objects.frozenset_test
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_simple_func(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.simple_func
        ser.dump(old_obj, '.\\test\\test.pickle')
        new_obj = ser.load('.\\test\\test.pickle')
        self.assertEqual(old_obj(4), new_obj(4))

    def test_pickle_lambda(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.simple_lambda
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_pickle_cmplx_func(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.cmplx_func
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_pickle_simple_class_obj(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.SimpleClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_pickle_cmplx_class_obj(self):
        ser = SerializeTester.pickle
        old_obj = test_objects.ComplexClass()
        new_obj = ser.loads(ser.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_test(), new_obj.func_with_test(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))

if __name__ == '__main__':
    unittest.main()