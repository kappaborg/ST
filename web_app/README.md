# Unified Web Application - SE302 Homework 01
## All Three Tasks in One Web Interface

---

## 🚀 Quick Start

### Prerequisites
```bash
pip3 install flask
```

### Run the Application
```bash
cd web_app
python3 app.py
```

### Open in Browser
```
http://localhost:5000
```

---

## 📋 Features

### Main Dashboard
- Choose which system to test
- Clean, unified interface
- Easy navigation between tasks

### Task 1: Shoe Store System
- Real-time input validation
- Shows equivalence classes covered
- Test all 25 test cases interactively
- Access: http://localhost:5000/task1

### Task 2: Library System
- User authentication (login/logout)
- Search books (title, author, ISBN)
- Borrow books with all acceptance criteria
- Return books
- View borrowed books
- Test all 19 test cases interactively
- Access: http://localhost:5000/task2

**Test Users:**
- `john_doe` / `pass123`
- `jane_smith` / `pass123` (has 5 books - test limit)
- `alice_brown` / `pass123`
- `mary_jones` / `pass123`

### Task 3: Statistical Functions
- Interactive calculator for all functions
- Mean, median, mode, range, outliers
- Predefined test case execution
- Visual test results (pass/fail)
- Access: http://localhost:5000/task3

---

## 🎯 API Endpoints

### Task 1
- `POST /api/task1/validate` - Validate shoe entry

### Task 2
- `POST /api/task2/login` - User login
- `POST /api/task2/logout` - User logout
- `GET /api/task2/check_login` - Check login status
- `POST /api/task2/borrow` - Borrow a book
- `POST /api/task2/return` - Return a book
- `POST /api/task2/search` - Search books
- `GET /api/task2/my_books` - Get user's borrowed books
- `GET /api/task2/catalog` - Get all books

### Task 3
- `POST /api/task3/calculate` - Calculate statistical function
- `POST /api/task3/test_case` - Run predefined test case

---

## 📁 File Structure

```
web_app/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Main dashboard
│   ├── task1.html        # Task 1: Shoe Store System
│   ├── task2.html        # Task 2: Library System
│   └── task3.html        # Task 3: Statistical Functions
└── README.md             # This file
```

---

## ✅ Benefits

1. **Single Application** - All three tasks in one place
2. **Easy Navigation** - Main menu to choose which to test
3. **Unified Interface** - Consistent design across all tasks
4. **Single Port** - One port (5000) instead of three
5. **Better Organization** - All API routes organized by task

---

## 🎓 Usage

1. Start the application: `python3 app.py`
2. Open browser: http://localhost:5000
3. Click on the system you want to test
4. Test all scenarios interactively
5. Use "Back to Main Menu" to switch between tasks

---

**Status:** ✅ Ready to Use

