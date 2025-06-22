from typing import Callable, Optional, List
from collections import deque
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import build_tree_from_list, tree_to_list

# def test(func, input, expected, name=""):
#     result = func(input)
#     if result == expected:
#         print(f"{name or 'Test'} ✅ Passed")
#     else:
#         print(f"{name or 'Test'} ❌ Failed")
#         print(f"   Input: {input}")
#         print(f"   Output: {result}")
#         print(f"   Expected: {expected}")


# def test(func, input_args, expected, name=""):
#     try:
#         if isinstance(input_args, tuple):
#             result = func(*input_args)
#         else:
#             result = func(input_args)

#         if result == expected:
#             print(f"{name or 'Test'} ✅ Passed")
#         else:
#             print(f"{name or 'Test'} ❌ Failed")
#             print(f"   Input: {input_args}")
#             print(f"   Output: {result}")
#             print(f"   Expected: {expected}")
#     except Exception as e:
#         print(f"{name or 'Test'} ❌ Error")
#         print(f"   Exception: {e}")



# Updated to accomodate a a variable number of input arguments
def test(func, *args):
    """
    Usage:
    test(func, args..., expected_output, test_name)
    e.g. test(myfunc, "AABABBA", 1, 4, "Test 1")
    """
    if len(args) < 2:
        raise ValueError("test() requires at least input(s) and expected output.")

    *inputs, expected, name = args
    try:
        result = func(*inputs)
        if result == expected:
            print(f"{name or 'Test'} ✅ Passed")
        else:
            print(f"{name or 'Test'} ❌ Failed")
            print(f"   Input: {tuple(inputs)}")
            print(f"   Output: {result}")
            print(f"   Expected: {expected}")
    except Exception as e:
        print(f"{name or 'Test'} ❌ Error")
        print(f"   Exception: {e}")


# Had to factor this in when i solved 049_group_anagrams
def test_unordered_groups(func, *args):
    """
    Compares unordered list-of-lists output (e.g., group anagrams).
    Sorts inner and outer lists before comparison.
    """
    *inputs, expected, name = args
    try:
        result = func(*inputs)

        result_sorted = sorted([sorted(group) for group in result])
        expected_sorted = sorted([sorted(group) for group in expected])
        passed = result_sorted == expected_sorted

        if passed:
            print(f"{name or 'Test'} ✅ Passed")
        else:
            print(f"{name or 'Test'} ❌ Failed")
            print(f"   Input: {tuple(inputs)}")
            print(f"   Output: {result}")
            print(f"   Expected: {expected}")
    except Exception as e:
        print(f"{name or 'Test'} ❌ Error")
        print(f"   Exception: {e}")
        

def test_tree(func: Callable, *args):
    """
    Usage:
    test_tree(func, input_tree, expected_output_list, test_name)

    Converts the result of func(input_tree) to list and compares with expected_output_list.
    """
    *inputs, expected_output_list, test_name = args
    try:
        result_root = func(*inputs)
        result_list = tree_to_list(result_root)
        if result_list == expected_output_list:
            print(f"{test_name or 'Test'} ✅ Passed")
        else:
            print(f"{test_name or 'Test'} ❌ Failed")
            print(f"   Input: {tuple(inputs)}")
            print(f"   Output: {result_list}")
            print(f"   Expected: {expected_output_list}")
    except Exception as e:
        print(f"{test_name or 'Test'} ❌ Error")
        print(f"   Exception: {e}")
