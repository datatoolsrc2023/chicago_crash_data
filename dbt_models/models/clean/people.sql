{{ config(materialized='table') }}
SELECT 
    person_id
    ,person_type
    ,crash_record_id
    ,rd_no
    ,vehicle_id
    ,crash_date::TIMESTAMP
    ,seat_no::INTEGER
    ,city
    ,state
    ,zipcode
    ,sex
    ,age::INTEGER
    ,drivers_license_state
    ,drivers_license_class
    ,safety_equipment
    ,airbag_deployed
    ,ejection
    ,injury_classification
    ,hospital
    ,ems_agency
    ,ems_run_no
    ,driver_action
    ,driver_vision
    ,physical_condition
    ,pedpedal_action
    ,pedpedal_visibility
    ,pedpedal_location
    ,bac_result
    ,bac_result_value::FLOAT
    ,case when cell_phone_use = 'N' then false
          when cell_phone_use = 'Y' then true
          else NULL end as cell_phone_use
FROM {{ source('chicago_crashes', 'people_raw') }}