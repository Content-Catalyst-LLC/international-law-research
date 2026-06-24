-- Universal Jurisdiction article starter schema
CREATE TABLE IF NOT EXISTS universal_jurisdiction_framework (
  issue TEXT PRIMARY KEY,
  legal_question TEXT,
  analysis_focus TEXT,
  practice_note TEXT
);

CREATE TABLE IF NOT EXISTS accountability_pathways (
  pathway TEXT PRIMARY KEY,
  institutional_actor TEXT,
  strength TEXT,
  constraint TEXT
);

CREATE TABLE IF NOT EXISTS immunity_extradition_issues (
  issue TEXT PRIMARY KEY,
  core_rule TEXT,
  risk TEXT,
  lawyer_task TEXT
);
