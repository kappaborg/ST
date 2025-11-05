// ============================================
// Task 1: Shoe Store Validation
// ============================================

function validateShoeEntry(line) {
    // Check for empty input first
    if (!line || !line.trim()) {
        return {valid: false, error: "Empty line", covered_classes: ["EC28"]};
    }
    
    // Clean input and split
    const cleaned = line.trim();
    const parts = cleaned.split(',').map(p => p.trim());
    
    // Must have at least name and one size
    if (parts.length < 2) {
        return {valid: false, error: "No sizes provided", covered_classes: ["EC23"]};
    }
    
    const itemName = parts[0];
    const sizes = parts.slice(1);
    
    if (!itemName) {
        return {valid: false, error: "Empty item name", covered_classes: ["EC17"]};
    }
    
    if (itemName.length < 2) {
        return {valid: false, error: "Item name too short (minimum 2 characters)", covered_classes: ["EC13"]};
    }
    
    if (itemName.length > 15) {
        return {valid: false, error: "Item name too long (maximum 15 characters)", covered_classes: ["EC14"]};
    }
    
    if (!/^[a-zA-Z]+$/.test(itemName)) {
        if (/\d/.test(itemName)) {
            return {valid: false, error: "Item name contains numeric characters", covered_classes: ["EC15"]};
        } else {
            return {valid: false, error: "Item name contains special characters", covered_classes: ["EC16"]};
        }
    }
    
    if (sizes.length > 5) {
        return {valid: false, error: "Too many sizes (maximum 5 allowed)", covered_classes: ["EC22"]};
    }
    
    // Keep track of valid sizes and equivalence classes
    const validSizes = [];
    const eqClasses = [];
    
    // Determine name length equivalence class
    const nameLen = itemName.length;
    if (nameLen === 2) {
        eqClasses.push("EC1");
    } else if (nameLen === 15) {
        eqClasses.push("EC3");
    } else {
        eqClasses.push("EC2");
    }
    
    // Check size count equivalence class
    const sizeCount = sizes.length;
    if (sizeCount === 1) {
        eqClasses.push("EC7");
    } else if (sizeCount === 5) {
        eqClasses.push("EC9");
    } else {
        eqClasses.push("EC8");
    }
    
    // Go through each size and validate
    for (const sizeStr of sizes) {
        if (sizeStr.includes('.')) {
            return {valid: false, error: `Size '${sizeStr}' contains decimal point`, covered_classes: ["EC20"]};
        }
        
        if (!/^\d+$/.test(sizeStr)) {
            return {valid: false, error: `Size '${sizeStr}' contains alphabetic characters`, covered_classes: ["EC21"]};
        }
        
        const size = parseInt(sizeStr, 10);
        
        if (size < 26) {
            return {valid: false, error: `Size ${size} is below minimum (26)`, covered_classes: ["EC18"]};
        }
        
        if (size > 55) {
            return {valid: false, error: `Size ${size} is above maximum (55)`, covered_classes: ["EC19"]};
        }
        
        // Size range equivalence classes
        if (size === 26) {
            eqClasses.push("EC4");
        } else if (size === 55) {
            eqClasses.push("EC6");
        } else {
            eqClasses.push("EC5");
        }
        
        validSizes.push(size);
    }
    
    // Check if sizes are in ascending order (required)
    const sorted = [...validSizes].sort((a, b) => a - b);
    if (JSON.stringify(validSizes) !== JSON.stringify(sorted)) {
        return {valid: false, error: "Sizes must be in ascending order", covered_classes: ["EC24"]};
    }
    
    // Add equivalence classes for valid cases
    eqClasses.push("EC10");  // ascending order
    eqClasses.push("EC11");  // comma separation
    
    // Spaces around commas are okay (should be ignored per spec)
    if (line.includes(' , ') || line.includes(', ') || line.includes(' ,')) {
        eqClasses.push("EC12");
    }
    
    // Return success with all info
    return {
        valid: true,
        item_name: itemName,
        sizes: validSizes,
        covered_classes: [...new Set(eqClasses)].sort()  // remove duplicates and sort
    };
}

const testUsers = {
    'user1': {password: 'IUS1', borrowed_books: []},
    'user2': {password: 'IUS2', borrowed_books: ['Book A', 'Book B', 'Book C', 'Book D', 'Book E']},
    'user3': {password: 'IUS3', borrowed_books: []},
    'kappasutra': {password: 'admin', borrowed_books: []}
};

