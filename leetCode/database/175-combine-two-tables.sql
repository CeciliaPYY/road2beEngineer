# Write your MySQL query statement below
SELECT tbl1.FirstName, tbl1.LastName, tbl2.City, tbl2.State
FROM Person tbl1
LEFT JOIN Address tbl2
ON tbl1.PersonId = tbl2.PersonId;