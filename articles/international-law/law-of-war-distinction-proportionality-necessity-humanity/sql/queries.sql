-- Example queries for the Law of War article support data.

-- List all primary authorities for the article.
SELECT source_id, source_title, source_type, institution, year, url
FROM primary_sources
ORDER BY year, source_title;

-- List law-of-war principles by analytic function.
SELECT principle, core_question, legal_function, common_authorities
FROM law_of_war_principles_matrix
ORDER BY principle;

-- List targeting risk flags.
SELECT issue, primary_rule, required_analysis, risk_flags
FROM targeting_rules_matrix
ORDER BY issue;
