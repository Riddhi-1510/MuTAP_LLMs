import importlib.util
import sys

# Function to load module dynamically from file path
def load_module_from_path(path, module_name="module_0"):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def test_case_0(module_0):
    bool_0 = True
    var_0 = module_0.function_put(bool_0, bool_0, bool_0)
    assert var_0 == "a is the greatest"


def test_case_1(module_0):
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.function_put(list_0, list_1, list_0)
    assert var_0 == "b is the greatest"


def test_case_2(module_0):
    str_0 = "=?V2} :o"
    var_0 = module_0.function_put(str_0, str_0, str_0)
    assert var_0 == "a is the greatest"
    var_1 = module_0.function_put(var_0, str_0, var_0)
    assert var_1 == "a is the greatest"
    str_1 = "gJNDNG7q`\\\x0c'RJb\x0c((Wr"
    var_2 = module_0.function_put(var_1, str_1, var_1)
    assert var_2 == "b is the greatest"
    var_3 = module_0.function_put(str_0, str_0, var_2)
    assert var_3 == "c is the greatest"
    var_4 = module_0.function_put(str_1, var_2, var_2)
    assert var_4 == "a is the greatest"
    var_5 = module_0.function_put(var_3, var_2, str_1)
    assert var_5 == "c is the greatest"
