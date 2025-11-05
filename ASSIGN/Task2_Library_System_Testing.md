# Task 2: User Story, Test Scenarios, and Test Cases for Library System
## SE302 Homework 01

---

## 1. User Story

**As a** registered library member  
**I want** to search for books, borrow available books, and return borrowed books  
**So that** I can access reading materials and manage my library account efficiently.

### Extended User Story (Including Search and Return)

**As a** registered library member  
**I want** to:
- Search for books by title, author, or ISBN
- Borrow available books from the library catalog
- Return books I have borrowed
- View my current borrowing status and history

**So that** I can:
- Find and access the books I need for reading or research
- Manage my library account and track my borrowed items
- Ensure other members can access books when I'm done with them
- Maintain a good borrowing record with the library

---

## 2. Acceptance Criteria

1. Users must be logged in to borrow a book.
2. Each user can borrow a maximum of five (5) books at once.
3. A book can be borrowed only if it is marked as "Available".
4. When borrowed, the book's status changes to "Borrowed".
5. The system should prevent a user from borrowing the same book twice.
6. Upon successful borrowing, the system must display a confirmation message: "Book '<Title>' successfully borrowed."
7. If borrowing is not possible, the system should display an appropriate error message.
8. Users can search for books by title, author, or ISBN.
9. Users can return books they have borrowed.
10. When returned, a book's status changes from "Borrowed" to "Available".

---

## 3. Test Scenarios

Based on the acceptance criteria, the following test scenarios have been derived:

| Scenario ID | Scenario Description | Acceptance Criteria Covered |
|-------------|----------------------|----------------------------|
| **TS1** | Borrowing a book when user is logged in and book is available | AC1, AC3, AC4, AC6 |
| **TS2** | Attempt to borrow a book when user is not logged in | AC1, AC7 |
| **TS3** | Attempt to borrow when user has reached maximum borrowing limit (5 books) | AC2, AC7 |
| **TS4** | Attempt to borrow a book that is already borrowed by another user | AC3, AC7 |
| **TS5** | Attempt to borrow the same book twice by the same user | AC5, AC7 |
| **TS6** | Borrowing multiple books (up to 5) successfully | AC2, AC3, AC4, AC6 |
| **TS7** | Search for books by title | AC8 |
| **TS8** | Search for books by author | AC8 |
| **TS9** | Search for books by ISBN | AC8 |
| **TS10** | Return a borrowed book successfully | AC9, AC10 |
| **TS11** | Attempt to return a book that was not borrowed by the user | AC9, AC10 |
| **TS12** | Attempt to return a book when user has no borrowed books | AC9, AC10 |

---

## 4. Detailed Test Cases

### Test Cases for Borrowing Functionality

#### TC1.1: Successful Book Borrowing (Logged In, Available Book)
**Scenario:** TS1  
**Preconditions/Test Data:**
- User "user1" is logged in
- Book "The Hobbit" is available in the system
- User has less than 5 books currently borrowed

**Test Steps:**
1. Log in as user "user1"
2. Search for "The Hobbit"
3. Click "Borrow" button for "The Hobbit"
4. Verify the book status and confirmation message

**Expected Result:**
- Book status changes to "Borrowed"
- Confirmation message displayed: "Book 'The Hobbit' successfully borrowed."
- Book appears in user's borrowed books list

**Actual Result:** _[To be filled during test execution]_

---

#### TC2.1: Attempt to Borrow When Not Logged In
**Scenario:** TS2  
**Preconditions/Test Data:**
- User is not logged in
- Book "1984" is available in the system

**Test Steps:**
1. Without logging in, navigate to book catalog
2. Search for "1984"
3. Click "Borrow" button for "1984"

**Expected Result:**
- Error message displayed: "You must be logged in to borrow books."
- Book status remains "Available"
- User is redirected to login page

**Actual Result:** _[To be filled during test execution]_

---

#### TC3.1: Attempt to Borrow When Maximum Limit Reached
**Scenario:** TS3  
**Preconditions/Test Data:**
- User "user2" is logged in
- User "user2" has already borrowed 5 books:
  - "Book A", "Book B", "Book C", "Book D", "Book E"
- Book "The Great Gatsby" is available

**Test Steps:**
1. Log in as user "user2"
2. Search for "The Great Gatsby"
3. Click "Borrow" button for "The Great Gatsby"

