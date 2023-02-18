with tabele_cte as(
SELECT 
    sum(users) as total
FROM
    analytics.`Language-demographic-overview`)
select 
	Language as language,
    Users / total as prop_users

from analytics.`Language-demographic-overview`, tabele_cte