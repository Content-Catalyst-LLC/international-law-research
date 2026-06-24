CREATE TABLE IF NOT EXISTS nuremberg_tokyo_development_matrix (
    phase TEXT,
    period TEXT,
    institution_or_forum TEXT,
    legal_contribution TEXT,
    limits_or_critique TEXT
);

CREATE TABLE IF NOT EXISTS tribunal_comparison_matrix (
    tribunal TEXT,
    legal_basis TEXT,
    jurisdiction_focus TEXT,
    legacy TEXT,
    core_limitation TEXT
);

CREATE TABLE IF NOT EXISTS doctrine_legacy_matrix (
    doctrine TEXT,
    postwar_origin_or_development TEXT,
    later_development TEXT,
    research_question TEXT
);