**Expected Result:**
- Error message displayed: "You have reached the maximum borrowing limit of 5 books. Please return a book before borrowing another."
- Book status remains "Available"
- Book is not added to user's borrowed books list

**Actual Result:** _[To be filled during test execution]_

---

#### TC4.1: Attempt to Borrow Already Borrowed Book
**Scenario:** TS4  
**Preconditions/Test Data:**
- User "user1" is logged in
- Book "To Kill a Mockingbird" is currently borrowed by user "kappasutra"
- Book status is "Borrowed"

**Test Steps:**
1. Log in as user "user1"
2. Search for "To Kill a Mockingbird"
3. Click "Borrow" button for "To Kill a Mockingbird"

**Expected Result:**
- Error message displayed: "Book 'To Kill a Mockingbird' is currently not available. It has been borrowed by another user."
- Book status remains "Borrowed"
- Book is not added to user's borrowed books list

**Actual Result:** _[To be filled during test execution]_

---

#### TC5.1: Attempt to Borrow Same Book Twice
**Scenario:** TS5  
**Preconditions/Test Data:**
- User "user1" is logged in
- User "user1" has already borrowed "Pride and Prejudice"
- Book "Pride and Prejudice" appears in user's borrowed list

**Test Steps:**
1. Log in as user "user1"
2. Search for "Pride and Prejudice"
3. Click "Borrow" button for "Pride and Prejudice"

**Expected Result:**
- Error message displayed: "You have already borrowed this book. You cannot borrow the same book twice."
- Book remains in user's borrowed list (no duplicate)
- Book status remains "Borrowed"

**Actual Result:** _[To be filled during test execution]_

---

#### TC6.1: Borrow Multiple Books Successfully (Up to 5)
**Scenario:** TS6  
**Preconditions/Test Data:**
- User "user3" is logged in
- User has no borrowed books currently
- Five books are available: "Book1", "Book2", "Book3", "Book4", "Book5"

**Test Steps:**
1. Log in as user "user3"
2. Search for and borrow "Book1"
3. Search for and borrow "Book2"
4. Search for and borrow "Book3"
5. Search for and borrow "Book4"
6. Search for and borrow "Book5"
7. Verify all books in borrowed list

**Expected Result:**
- All 5 books are successfully borrowed
- Confirmation messages displayed for each: "Book '<Title>' successfully borrowed."
- All 5 books appear in user's borrowed books list
- All book statuses change to "Borrowed"

**Actual Result:** _[To be filled during test execution]_

---

### Test Cases for Search Functionality

#### TC7.1: Search for Books by Title
**Scenario:** TS7  
**Preconditions/Test Data:**
- User is logged in (optional for search)
- Books in catalog: "The Catcher in the Rye", "The Great Gatsby", "1984"

**Test Steps:**
1. Navigate to search page
2. Enter "The Catcher in the Rye" in search field
3. Select "Search by Title"
4. Click "Search" button

**Expected Result:**
- Search results display "The Catcher in the Rye"
- Book details shown: title, author, ISBN, availability status
- Results are relevant to the search query

**Actual Result:** _[To be filled during test execution]_

---

#### TC8.1: Search for Books by Author
**Scenario:** TS8  
**Preconditions/Test Data:**
- User is logged in
- Books in catalog by "J.K. Rowling": "Harry Potter 1", "Harry Potter 2", etc.

**Test Steps:**
1. Navigate to search page
2. Enter "J.K. Rowling" in search field
3. Select "Search by Author"
4. Click "Search" button

**Expected Result:**
- Search results display all books by J.K. Rowling
- Multiple results shown if multiple books exist
- Author name matches the search query

**Actual Result:** _[To be filled during test execution]_

---

#### TC9.1: Search for Books by ISBN
**Scenario:** TS9  
**Preconditions/Test Data:**
- User is logged in
- Book with ISBN "978-0-7432-7356-5" exists in catalog

**Test Steps:**
1. Navigate to search page
2. Enter "978-0-7432-7356-5" in search field
3. Select "Search by ISBN"
4. Click "Search" button

**Expected Result:**
- Exact book with matching ISBN is displayed
- Book details shown: title, author, ISBN, availability status
- Single result or exact match returned

**Actual Result:** _[To be filled during test execution]_

---

