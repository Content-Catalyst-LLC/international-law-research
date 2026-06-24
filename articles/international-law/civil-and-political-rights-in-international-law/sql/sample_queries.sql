-- List civil and political rights by treaty source
SELECT right_area, core_source, core_question
FROM civil_political_rights_framework
ORDER BY right_area;

-- Review limitation and derogation checks
SELECT doctrine, question, risk
FROM limitations_derogations_matrix;

-- Compare accountability mechanisms
SELECT mechanism, role, limits
FROM accountability_mechanisms;
