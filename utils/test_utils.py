def test(func, input, expected, name=""):
    result = func(input)
    if result == expected:
        print(f"{name or 'Test'} ✅ Passed")
    else:
        print(f"{name or 'Test'} ❌ Failed")
        print(f"   Input: {input}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