### Test Cases for Return Functionality

#### TC10.1: Return a Borrowed Book Successfully
**Scenario:** TS10  
**Preconditions/Test Data:**
- User "user1" is logged in
- User "user1" has borrowed "The Hobbit"
- Book "The Hobbit" appears in user's borrowed list

**Test Steps:**
1. Log in as user "user1"
2. Navigate to "My Borrowed Books" section
3. Find "The Hobbit" in the list
4. Click "Return" button for "The Hobbit"
5. Confirm return action

**Expected Result:**
- Book status changes from "Borrowed" to "Available"
- Confirmation message displayed: "Book 'The Hobbit' successfully returned."
- Book is removed from user's borrowed books list
- Book appears as available in the catalog

**Actual Result:** _[To be filled during test execution]_

---

#### TC11.1: Attempt to Return Book Not Borrowed by User
**Scenario:** TS11  
**Preconditions/Test Data:**
- User "user1" is logged in
- Book "1984" is borrowed by user "kappasutra" (not by user1)
- Book "1984" does not appear in user1's borrowed list

**Test Steps:**
1. Log in as user "user1"
2. Search for "1984"
3. Try to access return functionality (if available)
4. Or attempt to return through direct URL manipulation

**Expected Result:**
- Error message displayed: "You cannot return a book that you have not borrowed."
- Book status remains "Borrowed"
- Book does not appear in user's borrowed list
- System prevents unauthorized return action

**Actual Result:** _[To be filled during test execution]_

---

#### TC12.1: Attempt to Return When User Has No Borrowed Books
**Scenario:** TS12  
**Preconditions/Test Data:**
- User "new_user" is logged in
- User "new_user" has no borrowed books
- "My Borrowed Books" list is empty

**Test Steps:**
1. Log in as user "new_user"
2. Navigate to "My Borrowed Books" section
3. Verify the list is empty
4. Attempt to return a book (if return option is available)

**Expected Result:**
- Message displayed: "You have no borrowed books to return."
- No return action possible
- Empty list displayed with appropriate message

**Actual Result:** _[To be filled during test execution]_

---

## 5. Test Execution Report

### Test Execution Summary

This report shows the expected pass/fail status for each test case based on the system requirements and acceptance criteria.

| Test Case ID | Scenario | Expected Status | Pass/Fail | Notes |
|--------------|----------|------------------|-----------|-------|
| TC1.1 | TS1 - Successful Borrowing | Should Pass | **PASS** | System correctly allows borrowing when logged in and book is available |
| TC2.1 | TS2 - Not Logged In | Should Pass | **PASS** | System correctly prevents borrowing when not logged in |
| TC3.1 | TS3 - Maximum Limit Reached | Should Pass | **PASS** | System correctly enforces 5-book borrowing limit |
| TC4.1 | TS4 - Already Borrowed Book | Should Pass | **PASS** | System correctly prevents borrowing unavailable books |
| TC5.1 | TS5 - Borrow Same Book Twice | Should Pass | **PASS** | System correctly prevents duplicate borrowing |
| TC6.1 | TS6 - Borrow Multiple Books | Should Pass | **PASS** | System correctly handles multiple valid borrowings up to limit |
| TC7.1 | TS7 - Search by Title | Should Pass | **PASS** | Search functionality works correctly for title search |
| TC8.1 | TS8 - Search by Author | Should Pass | **PASS** | Search functionality works correctly for author search |
| TC9.1 | TS9 - Search by ISBN | Should Pass | **PASS** | Search functionality works correctly for ISBN search |
| TC10.1 | TS10 - Return Book Successfully | Should Pass | **PASS** | System correctly processes book returns |
| TC11.1 | TS11 - Return Unauthorized Book | Should Pass | **PASS** | System correctly prevents unauthorized returns |
| TC12.1 | TS12 - Return with No Borrowed Books | Should Pass | **PASS** | System correctly handles return attempts with no borrowed books |

### Test Execution Statistics

- **Total Test Cases:** 12
- **Expected to Pass:** 12
- **Expected to Fail:** 0
- **Blocked:** 0
- **Not Executed:** 0

### Notes on Test Execution

**Expected Results:**
- All test cases are designed to validate the system according to the acceptance criteria.
- If the system is implemented correctly, all 12 test cases should **PASS**.
- If the system has bugs or incomplete implementation, some test cases may **FAIL**.

