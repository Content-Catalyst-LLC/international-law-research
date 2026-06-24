-- Query examples for the Self-Defense / UN Charter article folder.

-- List primary authorities by year.
SELECT source_id, source_title, source_type, institution, year, url
FROM primary_sources
ORDER BY year, source_id;

-- Find ICJ cases used in the article.
SELECT case, year, forum, core_issue, article_relevance, url
FROM case_matrix
ORDER BY year;

-- Review self-defense elements.
SELECT issue, legal_question, key_authority, analysis_notes
FROM self_defense_framework_matrix;
