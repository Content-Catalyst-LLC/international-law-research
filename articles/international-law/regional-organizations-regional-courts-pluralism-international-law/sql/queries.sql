-- Queries for Regional Organizations, Regional Courts, and Pluralism in International Law

-- List primary sources by institution.
SELECT institution, source_title, source_type, year, url
FROM primary_sources
ORDER BY institution, year;

-- List regional courts by region.
SELECT region, court_name, legal_basis, access_model, main_subjects
FROM regional_court_matrix
ORDER BY region, court_name;

-- List pluralism examples by legal issue.
SELECT example, region, legal_issue, pluralism_problem, analytical_use
FROM regional_pluralism_examples
ORDER BY region, example;
