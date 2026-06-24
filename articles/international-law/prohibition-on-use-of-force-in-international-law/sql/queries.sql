-- Example queries for The Prohibition on the Use of Force in International Law

-- List primary authorities by type
SELECT source_type, COUNT(*) AS authority_count
FROM primary_sources
GROUP BY source_type
ORDER BY authority_count DESC;

-- Review use-of-force authorities
SELECT authority, legal_role, core_rule, article_relevance
FROM use_of_force_authorities;

-- Review claimed lawful-force bases and risks
SELECT claimed_basis, legal_status, required_showing, main_risk
FROM exceptions_framework;

-- Review leading cases
SELECT case_or_authority, forum, year, issue, use_of_force_significance
FROM case_matrix;
