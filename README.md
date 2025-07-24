# PyPurse: A Command-Line Budget Tracker

#### Video Demo: (https://youtu.be/YCnHI1G2uEw)
#### Description:

**PyPurse** is a Python-based command-line personal finance tracker that enables users to manage their income and expenses with simplicity and clarity. Designed as the final project for CS50P, PyPurse helps users track financial transactions, categorize them, and monitor their overall financial health.

---

### Inspiration

Creating a budgeting tool is one of the most practical applications of programming. PyPurse was born out of a desire to build a real-world utility that can serve as a lightweight alternative to complex finance apps. The project provided an opportunity to implement concepts learned throughout CS50P, such as control structures, data structures, functions, error handling, third-party libraries, and testing with `pytest`.

---

### Features

- **Add Income:** Enter income amounts and categorize them (e.g., Salary, Freelance).
- **Add Expense:** Log spending with category labels (e.g., Food, Transport).
- **View Summary:** Get totals for income, expenses, and remaining balance.
- **Filter by Category:** View transactions grouped by any category (case-insensitive).
- **User Panel:** Quick snapshot of balance, total income, and expenses.
- **ASCII Art Title:** Uses `pyfiglet` to enhance the command-line interface.

---

### Files and Structure

- **project.py**: The core script containing the entire logic of PyPurse. It defines:
  - `main()`: The main interaction loop with user input.
  - `add_income()`, `add_expense()`: Functions to record transactions.
  - `display_summary()`: Calculates and prints totals.
  - `filter_by_category()`: Filters transactions by category.
  - `display_user_panel()`: Offers a quick glance at financial stats.

- **test_project.py**: A testing suite using `pytest` that validates:
  - `add_income()` – Correctly appends income records.
  - `add_expense()` – Correctly appends expense records.
  - `filter_by_category()` – Accurately filters based on category.
  - `display_summary()` – Covered but prints to stdout (assertion-free).

- **README.md**: Documentation for the project, including setup, features, and rationale.

---

### Testing

Tests were implemented using the `pytest` framework, covering key functions that handle data manipulation. This helped ensure correctness and allowed for easy debugging and refactoring.

