# SE302 Homework 01 - Web Application
# Combined all three tasks into one interface for easier testing

from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import sys
import os

# Adding parent directory to import stats_utils
# This is a bit hacky but works for this project structure
parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_path)
from stats_utils import mean, median, mode, range_list, remove_outliers

app = Flask(__name__)
# TODO: move to env var later
app.secret_key = 'se302_homework_secret_key_2025'

# Task 1: Shoe store validation logic
# Implemented based on the homework requirements

def validate_shoe_entry(line):
    """
    Validates shoe entry - checks format, name length, sizes, etc.
    Returns a dict with validation result and error messages
    """
    # Check for empty input first
    if not line or not line.strip():
        return {"valid": False, "error": "Empty line", "covered_classes": ["EC28"]}
    
    # Clean input and split
    cleaned = line.strip()
    parts = [p.strip() for p in cleaned.split(',')]
    
    # Must have at least name and one size
    if len(parts) < 2:
        return {"valid": False, "error": "No sizes provided", "covered_classes": ["EC23"]}
    
    item_name = parts[0]
    sizes = parts[1:]  # everything after first comma
    
    if not item_name:
        return {"valid": False, "error": "Empty item name", "covered_classes": ["EC17"]}
    
    if len(item_name) < 2:
        return {"valid": False, "error": "Item name too short (minimum 2 characters)", "covered_classes": ["EC13"]}
    
    if len(item_name) > 15:
        return {"valid": False, "error": "Item name too long (maximum 15 characters)", "covered_classes": ["EC14"]}
    
    if not item_name.isalpha():
        if any(char.isdigit() for char in item_name):
            return {"valid": False, "error": "Item name contains numeric characters", "covered_classes": ["EC15"]}
        else:
            return {"valid": False, "error": "Item name contains special characters", "covered_classes": ["EC16"]}
    
    if len(sizes) > 5:
        return {"valid": False, "error": "Too many sizes (maximum 5 allowed)", "covered_classes": ["EC22"]}
    
    # Keep track of valid sizes and equivalence classes
    valid_sizes = []
    eq_classes = []
    
    # Determine name length equivalence class
    name_len = len(item_name)
    if name_len == 2:
        eq_classes.append("EC1")
    elif name_len == 15:
        eq_classes.append("EC3")
    else:
        eq_classes.append("EC2")
    
    # Check size count equivalence class
    size_count = len(sizes)
    if size_count == 1:
        eq_classes.append("EC7")
    elif size_count == 5:
        eq_classes.append("EC9")
    else:
        eq_classes.append("EC8")
    
    # Go through each size and validate
    for size_str in sizes:
        if '.' in size_str:
            return {"valid": False, "error": f"Size '{size_str}' contains decimal point", "covered_classes": ["EC20"]}
        
        if not size_str.isdigit():
            return {"valid": False, "error": f"Size '{size_str}' contains alphabetic characters", "covered_classes": ["EC21"]}
        
        try:
            size = int(size_str)
        except ValueError:
            return {"valid": False, "error": f"Invalid size format: '{size_str}'", "covered_classes": ["EC21"]}
        
        if size < 26:
            return {"valid": False, "error": f"Size {size} is below minimum (26)", "covered_classes": ["EC18"]}
        
        if size > 55:
            return {"valid": False, "error": f"Size {size} is above maximum (55)", "covered_classes": ["EC19"]}
        
        # Size range equivalence classes
        if size == 26:
            eq_classes.append("EC4")
        elif size == 55:
            eq_classes.append("EC6")
        else:
            eq_classes.append("EC5")
        
        valid_sizes.append(size)
    
    # Check if sizes are in ascending order (required)
    if valid_sizes != sorted(valid_sizes):
        return {"valid": False, "error": "Sizes must be in ascending order", "covered_classes": ["EC24"]}
    
    # Add equivalence classes for valid cases
    eq_classes.append("EC10")  # ascending order
    eq_classes.append("EC11")  # comma separation
    
    # Spaces around commas are okay (should be ignored per spec)
    if ' , ' in line or ', ' in line or ' ,' in line:
        eq_classes.append("EC12")
    
    # Return success with all info
    return {
        "valid": True,
        "item_name": item_name,
        "sizes": valid_sizes,
        "covered_classes": sorted(set(eq_classes))  # remove duplicates and sort
    }

