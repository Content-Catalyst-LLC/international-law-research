-- Research support schema for Power, Inequality, and the Critique of International Law

CREATE TABLE IF NOT EXISTS critical_traditions (
  tradition TEXT PRIMARY KEY,
  central_question TEXT NOT NULL,
  typical_focus TEXT NOT NULL,
  article_relevance TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS power_domains (
  domain TEXT PRIMARY KEY,
  formal_legal_ideal TEXT NOT NULL,
  inequality_problem TEXT NOT NULL,
  diagnostic_question TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS critique_workflow (
  step INTEGER PRIMARY KEY,
  lawyer_facing_task TEXT NOT NULL,
  critique_question TEXT NOT NULL,
  output TEXT NOT NULL
);
