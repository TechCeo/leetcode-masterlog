from typing import Callable, Optional, List
from collections import deque
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.binary_tree_utils import build_tree_from_list, tree_to_list
from utils.linked_list_utils import build_linked_list, linked_list_to_list




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
        
def test_tree_int_return(func: Callable, *args):
    """
    Usage:
    test_tree_int_return(func, input_tree, expected_output_int, test_name)

    Calls func with input_tree and compares the integer result with expected_output_int.
    """
    *inputs, expected_output_int, test_name = args
    try:
        result_root = func(*inputs)
        # result_list = tree_to_list(result_root)
        if result_root == expected_output_int:
            print(f"{test_name or 'Test'} ✅ Passed")
        else:
            print(f"{test_name or 'Test'} ❌ Failed")
            print(f"   Input: {tuple(inputs)}")
            print(f"   Output: {result_root}")
            print(f"   Expected: {expected_output_int}")
    except Exception as e:
        print(f"{test_name or 'Test'} ❌ Error")
        print(f"   Exception: {e}")
        


def test_ll(func: Callable, *args):
    """
    Usage:
    test_ll(func, input_list_array, expected_output_array, test_name)
    
    1. Builds a Linked List from input_list_array.
    2. Runs func(head).
    3. Converts resulting Linked List back to an array to compare with expected_output_array.
    """
    if len(args) < 3:
        raise ValueError("test_ll() requires input_array, expected_array, and test_name.")

    *inputs, expected_arr, test_name = args
    try:
        # Convert the first input (the array representation of the LL) into actual nodes
        head = build_linked_list(inputs[0])
        
        # Execute the function with the head (and any other provided arguments)
        result_head = func(head, *inputs[1:])
        
        # Convert result back to list for easy comparison
        result_arr = linked_list_to_list(result_head)
        
        if result_arr == expected_arr:
            print(f"{test_name or 'Test'} ✅ Passed")
        else:
            print(f"{test_name or 'Test'} ❌ Failed")
            print(f"   Input: {inputs[0]}")
            print(f"   Output: {result_arr}")
            print(f"   Expected: {expected_arr}")
    except Exception as e:
        print(f"{test_name or 'Test'} ❌ Error")
        print(f"   Exception: {e}")
