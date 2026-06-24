-- Example SQLite queries for International Arbitration and the Peaceful Settlement of Disputes

-- List primary authorities by institution.
SELECT institution, source_title, year, url
FROM primary_sources
ORDER BY institution, year;

-- Find arbitration institutions by forum type.
SELECT institution_name, forum_type, primary_legal_basis, enforcement_pathway
FROM arbitration_institution_matrix
ORDER BY institution_name;

-- Compare peaceful settlement mechanisms.
SELECT mechanism, legal_basis, binding_effect, key_risks
FROM dispute_settlement_matrix
ORDER BY mechanism_id;

-- Compare award enforcement frameworks.
SELECT framework, scope, enforcement_mechanism, limits
FROM enforcement_framework_matrix
ORDER BY framework_id;
