-- Lightweight schema for Statelessness, Nationality, and International Protection
CREATE TABLE IF NOT EXISTS primary_authorities (
  source_id TEXT PRIMARY KEY,
  source_title TEXT NOT NULL,
  source_type TEXT,
  institution TEXT,
  year TEXT,
  url TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS statelessness_framework (
  concept TEXT,
  legal_source TEXT,
  core_question TEXT,
  practice_use TEXT
);

CREATE TABLE IF NOT EXISTS protection_pathways (
  pathway TEXT,
  trigger TEXT,
  institutional_actor TEXT,
  legal_question TEXT,
  output TEXT
);