const books = {
    'The Hobbit': {title: 'The Hobbit', author: 'J.R.R. Tolkien', isbn: '978-0547928227', status: 'Available', borrowed_by: null},
    '1984': {title: '1984', author: 'George Orwell', isbn: '978-0451524935', status: 'Available', borrowed_by: null},
    'Pride and Prejudice': {title: 'Pride and Prejudice', author: 'Jane Austen', isbn: '978-0141439518', status: 'Borrowed', borrowed_by: 'user1'},
    'To Kill a Mockingbird': {title: 'To Kill a Mockingbird', author: 'Harper Lee', isbn: '978-0061120084', status: 'Borrowed', borrowed_by: 'kappasutra'},
    'The Great Gatsby': {title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', isbn: '978-0743273565', status: 'Available', borrowed_by: null},
    'The Catcher in the Rye': {title: 'The Catcher in the Rye', author: 'J.D. Salinger', isbn: '978-0316769174', status: 'Available', borrowed_by: null},
    'Book1': {title: 'Book1', author: 'Author1', isbn: '978-0000000001', status: 'Available', borrowed_by: null},
    'Book2': {title: 'Book2', author: 'Author2', isbn: '978-0000000002', status: 'Available', borrowed_by: null},
    'Book3': {title: 'Book3', author: 'Author3', isbn: '978-0000000003', status: 'Available', borrowed_by: null},
    'Book4': {title: 'Book4', author: 'Author4', isbn: '978-0000000004', status: 'Available', borrowed_by: null},
    'Book5': {title: 'Book5', author: 'Author5', isbn: '978-0000000005', status: 'Available', borrowed_by: null}
};

// Initialize localStorage
function initLibraryStorage() {
    if (!localStorage.getItem('library_books')) {
        localStorage.setItem('library_books', JSON.stringify(books));
    }
    if (!localStorage.getItem('library_users')) {
        localStorage.setItem('library_users', JSON.stringify(testUsers));
    }
}

// Get current user from localStorage
function getCurrentUser() {
    const user = localStorage.getItem('current_user');
    return user ? JSON.parse(user) : null;
}

function setCurrentUser(username) {
    if (username) {
        localStorage.setItem('current_user', JSON.stringify(username));
    } else {
        localStorage.removeItem('current_user');
    }
}

// Library functions
function loginLibrary(username, password) {
    initLibraryStorage();
    const users = JSON.parse(localStorage.getItem('library_users'));
    
    if (users[username] && users[username].password === password) {
        setCurrentUser(username);
        return {success: true, username: username};
    }
    return {success: false, message: 'Invalid username or password'};
}

function logoutLibrary() {
    setCurrentUser(null);
    return {success: true};
}

function borrowBook(bookTitle) {
    const user = getCurrentUser();
    if (!user) {
        return {success: false, message: 'You must be logged in to borrow books.'};
    }
    
    initLibraryStorage();
    const users = JSON.parse(localStorage.getItem('library_users'));
    const booksData = JSON.parse(localStorage.getItem('library_books'));
    
    if (!booksData[bookTitle]) {
        return {success: false, message: `Book "${bookTitle}" not found in catalog.`};
    }
    
    const userBooks = users[user].borrowed_books || [];
    
    if (userBooks.includes(bookTitle)) {
        return {success: false, message: 'You have already borrowed this book. You cannot borrow the same book twice.'};
    }
    
    if (userBooks.length >= 5) {
        return {success: false, message: 'You have reached the maximum borrowing limit of 5 books. Please return a book before borrowing another.'};
    }
    
    const book = booksData[bookTitle];
    if (book.status !== 'Available') {
        return {success: false, message: `Book "${bookTitle}" is currently not available. It has been borrowed by another user.`};
    }
    
    // Update book status
    book.status = 'Borrowed';
    book.borrowed_by = user;
    userBooks.push(bookTitle);
    
    // Save to localStorage
    booksData[bookTitle] = book;
    users[user].borrowed_books = userBooks;
    localStorage.setItem('library_books', JSON.stringify(booksData));
    localStorage.setItem('library_users', JSON.stringify(users));
    
    return {success: true, message: `Book "${bookTitle}" successfully borrowed.`, borrowed_count: userBooks.length};
}

function returnBook(bookTitle) {
    const user = getCurrentUser();
    if (!user) {
        return {success: false, message: 'You must be logged in to return books.'};
    }
    
    initLibraryStorage();
    const users = JSON.parse(localStorage.getItem('library_users'));
    const booksData = JSON.parse(localStorage.getItem('library_books'));
    
    if (!booksData[bookTitle]) {
        return {success: false, message: `Book "${bookTitle}" not found.`};
    }
    
    const userBooks = users[user].borrowed_books || [];
    
    if (!userBooks.includes(bookTitle)) {
        return {success: false, message: 'You cannot return a book that you have not borrowed.'};
    }
    
    // Update book status
    const book = booksData[bookTitle];
    book.status = 'Available';
    book.borrowed_by = null;
    const index = userBooks.indexOf(bookTitle);
    userBooks.splice(index, 1);
    
    // Save to localStorage
    booksData[bookTitle] = book;
    users[user].borrowed_books = userBooks;
    localStorage.setItem('library_books', JSON.stringify(booksData));
    localStorage.setItem('library_users', JSON.stringify(users));
    
    return {success: true, message: `Book "${bookTitle}" successfully returned.`};
}

function searchBooks(query, searchType) {
    initLibraryStorage();
    const booksData = JSON.parse(localStorage.getItem('library_books'));
    const results = [];
    
    for (const key in booksData) {
        const book = booksData[key];
        let matches = false;
        
        if (searchType === 'title' && book.title.toLowerCase().includes(query.toLowerCase())) {
            matches = true;
        } else if (searchType === 'author' && book.author.toLowerCase().includes(query.toLowerCase())) {
            matches = true;
        } else if (searchType === 'isbn' && book.isbn.includes(query)) {
            matches = true;
        }
        
        if (matches) {
            results.push(book);
        }
    }
    
    return {success: true, results: results, count: results.length};
}

function getMyBooks() {
    const user = getCurrentUser();
    if (!user) {
        return {success: false, books: [], count: 0};
    }
    
    initLibraryStorage();
    const users = JSON.parse(localStorage.getItem('library_users'));
    const userBooks = users[user].borrowed_books || [];
    
    return {success: true, books: userBooks, count: userBooks.length};
}

function getCatalog() {
    initLibraryStorage();
    const booksData = JSON.parse(localStorage.getItem('library_books'));
    return {success: true, books: Object.values(booksData)};
}

// ============================================
// Task 3: Statistical Functions
// ============================================

function mean(numbers) {
    if (!numbers || numbers.length === 0) {
        return 0;
    }
    const total = numbers.reduce((sum, n) => sum + n, 0);
    return total / numbers.length;
}

function median(numbers) {
    if (!numbers || numbers.length === 0) {
        return 0;
    }
    const sorted = [...numbers].sort((a, b) => a - b);
    const mid = Math.floor(sorted.length / 2);
    if (sorted.length % 2 === 0) {
        return (sorted[mid] + sorted[mid - 1]) / 2;
    } else {
        return sorted[mid];
    }
}

function mode(numbers) {
    if (!numbers || numbers.length === 0) {
        return null;
    }
    const freq = {};
    for (const n of numbers) {
        freq[n] = (freq[n] || 0) + 1;
    }
    let maxFreq = 0;
    let modes = [];
    for (const key in freq) {
        if (freq[key] > maxFreq) {
            maxFreq = freq[key];
            modes = [parseFloat(key)];
        } else if (freq[key] === maxFreq) {
            modes.push(parseFloat(key));
        }
    }
    return modes[0];
}

function rangeList(numbers) {
    if (!numbers || numbers.length === 0) {
        return 0;
    }
    return Math.max(...numbers) - Math.min(...numbers);
}

function removeOutliers(numbers, threshold = 2) {
    if (!numbers || numbers.length < 2) {
        return [...(numbers || [])];
    }
    
    // Use IQR (Interquartile Range) method which is more robust to extreme outliers
    const sorted = [...numbers].sort((a, b) => a - b);
    const n = sorted.length;
    
    // Calculate quartiles
    const q1Idx = Math.floor(n / 4);
    const q3Idx = Math.floor(3 * n / 4);
    const q1 = sorted[q1Idx];
    const q3 = sorted[q3Idx];
    
    // Calculate IQR
    const iqr = q3 - q1;
    
    if (iqr === 0) {
        // If IQR is 0, fall back to standard deviation method
        const avg = mean(numbers);
        const variance = numbers.reduce((sum, x) => sum + Math.pow(x - avg, 2), 0) / numbers.length;
        const stdDev = Math.sqrt(variance);
        if (stdDev === 0) {
            return [...numbers];
        }
        const result = [];
        for (const n of numbers) {
            if (Math.abs(n - avg) <= threshold * stdDev) {
                result.push(n);
            }
        }
        return result;
    }
    
    // Calculate bounds using IQR method
    const lowerBound = q1 - threshold * iqr;
    const upperBound = q3 + threshold * iqr;
    
    // Filter numbers within bounds
    const result = [];
    for (const n of numbers) {
        if (n >= lowerBound && n <= upperBound) {
            result.push(n);
        }
    }
    
    return result;
}

// ============================================
// Test Cases for Statistics
// ============================================

const testCases = {
    'mean_normal': {
        function: 'mean',
        numbers: [1, 2, 3, 4, 5],
        expected: 3.0,
        description: 'Mean of [1, 2, 3, 4, 5]'
    },
    'mean_empty': {
        function: 'mean',
        numbers: [],
        expected: 0,
        description: 'Mean of empty list'
    },
    'median_even': {
        function: 'median',
        numbers: [1, 2, 3, 4],
        expected: 2.5,
        description: 'Median of [1, 2, 3, 4] (even length)'
    },
    'median_odd': {
        function: 'median',
        numbers: [1, 2, 3, 4, 5],
        expected: 3,
        description: 'Median of [1, 2, 3, 4, 5] (odd length)'
    },
    'mode_single': {
        function: 'mode',
        numbers: [1, 2, 2, 3],
        expected: 2,
        description: 'Mode of [1, 2, 2, 3]'
    },
    'range_normal': {
        function: 'range',
        numbers: [10, 2, 7, 5],
        expected: 8,
        description: 'Range of [10, 2, 7, 5]'
    },
    'outliers_normal': {
        function: 'outliers',
        numbers: [1, 2, 3, 100],
        threshold: 2,
        description: 'Remove outliers from [1, 2, 3, 100]'
    }
};

function calculateStats(numbersStr, functionName, threshold = 2) {
    try {
        // Parse the input string
        const numList = numbersStr.replace(/,/g, ' ').split(/\s+/)
            .filter(s => s.trim())
            .map(s => parseFloat(s.trim()))
            .filter(n => !isNaN(n));
        
        if (numList.length === 0) {
            return {success: false, error: 'Please enter at least one number'};
        }
        
        const result = {};
        let value;
        
        // Figure out which function to call
        if (functionName === 'mean') {
            value = mean(numList);
            result.description = `Mean of ${numList.length} numbers`;
        } else if (functionName === 'median') {
            value = median(numList);
            result.description = `Median of ${numList.length} numbers`;
        } else if (functionName === 'mode') {
            value = mode(numList);
            result.value = value !== null ? value : 'No mode (all values unique)';
            result.description = `Mode of ${numList.length} numbers`;
            return {success: true, result: result, input: numList};
        } else if (functionName === 'range') {
            value = rangeList(numList);
            result.description = `Range (max - min) of ${numList.length} numbers`;
        } else if (functionName === 'outliers') {
            const filtered = removeOutliers(numList, threshold);
            value = filtered;
            result.description = `Numbers after removing outliers (threshold: ${threshold} std dev)`;
            result.original_count = numList.length;
            result.filtered_count = filtered.length;
            result.removed_count = result.original_count - result.filtered_count;
        }
        
        result.value = value;
        return {success: true, result: result, input: numList};
        
    } catch (error) {
        return {success: false, error: error.message};
    }
}

function runTest(testCaseId) {
    const tc = testCases[testCaseId];
    if (!tc) {
        return {success: false, error: 'Test case not found'};
    }
    
    const numList = tc.numbers;
    let actual;
    
    // Execute the function for this test case
    if (tc.function === 'mean') {
        actual = mean(numList);
    } else if (tc.function === 'median') {
        actual = median(numList);
    } else if (tc.function === 'mode') {
        actual = mode(numList);
    } else if (tc.function === 'range') {
        actual = rangeList(numList);
    } else if (tc.function === 'outliers') {
        actual = removeOutliers(numList, tc.threshold || 2);
    }
    
    // Compare with expected result
    const expected = tc.expected;
    let passed = null;
    if (expected !== undefined) {
        if (Array.isArray(actual) && Array.isArray(expected)) {
            passed = JSON.stringify(actual.sort()) === JSON.stringify(expected.sort());
        } else {
            passed = Math.abs(actual - expected) < 0.0001;  // Float comparison
        }
    }
    
    return {
        success: true,
        test_case: tc,
        actual: actual,
        expected: expected !== undefined ? expected : 'N/A',
        passed: passed
    };
}

