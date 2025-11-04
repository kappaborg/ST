# Task 1: Equivalence Class Testing for Shoe Store System
## SE302 Homework 01

---

## System Requirements

The shoe store system reads a text file where each line contains:
- **Item name**: Alphabetic characters only, length between 2 and 15 characters
- **Sizes**: Whole numbers in the range of 26 to 55
- **Format**: `itemName,size1,size2,...`
- **Constraints**:
  - Sizes must be listed in ascending order
  - Maximum of five sizes per item
  - Commas are used as separators
  - Blank spaces should be ignored during input processing

---

## Equivalence Classes Identification

### Valid Equivalence Classes

#### For Item Name (Valid):
1. **EC1**: Item name with exactly 2 alphabetic characters (minimum valid length)
2. **EC2**: Item name with 3-14 alphabetic characters (normal valid length)
3. **EC3**: Item name with exactly 15 alphabetic characters (maximum valid length)

#### For Sizes (Valid):
4. **EC4**: Size exactly 26 (minimum valid size)
5. **EC5**: Sizes between 27-54 (normal valid sizes)
6. **EC6**: Size exactly 55 (maximum valid size)
7. **EC7**: Single size provided (valid)
8. **EC8**: Multiple sizes (2-5) provided (valid)
9. **EC9**: Exactly 5 sizes provided (maximum valid count)
10. **EC10**: Sizes in ascending order (valid)

#### For Format (Valid):
11. **EC11**: Proper comma separation (valid)
12. **EC12**: Spaces around commas (should be ignored - valid)

---

### Invalid Equivalence Classes

#### For Item Name (Invalid):
13. **EC13**: Item name with 1 character (below minimum)
14. **EC14**: Item name with more than 15 characters (above maximum)
15. **EC15**: Item name with numeric characters (invalid characters)
16. **EC16**: Item name with special characters (invalid characters)
17. **EC17**: Empty item name (invalid)

#### For Sizes (Invalid):
18. **EC18**: Size less than 26 (below minimum)
19. **EC19**: Size greater than 55 (above maximum)
20. **EC20**: Size with decimal point (not whole number)
21. **EC21**: Size with alphabetic characters (invalid)
22. **EC22**: More than 5 sizes provided (above maximum)
23. **EC23**: No sizes provided (invalid)
24. **EC24**: Sizes not in ascending order (invalid)

#### For Format (Invalid):
25. **EC25**: Missing comma between item name and sizes (invalid)
26. **EC26**: Missing comma between sizes (invalid)
27. **EC27**: Extra commas (invalid)
28. **EC28**: Empty line (invalid)

---

## Test Cases Design

### Test Case Table

| # | Test Input | Expected Output | Covered Classes | Rationale |
|---|------------|----------------|-----------------|-----------|
| 1 | `reebok,40,43` | VALID | 1, 4, 7, 9, 10, 13, 16, 18, 20 | Example from homework - valid item name, valid sizes, ascending order |
| 2 | `ab,26,30,35,40,55` | VALID | 1, 4, 6, 9, 10, 13, 16, 18, 20 | Minimum name length, min/max sizes, maximum size count |
| 3 | `nike,41,42,43,44,45,46` | INVALID | 17 | More than 5 sizes (violates maximum size count) |
| 4 | `abcdefghijklmno,40,45` | VALID | 3, 5, 8, 10, 13, 16, 18, 20 | Maximum name length (15 chars), valid sizes |
| 5 | `a,40` | INVALID | 13 | Item name too short (1 character) |
| 6 | `abcdefghijklmnop,40` | INVALID | 14 | Item name too long (16 characters) |
| 7 | `nike123,40` | INVALID | 15 | Item name contains numeric characters |
| 8 | `nike@pro,40` | INVALID | 16 | Item name contains special characters |
| 9 | `,40,45` | INVALID | 17 | Empty item name |
| 10 | `nike,25` | INVALID | 18 | Size below minimum (25 < 26) |
| 11 | `nike,56` | INVALID | 19 | Size above maximum (56 > 55) |
| 12 | `nike,40.5` | INVALID | 20 | Size with decimal point |
| 13 | `nike,40a` | INVALID | 21 | Size with alphabetic characters |
| 14 | `nike` | INVALID | 23 | No sizes provided |
| 15 | `nike,45,40` | INVALID | 24 | Sizes not in ascending order |
| 16 | `nike 40,45` | INVALID | 25 | Missing comma between item name and sizes |
| 17 | `nike,40 45` | INVALID | 26 | Missing comma between sizes |
| 18 | `nike,,40` | INVALID | 27 | Extra comma (double comma) |
| 19 | `` | INVALID | 28 | Empty line |
| 20 | `adidas,30,35,40,45,50` | VALID | 2, 5, 9, 10, 13, 16, 18, 20 | Normal case with 5 sizes |
| 21 | `nike,40` | VALID | 2, 5, 7, 13, 16, 18, 20 | Single size (minimum requirement) |
| 22 | `puma,27,30,35,40,45` | VALID | 2, 5, 9, 10, 13, 16, 18, 20 | Normal case with sizes in middle range |
| 23 | `nike , 40 , 45` | VALID | 2, 5, 8, 10, 12, 13, 16, 18, 20 | Spaces around commas (should be ignored) |
| 24 | `NIKE,40,45` | VALID | 2, 5, 8, 10, 13, 16, 18, 20 | Uppercase letters (alphabetic, valid) |
| 25 | `nike,26,55` | VALID | 2, 4, 6, 8, 10, 13, 16, 18, 20 | Boundary values for sizes (min and max) |

