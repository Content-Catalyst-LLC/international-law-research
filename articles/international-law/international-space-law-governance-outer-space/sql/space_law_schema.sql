-- International Space Law article support schema

CREATE TABLE IF NOT EXISTS space_law_architecture (
  category TEXT PRIMARY KEY,
  legal_or_institutional_source TEXT NOT NULL,
  function TEXT NOT NULL,
  article_use TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS outer_space_governance_matrix (
  governance_problem TEXT PRIMARY KEY,
  legal_tool TEXT NOT NULL,
  core_question TEXT NOT NULL,
  practical_risk TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS space_security_and_equity_matrix (
  issue TEXT PRIMARY KEY,
  legal_frame TEXT NOT NULL,
  distributional_or_security_problem TEXT NOT NULL,
  article_connection TEXT NOT NULL
);
