# SE302 Homework 01 - Complete Solution Summary

## Overview

This document provides a summary of all completed tasks for SE302 Homework 01 - Software Testing and Maintenance.

---

## Task Completion Status

✅ **Task 1**: Equivalence Class Testing for Shoe Store System - **COMPLETE**  
✅ **Task 2**: User Story, Test Scenarios, and Test Cases for Library System - **COMPLETE**  
✅ **Task 3**: Testing and Debugging Statistical Utility Functions - **COMPLETE**

---

## Deliverables

### Task 1 Files
- **Task1_Equivalence_Testing.md**: Complete equivalence class analysis and test case design
  - 28 equivalence classes identified (12 valid, 16 invalid)
  - 25 comprehensive test cases covering all equivalence classes
  - 100% coverage of identified equivalence classes

### Task 2 Files
- **Task2_Library_System_Testing.md**: Complete user story, test scenarios, and test cases
  - User story with extensions (search and return functionality)
  - 12 main test scenarios derived from acceptance criteria
  - 12 detailed test cases with preconditions, steps, and expected results
  - Test execution report template
  - Optional extensions for additional credit (7 additional test cases)

### Task 3 Files
- **test_stats_utils.py**: Comprehensive unit test suite
  - 25 test cases covering all statistical functions
  - Tests for normal cases, edge cases, and error cases
  - All tests passing after bug fixes
- **stats_utils.py**: Fixed implementation of statistical functions
  - All bugs identified and corrected
  - Functions now work correctly according to mathematical definitions
- **Task3_Bug_Report.md**: Detailed bug analysis and documentation
  - 4 bugs identified and documented
  - Root cause analysis for each bug
  - Fixes applied and verified
  - Test results showing all tests pass

---

## File Structure

```
/Users/kappasutra/302/
├── SE302_Homework01 1.pdf          # Original homework assignment
├── stats_utils.py                    # Fixed statistical functions (Task 3)
├── test_stats_utils.py               # Unit test suite (Task 3)
├── Task1_Equivalence_Testing.md      # Task 1 solution
├── Task2_Library_System_Testing.md   # Task 2 solution
├── Task3_Bug_Report.md              # Task 3 bug report
└── Homework_Summary.md              # This summary document
```

---

## Key Achievements

### Task 1: Equivalence Class Testing
- **28 equivalence classes** comprehensively identified
- **25 test cases** designed to cover all classes
- **100% coverage** achieved
- Both valid and invalid input scenarios covered
- Boundary value testing included

### Task 2: Library System Testing
- **Extended user story** including search and return features
- **12 test scenarios** derived from acceptance criteria
- **12 main test cases** with detailed documentation
- **7 additional test cases** for optional extensions
- **Test execution report** template provided

### Task 3: Statistical Functions Testing
- **4 bugs identified** and fixed:
  1. `mean()` - Incorrect addition of 1
  2. `median()` - Wrong index for odd-length lists
  3. `range_list()` - Addition instead of subtraction
  4. `remove_outliers()` - Missing standard deviation calculation
- **25 unit tests** created covering all functions
- **100% test pass rate** after fixes
- **Comprehensive bug report** with root cause analysis

---

## Testing Approach

### Task 1 Approach
- Equivalence partitioning method
- Systematic identification of valid and invalid classes
- Boundary value analysis
- Complete coverage of all equivalence classes

### Task 2 Approach
- User story driven testing
- Acceptance criteria based scenario derivation
- Positive and negative test case design
- Boundary value analysis for borrowing limits

### Task 3 Approach
- Unit testing with unittest framework
- Test-driven approach to bug identification
- Systematic testing of normal, edge, and error cases
- Verification of fixes through test execution

---

## Quality Assurance

All solutions have been:
- ✅ Thoroughly documented
- ✅ Following best practices
- ✅ Covering all requirements
- ✅ Including edge cases and error handling
- ✅ Ready for submission

---

## Submission Checklist

- [x] Task 1: Equivalence class testing document
- [x] Task 2: User story, scenarios, and test cases document
- [x] Task 3: Unit test file (`test_stats_utils.py`)
- [x] Task 3: Bug report document
- [x] All files properly formatted and documented
- [x] All tests passing
- [x] All bugs fixed and verified

---

## Notes for Submission

1. **File Naming**: According to the assignment, the submission should be:
   - PDF or DOCX document: `SE302 Homework01 <StudentID>.pdf`
   - Python test file: `test_stats_utils.py` (already created)

2. **Original Work**: All solutions are original and comprehensive.

3. **Completeness**: All three tasks are fully completed with detailed documentation.

4. **Test Results**: Task 3 tests can be run with:
   ```bash
   python3 test_stats_utils.py
   ```
   All 25 tests pass successfully.

---

## Additional Resources

- All test cases are documented with:
  - Clear preconditions
  - Step-by-step test procedures
  - Expected results
  - Actual results (to be filled during execution)

- Bug reports include:
  - Root cause analysis
  - Before/after code comparisons
  - Test verification results

---

**Status**: ✅ All tasks completed and ready for submission

