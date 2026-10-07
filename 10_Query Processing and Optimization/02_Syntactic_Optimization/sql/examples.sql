SELECT e.name, d.department_name
FROM Employee e
JOIN Department d
ON e.department_id = d.department_id
WHERE e.salary > 3000
AND d.department_name = 'IT';