-- Example schema for ICC global justice article data
CREATE TABLE IF NOT EXISTS icc_institutional_architecture (
  component TEXT PRIMARY KEY,
  legal_function TEXT,
  political_tension TEXT,
  lawyer_check TEXT
);

CREATE TABLE IF NOT EXISTS icc_admissibility_complementarity_matrix (
  issue TEXT PRIMARY KEY,
  question TEXT,
  authority TEXT,
  risk TEXT
);

CREATE TABLE IF NOT EXISTS icc_cooperation_enforcement_matrix (
  constraint_name TEXT PRIMARY KEY,
  legal_position TEXT,
  political_effect TEXT,
  practice_note TEXT
);
