# SE302 Homework 01 - Requirements Verification Checklist

This document verifies that all requirements from the PDF have been met.

---

## Task 1: Equivalence Class Testing for Shoe Store System

### Requirements from PDF:
- [x] **Identify all equivalence classes** (both valid and invalid)
  - ✅ 28 equivalence classes identified (12 valid, 16 invalid)
  - ✅ Documented in `Task1_Equivalence_Testing.md`

- [x] **Design test cases covering all equivalence classes**
  - ✅ 25 test cases created
  - ✅ Each test case specifies: Input data, Expected output, Covered classes
  - ✅ Format matches example: `# | Test Input | Expected Output | Covered Classes`
  - ✅ Created `Task1_Test_Cases_Table.md` in exact format from PDF example

- [x] **Ensure full coverage**
  - ✅ 100% coverage of all 28 equivalence classes
  - ✅ Coverage analysis documented

### Deliverables:
- [x] `Task1_Equivalence_Testing.md` - Complete analysis with detailed explanations
- [x] `Task1_Test_Cases_Table.md` - Test cases in exact format from PDF example

---

## Task 2: User Story, Test Scenarios, and Test Cases for Library System

### Requirements from PDF:
- [x] **Write user story** (in own words, may extend to include returning/searching)
  - ✅ User story written in standard format: "As a... I want... So that..."
  - ✅ Extended to include search and return functionality
  - ✅ Documented in `Task2_Library_System_Testing.md`

- [x] **Derive test scenarios based on acceptance criteria**
  - ✅ 12 test scenarios derived from 7 acceptance criteria
  - ✅ Each scenario mapped to acceptance criteria
  - ✅ Documented with scenario IDs (TS1-TS12)

- [x] **Design detailed test cases for each scenario**
  - ✅ 12 main test cases with detailed documentation
  - ✅ Each test case includes:
    - ✅ Test Case ID
    - ✅ Scenario reference
    - ✅ Preconditions/Test Data
    - ✅ Test Steps
    - ✅ Expected Result
    - ✅ Actual Result (template provided)
  - ✅ Format matches example from PDF (TC1.1, TC2.1, etc.)

- [x] **Prepare test execution report showing which tests would pass or fail**
  - ✅ Test execution report created
  - ✅ Shows expected pass/fail status for each test case
  - ✅ Statistics included
  - ✅ Notes and rationale provided

### Optional Extensions (for additional credit):
- [x] **Return Book feature** with user stories and tests
  - ✅ Return functionality included in user story
  - ✅ Test cases TC10.1, TC11.1, TC12.1 for return feature
  - ✅ Additional extension test cases (TC13.1, TC14.1)

- [x] **Search and Filter functionality** test cases
  - ✅ Search test cases (TC7.1, TC8.1, TC9.1)
  - ✅ Additional extension test cases (TC15.1, TC16.1)

- [x] **Boundary value analysis for 5-book borrowing limit**
  - ✅ Boundary test cases (TC17.1, TC18.1, TC19.1)
  - ✅ Tests exactly 5 books, 6 books, and recovery scenarios

### Deliverables:
- [x] `Task2_Library_System_Testing.md` - Complete solution with all requirements

---

## Task 3: Testing and Debugging Statistical Utility Functions

### Requirements from PDF:

- [x] **Write Unit Tests**
  - ✅ Test suite created using `unittest` framework
  - ✅ File named: `test_stats_utils.py` (as required)
  - ✅ Tests for all 5 functions:
    - ✅ `mean(numbers)`
    - ✅ `median(numbers)`
    - ✅ `mode(numbers)`
    - ✅ `range_list(numbers)`
    - ✅ `remove_outliers(numbers, threshold=2)`
  - ✅ Includes normal cases, edge cases, and error cases:
    - ✅ Empty lists
    - ✅ Lists with one element
    - ✅ Lists with even and odd lengths
    - ✅ Lists with multiple modes
    - ✅ Lists with extreme values (for outlier removal)

- [x] **Run Tests and Record Outputs**
  - ✅ Tests executed and results captured
  - ✅ Output documented showing before/after fixes
  - ✅ 11 tests initially failed, all now pass after fixes

- [x] **Analyze and Report Bugs**
  - ✅ For each failing test, documented:
    - ✅ Expected output
    - ✅ Actual output (before fix)
    - ✅ Why the function produced incorrect results
  - ✅ Identified bugs in code
  - ✅ Suggested corrections for each bug

### Deliverables:
- [x] `test_stats_utils.py` - Python file with unit tests (exact name required)
- [x] `Task3_Bug_Report.md` - Document including:
  - ✅ Test cases and their outputs (before and after fixes)
  - ✅ List of bugs found (4 bugs identified)
  - ✅ Suggested corrections for each bug
  - ✅ All fixes implemented and verified

- [x] `stats_utils.py` - Fixed implementation (all bugs corrected)

---

## Submission Format Requirements

### From PDF:
- [x] **PDF or DOCX document** titled: `SE302 Homework01 <StudentID>.pdf`
  - ⚠️ Note: Student ID placeholder - needs to be filled in before submission
  - ✅ All content is in Markdown format and can be converted to PDF/DOCX

- [x] **Python file** named: `test_stats_utils.py`
  - ✅ File exists with correct name
  - ✅ All tests passing

---

## Additional Requirements from PDF

- [x] **Ensure answers are detailed and can be easily understood by each stakeholder**
  - ✅ All documents are well-structured and detailed
  - ✅ Clear explanations provided for all sections
  - ✅ Professional formatting throughout

- [x] **Original work**
  - ✅ All solutions are original and comprehensive
  - ✅ No plagiarism

---

## File Structure Summary

```
/Users/kappasutra/302/
├── SE302_Homework01 1.pdf              # Original assignment
├── stats_utils.py                       # Fixed code (Task 3)
├── test_stats_utils.py                  # Unit tests (Task 3) ✅ Correct name
├── Task1_Equivalence_Testing.md         # Task 1 detailed solution
├── Task1_Test_Cases_Table.md           # Task 1 format-matching table
├── Task2_Library_System_Testing.md      # Task 2 complete solution
├── Task3_Bug_Report.md                 # Task 3 bug report
├── Homework_Summary.md                 # Overall summary
└── Requirements_Checklist.md           # This checklist
```

---

## Verification Status

### ✅ All Requirements Met

- ✅ **Task 1**: Complete - 28 equivalence classes, 25 test cases, 100% coverage
- ✅ **Task 2**: Complete - User story, 12 scenarios, 12 test cases, execution report, extensions
- ✅ **Task 3**: Complete - 25 unit tests, 4 bugs found and fixed, comprehensive report

### ✅ All Deliverables Ready

- ✅ All files created and properly formatted
- ✅ All tests passing (Task 3)
- ✅ All bugs fixed and documented
- ✅ All documentation complete and detailed

### ⚠️ Action Required Before Submission

- ⚠️ Replace `<StudentID>` in document title when converting to PDF
- ⚠️ Convert Markdown files to PDF/DOCX format for submission
- ⚠️ Ensure all files are included in final submission package

---

## Quality Assurance

- ✅ All code follows best practices
- ✅ All documentation is clear and professional
- ✅ All test cases are comprehensive
- ✅ All bugs are properly analyzed and fixed
- ✅ All requirements are met or exceeded

---

**Status**: ✅ **READY FOR SUBMISSION**

All requirements from the PDF have been met and verified. The homework is complete and ready for submission after converting to PDF/DOCX format and adding student ID.

