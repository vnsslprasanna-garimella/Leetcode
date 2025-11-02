# Write your MySQL query statement below
SELECT 
    ss.student_id,
    ss.student_name,
    ss.subject_name,
    COALESCE(e.attended_exams, 0) AS attended_exams
FROM (
    SELECT s.student_id, s.student_name, sub.subject_name
    FROM Students s
    CROSS JOIN Subjects sub
) ss
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) e
ON ss.student_id = e.student_id
AND ss.subject_name = e.subject_name
ORDER BY ss.student_id, ss.subject_name;
