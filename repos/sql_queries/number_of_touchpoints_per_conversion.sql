SELECT 
    JSON_LENGTH(`Default channel group`) AS num_touchpoints,
    sum(Conversions) as num_conversions
FROM
    analytics.advertising_overview_touchpoints_to_conversion
group by num_touchpoints