---

## Test Coverage Analysis

### Coverage Summary

**Total Equivalence Classes Identified:** 28
- **Valid Classes:** 12 (EC1-EC12)
- **Invalid Classes:** 16 (EC13-EC28)

**Test Cases Created:** 25
- **Valid Test Cases:** 9 (covering EC1-EC12)
- **Invalid Test Cases:** 16 (covering EC13-EC28)

**Coverage:** 100% of identified equivalence classes are covered by at least one test case.

---

## Detailed Test Case Descriptions

### Valid Test Cases

1. **TC1**: Basic valid case with 2 sizes
   - Input: `reebok,40,43`
   - Expected: VALID
   - Covers: Normal item name, normal sizes, proper format

2. **TC2**: Boundary test - minimum name length, min/max sizes, max size count
   - Input: `ab,26,30,35,40,55`
   - Expected: VALID
   - Covers: EC1 (min name), EC4 (min size), EC6 (max size), EC9 (max sizes)

3. **TC4**: Boundary test - maximum name length
   - Input: `abcdefghijklmno,40,45`
   - Expected: VALID
   - Covers: EC3 (max name length - 15 chars)

4. **TC20**: Normal case with 5 sizes
   - Input: `adidas,30,35,40,45,50`
   - Expected: VALID
   - Covers: Normal operation with maximum allowed sizes

5. **TC21**: Single size case
   - Input: `nike,40`
   - Expected: VALID
   - Covers: EC7 (single size)

6. **TC23**: Spaces around commas (should be ignored)
   - Input: `nike , 40 , 45`
   - Expected: VALID
   - Covers: EC12 (spaces should be ignored)

---

### Invalid Test Cases

1. **TC3**: More than 5 sizes
   - Input: `nike,41,42,43,44,45,46`
   - Expected: INVALID
   - Covers: EC22 (more than 5 sizes)

2. **TC5**: Item name too short
   - Input: `a,40`
   - Expected: INVALID
   - Covers: EC13 (1 character)

3. **TC6**: Item name too long
   - Input: `abcdefghijklmnop,40`
   - Expected: INVALID
   - Covers: EC14 (>15 characters)

4. **TC7**: Numeric characters in name
   - Input: `nike123,40`
   - Expected: INVALID
   - Covers: EC15 (numeric characters)

5. **TC8**: Special characters in name
   - Input: `nike@pro,40`
   - Expected: INVALID
   - Covers: EC16 (special characters)

6. **TC9**: Empty item name
   - Input: `,40,45`
   - Expected: INVALID
   - Covers: EC17 (empty name)

7. **TC10**: Size below minimum
   - Input: `nike,25`
   - Expected: INVALID
   - Covers: EC18 (<26)

8. **TC11**: Size above maximum
   - Input: `nike,56`
   - Expected: INVALID
   - Covers: EC19 (>55)

9. **TC12**: Decimal size
   - Input: `nike,40.5`
   - Expected: INVALID
   - Covers: EC20 (decimal)

10. **TC13**: Alphabetic characters in size
    - Input: `nike,40a`
    - Expected: INVALID
    - Covers: EC21 (alphabetic in size)

11. **TC14**: No sizes provided
    - Input: `nike`
    - Expected: INVALID
    - Covers: EC23 (no sizes)

12. **TC15**: Sizes not in ascending order
    - Input: `nike,45,40`
    - Expected: INVALID
    - Covers: EC24 (not ascending)

13. **TC16**: Missing comma between name and sizes
    - Input: `nike 40,45`
    - Expected: INVALID
    - Covers: EC25 (missing comma)

14. **TC17**: Missing comma between sizes
    - Input: `nike,40 45`
    - Expected: INVALID
    - Covers: EC26 (missing comma)

15. **TC18**: Extra commas
    - Input: `nike,,40`
    - Expected: INVALID
    - Covers: EC27 (extra commas)

16. **TC19**: Empty line
    - Input: `` (empty)
    - Expected: INVALID
    - Covers: EC28 (empty line)

---

## Conclusion

This test suite provides comprehensive coverage of all equivalence classes for the shoe store system. Each test case is designed to validate either a valid input condition or expose an invalid input condition according to the system requirements. The test cases follow the format specified in the homework assignment and achieve 100% coverage of all identified equivalence classes.

