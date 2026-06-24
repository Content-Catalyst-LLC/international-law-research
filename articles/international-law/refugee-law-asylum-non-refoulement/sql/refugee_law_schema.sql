CREATE TABLE IF NOT EXISTS refugee_law_authorities (
  source_id TEXT PRIMARY KEY,
  source_title TEXT NOT NULL,
  source_type TEXT,
  institution TEXT,
  year TEXT,
  url TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS refugee_law_framework (
  component TEXT,
  legal_source TEXT,
  core_question TEXT,
  lawyer_use TEXT
);

CREATE TABLE IF NOT EXISTS non_refoulement_analysis (
  pathway TEXT,
  source TEXT,
  threshold TEXT,
  common_issue TEXT
);
