CREATE TABLE IF NOT EXISTS article_sources (
  source_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  source_type TEXT,
  institution TEXT,
  year TEXT,
  url TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS article_matrices (
  matrix_name TEXT NOT NULL,
  row_id INTEGER NOT NULL,
  field_name TEXT NOT NULL,
  field_value TEXT,
  PRIMARY KEY (matrix_name, row_id, field_name)
);

