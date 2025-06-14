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
