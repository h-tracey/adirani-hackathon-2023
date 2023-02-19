with revenue_group as (
SELECT 
    month(engagement_page_and_screens_engagement_per_page_by_day.date) as month_num,
    MONTHNAME(engagement_page_and_screens_engagement_per_page_by_day.date) as month_of_year,
    YEAR(engagement_page_and_screens_engagement_per_page_by_day.date) as year,
    sum(`Faro Blanco Resort Yacht Club - Reservations - Room Availability` + `Hotels In Marathon FL | Faro Blanco Resort & Marina` + `Faro Blanco Resort | Resorts in Marathon FL | Official Website` + `Faro Blanco Resort Yacht Club - Reservations - Guest Details` + `Marathon Key Restaurants | Dining | Faro Blanco Resort & Marina`) AS tot_conversions,
	round(sum(pp.`Product Revenue`),2) as revenue

FROM
    analytics.engagement_page_and_screens_engagement_per_page_by_day
    left join analytics.product_performance_revenue_by_day pp on engagement_page_and_screens_engagement_per_page_by_day.date = pp.date
group by month_of_year, year, month_num)

select * from revenue_group where tot_conversions > 0
