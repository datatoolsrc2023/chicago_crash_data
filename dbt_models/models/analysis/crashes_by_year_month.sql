/* Total crashes by crash year and month */

SELECT extract('year' FROM crash_date) as year, crash_month as month, count(*) as crash_count
FROM {{ ref('crashes_stg') }}
GROUP BY 1, 2
ORDER BY 1