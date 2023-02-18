SELECT 
    sum(`Conversions`) / sum(`Views`) AS conversion_rate_total,
    sum(`Conversions`) / sum(`Users`)  AS conversion_rate_per_user,
    sum(`Views per user`) as views_per_user,
    `page_type` as ptype
FROM
    analytics.engagement_page_and_screens_page_engagements_totals 
 
GROUP BY ptype
