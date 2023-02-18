with tabele_cte as(
SELECT 
    sum(users) as total
FROM
    analytics.`Interest-demographic-overview`)
select 
	Interests as interests,
    Users / total as prop_users

from analytics.`Interest-demographic-overview`, tabele_cte