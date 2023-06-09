/* Total accidents by year */

SELECT EXTRACT(year from crash_date), count(*)
FROM {{ ref('crashes')}}
GROUP BY 1 ORDER BY 2 DESC