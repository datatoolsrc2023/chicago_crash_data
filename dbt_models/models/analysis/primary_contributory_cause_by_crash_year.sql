/* Primary contributory crash cause by year */

SELECT extract('year' FROM crash_date) AS year, prim_contributory_cause AS primary_contributory_cause, count(*) as count
FROM {{ ref('crashes_stg') }}
GROUP BY 1,2 ORDER BY 1
