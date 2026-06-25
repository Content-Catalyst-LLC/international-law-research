-- Cyber Operations and Digital Sovereignty article support schema

CREATE TABLE IF NOT EXISTS cyber_law_architecture (
  category TEXT PRIMARY KEY,
  legal_or_institutional_source TEXT NOT NULL,
  function TEXT NOT NULL,
  article_use TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cyber_operations_matrix (
  operation_type TEXT PRIMARY KEY,
  legal_questions TEXT NOT NULL,
  possible_legal_frames TEXT NOT NULL,
  practical_risk TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS digital_sovereignty_governance_matrix (
  issue TEXT PRIMARY KEY,
  governance_question TEXT NOT NULL,
  legal_tension TEXT NOT NULL,
  article_connection TEXT NOT NULL
);
