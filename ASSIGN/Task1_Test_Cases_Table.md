# Task 1: Test Cases Table (Example Format)
## SE302 Homework 01

This table matches the format specified in the homework assignment example.

| # | Test Input | Expected Output | Covered Classes |
|---|------------|----------------|----------------|
| 1 | reebok,40,43 | VALID | 1, 4, 7, 9, 10, 13, 16, 18, 20 |
| 2 | ab,26,30,35,40,55 | VALID | 1, 4, 6, 9, 10, 13, 16, 18, 20 |
| 3 | nike,41,42,43,44,45,46 | INVALID | 22 |
| 4 | abcdefghijklmno,40,45 | VALID | 3, 5, 8, 10, 13, 16, 18, 20 |
| 5 | a,40 | INVALID | 13 |
| 6 | abcdefghijklmnop,40 | INVALID | 14 |
| 7 | nike123,40 | INVALID | 15 |
| 8 | nike@pro,40 | INVALID | 16 |
| 9 | ,40,45 | INVALID | 17 |
| 10 | nike,25 | INVALID | 18 |
| 11 | nike,56 | INVALID | 19 |
| 12 | nike,40.5 | INVALID | 20 |
| 13 | nike,40a | INVALID | 21 |
| 14 | nike | INVALID | 23 |
| 15 | nike,45,40 | INVALID | 24 |
| 16 | nike 40,45 | INVALID | 25 |
| 17 | nike,40 45 | INVALID | 26 |
| 18 | nike,,40 | INVALID | 27 |
| 19 | (empty line) | INVALID | 28 |
| 20 | adidas,30,35,40,45,50 | VALID | 2, 5, 9, 10, 13, 16, 18, 20 |
| 21 | nike,40 | VALID | 2, 5, 7, 13, 16, 18, 20 |
| 22 | puma,27,30,35,40,45 | VALID | 2, 5, 9, 10, 13, 16, 18, 20 |
| 23 | nike , 40 , 45 | VALID | 2, 5, 8, 10, 12, 13, 16, 18, 20 |
| 24 | NIKE,40,45 | VALID | 2, 5, 8, 10, 13, 16, 18, 20 |
| 25 | nike,26,55 | VALID | 2, 4, 6, 8, 10, 13, 16, 18, 20 |

**Note:** This table matches the example format from the homework assignment. For detailed explanations of each test case and equivalence class coverage, see `Task1_Equivalence_Testing.md`.

