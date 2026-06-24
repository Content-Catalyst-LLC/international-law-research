CREATE TABLE womens_rights_primary_authorities (
  source_id TEXT PRIMARY KEY,
  source_title TEXT NOT NULL,
  source_type TEXT,
  institution TEXT,
  year TEXT,
  url TEXT,
  notes TEXT
);

CREATE TABLE womens_rights_framework_matrix (
  doctrine TEXT PRIMARY KEY,
  legal_function TEXT,
  practice_question TEXT
);

CREATE TABLE womens_rights_protection_mechanisms (
  mechanism TEXT PRIMARY KEY,
  legal_role TEXT,
  use_case TEXT
);
