simple_lambda = lambda q: q*q
int_test = 73
str_test = 'global'
float_test = 2.2
boolean_test = True
none_test = None
list_test = [1, '2', 3.3]
tuple_test = (1, '2', 3.3)
set_test = {1, '2', 3.3}
frozenset_test = frozenset(set_test)
dict_test = {'Name': 'Petr', 'Age' : 23, 'has_job': False}

class SimpleClass:
    def __init__(self):
        self.can_say = True
        self.count = 5
        self.word = "ku"
    def say_kuku(self):
        return self.word * self.count

class ComplexClass:
    def __init__(self):
        self.simple_class = SimpleClass()
        self.const = int_test
        self.name = 'CmplexClass'
    def func_with_test(self):
        return "local_str" + str_test

def cmplx_func(a):
    b = int_test
    return simple_func(2)*b**a

def simple_func(a):
    return a+10