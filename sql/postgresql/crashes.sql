CREATE TABLE IF NOT EXISTS crashes (
    crash_record_id TEXT,
    rd_no TEXT,
    crash_date_est_i BOOLEAN,
    crash_date TIMESTAMP,
    posted_speed_limit TEXT,
    traffic_control_device TEXT,
    device_condition TEXT,
    weather_condition TEXT,
    lighting_condition TEXT,
    first_crash_type TEXT,
    trafficway_type TEXT,
    lane_cnt INTEGER,
    alignment TEXT, 
    roadway_surface_cond TEXT, 
    road_defect TEXT, 
    report_type TEXT, 
    crash_type TEXT, 
    intersection_related_i BOOLEAN, 
    not_right_of_way_i BOOLEAN, 
    hit_and_run_i BOOLEAN, 
    damage TEXT, 
    date_police_notified TIMESTAMP, 
    prim_contributory_cause TEXT, 
    sec_contributory_cause TEXT, 
    street_no INTEGER, 
    street_direction TEXT, 
    street_name TEXT, 
    beat_of_occurrence INTEGER, 
    photos_taken_i BOOLEAN, 
    statements_taken_i BOOLEAN, 
    dooring_i BOOLEAN, 
    work_zone_i BOOLEAN, 
    work_zone_type TEXT, 
    workers_present_i BOOLEAN, 
    num_units INTEGER, 
    most_severe_injury TEXT, 
    injuries_total INTEGER,
    injuries_fatal INTEGER,
    injuries_incapacitating INTEGER,
    injuries_non_incapacitating INTEGER,
    injuries_reported_not_evident INTEGER,
    injuries_no_indication INTEGER,
    injuries_unknown INTEGER,
    crash_hour INTEGER,
    crash_day_of_week INTEGER,
    crash_month INTEGER,
    latitude TEXT, 
    longitude TEXT, 
    location TEXT
);