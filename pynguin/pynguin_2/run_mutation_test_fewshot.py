import os
import importlib.util
import sys
from test_put_code_2 import (
    test_case_0, test_case_1, test_case_2, test_case_3, test_case_4,
    test_case_5, test_case_6, test_case_7, test_case_8, test_case_9
)

# Function to load a module from a given path
def load_module_from_path(path, module_name="module_0"):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Automatically fetch mutant files from 'generated_tests' folder ending with '_zeroshot.py'
generated_tests_dir = os.path.join(os.path.dirname(__file__), "generated_tests")
mutant_files = [f for f in os.listdir(generated_tests_dir) if f.endswith("_fewshot.py")]

# Function to run tests on a mutant
def run_tests_on_mutant(mutant_file):
    print(f"\nRunning tests on: {mutant_file}")
    path = os.path.join(os.path.dirname(__file__), "generated_tests", mutant_file)
    module_0 = load_module_from_path(path)

    test_functions = [
        test_case_0, test_case_1, test_case_2, test_case_3, test_case_4,
        test_case_5, test_case_6, test_case_7, test_case_8, test_case_9,
    ]

    killed = False
    try:
        # Inject the mutant into each test's global namespace
        for test_func in test_functions:
            test_func.__globals__["module_0"] = module_0
            test_func()
    except AssertionError:
        print(f" Mutant killed: {mutant_file}")
        killed = True
    except Exception as e:
        print(f" Error during test execution for {mutant_file}: {e}")
        killed = True

    if not killed:
        print(f" Mutant survived: {mutant_file}")
    return "killed" if killed else "survived"

# Run mutation testing
killed_count = 0
survived_count = 0

for mutant in mutant_files:
    result = run_tests_on_mutant(mutant)
    if result == "killed":
        killed_count += 1
    else:
        survived_count += 1

# Mutation score
total_mutants = killed_count + survived_count
score = killed_count / total_mutants if total_mutants > 0 else 0

# Summary
print("\n=== Mutation Testing Summary ===")
print(f"Total Mutants Killed   : {killed_count}")
print(f"Total Mutants Survived : {survived_count}")
print(f"Mutation Score         : {score}")