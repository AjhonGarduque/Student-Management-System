# Student-Management-System
Week 2 - Python Project

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

beginner Python project that simulates a simple terminal based student record system. Users can add students, enter their grades, calculate the average, assign honors or failure remarks, search and view students, and store everything persistently using a JSON file.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FEATURES

ADD STUDENTS
- Enter a student name and the number of subjects.
- Input grades for each subject (supports float).
- Calculates:
  - Total and average
  - Honors classification or fail notice
  - Remarks saved per student

GRADE VALIDATION
- Accepts only grades between 0–100
- Rejects invalid inputs and prompts re-entry

OUTPUT:
- Student’s average (rounded to 2 decimal places)
- Classification:
  - Passed
  - With Honors (89.5+)
  - With High Honors (94.5+)
  - With Highest Honors (98+)
  - Failed (Below 75)

STUDENT RECORD MANAGEMENT:
- View all saved students
- Search for a student by name
- Delete a student’s record
- Quit gracefully and automatically save data

FILE STORAGE:
- Uses `students.json` to save/load all data persistently

---

SAMPLE MENU:
1. Add Students
2. View Students
3. Search Students
4. Delete Students
5. Quit


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Concepts Used

- Variables  
- `if` / `elif` / `else`  
- Loops (`while`, `for`)  
- Functions & modular structure  
- Dictionaries & JSON  
- Error handling (`try` / `except`)  
- File I/O  
- Input validation  
- Global variables  
- Clean and readable UI

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project was built during my second week of learning Python as a beginner-level terminal application.  
It started as a basic grade calculator and evolved into a mini Student Management System to track my learning progress and understand how to handle real-world input/output and file operations.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I was kinda just trying to upgrade the student calculator by adding a system in it but I realized that it wasn't just a calculator anymore..
