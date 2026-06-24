CREATE TABLE IF NOT EXISTS civil_political_rights_framework (
  right_area TEXT PRIMARY KEY,
  core_source TEXT,
  core_question TEXT,
  typical_issues TEXT
);

CREATE TABLE IF NOT EXISTS limitations_derogations_matrix (
  doctrine TEXT PRIMARY KEY,
  question TEXT,
  risk TEXT
);

CREATE TABLE IF NOT EXISTS accountability_mechanisms (
  mechanism TEXT PRIMARY KEY,
  role TEXT,
  limits TEXT
);
