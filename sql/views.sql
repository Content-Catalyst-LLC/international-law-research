CREATE VIEW IF NOT EXISTS v_article_roadmap AS
SELECT
    pa.priority,
    pa.status,
    r.regime_name,
    pa.title,
    pa.slug,
    pa.article_type,
    pa.source_focus,
    pa.notes
FROM planned_articles pa
JOIN regimes r ON pa.regime_key = r.regime_key
ORDER BY pa.priority ASC, r.regime_name ASC, pa.title ASC;

CREATE VIEW IF NOT EXISTS v_regime_source_map AS
SELECT
    r.regime_key,
    r.regime_name,
    COUNT(DISTINCT t.treaty_key) AS treaty_count,
    COUNT(DISTINCT i.institution_key) AS institution_count,
    COUNT(DISTINCT c.case_key) AS case_count,
    COUNT(DISTINCT pa.slug) AS article_count
FROM regimes r
LEFT JOIN treaties t ON r.regime_key = t.regime_key
LEFT JOIN institutions i ON r.regime_key = i.regime_key
LEFT JOIN cases c ON r.regime_key = c.regime_key
LEFT JOIN planned_articles pa ON r.regime_key = pa.regime_key
GROUP BY r.regime_key, r.regime_name
ORDER BY r.priority ASC, r.regime_name ASC;

CREATE VIEW IF NOT EXISTS v_treaty_map AS
SELECT
    r.regime_name,
    t.title,
    t.year,
    t.source_type,
    t.official_url,
    t.notes
FROM treaties t
JOIN regimes r ON t.regime_key = r.regime_key
ORDER BY r.priority ASC, t.year ASC, t.title ASC;

CREATE VIEW IF NOT EXISTS v_case_law_map AS
SELECT
    r.regime_name,
    c.title,
    c.year,
    c.court_or_body,
    c.source_type,
    c.official_url,
    c.notes
FROM cases c
JOIN regimes r ON c.regime_key = r.regime_key
ORDER BY c.year ASC, c.title ASC;

CREATE VIEW IF NOT EXISTS v_institution_map AS
SELECT
    r.regime_name,
    i.name,
    i.type,
    i.official_url,
    i.notes
FROM institutions i
JOIN regimes r ON i.regime_key = r.regime_key
ORDER BY r.priority ASC, i.name ASC;

CREATE VIEW IF NOT EXISTS v_missing_official_urls AS
SELECT
    'treaty' AS record_group,
    treaty_key AS record_key,
    title,
    source_type,
    official_url
FROM treaties
WHERE official_url IS NULL OR TRIM(official_url) = ''
UNION ALL
SELECT
    'institution' AS record_group,
    institution_key AS record_key,
    name AS title,
    type AS source_type,
    official_url
FROM institutions
WHERE official_url IS NULL OR TRIM(official_url) = ''
UNION ALL
SELECT
    'case' AS record_group,
    case_key AS record_key,
    title,
    source_type,
    official_url
FROM cases
WHERE official_url IS NULL OR TRIM(official_url) = ''
UNION ALL
SELECT
    'citation' AS record_group,
    citation_key AS record_key,
    title,
    source_type,
    official_url
FROM citation_records
WHERE official_url IS NULL OR TRIM(official_url) = '';
