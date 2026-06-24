-- Example queries for Compliance, Enforcement, and the Limits of International Adjudication

-- List primary authorities by type
SELECT source_type, COUNT(*) AS authority_count
FROM primary_sources
GROUP BY source_type
ORDER BY authority_count DESC;

-- Compare enforcement mechanisms
SELECT forum, instrument_or_basis, compliance_pathway, main_limit
FROM enforcement_mechanisms
ORDER BY forum;

-- Identify compliance pathways and practical constraints
SELECT pathway, actors, practical_constraint
FROM compliance_pathways;
