"""
Management command to populate Ram Sir Platform with initial course data.
Run: python manage.py populate_courses
"""
from django.core.management.base import BaseCommand
from courses.models import Category, Course, Module


COURSES_DATA = [
    {
        'category': 'Programming',
        'title': 'C Programming - Complete Course',
        'short_description': 'Master C from basics to pointers, memory management & file handling',
        'description': 'Learn C programming from scratch. This course covers all fundamentals including data types, loops, functions, arrays, pointers, structures, file I/O and more with practical examples.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '25 hours',
        'rating': 4.9,
        'students_count': 320,
        'is_featured': True,
        'what_you_learn': 'Variables & Data Types\nControl Flow (if/else, loops)\nFunctions & Recursion\nArrays & Strings\nPointers & Memory Management\nStructures & Unions\nFile Handling\nDynamic Memory Allocation',
        'modules': [
            {'title': 'Introduction to C Programming', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Welcome to C Programming!</h2><p>C is a general-purpose programming language created by Dennis Ritchie in 1972. It is one of the most widely used programming languages of all time.</p><h3>Why Learn C?</h3><ul><li>Foundation of many modern languages</li><li>Used in operating systems, embedded systems</li><li>Fast and efficient</li><li>Teaches you memory management</li></ul><h3>Your First C Program</h3><pre><code>#include &lt;stdio.h&gt;\n\nint main() {\n    printf("Hello, World!\\n");\n    return 0;\n}</code></pre><p>This simple program prints "Hello, World!" to the screen. Let\'s break it down:</p><ul><li><strong>#include &lt;stdio.h&gt;</strong> - includes standard input/output library</li><li><strong>int main()</strong> - main function where execution begins</li><li><strong>printf()</strong> - function to print output</li></ul>', 'duration_minutes': 15},
            {'title': 'Variables & Data Types', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Variables and Data Types in C</h2><h3>Basic Data Types</h3><table border="1" style="width:100%;border-collapse:collapse;padding:8px"><tr><th>Type</th><th>Size</th><th>Range</th><th>Example</th></tr><tr><td>int</td><td>4 bytes</td><td>-2147483648 to 2147483647</td><td>int age = 22;</td></tr><tr><td>float</td><td>4 bytes</td><td>3.4e-38 to 3.4e+38</td><td>float pi = 3.14;</td></tr><tr><td>double</td><td>8 bytes</td><td>1.7e-308 to 1.7e+308</td><td>double x = 3.14159;</td></tr><tr><td>char</td><td>1 byte</td><td>-128 to 127</td><td>char grade = \'A\';</td></tr></table><h3>Variable Declaration</h3><pre><code>int main() {\n    int age = 22;\n    float marks = 95.5;\n    char grade = \'A\';\n    \n    printf("Age: %d\\n", age);\n    printf("Marks: %.1f\\n", marks);\n    printf("Grade: %c\\n", grade);\n    return 0;\n}</code></pre>', 'duration_minutes': 20},
            {'title': 'Control Flow - if/else & Loops', 'order': 3, 'content_type': 'text', 'text_content': '<h2>Control Flow in C</h2><h3>If-Else Statement</h3><pre><code>int marks = 75;\nif (marks >= 90) {\n    printf("Grade: A");\n} else if (marks >= 75) {\n    printf("Grade: B");\n} else {\n    printf("Grade: C");\n}</code></pre><h3>Loops</h3><h4>For Loop</h4><pre><code>for (int i = 1; i &lt;= 10; i++) {\n    printf("%d ", i);\n}</code></pre><h4>While Loop</h4><pre><code>int i = 1;\nwhile (i &lt;= 5) {\n    printf("%d\\n", i);\n    i++;\n}</code></pre><h3>Practice Task</h3><p>Write a program to print multiplication table of any number entered by user.</p>', 'duration_minutes': 25},
            {'title': 'Functions & Recursion', 'order': 4, 'content_type': 'text', 'text_content': '<h2>Functions in C</h2><p>Functions are blocks of code that perform specific tasks. They help in code reusability and organization.</p><h3>Syntax</h3><pre><code>return_type function_name(parameters) {\n    // function body\n    return value;\n}</code></pre><h3>Example</h3><pre><code>int add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    int result = add(5, 3);\n    printf("Sum = %d", result);\n    return 0;\n}</code></pre><h3>Recursion - Factorial</h3><pre><code>int factorial(int n) {\n    if (n == 0 || n == 1) return 1;\n    return n * factorial(n-1);\n}</code></pre>', 'duration_minutes': 30},
            {'title': 'Pointers - The Power of C', 'order': 5, 'content_type': 'text', 'text_content': '<h2>Pointers in C</h2><p>A pointer is a variable that stores the memory address of another variable. This is one of the most powerful features of C.</p><h3>Declaration & Usage</h3><pre><code>int main() {\n    int num = 42;\n    int *ptr = &num;  // ptr stores address of num\n    \n    printf("Value: %d\\n", num);      // 42\n    printf("Address: %p\\n", &num);   // memory address\n    printf("Via pointer: %d\\n", *ptr); // 42 (dereferencing)\n    \n    *ptr = 100;  // change value via pointer\n    printf("New value: %d\\n", num);  // 100\n    return 0;\n}</code></pre><h3>Pointer Diagram</h3><div style="background:#f0f0f0;padding:15px;border-radius:8px;font-family:monospace"><p>num = 42 → stored at address 1000</p><p>ptr = 1000 → stored at address 2000</p><p>*ptr = value at address 1000 = 42</p></div>', 'duration_minutes': 35},
        ]
    },
    {
        'category': 'Programming',
        'title': 'C++ Programming - OOP & Beyond',
        'short_description': 'Master C++ with OOP concepts, STL, templates and advanced techniques',
        'description': 'Complete C++ course covering Object-Oriented Programming, classes, inheritance, polymorphism, STL containers, templates, and modern C++ features.',
        'course_type': 'free',
        'level': 'intermediate',
        'duration': '30 hours',
        'rating': 4.9,
        'students_count': 280,
        'is_featured': True,
        'what_you_learn': 'OOP Concepts\nClasses & Objects\nInheritance & Polymorphism\nEncapsulation & Abstraction\nSTL - Vectors, Maps, Sets\nTemplates & Generic Programming\nException Handling\nModern C++11/17 Features',
        'modules': [
            {'title': 'Introduction to C++ & OOP', 'order': 1, 'content_type': 'text', 'text_content': '<h2>C++ - The Power of OOP</h2><p>C++ is an extension of C that adds Object-Oriented Programming features. Created by Bjarne Stroustrup in 1979.</p><h3>Key OOP Concepts</h3><ul><li><strong>Class</strong> - Blueprint for objects</li><li><strong>Object</strong> - Instance of a class</li><li><strong>Encapsulation</strong> - Hiding internal data</li><li><strong>Inheritance</strong> - Reusing code from parent class</li><li><strong>Polymorphism</strong> - Same interface, different behavior</li></ul><h3>First C++ Program</h3><pre><code>#include &lt;iostream&gt;\nusing namespace std;\n\nint main() {\n    cout &lt;&lt; "Hello from Ram Sir!" &lt;&lt; endl;\n    return 0;\n}</code></pre>', 'duration_minutes': 20},
            {'title': 'Classes and Objects', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Classes and Objects in C++</h2><pre><code>class Student {\nprivate:\n    string name;\n    int rollNo;\n    float marks;\n\npublic:\n    // Constructor\n    Student(string n, int r, float m) {\n        name = n;\n        rollNo = r;\n        marks = m;\n    }\n    \n    // Getter methods\n    void display() {\n        cout &lt;&lt; "Name: " &lt;&lt; name &lt;&lt; endl;\n        cout &lt;&lt; "Roll: " &lt;&lt; rollNo &lt;&lt; endl;\n        cout &lt;&lt; "Marks: " &lt;&lt; marks &lt;&lt; endl;\n    }\n    \n    // Calculate grade\n    char getGrade() {\n        if (marks >= 90) return \'A\';\n        if (marks >= 75) return \'B\';\n        return \'C\';\n    }\n};\n\nint main() {\n    Student s1("Ramgopal", 101, 95.5);\n    s1.display();\n    cout &lt;&lt; "Grade: " &lt;&lt; s1.getGrade();\n    return 0;\n}</code></pre>', 'duration_minutes': 30},
            {'title': 'Inheritance', 'order': 3, 'content_type': 'text', 'text_content': '<h2>Inheritance in C++</h2><p>Inheritance allows a class to inherit properties and methods from another class.</p><pre><code>// Base class\nclass Animal {\npublic:\n    string name;\n    void eat() {\n        cout &lt;&lt; name &lt;&lt; " is eating" &lt;&lt; endl;\n    }\n    virtual void sound() {\n        cout &lt;&lt; "Some sound" &lt;&lt; endl;\n    }\n};\n\n// Derived class\nclass Dog : public Animal {\npublic:\n    void sound() override {\n        cout &lt;&lt; "Woof! Woof!" &lt;&lt; endl;\n    }\n    void fetch() {\n        cout &lt;&lt; name &lt;&lt; " fetches the ball!" &lt;&lt; endl;\n    }\n};\n\nclass Cat : public Animal {\npublic:\n    void sound() override {\n        cout &lt;&lt; "Meow!" &lt;&lt; endl;\n    }\n};</code></pre><h3>Types of Inheritance</h3><ul><li>Single Inheritance</li><li>Multiple Inheritance</li><li>Multilevel Inheritance</li><li>Hierarchical Inheritance</li><li>Hybrid Inheritance</li></ul>', 'duration_minutes': 35},
        ]
    },
    {
        'category': 'Programming',
        'title': 'Python Core + Advanced',
        'short_description': 'Complete Python - from basics to OOP, File I/O, Libraries & more',
        'description': 'Master Python programming from variables to advanced OOP, file handling, regular expressions, decorators, generators, and popular libraries.',
        'course_type': 'free',
        'level': 'all',
        'duration': '40 hours',
        'rating': 4.9,
        'students_count': 520,
        'is_featured': True,
        'what_you_learn': 'Python Basics & Syntax\nData Structures - List, Tuple, Dict, Set\nOOP - Classes, Objects, Inheritance\nFile Handling & Exception Handling\nModules & Libraries\nDecorators & Generators\nRegular Expressions\nMultithreading Basics',
        'modules': [
            {'title': 'Python Introduction & Setup', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Welcome to Python!</h2><p>Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. Python\'s philosophy emphasizes code readability and simplicity.</p><h3>Why Python?</h3><ul><li>Easy to learn and read</li><li>Huge library ecosystem</li><li>Used in Web Dev, AI, Data Science, Automation</li><li>Large community support</li></ul><h3>Installation</h3><p>Download Python from <strong>python.org</strong> and install it. Check installation:</p><pre><code>python --version\n# Python 3.x.x</code></pre><h3>Your First Python Program</h3><pre><code># Hello World\nprint("Hello, World!")\nprint("Welcome to Ram Sir Python Course!")\n\n# Basic calculation\na = 10\nb = 20\nprint(f"Sum = {a + b}")</code></pre>', 'duration_minutes': 20},
            {'title': 'Variables, Data Types & Input', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Variables and Data Types</h2><pre><code># Different data types\nname = "Ramgopal"       # str\nage = 22               # int\nmarks = 95.5           # float\nis_student = True      # bool\n\nprint(type(name))    # &lt;class \'str\'&gt;\nprint(type(age))     # &lt;class \'int\'&gt;\n\n# Type conversion\nnum_str = "42"\nnum_int = int(num_str)   # "42" → 42\nnum_float = float("3.14")  # "3.14" → 3.14\nback_to_str = str(42)    # 42 → "42"</code></pre><h3>Taking Input</h3><pre><code>name = input("Enter your name: ")\nage = int(input("Enter age: "))\nprint(f"Hello {name}, you are {age} years old!")</code></pre><h3>String Methods</h3><pre><code>s = "Hello Ram Sir"\nprint(s.upper())     # HELLO RAM SIR\nprint(s.lower())     # hello ram sir\nprint(s.replace("Ram", "Ramgopal"))  # Hello Ramgopal Sir\nprint(len(s))        # 13\nprint(s.split())     # [\'Hello\', \'Ram\', \'Sir\']</code></pre>', 'duration_minutes': 25},
            {'title': 'Lists, Tuples, Sets & Dicts', 'order': 3, 'content_type': 'text', 'text_content': '<h2>Python Data Structures</h2><h3>List - Ordered, Mutable</h3><pre><code>students = ["Alice", "Bob", "Charlie", "Ram"]\nstudents.append("Priya")       # Add\nstudents.remove("Bob")         # Remove\nprint(students[0])             # Alice (indexing)\nprint(students[-1])            # Last element\nprint(students[1:3])           # Slice - [\'Charlie\']\n\n# List comprehension\nsquares = [x**2 for x in range(1, 6)]\n# [1, 4, 9, 16, 25]</code></pre><h3>Dictionary - Key-Value Pairs</h3><pre><code>student = {\n    "name": "Ramgopal",\n    "age": 22,\n    "city": "Indore",\n    "marks": 95.5\n}\nprint(student["name"])         # Ramgopal\nstudent["phone"] = "9753528324"  # Add key\nprint(student.keys())          # All keys\nprint(student.values())        # All values\n\n# Loop through dict\nfor key, value in student.items():\n    print(f"{key}: {value}")</code></pre>', 'duration_minutes': 30},
            {'title': 'OOP in Python', 'order': 4, 'content_type': 'text', 'text_content': '<h2>Object-Oriented Programming in Python</h2><pre><code>class Student:\n    # Class variable\n    school = "Ram Sir Academy"\n    \n    def __init__(self, name, roll, marks):\n        # Instance variables\n        self.name = name\n        self.roll = roll\n        self.marks = marks\n    \n    def get_grade(self):\n        if self.marks >= 90:\n            return "A"\n        elif self.marks >= 75:\n            return "B"\n        return "C"\n    \n    def __str__(self):\n        return f"Student: {self.name} | Grade: {self.get_grade()}"\n\n# Inheritance\nclass Engineer(Student):\n    def __init__(self, name, roll, marks, branch):\n        super().__init__(name, roll, marks)\n        self.branch = branch\n    \n    def __str__(self):\n        return f"{super().__str__()} | Branch: {self.branch}"\n\n# Create objects\ns1 = Student("Ramgopal", 101, 95.5)\ne1 = Engineer("Priya", 102, 88, "IT")\nprint(s1)\nprint(e1)</code></pre>', 'duration_minutes': 35},
        ]
    },
    {
        'category': 'Database',
        'title': 'SQL - Complete Database Course',
        'short_description': 'Master SQL from basics to advanced queries, joins, stored procedures',
        'description': 'Complete SQL course covering DDL, DML, DCL, TCL, DQL, all types of Joins, subqueries, views, stored procedures, triggers and database design.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '20 hours',
        'rating': 4.8,
        'students_count': 410,
        'is_featured': True,
        'what_you_learn': 'DDL - CREATE, ALTER, DROP\nDML - INSERT, UPDATE, DELETE\nDQL - SELECT with WHERE, ORDER BY\nAll Types of Joins\nSubqueries & Views\nAggregate Functions\nStored Procedures & Triggers\nDatabase Design & Normalization',
        'modules': [
            {'title': 'Introduction to SQL & DBMS', 'order': 1, 'content_type': 'text', 'text_content': '<h2>SQL - Structured Query Language</h2><p>SQL is the standard language for managing relational databases. It was developed in the 1970s by IBM.</p><h3>What is DBMS?</h3><p>Database Management System - software to create, manage, and query databases. Examples: MySQL, PostgreSQL, Oracle, SQL Server, SQLite.</p><h3>Types of SQL Commands</h3><table border="1" style="width:100%;border-collapse:collapse"><tr style="background:#ff6b35;color:white"><th>Category</th><th>Full Form</th><th>Commands</th></tr><tr><td><strong>DDL</strong></td><td>Data Definition Language</td><td>CREATE, ALTER, DROP, TRUNCATE</td></tr><tr><td><strong>DML</strong></td><td>Data Manipulation Language</td><td>INSERT, UPDATE, DELETE</td></tr><tr><td><strong>DQL</strong></td><td>Data Query Language</td><td>SELECT</td></tr><tr><td><strong>DCL</strong></td><td>Data Control Language</td><td>GRANT, REVOKE</td></tr><tr><td><strong>TCL</strong></td><td>Transaction Control Language</td><td>COMMIT, ROLLBACK, SAVEPOINT</td></tr></table>', 'duration_minutes': 20},
            {'title': 'CREATE & INSERT - DDL & DML', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Creating Tables and Inserting Data</h2><pre><code>-- Create Database\nCREATE DATABASE RamSirAcademy;\nUSE RamSirAcademy;\n\n-- Create Table\nCREATE TABLE Students (\n    StudentID INT PRIMARY KEY AUTO_INCREMENT,\n    Name VARCHAR(100) NOT NULL,\n    Email VARCHAR(100) UNIQUE,\n    Phone VARCHAR(15),\n    City VARCHAR(50),\n    Marks DECIMAL(5,2),\n    EnrollDate DATE DEFAULT CURRENT_DATE\n);\n\n-- Insert Data\nINSERT INTO Students (Name, Email, Phone, City, Marks)\nVALUES \n    ("Ramgopal Prajapati", "ramsir@email.com", "9753528324", "Indore", 95.5),\n    ("Alice Sharma", "alice@email.com", "9876543210", "Bhopal", 88.0),\n    ("Bob Kumar", "bob@email.com", "9012345678", "Indore", 76.5);\n\n-- View data\nSELECT * FROM Students;</code></pre>', 'duration_minutes': 25},
            {'title': 'SELECT Queries & Filtering', 'order': 3, 'content_type': 'text', 'text_content': '<h2>SELECT - The Most Important SQL Command</h2><pre><code>-- Basic SELECT\nSELECT * FROM Students;\nSELECT Name, Email, Marks FROM Students;\n\n-- WHERE clause - filtering\nSELECT * FROM Students WHERE City = "Indore";\nSELECT * FROM Students WHERE Marks > 90;\nSELECT * FROM Students WHERE Marks BETWEEN 70 AND 90;\nSELECT * FROM Students WHERE Name LIKE "R%";  -- starts with R\n\n-- ORDER BY - sorting\nSELECT * FROM Students ORDER BY Marks DESC;\nSELECT * FROM Students ORDER BY Name ASC;\n\n-- LIMIT - restrict results\nSELECT * FROM Students ORDER BY Marks DESC LIMIT 3;\n\n-- Aggregate Functions\nSELECT COUNT(*) as TotalStudents FROM Students;\nSELECT AVG(Marks) as AvgMarks FROM Students;\nSELECT MAX(Marks) as HighestMarks FROM Students;\nSELECT MIN(Marks) as LowestMarks FROM Students;\nSELECT SUM(Marks) as TotalMarks FROM Students;</code></pre>', 'duration_minutes': 30},
            {'title': 'JOINS - Combining Tables', 'order': 4, 'content_type': 'text', 'text_content': '<h2>SQL Joins - Most Important Concept!</h2><pre><code>-- Sample tables\nCREATE TABLE Courses (\n    CourseID INT PRIMARY KEY,\n    CourseName VARCHAR(100),\n    Price DECIMAL(8,2)\n);\n\nCREATE TABLE Enrollments (\n    EnrollID INT PRIMARY KEY AUTO_INCREMENT,\n    StudentID INT,\n    CourseID INT,\n    EnrollDate DATE\n);\n\n-- INNER JOIN - Only matching records\nSELECT s.Name, c.CourseName, e.EnrollDate\nFROM Students s\nINNER JOIN Enrollments e ON s.StudentID = e.StudentID\nINNER JOIN Courses c ON e.CourseID = c.CourseID;\n\n-- LEFT JOIN - All students, even without enrollment\nSELECT s.Name, c.CourseName\nFROM Students s\nLEFT JOIN Enrollments e ON s.StudentID = e.StudentID\nLEFT JOIN Courses c ON e.CourseID = c.CourseID;\n\n-- GROUP BY with JOIN\nSELECT s.Name, COUNT(e.CourseID) as CoursesEnrolled\nFROM Students s\nLEFT JOIN Enrollments e ON s.StudentID = e.StudentID\nGROUP BY s.StudentID, s.Name\nORDER BY CoursesEnrolled DESC;</code></pre>', 'duration_minutes': 40},
        ]
    },
    {
        'category': 'Data Science',
        'title': 'Power BI - Data Visualization',
        'short_description': 'Master Power BI from data import to advanced DAX and interactive dashboards',
        'description': 'Complete Power BI course covering data import, Power Query, DAX formulas, creating interactive reports and dashboards for business intelligence.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '18 hours',
        'rating': 4.8,
        'students_count': 195,
        'is_featured': False,
        'what_you_learn': 'Power BI Desktop Introduction\nData Import from Multiple Sources\nPower Query Editor\nData Modeling & Relationships\nDAX Basics - Calculated Columns & Measures\nVisualizations - Charts, Maps, Tables\nInteractive Reports & Filters\nPublishing & Sharing Dashboards',
        'modules': [
            {'title': 'Power BI Introduction', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Power BI - Business Intelligence Tool</h2><p>Power BI is a Microsoft business analytics tool that transforms raw data into meaningful insights through interactive visualizations and reports.</p><h3>Power BI Components</h3><ul><li><strong>Power BI Desktop</strong> - Free tool for creating reports</li><li><strong>Power BI Service</strong> - Cloud-based sharing platform</li><li><strong>Power BI Mobile</strong> - Mobile app for viewing reports</li></ul><h3>Power BI Workflow</h3><div style="background:#f0f8ff;padding:15px;border-radius:8px"><p>1. <strong>Get Data</strong> → Import from Excel, SQL, Web, etc.</p><p>2. <strong>Transform Data</strong> → Clean using Power Query</p><p>3. <strong>Model Data</strong> → Create relationships between tables</p><p>4. <strong>Create Visuals</strong> → Charts, graphs, maps</p><p>5. <strong>Publish</strong> → Share with team/clients</p></div>', 'duration_minutes': 20},
            {'title': 'DAX Functions', 'order': 2, 'content_type': 'text', 'text_content': '<h2>DAX - Data Analysis Expressions</h2><p>DAX is a formula language used in Power BI to create calculated columns and measures.</p><h3>Basic DAX Measures</h3><pre><code>// Total Sales\nTotal Sales = SUM(Sales[Amount])\n\n// Average Sales  \nAvg Sales = AVERAGE(Sales[Amount])\n\n// Count of Orders\nOrder Count = COUNT(Sales[OrderID])\n\n// Percentage calculation\nSales % = \nDIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Sales)), 0)\n\n// Year-over-Year comparison\nPrev Year Sales = \nCALCULATE([Total Sales], DATEADD(\'Date\'[Date], -1, YEAR))\n\nYoY Growth = \nDIVIDE([Total Sales] - [Prev Year Sales], [Prev Year Sales], 0)</code></pre>', 'duration_minutes': 35},
        ]
    },
    {
        'category': 'Programming',
        'title': 'DSA - Data Structures & Algorithms',
        'short_description': 'Master DSA concepts with Python/C++ implementations for competitive programming & interviews',
        'description': 'Complete DSA course covering Arrays, Linked Lists, Stacks, Queues, Trees, Graphs, Sorting, Searching algorithms with implementations and complexity analysis.',
        'course_type': 'free',
        'level': 'intermediate',
        'duration': '45 hours',
        'rating': 4.9,
        'students_count': 380,
        'is_featured': True,
        'what_you_learn': 'Arrays & Strings\nLinked Lists (Singly, Doubly, Circular)\nStacks & Queues\nTrees - Binary, BST, AVL\nHeaps & Priority Queues\nGraphs - BFS, DFS\nSorting - Bubble, Merge, Quick, Heap\nDynamic Programming',
        'modules': [
            {'title': 'Introduction to DSA & Complexity', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Data Structures & Algorithms</h2><p>DSA is the backbone of computer science and software engineering. Every efficient program uses proper data structures.</p><h3>Time Complexity - Big O Notation</h3><table border="1" style="width:100%;border-collapse:collapse"><tr style="background:#ff6b35;color:white"><th>Complexity</th><th>Name</th><th>Example</th></tr><tr><td>O(1)</td><td>Constant</td><td>Array access by index</td></tr><tr><td>O(log n)</td><td>Logarithmic</td><td>Binary Search</td></tr><tr><td>O(n)</td><td>Linear</td><td>Linear Search</td></tr><tr><td>O(n log n)</td><td>Linearithmic</td><td>Merge Sort</td></tr><tr><td>O(n²)</td><td>Quadratic</td><td>Bubble Sort</td></tr><tr><td>O(2ⁿ)</td><td>Exponential</td><td>Recursive Fibonacci</td></tr></table>', 'duration_minutes': 25},
            {'title': 'Arrays & Searching', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Arrays and Searching Algorithms</h2><h3>Linear Search - O(n)</h3><pre><code>def linear_search(arr, target):\n    for i in range(len(arr)):\n        if arr[i] == target:\n            return i  # Found at index i\n    return -1  # Not found\n\narr = [64, 34, 25, 12, 22, 11, 90]\nresult = linear_search(arr, 25)\nprint(f"Found at index: {result}")  # Found at index: 2</code></pre><h3>Binary Search - O(log n)</h3><pre><code>def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    \n    while left &lt;= right:\n        mid = (left + right) // 2\n        \n        if arr[mid] == target:\n            return mid\n        elif arr[mid] &lt; target:\n            left = mid + 1  # Search right half\n        else:\n            right = mid - 1  # Search left half\n    \n    return -1\n\n# Array MUST be sorted!\narr = [11, 12, 22, 25, 34, 64, 90]\nresult = binary_search(arr, 25)\nprint(f"Found at index: {result}")  # Found at index: 3</code></pre>', 'duration_minutes': 30},
            {'title': 'Linked Lists', 'order': 3, 'content_type': 'text', 'text_content': '<h2>Linked Lists</h2><p>A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node.</p><pre><code>class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\nclass LinkedList:\n    def __init__(self):\n        self.head = None\n    \n    def append(self, data):\n        new_node = Node(data)\n        if not self.head:\n            self.head = new_node\n            return\n        current = self.head\n        while current.next:\n            current = current.next\n        current.next = new_node\n    \n    def display(self):\n        elements = []\n        current = self.head\n        while current:\n            elements.append(str(current.data))\n            current = current.next\n        print(" → ".join(elements))\n    \n    def delete(self, data):\n        if self.head and self.head.data == data:\n            self.head = self.head.next\n            return\n        current = self.head\n        while current.next:\n            if current.next.data == data:\n                current.next = current.next.next\n                return\n            current = current.next\n\n# Usage\nll = LinkedList()\nll.append(10)\nll.append(20)\nll.append(30)\nll.display()  # 10 → 20 → 30</code></pre>', 'duration_minutes': 40},
        ]
    },
    {
        'category': 'Programming',
        'title': 'Java Core - Complete Course',
        'short_description': 'Learn Java from basics to OOP, Collections, Exception Handling & Multithreading',
        'description': 'Complete Java programming course covering all fundamentals, OOP concepts, Collections Framework, Exception Handling, File I/O, Multithreading and more.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '35 hours',
        'rating': 4.8,
        'students_count': 290,
        'is_featured': False,
        'what_you_learn': 'Java Basics & JVM Concepts\nOOP - Classes, Objects, Inheritance\nInterfaces & Abstract Classes\nCollections Framework\nException Handling\nFile I/O & Streams\nMultithreading\nJava 8+ Features - Lambdas, Streams',
        'modules': [
            {'title': 'Java Introduction & Setup', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Java - Write Once, Run Anywhere</h2><p>Java is a class-based, object-oriented programming language created by James Gosling at Sun Microsystems in 1995.</p><h3>Java vs C++</h3><table border="1" style="width:100%;border-collapse:collapse"><tr style="background:#ff6b35;color:white"><th>Feature</th><th>Java</th><th>C++</th></tr><tr><td>Memory Management</td><td>Automatic (Garbage Collector)</td><td>Manual (delete)</td></tr><tr><td>Platform</td><td>Platform Independent (JVM)</td><td>Platform Dependent</td></tr><tr><td>Pointers</td><td>Not supported</td><td>Supported</td></tr><tr><td>Multiple Inheritance</td><td>Via Interfaces only</td><td>Supported</td></tr></table><h3>First Java Program</h3><pre><code>public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello from Ram Sir!");\n        System.out.println("Welcome to Java!");\n    }\n}</code></pre>', 'duration_minutes': 20},
        ]
    },
    {
        'category': 'AI & ML',
        'title': 'Prompt Engineering - Master AI Communication',
        'short_description': 'Learn to write effective prompts for ChatGPT, Claude, Gemini & other AI tools',
        'description': 'Complete Prompt Engineering course. Learn to communicate with AI effectively, write structured prompts, use system prompts, chain-of-thought, few-shot learning and build AI-powered workflows.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '12 hours',
        'rating': 4.9,
        'students_count': 450,
        'is_featured': True,
        'what_you_learn': 'Understanding AI Language Models\nBasic to Advanced Prompt Techniques\nZero-shot & Few-shot Prompting\nChain-of-Thought Reasoning\nSystem Prompts & Role Prompting\nPrompt Chaining\nAI Tools - ChatGPT, Claude, Gemini\nBuilding AI Workflows',
        'modules': [
            {'title': 'What is Prompt Engineering?', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Prompt Engineering - The New Superpower!</h2><p>Prompt Engineering is the skill of designing effective inputs (prompts) for AI language models to get the best outputs. In 2024, this skill is one of the most in-demand skills globally.</p><h3>Why Learn Prompt Engineering?</h3><ul><li>10x your productivity with AI tools</li><li>High-paying jobs and freelance opportunities</li><li>Works with ChatGPT, Claude, Gemini, Copilot</li><li>No coding required to get started</li><li>The future of human-computer interaction</li></ul><h3>Basic Prompt Formula</h3><div style="background:#f0f8ff;padding:20px;border-radius:10px;border-left:4px solid #ff6b35"><strong>Role + Task + Context + Format + Constraints</strong><br><br><em>Example:</em> "You are an expert Python teacher. Explain list comprehension to a beginner using 3 simple examples. Format your response with code blocks and explanations. Keep each example under 10 lines."</div>', 'duration_minutes': 20},
            {'title': 'Advanced Prompting Techniques', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Advanced Prompting Techniques</h2><h3>1. Chain-of-Thought (CoT) Prompting</h3><div style="background:#fff3cd;padding:15px;border-radius:8px"><p><strong>Bad prompt:</strong> "What is 15% of 2400?"</p><p><strong>Good CoT prompt:</strong> "Calculate 15% of 2400. Think step by step: First find 10%, then 5%, then add them."</p></div><h3>2. Few-Shot Prompting</h3><pre><code>Classify the sentiment:\n\nText: "The course was amazing!" → Positive\nText: "I didn\'t like the content" → Negative  \nText: "The video quality was okay" → Neutral\n\nNow classify:\nText: "Ram Sir explains everything so clearly!" → ?</code></pre><h3>3. Role Prompting</h3><pre><code>You are Ram Sir, an expert technical trainer from Indore with 2+ years experience teaching Python, Java, and Data Science. You explain concepts in simple terms with real-world Indian examples. Always encourage students and answer their doubts patiently.</code></pre><h3>4. Structured Output</h3><pre><code>Generate a course outline for "Python for Beginners".\nOutput as JSON:\n{\n  "course": "Python for Beginners",\n  "modules": [\n    {"id": 1, "title": "...", "duration": "..."},\n    ...\n  ]\n}</code></pre>', 'duration_minutes': 30},
        ]
    },
    {
        'category': 'AI & ML',
        'title': 'Generative AI - Complete Guide',
        'short_description': 'Understand and use Generative AI tools - ChatGPT, Midjourney, Claude, Stable Diffusion',
        'description': 'Complete Generative AI course covering LLMs, image generation, AI tools for productivity, creating content with AI, AI agents and the future of AI.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '15 hours',
        'rating': 4.9,
        'students_count': 380,
        'is_featured': True,
        'what_you_learn': 'What is Generative AI?\nLarge Language Models (LLMs)\nChatGPT, Claude, Gemini - Deep Dive\nAI Image Generation - Midjourney, DALL-E\nAI for Code Generation\nAI Video & Audio Tools\nBuilding AI Workflows\nFuture of AI & Career Opportunities',
        'modules': [
            {'title': 'Introduction to Generative AI', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Generative AI - The Technology Changing Everything!</h2><p>Generative AI refers to AI systems that can create new content - text, images, code, audio, video - based on patterns learned from training data.</p><h3>Timeline of AI</h3><div style="background:#f0f8ff;padding:15px;border-radius:8px"><p>🔵 <strong>1950s</strong> - AI concept introduced by Alan Turing</p><p>🔵 <strong>1980s</strong> - Expert systems and rule-based AI</p><p>🔵 <strong>2012</strong> - Deep Learning breakthrough (ImageNet)</p><p>🔵 <strong>2017</strong> - Transformer architecture (Attention is All You Need)</p><p>🔵 <strong>2022</strong> - ChatGPT launches → AI revolution begins!</p><p>🔵 <strong>2023-24</strong> - Multimodal AI, AI agents, AI everywhere!</p></div><h3>Popular Gen AI Tools</h3><table border="1" style="width:100%;border-collapse:collapse"><tr style="background:#ff6b35;color:white"><th>Category</th><th>Tools</th></tr><tr><td>Text/Chat</td><td>ChatGPT, Claude, Gemini, Llama</td></tr><tr><td>Images</td><td>Midjourney, DALL-E, Stable Diffusion</td></tr><tr><td>Code</td><td>GitHub Copilot, Cursor, Replit AI</td></tr><tr><td>Video</td><td>Sora, RunwayML, Pika</td></tr><tr><td>Audio</td><td>ElevenLabs, Murf.ai, Suno</td></tr></table>', 'duration_minutes': 25},
        ]
    },
    {
        'category': 'AI & ML',
        'title': 'Artificial Intelligence - Core Concepts',
        'short_description': 'Complete AI course - Machine Learning, Deep Learning, Neural Networks & more',
        'description': 'Comprehensive AI course covering Machine Learning algorithms, Deep Learning, Neural Networks, Computer Vision, NLP, and practical AI implementation with Python.',
        'course_type': 'free',
        'level': 'intermediate',
        'duration': '50 hours',
        'rating': 4.8,
        'students_count': 220,
        'is_featured': False,
        'what_you_learn': 'Machine Learning Fundamentals\nSupervised & Unsupervised Learning\nNeural Networks & Deep Learning\nCNN for Computer Vision\nRNN & LSTM for Sequences\nNLP & Text Processing\nModel Training & Evaluation\nDeployment with Flask/Django',
        'modules': [
            {'title': 'Machine Learning Introduction', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Machine Learning - Teaching Computers to Learn!</h2><p>Machine Learning is a subset of AI where systems learn from data to make decisions without being explicitly programmed.</p><h3>Types of Machine Learning</h3><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:15px;margin:15px 0"><div style="background:#e8f5e9;padding:15px;border-radius:8px;text-align:center"><h4>Supervised Learning</h4><p>Learns from labeled data</p><p><em>Email spam detection, House price prediction</em></p></div><div style="background:#e3f2fd;padding:15px;border-radius:8px;text-align:center"><h4>Unsupervised Learning</h4><p>Finds patterns in unlabeled data</p><p><em>Customer segmentation, Topic modeling</em></p></div><div style="background:#fce4ec;padding:15px;border-radius:8px;text-align:center"><h4>Reinforcement Learning</h4><p>Learns through rewards & penalties</p><p><em>Game playing, Robot control</em></p></div></div>', 'duration_minutes': 30},
        ]
    },
    {
        'category': 'AI & ML',
        'title': 'AI Tools Masterclass',
        'short_description': 'Master 20+ AI tools for productivity, content creation, coding & business',
        'description': 'Practical masterclass on using AI tools effectively for different purposes - writing, design, coding, video, audio, presentations, research and automation.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '10 hours',
        'rating': 4.9,
        'students_count': 520,
        'is_featured': True,
        'what_you_learn': 'ChatGPT Advanced Usage\nClaude AI for Writing & Analysis\nMidjourney for Image Generation\nCanva AI Features\nNotion AI for Productivity\nGitHub Copilot for Coding\nElevenLabs for Voice\nAutomate Work with AI',
        'modules': [
            {'title': 'Top AI Tools Overview', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Top 20 AI Tools You Must Know in 2025!</h2><h3>Category-wise AI Tools</h3><h4>🤖 AI Chatbots & Writing</h4><ul><li><strong>ChatGPT (OpenAI)</strong> - Best for general tasks, coding, writing</li><li><strong>Claude (Anthropic)</strong> - Best for analysis, long documents, safety</li><li><strong>Gemini (Google)</strong> - Best for Google Workspace integration</li><li><strong>Perplexity AI</strong> - Best for research with citations</li></ul><h4>🎨 AI Image Generation</h4><ul><li><strong>Midjourney</strong> - Highest quality artistic images</li><li><strong>DALL-E 3</strong> - Available in ChatGPT Plus</li><li><strong>Stable Diffusion</strong> - Free, open-source, local</li><li><strong>Adobe Firefly</strong> - Professional, commercially safe</li></ul><h4>💻 AI Coding Tools</h4><ul><li><strong>GitHub Copilot</strong> - Best AI pair programmer</li><li><strong>Cursor</strong> - AI-first code editor</li><li><strong>Replit AI</strong> - Online coding with AI</li><li><strong>Claude</strong> - Excellent at code review and generation</li></ul><h4>🎵 AI Audio & Video</h4><ul><li><strong>ElevenLabs</strong> - Ultra-realistic voice cloning</li><li><strong>Suno AI</strong> - Generate complete songs with AI</li><li><strong>RunwayML</strong> - AI video generation & editing</li><li><strong>Descript</strong> - Edit video by editing text</li></ul>', 'duration_minutes': 25},
        ]
    },
    {
        'category': 'Data Science',
        'title': 'Data Science Complete Bootcamp',
        'short_description': 'Complete Data Science - Python, Pandas, NumPy, Matplotlib, ML & more',
        'description': 'Full Data Science bootcamp covering Python for Data Science, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, and real-world projects.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '60 hours',
        'rating': 4.9,
        'students_count': 340,
        'is_featured': True,
        'what_you_learn': 'Python for Data Science\nNumPy - Array Operations\nPandas - Data Manipulation\nMatplotlib & Seaborn - Visualization\nExploratory Data Analysis (EDA)\nStatistics for Data Science\nMachine Learning with Sklearn\nReal-world Project',
        'modules': [
            {'title': 'NumPy - Numerical Python', 'order': 1, 'content_type': 'text', 'text_content': '<h2>NumPy - The Foundation of Data Science</h2><p>NumPy (Numerical Python) is the fundamental library for scientific computing in Python. It provides powerful N-dimensional array objects and mathematical functions.</p><pre><code>import numpy as np\n\n# Creating arrays\narr1 = np.array([1, 2, 3, 4, 5])\narr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n\nprint(arr1.shape)    # (5,)\nprint(arr2.shape)    # (3, 3)\nprint(arr2.ndim)     # 2 dimensions\n\n# Array operations\na = np.array([10, 20, 30, 40])\nb = np.array([1, 2, 3, 4])\n\nprint(a + b)     # [11 22 33 44]\nprint(a * b)     # [10 40 90 160]\nprint(a ** 2)    # [100 400 900 1600]\n\n# Statistical operations\ndata = np.array([23, 45, 12, 67, 34, 89, 56])\nprint(f"Mean: {np.mean(data):.2f}")     # Mean: 46.57\nprint(f"Std: {np.std(data):.2f}")      # Std: 23.97\nprint(f"Max: {np.max(data)}")          # Max: 89\nprint(f"Min: {np.min(data)}")          # Min: 12</code></pre>', 'duration_minutes': 30},
            {'title': 'Pandas - Data Manipulation', 'order': 2, 'content_type': 'text', 'text_content': '<h2>Pandas - Power Tool for Data Analysis</h2><pre><code>import pandas as pd\n\n# Create DataFrame\ndata = {\n    "Name": ["Ramgopal", "Alice", "Bob", "Priya"],\n    "City": ["Indore", "Bhopal", "Indore", "Delhi"],\n    "Age": [22, 25, 28, 23],\n    "Salary": [50000, 75000, 60000, 80000]\n}\ndf = pd.DataFrame(data)\n\n# Basic info\nprint(df.head())        # First 5 rows\nprint(df.info())        # Column types\nprint(df.describe())    # Statistics\n\n# Filtering\nindore_people = df[df["City"] == "Indore"]\nhigh_salary = df[df["Salary"] > 65000]\n\n# Groupby\navg_salary_by_city = df.groupby("City")["Salary"].mean()\nprint(avg_salary_by_city)\n\n# Sorting\ndf_sorted = df.sort_values("Salary", ascending=False)\n\n# Adding new column\ndf["Experience"] = [2, 5, 7, 3]\ndf["Salary_Per_Year"] = df["Salary"] * 12</code></pre>', 'duration_minutes': 35},
        ]
    },
    {
        'category': 'Web Development',
        'title': 'Web Development - HTML, CSS, JS',
        'short_description': 'Complete frontend web development from scratch to building real websites',
        'description': 'Comprehensive web development course covering HTML5, CSS3, JavaScript, Bootstrap, Responsive Design, and building complete websites.',
        'course_type': 'free',
        'level': 'beginner',
        'duration': '30 hours',
        'rating': 4.8,
        'students_count': 460,
        'is_featured': False,
        'what_you_learn': 'HTML5 Structure & Semantic Tags\nCSS3 - Selectors, Box Model, Flexbox, Grid\nJavaScript - Variables, Functions, DOM\nES6+ Modern JavaScript\nBootstrap 5\nResponsive Design\nForm Validation\nBuilding Complete Projects',
        'modules': [
            {'title': 'HTML5 Basics', 'order': 1, 'content_type': 'text', 'text_content': '<h2>HTML5 - The Structure of the Web</h2><p>HTML (HyperText Markup Language) is the standard markup language for creating web pages. Every website you visit uses HTML!</p><pre><code>&lt;!DOCTYPE html&gt;\n&lt;html lang="en"&gt;\n&lt;head&gt;\n    &lt;meta charset="UTF-8"&gt;\n    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;\n    &lt;title&gt;Ram Sir Academy&lt;/title&gt;\n&lt;/head&gt;\n&lt;body&gt;\n    &lt;header&gt;\n        &lt;h1&gt;Welcome to Ram Sir Academy!&lt;/h1&gt;\n        &lt;nav&gt;\n            &lt;a href="#home"&gt;Home&lt;/a&gt;\n            &lt;a href="#courses"&gt;Courses&lt;/a&gt;\n            &lt;a href="#contact"&gt;Contact&lt;/a&gt;\n        &lt;/nav&gt;\n    &lt;/header&gt;\n    &lt;main&gt;\n        &lt;section id="home"&gt;\n            &lt;h2&gt;Free Tech Courses&lt;/h2&gt;\n            &lt;p&gt;Learn programming, web dev, AI and more!&lt;/p&gt;\n            &lt;a href="#courses" class="btn"&gt;Explore Courses&lt;/a&gt;\n        &lt;/section&gt;\n    &lt;/main&gt;\n    &lt;footer&gt;\n        &lt;p&gt;&copy; 2025 Ram Sir. All rights reserved.&lt;/p&gt;\n    &lt;/footer&gt;\n&lt;/body&gt;\n&lt;/html&gt;</code></pre>', 'duration_minutes': 20},
        ]
    },
    {
        'category': 'Data Science',
        'title': 'Data Analytics with Python',
        'short_description': 'Learn data analysis, EDA, visualization and statistical analysis with Python',
        'description': 'Practical Data Analytics course covering exploratory data analysis, statistical methods, data cleaning, visualization, and insights generation.',
        'course_type': 'free',
        'level': 'intermediate',
        'duration': '25 hours',
        'rating': 4.8,
        'students_count': 275,
        'is_featured': False,
        'what_you_learn': 'Data Collection & Cleaning\nExploratory Data Analysis\nStatistical Analysis\nData Visualization with Matplotlib\nSeaborn for Statistical Plots\nCorrelation & Regression\nTime Series Analysis\nBusiness Insights & Reporting',
        'modules': [
            {'title': 'EDA - Exploratory Data Analysis', 'order': 1, 'content_type': 'text', 'text_content': '<h2>Exploratory Data Analysis (EDA)</h2><p>EDA is the first and most important step in any data analysis project. It helps you understand the data before applying any models.</p><h3>EDA Steps</h3><ol><li><strong>Load Data</strong> - Import dataset</li><li><strong>Understand Structure</strong> - Shape, columns, types</li><li><strong>Handle Missing Values</strong> - Find and fix nulls</li><li><strong>Descriptive Statistics</strong> - Mean, median, std</li><li><strong>Distributions</strong> - Histograms, box plots</li><li><strong>Relationships</strong> - Correlation, scatter plots</li><li><strong>Insights</strong> - Draw conclusions</li></ol><pre><code>import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# Load data\ndf = pd.read_csv("student_data.csv")\n\n# Basic exploration\nprint(df.shape)           # (rows, columns)\nprint(df.dtypes)          # Column types\nprint(df.isnull().sum())  # Missing values\nprint(df.describe())      # Statistics\n\n# Visualization\nfig, axes = plt.subplots(1, 2, figsize=(12, 5))\n\n# Distribution of marks\naxes[0].hist(df[\'marks\'], bins=20, color=\'#ff6b35\')\naxes[0].set_title(\'Marks Distribution\')\n\n# Box plot by city\ndf.boxplot(column=\'marks\', by=\'city\', ax=axes[1])\naxes[1].set_title(\'Marks by City\')\n\nplt.tight_layout()\nplt.show()</code></pre>', 'duration_minutes': 35},
        ]
    },
    # PAID COURSES
    {
        'category': 'Web Development',
        'title': 'Full Stack Django Masterclass',
        'short_description': 'Build production-ready web apps with Django, REST API, PostgreSQL & deployment',
        'description': 'Advanced Full Stack Django course. Build complete web applications with Django, Django REST Framework, PostgreSQL, Redis, Celery, Docker, and deploy to cloud.',
        'course_type': 'paid',
        'price': 999,
        'level': 'advanced',
        'duration': '60 hours',
        'rating': 4.9,
        'students_count': 85,
        'is_featured': True,
        'what_you_learn': 'Django Advanced Architecture\nDjango REST Framework\nAuthentication with JWT\nPostgreSQL & Advanced Queries\nRedis for Caching\nCelery for Background Tasks\nDocker & Containerization\nAWS/Heroku Deployment',
        'modules': [
            {'title': 'Course Preview - Django Architecture', 'order': 1, 'is_preview': True, 'content_type': 'text', 'text_content': '<h2>Full Stack Django Masterclass Preview</h2><p>Welcome! This is a preview of our premium Django course. In this course you will build a complete e-commerce platform from scratch.</p><h3>What You Will Build</h3><ul><li>Complete e-commerce website with cart & checkout</li><li>REST API for mobile apps</li><li>Admin dashboard with analytics</li><li>Payment integration</li><li>Docker containerization</li><li>AWS deployment</li></ul><p><strong>Enroll now to get full access to all 60+ video lectures, projects, and doubt sessions!</strong></p>', 'duration_minutes': 10},
        ]
    },
    {
        'category': 'Data Science',
        'title': 'Machine Learning & Deep Learning Pro',
        'short_description': 'Advanced ML & DL - build real projects using TensorFlow, PyTorch & more',
        'description': 'Advanced Machine Learning and Deep Learning course. Build neural networks, CNNs, RNNs, GANs, Transformers. Real projects including image classification, NLP, recommendation systems.',
        'course_type': 'paid',
        'price': 1499,
        'level': 'advanced',
        'duration': '80 hours',
        'rating': 4.9,
        'students_count': 62,
        'is_featured': True,
        'what_you_learn': 'Advanced ML Algorithms\nNeural Networks from Scratch\nCNN - Image Classification\nRNN & LSTM - Sequence Models\nTransformers & Attention\nGANs - Generative Models\nTensorFlow & PyTorch\n5 Real Projects',
        'modules': [
            {'title': 'Course Preview - What You Will Learn', 'order': 1, 'is_preview': True, 'content_type': 'text', 'text_content': '<h2>ML & DL Pro - Course Preview</h2><p>This premium course takes you from intermediate ML to advanced Deep Learning. You will build 5 complete projects.</p><h3>Projects Included</h3><ol><li>Face Recognition System</li><li>Sentiment Analysis API</li><li>Object Detection App</li><li>Music Recommendation System</li><li>Stock Price Predictor</li></ol>', 'duration_minutes': 10},
        ]
    },
    {
        'category': 'Cloud',
        'title': 'AWS Cloud Practitioner + Solutions Architect',
        'short_description': 'Complete AWS course - from basics to Solutions Architect certification prep',
        'description': 'Comprehensive AWS course covering 30+ services, hands-on labs, architecture design, security, and preparation for AWS Solutions Architect Associate certification.',
        'course_type': 'paid',
        'price': 1999,
        'level': 'intermediate',
        'duration': '50 hours',
        'rating': 4.8,
        'students_count': 48,
        'is_featured': False,
        'what_you_learn': 'AWS Core Services (EC2, S3, RDS, Lambda)\nVPC & Networking\nIAM & Security\nLoad Balancing & Auto Scaling\nServerless Architecture\nCloudFormation & IaC\nMonitoring with CloudWatch\nCertification Exam Prep',
        'modules': [
            {'title': 'AWS Preview - Cloud Concepts', 'order': 1, 'is_preview': True, 'content_type': 'text', 'text_content': '<h2>AWS Cloud Course Preview</h2><p>Cloud computing is the future! AWS holds 31% market share. This course prepares you for real-world cloud jobs and AWS certification.</p><h3>Why AWS?</h3><ul><li>Most widely used cloud platform</li><li>Average salary: 8-15 LPA for cloud engineers</li><li>Certifications highly valued by employers</li><li>Hands-on labs on real AWS account</li></ul>', 'duration_minutes': 10},
        ]
    },
]


class Command(BaseCommand):
    help = 'Populate database with initial course data for Ram Sir Platform'

    def handle(self, *args, **options):
        self.stdout.write('Creating categories...')

        categories = {
            'Programming': Category.objects.get_or_create(name='Programming', defaults={'icon': 'fas fa-code', 'color': '#ff6b35'})[0],
            'Database': Category.objects.get_or_create(name='Database', defaults={'icon': 'fas fa-database', 'color': '#4361ee'})[0],
            'Data Science': Category.objects.get_or_create(name='Data Science', defaults={'icon': 'fas fa-chart-line', 'color': '#7209b7'})[0],
            'AI & ML': Category.objects.get_or_create(name='AI & ML', defaults={'icon': 'fas fa-robot', 'color': '#2ec4b6'})[0],
            'Web Development': Category.objects.get_or_create(name='Web Development', defaults={'icon': 'fas fa-globe', 'color': '#e63946'})[0],
            'Cloud': Category.objects.get_or_create(name='Cloud Computing', defaults={'icon': 'fas fa-cloud', 'color': '#0077b6'})[0],
        }

        self.stdout.write('Creating courses and modules...')

        for course_data in COURSES_DATA:
            cat_name = course_data.pop('category')
            modules_data = course_data.pop('modules', [])

            course, created = Course.objects.get_or_create(
                title=course_data['title'],
                defaults={**course_data, 'category': categories[cat_name]}
            )

            if created:
                for mod_data in modules_data:
                    Module.objects.create(course=course, **mod_data)
                self.stdout.write(f'  ✅ Created: {course.title}')
            else:
                self.stdout.write(f'  ⏭️  Exists: {course.title}')

        self.stdout.write(self.style.SUCCESS(f'\n🎉 Done! Created {len(COURSES_DATA)} courses.'))
        self.stdout.write('\nNext steps:')
        self.stdout.write('  python manage.py createsuperuser')
        self.stdout.write('  python manage.py runserver')
