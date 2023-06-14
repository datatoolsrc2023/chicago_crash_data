/* Primary contributory cause by total count, over all years of available data */

SELECT prim_contributory_cause, count(*) as count
FROM {{ ref('crashes_stg') }}
GROUP BY 1 ORDER BY 2 DESC