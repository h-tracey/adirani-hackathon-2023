SELECT 
    DAYNAME(engagement_page_and_screens_engagement_per_page_by_day.date) as day_of_week,
    sum(`Faro Blanco Resort Yacht Club - Reservations - Room Availability` + `Hotels In Marathon FL | Faro Blanco Resort & Marina` + `Faro Blanco Resort | Resorts in Marathon FL | Official Website` + `Faro Blanco Resort Yacht Club - Reservations - Guest Details` + `Marathon Key Restaurants | Dining | Faro Blanco Resort & Marina`) AS tot_conversions,
	round(sum(pp.`Product Revenue`),2) as revenue
FROM
    analytics.engagement_page_and_screens_engagement_per_page_by_day
    
    left join analytics.product_performance_revenue_by_day pp on engagement_page_and_screens_engagement_per_page_by_day.date = pp.date
group by day_of_week
