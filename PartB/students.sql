CREATE TABLE Students (
    MatricNo TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    CGPA REAL
);

INSERT INTO Students (MatricNo, Name, Department, CGPA) VALUES
('011', 'Tolu Fabiyi', 'Software Engineering', 3.8),
('012', 'Ruth Oluwa', 'IT', 4.5),
('013', 'David Chuks', 'Computer Science', 3.5),
('014', 'Hanna Abiodun', 'Software Engineering', 3.9);

-- Retrieve all students
SELECT * FROM Students;

-- Search for a student by Matric number
SELECT * FROM Students WHERE MatricNo = '012';

-- Find students with GPA > 3.5
SELECT Name, CGPA FROM Students WHERE CGPA > 3.5;
