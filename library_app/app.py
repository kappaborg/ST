from flask import Flask, render_template, request, jsonify, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'library_system_secret_key_2024'

#Defining users 
users = {
    'usr1': {'password': 'IUS1', 'borrowed_books': []},
    'usr2': {'password': 'IUS3', 'borrowed_books': []},
    'usr3': {'password': 'IUS4', 'borrowed_books': []},
    'kappasutra': {'password': 'admin', 'borrowed_books': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E']}
}
#Defining datas about books and so on
books = {
    'The Hobbit': {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'isbn': '978-0547928227', 'status': 'Available', 'borrowed_by': None},
    '1984': {'title': '1984', 'author': 'George Orwell', 'isbn': '978-0451524935', 'status': 'Available', 'borrowed_by': None},
    'Pride and Prejudice': {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'isbn': '978-0141439518', 'status': 'Borrowed', 'borrowed_by': 'user1'},
    'To Kill a Mockingbird': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '978-0061120084', 'status': 'Borrowed', 'borrowed_by': 'kappasutra'},
    'The Great Gatsby': {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '978-0743273565', 'status': 'Available', 'borrowed_by': None},
    'The Catcher in the Rye': {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'isbn': '978-0316769174', 'status': 'Available', 'borrowed_by': None},
    'Book1': {'title': 'Book1', 'author': 'Author1', 'isbn': '978-0000000001', 'status': 'Available', 'borrowed_by': None},
    'Book2': {'title': 'Book2', 'author': 'Author2', 'isbn': '978-0000000002', 'status': 'Available', 'borrowed_by': None},
    'Book3': {'title': 'Book3', 'author': 'Author3', 'isbn': '978-0000000003', 'status': 'Available', 'borrowed_by': None},
    'Book4': {'title': 'Book4', 'author': 'Author4', 'isbn': '978-0000000004', 'status': 'Available', 'borrowed_by': None},
    'Book5': {'title': 'Book5', 'author': 'Author5', 'isbn': '978-0000000005', 'status': 'Available', 'borrowed_by': None},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    
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

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

@app.route('/check_login')
def check_login():
    return jsonify({
        'logged_in': session.get('logged_in', False),
        'username': session.get('username', None)
    })

@app.route('/borrow', methods=['POST'])
def borrow():
    """Borrow a book - implements all acceptance criteria"""
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
    
    if book_title not in books:
        return jsonify({
            'success': False,
            'message': f'Book "{book_title}" not found in catalog.'
        })
    
    book = books[book_title]
    user_books = users[username]['borrowed_books']
    
    # AC5: Prevent duplicate borrowing
    if book_title in user_books:
        return jsonify({
            'success': False,
            'message': 'You have already borrowed this book. You cannot borrow the same book twice.',
            'test_scenario': 'TS5',
            'test_case': 'TC5.1'
        })
    
    # AC2: Maximum 5 books limit
    if len(user_books) >= 5:
        return jsonify({
            'success': False,
            'message': 'You have reached the maximum borrowing limit of 5 books. Please return a book before borrowing another.',
            'test_scenario': 'TS3',
            'test_case': 'TC3.1'
        })
    
    # AC3: Book must be available
    if book['status'] != 'Available':
        return jsonify({
            'success': False,
            'message': f'Book "{book_title}" is currently not available. It has been borrowed by another user.',
            'test_scenario': 'TS4',
            'test_case': 'TC4.1'
        })
    
    # AC1, AC3, AC4, AC6; Successfully borrow
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

@app.route('/return', methods=['POST'])
def return_book():
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
    
    # Check if user borrowed this book
    if book_title not in user_books:
        return jsonify({
            'success': False,
            'message': 'You cannot return a book that you have not borrowed.',
            'test_scenario': 'TS11',
            'test_case': 'TC11.1'
        })
    
    # Return book
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

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '').lower()
    search_type = data.get('search_type', 'title')  # title, author, or isbn
    
    results = []
    for book in books.values():
        if search_type == 'title' and query in book['title'].lower():
            results.append(book)
        elif search_type == 'author' and query in book['author'].lower():
            results.append(book)
        elif search_type == 'isbn' and query in book['isbn'].lower():
            results.append(book)
    
    return jsonify({
        'success': True,
        'results': results,
        'count': len(results),
        'test_scenario': f'TS{7 if search_type == "title" else 8 if search_type == "author" else 9}',
        'test_case': f'TC{7 if search_type == "title" else 8 if search_type == "author" else 9}.1'
    })

@app.route('/my_books')
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

@app.route('/catalog')
def catalog():
    """Get all books in catalog"""
    return jsonify({
        'success': True,
        'books': list(books.values())
    })

if __name__ == '__main__':
    app.run(debug=True, port=5002)

