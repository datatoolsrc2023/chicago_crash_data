SELECT extract('year' FROM crash_date) as crash_year, crash_month, count(*)
FROM {{ ref('crashes_stg') }}
GROUP BY 1, 2
ORDER BY 1