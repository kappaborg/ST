# Task 3: Bug Report - Statistical Utility Functions
## SE302 Homework 01

---

## Test Execution Summary

**Total Tests:** 25  
**Passed:** 25  
**Failed:** 0 (after fixes)

All tests now pass successfully after implementing the bug fixes.

---

## Test Execution Output

### Test Results (Before Fixes)

Initially, **11 tests failed** out of 25 tests. The failures were:

1. **TestMean.test_normal_case** - FAILED (AssertionError: 4.0 != 3.0)
2. **TestMean.test_single_element** - FAILED (AssertionError: 6.0 != 5.0)
3. **TestMean.test_negative_numbers** - FAILED (AssertionError: -1.0 != -2.0)
4. **TestMean.test_float_numbers** - FAILED (AssertionError: 3.5 != 2.5)
5. **TestMedian.test_odd_length** - FAILED (AssertionError: 1 != 3)
6. **TestMedian.test_unsorted_list** - FAILED (AssertionError: 2 != 3)
7. **TestRangeList.test_normal_case** - FAILED (AssertionError: 12 != 8)
8. **TestRangeList.test_single_element** - FAILED (AssertionError: 10 != 0)
9. **TestRangeList.test_all_same** - FAILED (AssertionError: 10 != 0)
10. **TestRangeList.test_negative_numbers** - FAILED (AssertionError: -6 != 4)
11. **TestRemoveOutliers.test_no_outliers** - FAILED (AssertionError: 3 != 5)

### Test Results (After Fixes)

```
test_empty_list (__main__.TestMean.test_empty_list)
Test mean with empty list ... ok
test_float_numbers (__main__.TestMean.test_float_numbers)
Test mean with float numbers ... ok
test_negative_numbers (__main__.TestMean.test_negative_numbers)
Test mean with negative numbers ... ok
test_normal_case (__main__.TestMean.test_normal_case)
Test mean with normal list of numbers ... ok
test_single_element (__main__.TestMean.test_single_element)
Test mean with single element ... ok
test_empty_list (__main__.TestMedian.test_empty_list)
Test median with empty list ... ok
test_even_length (__main__.TestMedian.test_even_length)
Test median with even number of elements ... ok
test_odd_length (__main__.TestMedian.test_odd_length)
Test median with odd number of elements ... ok
test_single_element (__main__.TestMedian.test_single_element)
Test median with single element ... ok
test_unsorted_list (__main__.TestMedian.test_unsorted_list)
Test median with unsorted list ... ok
test_all_same (__main__.TestMode.test_all_same)
Test mode when all elements are the same ... ok
test_empty_list (__main__.TestMode.test_empty_list)
Test mode with empty list ... ok
test_multiple_modes (__main__.TestMode.test_multiple_modes)
Test mode with multiple modes (should return first encountered) ... ok
test_no_duplicates (__main__.TestMode.test_no_duplicates)
Test mode when no duplicates exist ... ok
test_single_mode (__main__.TestMode.test_single_mode)
Test mode with single most frequent value ... ok
test_all_same (__main__.TestRangeList.test_all_same)
Test range when all elements are the same ... ok
test_empty_list (__main__.TestRangeList.test_empty_list)
Test range with empty list ... ok
test_negative_numbers (__main__.TestRangeList.test_negative_numbers)
Test range with negative numbers ... ok
test_normal_case (__main__.TestRangeList.test_normal_case)
Test range with normal list ... ok
test_single_element (__main__.TestRangeList.test_single_element)
Test range with single element ... ok
test_all_outliers (__main__.TestRemoveOutliers.test_all_outliers)
Test outlier removal when all values are outliers ... ok
test_empty_list (__main__.TestRemoveOutliers.test_empty_list)
Test outlier removal with empty list ... ok
test_no_outliers (__main__.TestRemoveOutliers.test_no_outliers)
Test outlier removal when no outliers exist ... ok
test_normal_case (__main__.TestRemoveOutliers.test_normal_case)
Test outlier removal with normal distribution ... ok
test_single_element (__main__.TestRemoveOutliers.test_single_element)
Test outlier removal with single element ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.001s

OK
```

**Result:** All 25 tests now pass successfully.

---

## Bugs Found and Fixed

### Bug #1: `mean()` Function - Incorrect Addition
**Location:** Line 8  
**Severity:** Critical

**Description:**
The function incorrectly adds 1 to the mean calculation, causing all results to be off by 1.

**Original Code:**
```python
return total / len(numbers) + 1
```

**Expected Behavior:**
- `mean([1, 2, 3, 4, 5])` should return `3.0`
- `mean([5])` should return `5.0`
- `mean([-1, -2, -3])` should return `-2.0`

**Actual Behavior (Before Fix):**
- `mean([1, 2, 3, 4, 5])` returned `4.0` (incorrect)
- `mean([5])` returned `6.0` (incorrect)
- `mean([-1, -2, -3])` returned `-1.0` (incorrect)

**Root Cause:**
The function adds 1 to every calculation, which is incorrect for computing the arithmetic mean.

**Fix Applied:**
```python
return total / len(numbers)
```

**Test Results After Fix:**
✅ All mean tests now pass

---

