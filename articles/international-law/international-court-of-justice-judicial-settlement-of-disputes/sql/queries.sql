-- Starter SQL for The International Court of Justice and the Judicial Settlement of Disputes
-- These queries assume the Catalyst Data export tables have been loaded.

-- Sources connected to this article
SELECT source_id, title, source_type, institution, year, url
FROM sources
WHERE article_slug = 'international-court-of-justice-judicial-settlement-of-disputes'
ORDER BY year, source_id;

-- Legal instruments connected to this article
SELECT instrument_id, instrument_title, instrument_type, institution, year, url
FROM legal_instruments
WHERE article_slug = 'international-court-of-justice-judicial-settlement-of-disputes'
ORDER BY year, instrument_id;

-- Topics connected to this article
SELECT topic, instrument_id, notes
FROM instrument_topics
WHERE article_slug = 'international-court-of-justice-judicial-settlement-of-disputes'
ORDER BY topic, instrument_id;

-- Article map row
SELECT *
FROM article_repository_map
WHERE article_slug = 'international-court-of-justice-judicial-settlement-of-disputes';
