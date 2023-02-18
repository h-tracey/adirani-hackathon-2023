SELECT * FROM analytics.`Country-demographic-overview`;

with tabele_cte as(
SELECT 
    sum(users) as total
FROM
    analytics.`Country-demographic-overview`)
select 
	o.Country as country,
    d.Conversions as conversions,
    Users as total_users,
    Users / total as prop_users,
	d.Conversions / Users as conversion_per_user
    

from tabele_cte, analytics.`Country-demographic-overview` o
inner join analytics.`demographic_details` d on d.Country = o.Country