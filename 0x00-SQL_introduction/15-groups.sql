-- group by score
SELECT score, COUNT(score) number
FROM second_table
GROUP BY score
ORDER BY score DESC
