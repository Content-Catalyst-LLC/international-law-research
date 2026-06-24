-- Weapons law article support schema
CREATE TABLE IF NOT EXISTS weapons_law_matrix (
  category TEXT PRIMARY KEY,
  legal_question TEXT NOT NULL,
  key_sources TEXT NOT NULL,
  lawyer_task TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS article_36_review_matrix (
  stage TEXT PRIMARY KEY,
  review_question TEXT NOT NULL,
  evidence TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS emerging_military_technologies_matrix (
  technology TEXT PRIMARY KEY,
  core_issue TEXT NOT NULL,
  review_focus TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS war_crimes_weapons_law_matrix (
  risk_area TEXT PRIMARY KEY,
  legal_concern TEXT NOT NULL,
  documentation_needed TEXT NOT NULL
);
