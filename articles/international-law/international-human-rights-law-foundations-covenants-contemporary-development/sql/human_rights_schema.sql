CREATE TABLE IF NOT EXISTS human_rights_framework (
  component TEXT PRIMARY KEY,
  core_instruments TEXT,
  legal_function TEXT,
  practice_question TEXT
);

CREATE TABLE IF NOT EXISTS rights_categories (
  rights_category TEXT PRIMARY KEY,
  core_sources TEXT,
  examples TEXT,
  legal_function TEXT
);

CREATE TABLE IF NOT EXISTS accountability_mechanisms (
  mechanism TEXT PRIMARY KEY,
  institutional_form TEXT,
  strength TEXT,
  limit TEXT
);
