insert into crashes
select
        crash_record_id
        ,rd_no
        ,case when crash_date_est_i = '' then NULL
                when upper(crash_date_est_i) = 'N' then false
                else true end as crash_date_est_i
        ,crash_date::timestamp
        ,case when posted_speed_limit = '' then NULL
                else posted_speed_limit::INTEGER
                end as posted_speed_limit
        ,traffic_control_device
        ,device_condition
        ,weather_condition
        ,lighting_condition
        ,first_crash_type
        ,trafficway_type
        ,case when lane_cnt = '' then NULL
                else lane_cnt::INTEGER
                end as lane_cnt
        ,alignment
        ,roadway_surface_cond
        ,road_defect
        ,report_type
        ,crash_type
        ,case when intersection_related_i = '' then NULL
                when upper(intersection_related_i) = 'N' then false
                else true end as intersection_related_i
        ,case when not_right_of_way_i = '' then NULL
                when upper(not_right_of_way_i) = 'N' then false
                else true end as not_right_of_way_i
        ,case when hit_and_run_i = '' then NULL
                when upper(hit_and_run_i) = 'N' then false
                else true end as hit_and_run_i
        ,damage
        ,date_police_notified::timestamp
        ,prim_contributory_cause
        ,sec_contributory_cause
        ,street_no::INTEGER
        ,street_direction
        ,street_name
        ,case when beat_of_occurrence = '' then NULL
                else beat_of_occurrence::INTEGER
                end as beat_of_occurrence
        ,case when photos_taken_i = '' then NULL
                when upper(photos_taken_i) = 'N' then false
                else true end as photos_taken_i
        ,case when statements_taken_i = '' then NULL
                when upper(statements_taken_i) = 'N' then false
                else true end as statements_taken_i
        ,case when dooring_i = '' then NULL
                when upper(dooring_i) = 'N' then false
                else true end as dooring_i
        ,case when work_zone_i = '' then NULL
                when upper(work_zone_i) = 'N' then false
                else true end as work_zone_i
        ,work_zone_type
        ,case when workers_present_i = '' then NULL
                when upper(workers_present_i) = 'N' then false
                else true end as workers_present_i
        ,num_units::INTEGER
        ,most_severe_injury
        ,injuries_total::INTEGER
        ,injuries_fatal::INTEGER
        ,injuries_incapacitating::INTEGER
        ,injuries_non_incapacitating::INTEGER
        ,injuries_reported_not_evident::INTEGER
        ,injuries_no_indication::INTEGER
        ,injuries_unknown::INTEGER
        ,crash_hour::INTEGER
        ,crash_day_of_week::INTEGER
        ,crash_month::INTEGER
        ,latitude
        ,longitude
        ,location
FROM crashes_raw
;