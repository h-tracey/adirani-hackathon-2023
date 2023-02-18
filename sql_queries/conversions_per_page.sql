SELECT 
    `Page title and screen class` AS page,
    `Conversions` / `Views` AS conversion_rate_total,
    `Conversions` / `Users` AS conversion_rate_per_user,
    `Views per user` as views_per_user
FROM
    analytics.engagement_page_and_screens_page_engagements_totals;