-- Occupation, detention, and war-torn territory query helpers

SELECT source_id, source_title, source_type, institution, year, url
FROM primary_sources
ORDER BY year, source_id;

SELECT concept, rule_summary, key_authorities
FROM detention_framework_matrix
ORDER BY concept;

SELECT issue, rule_summary, key_authorities
FROM war_crimes_matrix
ORDER BY issue;
