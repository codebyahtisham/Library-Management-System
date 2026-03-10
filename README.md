# 📚 Library Management System

> A Python-based library catalog management system with role-based access control (Librarian & Student), CRUD operations on books, and CSV file persistence.

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-3776AB)
![Type](https://img.shields.io/badge/Type-University%20Project-orange)
![Course](https://img.shields.io/badge/Course-Data%20Structures%20%26%20Algorithms-purple)

---

## 📌 Overview

This project implements a **Library Management System (LMS)** for Namal University's library. It provides a console-based interface where librarians can manage the book catalog (add, remove, modify, search, display) while students have read-only access (search and display). The system features role-based authentication, CSV-based data persistence, and input validation — all built using core Python with OOP principles and file handling.

---

## 🎯 Features

- **Role-based authentication** — Librarian (full access) and Student (read-only) with separate login credentials
- **Add Book** — Register a new book with title, author, and subject
- **Remove Book** — Delete a book from the catalog by title, with confirmation details displayed
- **Search Book** — Find a book by title and view its complete details (author, subject)
- **Modify Book** — Update the title of an existing book
- **Display All Books** — View the complete library catalog
- **CSV Persistence** — All changes are automatically saved to `library.csv` and loaded on startup
- **Input Validation** — Handles invalid menu choices gracefully with re-prompting

---

## ⚙️ How It Works

```
╔══════════════════════════════════════════════╗
║   Welcome to Namal Library Management System ║
╚══════════════════════════════════════════════╝

Login as:
  1:- Librarian    →  Full CRUD access
  2:- Student      →  Search & Display only
  3:- Close Program
```

### Librarian Menu
```
Library Management System
  1:- Add Book
  2:- Remove Book
  3:- Search Book
  4:- Modify Book
  5:- Display Books
  6:- Exit (Logout)
```

### Student Menu
```
  1. Search Book
  2. Display Book
  3. Exit (Logout)
```

---

## 🏗️ Architecture

The system is built with two core classes and modular functions:

```
┌─────────────┐       ┌──────────────────┐
│   Books      │       │     Library       │
├─────────────┤       ├──────────────────┤
│ - title      │◄──────│ - books: list     │
│ - author     │       ├──────────────────┤
│ - subject    │       │ + add_book()      │
└─────────────┘       │ + remove_book()   │
                      │ + search_book()   │
                      │ + modify_book()   │
                      │ + display_books() │
                      └──────────────────┘

Helper Functions:
  save_library()  →  Writes catalog to library.csv
  load_library()  →  Reads catalog from library.csv on startup
  get_user_type() →  Role selection (Librarian/Student/Exit)
  librarian_login() / Student_login()  →  Credential checks
```

---

## 🧰 Tech Stack

| Category        | Tools                        |
|----------------|------------------------------|
| Language        | Python 3                     |
| Paradigm        | Object-Oriented Programming  |
| Data Storage    | CSV file (`library.csv`)     |
| Concepts Used   | Classes, File Handling, Lists, Linear Search |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/codebyahtisham/Library-Management-System.git
cd Library-Management-System

# Run the program
python Final_LMS.py
```

### Default Credentials

| Role      | Username | Password |
|-----------|----------|----------|
| Librarian | `namal`  | `123`    |
| Student   | `guest`  | `123`    |

---

## 🧪 Testing

A comprehensive **Test Plan** (10 pages) was created covering 8 test scenarios:

| # | Test Case                    | Status |
|---|------------------------------|--------|
| 1 | Login with valid credentials | ✅ Pass |
| 2 | Login with invalid credentials | ✅ Pass |
| 3 | Add book functionality       | ✅ Pass |
| 4 | Remove book functionality    | ✅ Pass |
| 5 | Modify book functionality    | ✅ Pass |
| 6 | Search book functionality    | ✅ Pass |
| 7 | Invalid input handling        | ✅ Pass |
| 8 | Logout & close program       | ✅ Pass |

---

## 📁 Repository Structure

```
├── README.md                # Project documentation
├── Final_LMS.py             # Complete source code
├── Report.pdf               # Lab project report
├── Test_Plan.pdf            # Detailed test plan document
└── library.csv              # Auto-generated data file (created on first run)
```

---

## 📄 Documentation

| Document                | Link                                    |
|------------------------|-----------------------------------------|
| 📘 Project Report (PDF) | [View Report](./Report.pdf)             |
| 🧪 Test Plan (PDF)      | [View Test Plan](./Test_Plan.pdf)       |

---

## 📸 Screenshots

<details>
<summary>Click to view screenshots</summary>

### Welcome & Login Screen
The system greets users and prompts for role selection (Librarian/Student/Close). Each role requires username and password authentication.

### Add Book
Librarian enters book name, author, and subject. The system confirms with "Book added successfully!" and saves to CSV.

### Search Book
Both librarian and student can search by title. The system displays title, author, and subject if found.

### Display All Books
Lists all books in the catalog with their complete details, separated by dividers for readability.

### Remove & Modify
Librarian can remove books by title (shows removed book's details) or modify a book's title while retaining author and subject data.

</details>

---

## 🏫 Academic Info

| Detail          | Info                                        |
|----------------|---------------------------------------------|
| University      | Namal University, Mianwali                  |
| Department      | Electrical Engineering                      |
| Course          | EE-253 Data Structures and Algorithms       |
| Supervisor      | Engr. Naureen Shaukat                       |
| Type            | Individual Lab Project                      |

---

## 📬 Contact

- **Email:** engr.ahtishamsaleem@gmail.com
- **LinkedIn:** [Ahtisham Saleem](https://www.linkedin.com/in/ahtisham-salim)
- **GitHub:** [@codebyahtisham](https://github.com/codebyahtisham)

---

<p align="center">
  ⭐ If you found this project interesting, consider giving it a star!
</p>
