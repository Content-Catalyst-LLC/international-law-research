-- International criminal law article schema
CREATE TABLE IF NOT EXISTS icl_primary_sources (
  source_id TEXT PRIMARY KEY,
  source_title TEXT NOT NULL,
  source_type TEXT,
  institution TEXT,
  year INTEGER,
  url TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS icl_crime_architecture (
  crime_category TEXT PRIMARY KEY,
  core_conduct TEXT,
  contextual_element TEXT,
  mental_element TEXT,
  primary_sources TEXT,
  analysis_notes TEXT
);

CREATE TABLE IF NOT EXISTS icl_modes_of_liability (
  mode TEXT PRIMARY KEY,
  core_question TEXT,
  evidence_needed TEXT,
  risk_or_pitfall TEXT
);

CREATE TABLE IF NOT EXISTS icl_workflow_steps (
  step INTEGER PRIMARY KEY,
  task TEXT,
  output TEXT
);
