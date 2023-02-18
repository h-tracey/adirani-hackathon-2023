with tabele_cte as(
SELECT 
    sum(users) as total
FROM
    analytics.`Age-demographic-overview`)
select 
	Age as age,
    users / total as age_prop

from analytics.`Age-demographic-overview`, tabele_cte