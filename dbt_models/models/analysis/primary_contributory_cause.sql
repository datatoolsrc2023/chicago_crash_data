SELECT prim_contributory_cause, count(*)
FROM {{ ref(crashes_stg) }}
GROUP BY 1 ORDER BY 2 DESC;