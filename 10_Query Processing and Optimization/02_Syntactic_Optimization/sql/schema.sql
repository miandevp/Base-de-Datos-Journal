CREATE TABLE Department (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE Employee (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    salary NUMERIC(10,2),
    department_id INTEGER
);