# Accounting Management System

A simple accounting management system built with Python, using object-oriented programming principles. This system allows user authentication, management of financial accounts and transactions, and generation of financial statements.

## Features

- User Authentication (Admin and Accountant roles)
- Manage Financial Accounts
- Record and Manage Transactions
- Generate Financial Statements
  - Income Statement
  - Balance Sheet
  - Cash Flow Statement
- Data Persistence with JSON files

## Project Structure
```
accounting_system/
├── main.py
├── models/
│ ├── init.py
│ ├── user.py
│ ├── account.py
│ ├── transaction.py
│ ├── financial_statement.py
│ ├── income_statement.py
│ ├── balance_sheet.py
│ ├── cash_flow_statement.py
├── services/
│ ├── init.py
│ ├── user_service.py
│ ├── account_service.py
│ ├── transaction_service.py
│ ├── statement_service.py
└── data/
├── init.py
├── data_manager.py
├── users.json
├── accounts.json
├── transactions.json
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/accounting-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd accounting-management-system
   ```

### Usage

1. Run the main script:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to register, login, and manage accounts and transactions.

### Example

Register a new user.
Login with the registered user.
Add financial accounts and transactions.
View accounts, transactions, and financial statements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any changes.
