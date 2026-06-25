-- Empire, Decolonization, and the Making of International Law
-- Lightweight research schema for article support materials.

CREATE TABLE IF NOT EXISTS colonial_legal_forms (
  legal_form TEXT PRIMARY KEY,
  function TEXT NOT NULL,
  modern_relevance TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS decolonization_doctrines (
  doctrine TEXT PRIMARY KEY,
  authority TEXT NOT NULL,
  critical_issue TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS critical_frameworks (
  framework TEXT PRIMARY KEY,
  core_question TEXT NOT NULL,
  article_use TEXT NOT NULL
);