# Task 2: Library System
# Using simple in-memory storage for now
# In a real app I'd use a database like PostgreSQL or MongoDB

# Test users - created these to test different scenarios
users = {
    'john_doe': {'password': 'pass123', 'borrowed_books': []},
    'jane_smith': {'password': 'pass123', 'borrowed_books': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E']},  # maxed out
    'alice_brown': {'password': 'pass123', 'borrowed_books': []},
    'mary_jones': {'password': 'pass123', 'borrowed_books': []}
}

# Sample book catalog
books = {
    'The Hobbit': {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'isbn': '978-0547928227', 'status': 'Available', 'borrowed_by': None},
    '1984': {'title': '1984', 'author': 'George Orwell', 'isbn': '978-0451524935', 'status': 'Available', 'borrowed_by': None},
    'Pride and Prejudice': {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'isbn': '978-0141439518', 'status': 'Borrowed', 'borrowed_by': 'john_doe'},
    'To Kill a Mockingbird': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '978-0061120084', 'status': 'Borrowed', 'borrowed_by': 'mary_jones'},
    'The Great Gatsby': {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '978-0743273565', 'status': 'Available', 'borrowed_by': None},
    'The Catcher in the Rye': {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'isbn': '978-0316769174', 'status': 'Available', 'borrowed_by': None},
    'Book1': {'title': 'Book1', 'author': 'Author1', 'isbn': '978-0000000001', 'status': 'Available', 'borrowed_by': None},
    'Book2': {'title': 'Book2', 'author': 'Author2', 'isbn': '978-0000000002', 'status': 'Available', 'borrowed_by': None},
    'Book3': {'title': 'Book3', 'author': 'Author3', 'isbn': '978-0000000003', 'status': 'Available', 'borrowed_by': None},
    'Book4': {'title': 'Book4', 'author': 'Author4', 'isbn': '978-0000000004', 'status': 'Available', 'borrowed_by': None},
    'Book5': {'title': 'Book5', 'author': 'Author5', 'isbn': '978-0000000005', 'status': 'Available', 'borrowed_by': None},
}

# Routes for rendering pages

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')

@app.route('/task1')
def task1():
    """Shoe store validation page"""
    return render_template('task1.html')

@app.route('/task2')
def task2():
    """Library management page"""
    return render_template('task2.html')

@app.route('/task3')
def task3():
    """Statistics calculator page"""
    return render_template('task3.html')

# API endpoints

# Task 1 endpoints
@app.route('/api/task1/validate', methods=['POST'])
def validate_shoe():
    """API endpoint for validating shoe entries"""
    data = request.json
    input_line = data.get('input', '')
    result = validate_shoe_entry(input_line)
    return jsonify(result)

# API endpoints for Task 2 - Library System

@app.route('/api/task2/login', methods=['POST'])
def login():
    """Handle user login"""
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    
    # Check if user exists and password matches
    if username in users and users[username]['password'] == password:
        session['username'] = username
        session['logged_in'] = True
        return jsonify({
            'success': True,
            'message': f'Welcome, {username}!',
            'username': username
        })
    return jsonify({
        'success': False,
        'message': 'Invalid username or password'
    })

