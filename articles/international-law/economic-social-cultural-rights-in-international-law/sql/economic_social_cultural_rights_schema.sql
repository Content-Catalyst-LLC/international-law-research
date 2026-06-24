-- Economic, Social, and Cultural Rights article schema
CREATE TABLE IF NOT EXISTS esc_rights_framework (
  right_area TEXT PRIMARY KEY,
  core_rights TEXT NOT NULL,
  primary_sources TEXT NOT NULL,
  analysis_notes TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS progressive_realization_matrix (
  concept TEXT PRIMARY KEY,
  meaning TEXT NOT NULL,
  lawyer_question TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS accountability_mechanisms_matrix (
  mechanism TEXT PRIMARY KEY,
  function TEXT NOT NULL,
  limits TEXT NOT NULL
);
