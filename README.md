# TECHNICAL REPORT

**Course:** PFP191 - Programming Fundamentals with Python

**Project Topic:** Topic 1 - Student Management

**University:** FPT University

**Main contributor:**  Mai Nguyễn Nhật Nguyên - QE210097 

**Instructor:**  Khoa Nguyen 

**Date:**  24/03/2026 

---

## TABLE OF CONTENTS

1. [Introduction](#1-introduction)
2. [System Analysis and Design](#2-system-analysis-and-design)
3. [Implementation Details](#3-implementation-details)
4. [Advanced Features](#4-advanced-features)
5. [Testing and Results](#5-testing-and-results)
6. [Conclusion](#6-conclusion)

---

## 1. INTRODUCTION

### 1.1 Project Overview
In educational institutions, managing student data efficiently is critical. This project focuses on designing and implementing a Python application to manage student records via a simple, text-based Console-Based User Interface (CLI). By transitioning from manual tracking to a structured digital system, this application automates the storage, retrieval, and evaluation of student academic performances.

### 1.2 Project Objectives
The primary goal of this application is to practically apply the concepts learned in the PFP191 course. Specifically, the project demonstrates:
* **Object-Oriented Programming (OOP)** principles such as encapsulation and constructors.
* Data management leveraging Python's built-in `list` and `dictionary` structures.
* Robust file processing for reading and writing text files.
* Comprehensive Exception Handling to prevent system crashes.
* Modular Programming by organizing code across multiple `.py` files.

### 1.3 Scope of Work
The system covers the following core functional areas:
* **Student Records:** Add, edit, and maintain basic student information.
* **Academic Scores:** Dynamically enter scores for various subjects and calculate the Grade Point Average (GPA).
* **Search & Sort:** Locate students by name or ID, and sort the database using multiple criteria.
* **Data Persistence:** Save and load all student data from a local `.txt` file.

---

## 2. SYSTEM ANALYSIS AND DESIGN

### 2.1 Class Architecture
The system is built with high cohesion, primarily utilizing two main classes:
* `Student`: The fundamental data model representing an individual student. It stores the `student_id`, `name`, `birth_year`, `major`, and a dictionary of `scores`.
* `SystemManager`: The core controller class responsible for managing the student list and executing business logic (searching, sorting, file synchronization).
<img width="7035" height="1700" alt="classUML" src="https://github.com/user-attachments/assets/eba55117-4075-493a-ae4f-3a9712148f72" />

<img width="928" height="792" alt="image" src="https://github.com/user-attachments/assets/14cdd791-6463-4993-a11f-870177df5338" />



### 2.2 Modular Structure
To adhere to best practices, the application architecture is separated into distinct packages:
* `models/`: Contains the `student.py` data model.
* `services/`: Contains the `system_manager.py` controller.
* `utils/`: Contains the `file_io.py` module for handling data persistence.
* `main.py`: Acts as the entry point and handles the CLI menu system.

---

## 3. IMPLEMENTATION DETAILS

### 3.1 Object-Oriented Programming (OOP) Paradigm
**Dynamic Properties and Clean Interfaces:**
Instead of hardcoding the GPA as a static float, the system dynamically calculates it based on the `scores` dictionary. The `@property` decorator is utilized to provide a clean object interface, allowing the GPA to be accessed like an attribute while remaining computationally accurate behind the scenes.

```python
@property
def gpa(self) -> float:
    if not self.scores:
        return 0.0
    return sum(self.scores.values()) / len(self.scores)
```

Additionally, the `__str__` magic method is overridden in the `Student` class to return a neatly formatted string, streamlining console outputs.

### 3.2 Data Management and Query Optimization
The `SystemManager` utilizes Python lists to hold `Student` objects. To optimize data querying, the system leverages **List Comprehensions**.
* **Searching:** The `search_students` method implements a concise list comprehension combined with string lowercasing to provide a case-insensitive, partial-match search for both IDs and names.

```python
def search_students(self, keyword: str):
    keyword = keyword.lower()
    return [s for s in self.students if keyword in s.name.lower() or keyword in s.student_id.lower()]
```

* **Sorting:** The `sort_students` method allows users to sort students by GPA, name, or birth year. This is achieved using Python's built-in `.sort()` function paired with `lambda` expressions to dynamically target specific object attributes.

### 3.3 File I/O and JSON Serialization
To ensure data persists between sessions, `utils/file_io.py` handles the reading and writing of `students_data.txt`.
Because the `Student` object contains nested structures (a dictionary of scores), plain text processing is insufficient. Therefore, the system serializes `Student` objects into JSON dictionaries using the `to_dict()` method before saving. Upon initialization, `load_data_from_file` parses the JSON and reconstructs the objects using the `@classmethod` `from_dict()`.

---

## 4. ADVANCED FEATURES

### Robust Exception Handling
To ensure the application runs continuously without crashing from bad user inputs, comprehensive `try-except` blocks are implemented. 
* **Input Validation:** In `main.py`, when adding a student or entering a score, the program attempts to cast inputs to `int` or `float`. If a user inputs text instead of a number, a `ValueError` is caught, and a user-friendly error message is displayed.
* **File Safeguards:** The `file_io.py` module utilizes `try-except` to catch file system errors (e.g., missing files, permission issues) during serialization. It also checks `os.path.exists()` before loading to prevent crashes if the file is absent.

---

## 5. INSTALLATION & USAGE

### 5.1 Prerequisites
* Python 3.7 or higher.

### 5.2 Running the Application
1. Ensure the directory structure follows the required modular design (`models/`, `services/`, `utils/`).
2. Open a terminal and navigate to the root directory of the project.
3. Execute the main script:
   ```bash
   python main.py
   ```
4. Follow the interactive menu (Options 1-6) to manage the system. Always select **Option 6** to safely save data and exit the program.

---

## 6. CONCLUSION

The completed Student Management application successfully meets all the foundational and technical requirements outlined in the course syllabus. By effectively utilizing OOP, list comprehensions, robust Exception Handling, and Modular Design, the project provides a scalable and crash-resistant tool for academic tracking. Future enhancements could include transitioning from a `.txt` database to SQLite, or implementing a Graphical User Interface (GUI) to further improve user experience.