@app.route('/api/task2/logout', methods=['POST'])
def logout():
    """Handle user logout"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

@app.route('/api/task2/check_login')
def check_login():
    """Check if user is logged in"""
    return jsonify({
        'logged_in': session.get('logged_in', False),
        'username': session.get('username', None)
    })

@app.route('/api/task2/borrow', methods=['POST'])
def borrow():
    """Handle book borrowing - checks all the acceptance criteria"""
    # First check if user is logged in
    if not session.get('logged_in'):
        return jsonify({
            'success': False,
            'message': 'You must be logged in to borrow books.',
            'test_scenario': 'TS2',
            'test_case': 'TC2.1'
        })
    
    username = session.get('username')
    data = request.json
    book_title = data.get('book_title', '')
    
    # Check if book exists
    if book_title not in books:
        return jsonify({
            'success': False,
            'message': f'Book "{book_title}" not found in catalog.'
        })
    
    book = books[book_title]
    user_books = users[username]['borrowed_books']
    
    # Check if user already borrowed this book
    if book_title in user_books:
        return jsonify({
            'success': False,
            'message': 'You have already borrowed this book. You cannot borrow the same book twice.',
            'test_scenario': 'TS5',
            'test_case': 'TC5.1'
        })
    
    # Check if user has reached the 5 book limit
    if len(user_books) >= 5:
        return jsonify({
            'success': False,
            'message': 'You have reached the maximum borrowing limit of 5 books. Please return a book before borrowing another.',
            'test_scenario': 'TS3',
            'test_case': 'TC3.1'
        })
    
    # Check if book is available
    if book['status'] != 'Available':
        return jsonify({
            'success': False,
            'message': f'Book "{book_title}" is currently not available. It has been borrowed by another user.',
            'test_scenario': 'TS4',
            'test_case': 'TC4.1'
        })
    
    # All checks passed - borrow the book
    book['status'] = 'Borrowed'
    book['borrowed_by'] = username
    user_books.append(book_title)
    
    return jsonify({
        'success': True,
        'message': f'Book "{book_title}" successfully borrowed.',
        'book': book,
        'borrowed_count': len(user_books),
        'test_scenario': 'TS1',
        'test_case': 'TC1.1'
    })

@app.route('/api/task2/return', methods=['POST'])
def return_book():
    """Handle book return"""
    if not session.get('logged_in'):
        return jsonify({
            'success': False,
            'message': 'You must be logged in to return books.'
        })
    
    username = session.get('username')
    data = request.json
    book_title = data.get('book_title', '')
    
    if book_title not in books:
        return jsonify({
            'success': False,
            'message': f'Book "{book_title}" not found.'
        })
    
    user_books = users[username]['borrowed_books']
    
    # Check if user actually borrowed this book
    if book_title not in user_books:
        return jsonify({
            'success': False,
            'message': 'You cannot return a book that you have not borrowed.',
            'test_scenario': 'TS11',
            'test_case': 'TC11.1'
        })
    
    # Return the book
    book = books[book_title]
    book['status'] = 'Available'
    book['borrowed_by'] = None
    user_books.remove(book_title)
    
    return jsonify({
        'success': True,
        'message': f'Book "{book_title}" successfully returned.',
        'test_scenario': 'TS10',
        'test_case': 'TC10.1'
    })

@app.route('/api/task2/search', methods=['POST'])
def search():
    """Search books by title, author, or ISBN"""
    data = request.json
    query = data.get('query', '').lower()
    search_type = data.get('search_type', 'title')
    
    results = []
    # Search through all books
    for book in books.values():
        if search_type == 'title' and query in book['title'].lower():
            results.append(book)
        elif search_type == 'author' and query in book['author'].lower():
            results.append(book)
        elif search_type == 'isbn' and query in book['isbn'].lower():
            results.append(book)
    
    # Determine test scenario based on search type
    if search_type == 'title':
        ts = 'TS7'
        tc = 'TC7.1'
    elif search_type == 'author':
        ts = 'TS8'
        tc = 'TC8.1'
    else:
        ts = 'TS9'
        tc = 'TC9.1'
    
    return jsonify({
        'success': True,
        'results': results,
        'count': len(results),
        'test_scenario': ts,
        'test_case': tc
    })

@app.route('/api/task2/my_books')
def my_books():
    """Get user's borrowed books"""
    if not session.get('logged_in'):
        return jsonify({
            'success': False,
            'books': [],
            'count': 0
        })
    
    username = session.get('username')
    user_books = users[username]['borrowed_books']
    
    return jsonify({
        'success': True,
        'books': user_books,
        'count': len(user_books)
    })

@app.route('/api/task2/catalog')
def catalog():
    """Get all books in catalog"""
    return jsonify({
        'success': True,
        'books': list(books.values())
    })

# API endpoints for Task 3 - Statistical Functions

