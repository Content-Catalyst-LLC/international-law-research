-- International Health Law article support schema

CREATE TABLE IF NOT EXISTS health_law_architecture (
  category TEXT PRIMARY KEY,
  legal_or_institutional_source TEXT NOT NULL,
  function TEXT NOT NULL,
  article_use TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pandemic_coordination_matrix (
  coordination_problem TEXT PRIMARY KEY,
  legal_tool TEXT NOT NULL,
  governance_question TEXT NOT NULL,
  practical_risk TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS health_equity_matrix (
  equity_issue TEXT PRIMARY KEY,
  legal_frame TEXT NOT NULL,
  distributional_problem TEXT NOT NULL,
  article_connection TEXT NOT NULL
);
