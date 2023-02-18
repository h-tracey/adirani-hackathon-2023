SELECT 
    JSON_LENGTH(`Default channel group`) AS num_touchpoints,
    sum(Conversions)
FROM
    analytics.advertising_overview_touchpoints_to_conversion
group by array_length