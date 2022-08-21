# Write your MySQL query statement below
SELECT e.Name, b.Bonus 
FROM Employee e
LEFT JOIN Bonus b on e.empId=b.empId
WHERE b.bonus<1000 OR b.bonus is NULL