WITH agg as (
    SELECT year, clean_make || ' ' || model || ' ' || vehicle_year AS make_model_year, count
    FROM {{ ref('make_model_year_by_crash_year') }}
)

SELECT year, make_model_year, count, rank() OVER (PARTITION BY year ORDER BY count desc) position
FROM agg
ORDER BY year

