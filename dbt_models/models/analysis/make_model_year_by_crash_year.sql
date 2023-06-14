/* Vehicle make, model, and vehicle year by crash year */

SELECT extract('year' FROM crash_date) AS year, clean_make, model, vehicle_year, count(*) AS count
FROM {{ ref('vehicles_stg') }}
GROUP BY 1, 2, 3, 4
ORDER BY 1

