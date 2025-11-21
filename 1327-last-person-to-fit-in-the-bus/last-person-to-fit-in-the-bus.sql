# Write your MySQL query statement below
WITH ordered AS (
    SELECT 
        person_name,
        weight,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
)
SELECT person_name
FROM ordered
WHERE cumulative_weight <= 1000
ORDER BY cumulative_weight DESC
LIMIT 1;