@app.route('/api/task3/calculate', methods=['POST'])
def calculate():
    """Calculate stats function on the given numbers"""
    data = request.json
    numbers_str = data.get('numbers', '')
    threshold = data.get('threshold', 2)
    func_name = data.get('function', 'mean')
    
    try:
        # Parse the input string - handles comma or space separated
        num_list = []
        for part in numbers_str.replace(',', ' ').split():
            try:
                num_list.append(float(part))
            except ValueError:
                return jsonify({
                    'success': False,
                    'error': f'Invalid number: {part}'
                })
        
        if not num_list:
            return jsonify({
                'success': False,
                'error': 'Please enter at least one number'
            })
        
        result = {}
        
        # Figure out which function to call
        if func_name == 'mean':
            result['value'] = mean(num_list)
            result['description'] = f'Mean of {len(num_list)} numbers'
        elif func_name == 'median':
            result['value'] = median(num_list)
            result['description'] = f'Median of {len(num_list)} numbers'
        elif func_name == 'mode':
            mode_val = mode(num_list)
            result['value'] = mode_val if mode_val is not None else 'No mode (all values unique)'
            result['description'] = f'Mode of {len(num_list)} numbers'
        elif func_name == 'range':
            result['value'] = range_list(num_list)
            result['description'] = f'Range (max - min) of {len(num_list)} numbers'
        elif func_name == 'outliers':
            filtered = remove_outliers(num_list, threshold)
            result['value'] = filtered
            result['description'] = f'Numbers after removing outliers (threshold: {threshold} std dev)'
            result['original_count'] = len(num_list)
            result['filtered_count'] = len(filtered)
            result['removed_count'] = result['original_count'] - result['filtered_count']
        
        return jsonify({
            'success': True,
            'result': result,
            'input': num_list
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/task3/test_case', methods=['POST'])
def test_case():
    """Run one of the predefined test cases"""
    data = request.json
    test_case_id = data.get('test_case', '')
    
    # Test cases from the homework assignment
    test_cases = {
        'mean_normal': {
            'function': 'mean',
            'numbers': [1, 2, 3, 4, 5],
            'expected': 3.0,
            'description': 'Mean of [1, 2, 3, 4, 5]'
        },
        'mean_empty': {
            'function': 'mean',
            'numbers': [],
            'expected': 0,
            'description': 'Mean of empty list'
        },
        'median_even': {
            'function': 'median',
            'numbers': [1, 2, 3, 4],
            'expected': 2.5,
            'description': 'Median of [1, 2, 3, 4] (even length)'
        },
        'median_odd': {
            'function': 'median',
            'numbers': [1, 2, 3, 4, 5],
            'expected': 3,
            'description': 'Median of [1, 2, 3, 4, 5] (odd length)'
        },
        'mode_single': {
            'function': 'mode',
            'numbers': [1, 2, 2, 3],
            'expected': 2,
            'description': 'Mode of [1, 2, 2, 3]'
        },
        'range_normal': {
            'function': 'range',
            'numbers': [10, 2, 7, 5],
            'expected': 8,
            'description': 'Range of [10, 2, 7, 5] (max - min = 10 - 2 = 8)'
        },
        'outliers_normal': {
            'function': 'outliers',
            'numbers': [1, 2, 3, 100],
            'threshold': 2,
            'description': 'Remove outliers from [1, 2, 3, 100]'
        }
    }
    
    if test_case_id not in test_cases:
        return jsonify({
            'success': False,
            'error': 'Test case not found'
        })
    
    tc = test_cases[test_case_id]
    num_list = tc['numbers']
    
    # Execute the function for this test case
    if tc['function'] == 'mean':
        actual = mean(num_list)
    elif tc['function'] == 'median':
        actual = median(num_list)
    elif tc['function'] == 'mode':
        actual = mode(num_list)
    elif tc['function'] == 'range':
        actual = range_list(num_list)
    elif tc['function'] == 'outliers':
        actual = remove_outliers(num_list, tc.get('threshold', 2))
    
    # Compare with expected result
    expected = tc.get('expected', None)
    passed = None
    if expected is not None:
        passed = actual == expected
    
    return jsonify({
        'success': True,
        'test_case': tc,
        'actual': actual,
        'expected': expected if expected is not None else 'N/A',
        'passed': passed
    })

if __name__ == '__main__':
    # Running in debug mode for development
    app.run(debug=True, port=5000)

