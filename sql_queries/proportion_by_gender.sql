with tabele_cte as(
SELECT 
    sum(users) as total
FROM
    analytics.`Gender-demographic-overview`)
select 
	Gender as gender,
    users / total as gender_prop

from analytics.`Gender-demographic-overview`, tabele_cte