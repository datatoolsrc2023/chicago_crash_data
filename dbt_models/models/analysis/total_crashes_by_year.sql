/* Total accident count by year */

SELECT EXTRACT(year from crash_date) as crash_year, count(*) AS count
FROM {{ ref('crashes_stg')}}
GROUP BY 1 ORDER BY 2 DESC