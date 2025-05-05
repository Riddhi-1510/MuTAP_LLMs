import os
import importlib.util
import sys
from test_put_code_1 import test_case_0, test_case_1, test_case_2

# Function to load the mutant file as a module
def load_module_from_path(path, module_name="module_0"):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# Automatically fetch mutant files from 'generated_tests' folder ending with '_zeroshot.py'
generated_tests_dir = os.path.join(os.path.dirname(__file__), "generated_tests")
mutant_files = [f for f in os.listdir(generated_tests_dir) if f.endswith("_zeroshot.py")]

# Function to run tests on each mutant
def run_tests_on_mutant(mutant_file):
    print(f"\nRunning tests on: {mutant_file}")
    path = os.path.join(generated_tests_dir, mutant_file)
    module_0 = load_module_from_path(path)

    # Track if any tests fail (mutant is killed)
    killed = False
    try:
        test_case_0(module_0)
        test_case_1(module_0)
        test_case_2(module_0)
    except AssertionError as e:
        print(f"Mutant killed: {mutant_file}")
        killed = True

    if not killed:
        print(f" Mutant survived: {mutant_file}")
    return "killed" if killed else "survived"

# Variables to count killed and survived mutants
killed_count = 0
survived_count = 0

# Iterate over all mutants and run tests
for mutant in mutant_files:
    result = run_tests_on_mutant(mutant)
    if result == "killed":
        killed_count += 1
    else:
        survived_count += 1

# Calculate mutation score
total = killed_count + survived_count
score = killed_count / total if total > 0 else 0.0

# Print summary
print(f"\nTotal Mutants Killed: {killed_count}")
print(f"Total Mutants Survived: {survived_count}")
print(f"Mutation Score: {score:.2f}")