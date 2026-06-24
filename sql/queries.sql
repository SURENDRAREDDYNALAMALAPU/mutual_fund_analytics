-- Total records
SELECT COUNT(*) FROM fact_nav;

-- Maximum NAV
SELECT MAX(nav) FROM fact_nav;

-- Minimum NAV
SELECT MIN(nav) FROM fact_nav;

-- Average NAV
SELECT AVG(nav) FROM fact_nav;

-- Top 10 NAV values
SELECT * FROM fact_nav
ORDER BY nav DESC
LIMIT 10;