### Bug #2: `median()` Function - Incorrect Index for Odd-Length Lists
**Location:** Line 19  
**Severity:** Critical

**Description:**
For lists with odd length, the function returns `numbers[mid-1]` instead of `numbers[mid]`, causing incorrect median calculation.

**Original Code:**
```python
if len(numbers) % 2 == 0:
    return (numbers[mid] + numbers[mid-1]) / 2
else:
    return numbers[mid-1]  # BUG: Should be numbers[mid]
```

**Expected Behavior:**
- `median([1, 3, 5])` should return `3` (middle element)
- `median([5, 1, 3, 2, 4])` should return `3` (middle element after sorting)

**Actual Behavior (Before Fix):**
- `median([1, 3, 5])` returned `1` (incorrect - returns first element)
- `median([5, 1, 3, 2, 4])` returned `2` (incorrect - returns element before middle)

**Root Cause:**
The index calculation for odd-length lists is off by one. When `mid = len(numbers) // 2`, for a list of length 5, `mid = 2`, so `numbers[2]` is the correct middle element, not `numbers[1]`.

**Fix Applied:**
```python
if len(numbers) % 2 == 0:
    return (numbers[mid] + numbers[mid-1]) / 2
else:
    return numbers[mid]  # Fixed: Use mid instead of mid-1
```

**Test Results After Fix:**
✅ All median tests now pass

---

### Bug #3: `range_list()` Function - Addition Instead of Subtraction
**Location:** Line 36  
**Severity:** Critical

**Description:**
The function adds the maximum and minimum values instead of subtracting them, which is incorrect for calculating range.

**Original Code:**
```python
return max(numbers) + min(numbers)
```

**Expected Behavior:**
- `range_list([10, 2, 7, 5])` should return `8` (10 - 2 = 8)
- `range_list([5, 5, 5, 5])` should return `0` (5 - 5 = 0)
- `range_list([-5, -1, -3])` should return `4` (-1 - (-5) = 4)

**Actual Behavior (Before Fix):**
- `range_list([10, 2, 7, 5])` returned `12` (incorrect - 10 + 2 = 12)
- `range_list([5, 5, 5, 5])` returned `10` (incorrect - 5 + 5 = 10)
- `range_list([-5, -1, -3])` returned `-6` (incorrect - -5 + (-1) = -6)

**Root Cause:**
The function uses addition (+) instead of subtraction (-) for calculating the range.

**Fix Applied:**
```python
return max(numbers) - min(numbers)
```

**Test Results After Fix:**
✅ All range_list tests now pass

---

### Bug #4: `remove_outliers()` Function - Incorrect Standard Deviation Implementation
**Location:** Lines 44-48  
**Severity:** Critical

**Description:**
The function doesn't actually calculate or use standard deviation. Instead, it uses a simple absolute threshold comparison, which is incorrect.

**Original Code:**
```python
avg = mean(numbers)
result = []
for n in numbers:
    if abs(n - avg) < threshold:  # BUG: Not using standard deviation
        result.append(n)
return result
```

**Expected Behavior:**
The function should remove numbers that are more than `threshold` standard deviations from the mean. For example:
- `remove_outliers([1, 2, 3, 100], threshold=2)` should remove 100 if it's more than 2 standard deviations away
- `remove_outliers([1, 2, 3, 4, 5], threshold=2)` should keep all values if none are outliers

**Actual Behavior (Before Fix):**
- `remove_outliers([1, 2, 3, 4, 5], threshold=2)` incorrectly removed values 4 and 5 because they were more than 2 units away from the mean (3.0), even though they're within normal distribution
- The function didn't consider the actual standard deviation of the data

**Root Cause:**
The function doesn't calculate standard deviation and uses a fixed threshold instead of a threshold multiplied by the standard deviation.

**Fix Applied:**
```python
if not numbers or len(numbers) < 2:
    return numbers[:]  # Return copy if can't calculate std dev

# Calculate mean
avg = mean(numbers)

# Calculate standard deviation
variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
std_dev = variance ** 0.5

# Filter out values beyond threshold standard deviations
result = []
for n in numbers:
    if std_dev == 0 or abs(n - avg) <= threshold * std_dev:
        result.append(n)
return result
```

**Test Results After Fix:**
✅ All remove_outliers tests now pass

---

## Summary of Corrections

1. **mean()**: Removed the incorrect `+ 1` addition
2. **median()**: Fixed index calculation for odd-length lists (`numbers[mid]` instead of `numbers[mid-1]`)
3. **range_list()**: Changed from addition to subtraction (`max - min` instead of `max + min`)
4. **remove_outliers()**: Implemented proper standard deviation calculation and filtering

---

## Test Coverage

The test suite includes:
- **Normal cases**: Standard input with expected outputs
- **Edge cases**: Empty lists, single elements, all same values
- **Error cases**: Negative numbers, floats, unsorted lists
- **Boundary cases**: Even/odd lengths, multiple modes, extreme values

All 25 test cases pass successfully after implementing the fixes.

---

## Verification

After applying all fixes, all unit tests pass:
```
Ran 25 tests in 0.000s
OK
```

All statistical functions now work correctly according to standard mathematical definitions.

