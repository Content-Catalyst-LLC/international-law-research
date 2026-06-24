-- Command Responsibility / Modes of Participation article schema
CREATE TABLE IF NOT EXISTS liability_modes (
  mode TEXT PRIMARY KEY,
  core_question TEXT,
  key_evidence TEXT,
  common_risk TEXT
);

CREATE TABLE IF NOT EXISTS command_responsibility_elements (
  element TEXT PRIMARY KEY,
  proof_question TEXT,
  evidence TEXT,
  analysis_note TEXT
);

CREATE TABLE IF NOT EXISTS evidence_linkage (
  evidence_category TEXT PRIMARY KEY,
  function TEXT,
  examples TEXT,
  linkage_issue TEXT
);
