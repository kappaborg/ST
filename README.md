# SE302 Homework 01 - Complete Solution
## Software Testing and Maintenance

---

## 📋 Overview

This repository contains a complete solution for SE302 Homework 01 with:
1. **Core Deliverables** - All required homework files
2. **Real-World Web Applications** - Interactive web apps implementing the test cases

---

## 📁 Project Structure

```
/302/
├── Core Deliverables (Homework Requirements)
│   ├── Task1_Equivalence_Testing.md          # Task 1 main solution
│   ├── Task1_Test_Cases_Table.md              # Task 1 format-matching table
│   ├── Task2_Library_System_Testing.md        # Task 2 complete solution
│   ├── test_stats_utils.py                    # Task 3 unit tests (required)
│   ├── Task3_Bug_Report.md                     # Task 3 bug report
│   └── stats_utils.py                          # Task 3 fixed code
│
├── Web Application (Next-Level Enhancement)
│   └── web_app/                                 # Unified Web Application
│       ├── app.py                                # Main Flask app (all 3 tasks)
│       ├── templates/
│       │   ├── index.html                        # Main dashboard
│       │   ├── task1.html                        # Task 1: Shoe Store System
│       │   ├── task2.html                        # Task 2: Library System
│       │   └── task3.html                        # Task 3: Statistical Functions
│       └── README.md
│
└── Original Assignment
    └── SE302_Homework01 1.pdf
```

---

## 🚀 Quick Start

### Running the Unified Web Application

**All three tasks in one application!**

```bash
cd web_app
python3 app.py
```

**Open browser:** http://localhost:5000

**Main Dashboard:**
- Choose which system to test (Task 1, Task 2, or Task 3)
- Easy navigation between all three tasks
- Single unified interface

**Test Users (for Task 2 - Library System):**
- `john_doe` / `pass123`
- `jane_smith` / `pass123` (already has 5 books)
- `alice_brown` / `pass123`
- `mary_jones` / `pass123`

### Running Unit Tests (Task 3)
```bash
python3 test_stats_utils.py
```

---

## ✅ Requirements Met

### Task 1: Equivalence Class Testing
- ✅ 28 equivalence classes identified
- ✅ 25 test cases covering all classes
- ✅ 100% coverage achieved
- ✅ **Web App**: Interactive validation system

### Task 2: Library System Testing
- ✅ User story with extensions
- ✅ 12 test scenarios
- ✅ 19 test cases (12 main + 7 extensions)
- ✅ 100% requirement traceability
- ✅ **Web App**: Full library system with login, search, borrow, return

### Task 3: Statistical Functions Testing
- ✅ 25 unit tests
- ✅ 4 bugs identified and fixed
- ✅ 100% code coverage
- ✅ **Web App**: Interactive statistical calculator

---

## 🎯 Features

### Unified Web Application
- ✅ **Main Dashboard** - Choose which system to test
- ✅ **Task 1: Shoe Store** - Real-time input validation, equivalence class coverage
- ✅ **Task 2: Library System** - Complete library management (login, search, borrow, return)
- ✅ **Task 3: Statistical Functions** - Interactive calculator and test case execution
- ✅ **Unified Interface** - All three tasks in one application
- ✅ **Easy Navigation** - Switch between tasks seamlessly

---

## 📊 Test Coverage

| Task | Test Cases | Coverage | Status |
|------|------------|----------|--------|
| **Task 1** | 25 | 100% (28/28 ECs) | ✅ Complete |
| **Task 2** | 19 | 100% (10/10 ACs) | ✅ Complete |
| **Task 3** | 25 | 100% (Code/Branch/Func) | ✅ Complete |

---

## 🔧 Requirements

- Python 3.6+
- Flask (`pip install flask`)

---

## 📝 Documentation

All required homework documents are included:
- Task 1: Equivalence class testing documentation
- Task 2: User story, scenarios, and test cases
- Task 3: Unit tests and bug report

---

## 🎓 Next-Level Enhancements

The web applications demonstrate:
- ✅ Real-world implementation of test cases
- ✅ Interactive testing of all scenarios
- ✅ Visual feedback and validation
- ✅ Complete system functionality
- ✅ Professional user interface

---

## 📧 Contact

For questions about this submission, please refer to the homework documents.

---

**Status:** ✅ Complete and Ready for Submission  
**Quality Level:** Production-Ready  
**Last Updated:** 2024
