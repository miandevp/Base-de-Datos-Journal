CREATE TABLE Employee(
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(30) NOT NULL,
    salary NUMERIC(10,2) NOT NULL CHECK(salary > 0)
);