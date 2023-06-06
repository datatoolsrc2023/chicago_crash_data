INSERT INTO vehicles
SELECT
    crash_unit_id::INTEGER,
    crash_record_id,
    rd_no,
    crash_date::TIMESTAMP,
    unit_no::INTEGER,
    unit_type,
    num_passengers::INTEGER,
    vehicle_id::INTEGER,
    case when cmrc_veh_i = 'N' then false
        else true end as cmrc_veh_i,
    make,
    case when make = 'TOYOTA MOTOR COMPANY, LTD.' then 'TOYOTA'
        when make = 'GENERAL MOTORS CORP.' then 'GMC'
        when make = 'GENERAL MOTORS CORPORATION (GMC)' then 'GMC'
        when make = 'LINCOLN-CONTINENTAL' then 'LINCOLN'
        when make = 'FREIGHTLINER CORPORATION' then 'FREIGHTLINER'
        when make = 'FREIGHTLINER CORP.' then 'FREIGHTLINER'
        when make = 'ACURA (DIV. OF AMERICAN HONDA MOTOR CO.)' then 'ACURA'
        when make = 'TESLA MOTORS' then 'TESLA'
        when make = 'RANGE ROVER OF NORTH AMERICA' then 'RANGE ROVER'
        when make = 'PONTIAC (CANADIAN)' then 'PONTIAC'
        else make end as clean_make,
    model,
    lic_plate_state,
    vehicle_year::INTEGER,
    vehicle_defect,
    vehicle_type,
    vehicle_use,
    travel_direction,
    maneuver,
    case when towed_i = 'N' then false
        else true end as towed_i,
    case when fire_i = 'N' then false
        else true end as fire_i,
    occupant_cnt::INTEGER,
    case when exceed_speed_limit_i = 'N' then false
        else true end as exceed_speed_limit_i,
    towed_by,
    towed_to,
    case when area_00_i = 'N' then false
        else true end as area_00_i,
    case when area_01_i = 'N' then false
        else true end as area_01_i,
    case when area_02_i = 'N' then false
        else true end as area_02_i,
    case when area_03_i = 'N' then false
        else true end as area_03_i,
    case when area_04_i = 'N' then false
        else true end as area_04_i,
    case when area_05_i = 'N' then false
        else true end as area_05_i,
    case when area_06_i = 'N' then false
        else true end as area_06_i,
    case when area_07_i = 'N' then false
        else true end as area_07_i,
    case when area_08_i = 'N' then false
        else true end as area_08_i,
    case when area_09_i = 'N' then false
        else true end as area_09_i,
    case when area_10_i = 'N' then false
        else true end as area_10_i,
    case when area_11_i = 'N' then false
        else true end as area_11_i,
    case when area_12_i = 'N' then false
        else true end as area_12_i,
    case when area_99_i = 'N' then false
        else true end as area_99_i,
    first_contact_point,
    cmv_id::INTEGER,
    usdot_no,
    ccmc_no,
    ilcc_no,
    commercial_src,
    gvwr,
    carrier_name,
    carrier_state,
    carrier_city,
    case when hazmat_placards_i = 'N' then false
        else true end as hazmat_placards_i,
    hazmat_name,
    un_no,
    case when hazmat_present_i = 'N' then false
        else true end as hazmat_present_i,
    case when hazmat_report_i = 'N' then false
        else true end as hazmat_report_i,
    hazmat_report_no,
    case when mcs_report_i = 'N' then false
        else true end as mcs_report_i,
    mcs_report_no,
    case when hazmat_vio_cause_crash_i = 'N' then false
        else true end as hazmat_vio_cause_crash_i,
    case when mcs_vio_cause_crash_i = 'N' then false
        else true end as mcs_vio_cause_crash_i,
    idot_permit_no,
    case when wide_load_i = 'N' then false
        else true end as wide_load_i,
    trailer1_width,
    trailer2_width,
    trailer1_length::INTEGER,
    trailer2_length::INTEGER,
    total_vehicle_length::INTEGER,
    axle_cnt::INTEGER,
    vehicle_config,
    cargo_body_type,
    load_type,
    case when hazmat_out_of_service_i = 'N' then false
        else true end as hazmat_out_of_service_i,
    case when mcs_out_of_service_i = 'N' then false
        else true end as mcs_out_of_service_i,
    hazmat_class
FROM vehicles_raw
;