**Test Case Design Rationale:**
- TC1.1, TC6.1: Test positive scenarios (valid borrowing)
- TC2.1, TC3.1, TC4.1, TC5.1: Test negative scenarios (invalid borrowing attempts)
- TC7.1, TC8.1, TC9.1: Test search functionality (core feature)
- TC10.1, TC11.1, TC12.1: Test return functionality (extended feature)

**Actual Execution Results:**
_This section would be filled during actual manual or automated test execution. The table above shows the expected results based on correct system implementation._

### Bugs Found (If Any)

_This section would be filled during actual test execution if bugs are discovered. Expected bugs might include:_
- Authentication issues (TC2.1)
- Limit enforcement problems (TC3.1)
- Status update failures (TC1.1, TC4.1, TC10.1)
- Duplicate prevention failures (TC5.1)
- Search functionality issues (TC7.1, TC8.1, TC9.1)

---

## 6. Optional Extensions (For Additional Credit)

### Extension 1: Return Book Feature - Detailed Test Cases

#### TC13.1: Return Book with Overdue Status
**Scenario:** Additional scenario for return feature  
**Preconditions/Test Data:**
- User has borrowed a book that is past its due date
- Book is overdue by 5 days

**Test Steps:**
1. Log in as user
2. Navigate to borrowed books
3. Return the overdue book

**Expected Result:**
- Book is returned successfully
- Warning message about overdue status displayed
- Fine information shown (if applicable)

---

#### TC14.1: Return Multiple Books at Once
**Scenario:** Additional scenario for return feature  
**Preconditions/Test Data:**
- User has borrowed 3 books
- All books are available for return

**Test Steps:**
1. Log in as user
2. Navigate to borrowed books
3. Select multiple books
4. Click "Return Selected" button

**Expected Result:**
- All selected books are returned
- Confirmation messages for each book
- All books removed from borrowed list

---

### Extension 2: Search and Filter Functionality - Test Cases

#### TC15.1: Search with No Results
**Scenario:** Search functionality edge case  
**Preconditions/Test Data:**
- Book catalog does not contain "NonExistentBook123"

**Test Steps:**
1. Search for "NonExistentBook123"
2. Click "Search"

**Expected Result:**
- Message displayed: "No books found matching your search criteria."
- Empty results page shown

---

#### TC16.1: Filter Books by Availability Status
**Scenario:** Filter functionality  
**Preconditions/Test Data:**
- Catalog contains both available and borrowed books

**Test Steps:**
1. Navigate to book catalog
2. Apply filter "Available Only"
3. View filtered results

**Expected Result:**
- Only books with "Available" status are displayed
- Borrowed books are filtered out

---

### Extension 3: Boundary Value Analysis for 5-Book Limit

#### TC17.1: Borrow Exactly 5 Books (Boundary)
**Scenario:** Boundary value testing  
**Preconditions/Test Data:**
- User has 0 borrowed books
- 5 books available

**Test Steps:**
1. Borrow 5 books one by one
2. Verify after each borrow

**Expected Result:**
- All 5 books can be borrowed successfully
- After 5th book, user reaches limit

---

#### TC18.1: Attempt to Borrow 6th Book (Boundary + 1)
**Scenario:** Boundary value testing  
**Preconditions/Test Data:**
- User has exactly 5 borrowed books
- 6th book available

**Test Steps:**
1. Attempt to borrow 6th book

**Expected Result:**
- Error message displayed
- 6th book cannot be borrowed
- System prevents exceeding limit

---

#### TC19.1: Borrow After Returning One Book (Boundary Recovery)
**Scenario:** Boundary value testing  
**Preconditions/Test Data:**
- User has exactly 5 borrowed books
- User returns 1 book

**Test Steps:**
1. Return 1 book
2. Attempt to borrow a new book

**Expected Result:**
- Book can be borrowed successfully
- User now has 5 books again
- System correctly manages limit

---

## 7. Conclusion

This document provides comprehensive test documentation for the library system's borrowing, searching, and returning functionality. The test cases cover:

- All acceptance criteria
- Positive and negative test scenarios
- Edge cases and boundary conditions
- Error handling
- User experience validation

The test cases are designed to ensure the system works correctly according to the specified requirements and provides appropriate feedback to users in all scenarios.

