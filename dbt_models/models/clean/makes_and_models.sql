/* Top 50 make, model, and year of car ordered by total injuries */

SELECT clean_make, model, vehicle_year, sum(injuries_total) sum_total_injuries, sum(injuries_fatal) sum_fatal_injuries
FROM {{ ref('crashes') }} a
INNER JOIN {{ ref('vehicles') }} b
ON a.crash_record_id = b.crash_record_id
WHERE clean_make IS NOT NULL
AND clean_make <> 'UNKNOWN'
AND injuries_total IS NOT NULL
GROUP BY 1,2,3 ORDER BY 4 DESC
LIMIT 50