-- Starter Catalyst Data queries for International Humanitarian Law: The Geneva Conventions and the Regulation of Armed Conflict

-- Primary sources for the article
SELECT *
FROM sources
WHERE article_slug = 'international-humanitarian-law-geneva-conventions-regulation-armed-conflict'
ORDER BY source_type, year;

-- IHL instruments and cases
SELECT *
FROM legal_instruments
WHERE topic LIKE '%international humanitarian law%'
   OR topic LIKE '%Geneva Conventions%'
   OR topic LIKE '%armed conflict%'
ORDER BY year;

-- Article repository mapping
SELECT *
FROM article_repository_map
WHERE article_slug = 'international-humanitarian-law-geneva-conventions-regulation-armed-conflict';
