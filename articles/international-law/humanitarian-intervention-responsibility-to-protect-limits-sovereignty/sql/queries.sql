-- Example Catalyst Data-style queries for the Humanitarian Intervention / R2P article.

SELECT *
FROM sources
WHERE article_id = 'humanitarian-intervention-responsibility-to-protect-limits-sovereignty'
ORDER BY year, source_id;
