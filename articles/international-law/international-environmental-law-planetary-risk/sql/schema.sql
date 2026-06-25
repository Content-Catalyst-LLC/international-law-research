-- Article support schema for International Environmental Law and the Governance of Planetary Risk
CREATE TABLE IF NOT EXISTS article_metadata (
  slug TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  seo_title TEXT,
  focus_keyword TEXT,
  series TEXT,
  excerpt TEXT
);

CREATE TABLE IF NOT EXISTS primary_authorities (
  authority TEXT NOT NULL,
  year TEXT,
  institution TEXT,
  legal_function TEXT,
  url TEXT
);

CREATE TABLE IF NOT EXISTS environmental_law_framework (
  principle_or_duty TEXT NOT NULL,
  legal_role TEXT,
  typical_evidence TEXT,
  practice_question TEXT
);

CREATE TABLE IF NOT EXISTS planetary_risk_governance (
  risk_domain TEXT NOT NULL,
  legal_tools TEXT,
  governance_challenge TEXT
);
