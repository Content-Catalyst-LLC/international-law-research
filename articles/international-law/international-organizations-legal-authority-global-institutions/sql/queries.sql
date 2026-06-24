-- Catalyst Data helper queries for International Organizations and the Legal Authority of Global Institutions

-- List primary authorities for the article.
SELECT source_id, source_title, source_type, institution, year, url
FROM primary_sources
ORDER BY year, institution, source_title;

-- Identify sources relevant to institutional legal personality.
SELECT source_id, source_title, institution, notes
FROM primary_sources
WHERE lower(notes) LIKE '%legal personality%'
   OR lower(source_title) LIKE '%reparation for injuries%';

-- Review institutional authority concepts.
SELECT concept_id, principle, leading_authority_or_example, practice_note
FROM institution_authority_matrix
ORDER BY concept_id;

-- Organization profile lookup.
SELECT organization_id, organization_name, primary_field, legal_basis, authority_note
FROM organization_profiles
ORDER BY organization_name;
