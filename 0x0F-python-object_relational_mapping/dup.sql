-- check duplicates
SELECT state, COUNT(*) AS num_rows
FROM states
GROUP BY state
HAVING COUNT(*) > 1;
