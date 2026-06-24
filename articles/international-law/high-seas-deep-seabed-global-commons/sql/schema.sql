-- Schema for structured notes supporting: The High Seas, Deep Seabed Governance, and the Global Commons

CREATE TABLE IF NOT EXISTS authorities (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  year TEXT,
  short_name TEXT,
  url TEXT,
  article_relevance TEXT
);

CREATE TABLE IF NOT EXISTS commons_framework (
  id INTEGER PRIMARY KEY,
  domain TEXT NOT NULL,
  legal_logic TEXT,
  core_issues TEXT,
  primary_sources TEXT,
  interpretive_note TEXT
);

CREATE TABLE IF NOT EXISTS governance_risks (
  id INTEGER PRIMARY KEY,
  issue TEXT NOT NULL,
  governance_risk TEXT,
  legal_response TEXT
);
