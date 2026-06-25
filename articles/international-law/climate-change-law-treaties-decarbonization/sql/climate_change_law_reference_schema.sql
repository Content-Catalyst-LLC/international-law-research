-- Climate Change Law, Treaties, and the Legal Politics of Decarbonization
-- Lightweight reference schema for article research materials.

CREATE TABLE IF NOT EXISTS climate_law_authorities (
    id INTEGER PRIMARY KEY,
    authority_name TEXT NOT NULL,
    authority_type TEXT,
    legal_role TEXT,
    url TEXT
);

CREATE TABLE IF NOT EXISTS decarbonization_issues (
    id INTEGER PRIMARY KEY,
    issue_name TEXT NOT NULL,
    legal_hook TEXT,
    practical_question TEXT
);

CREATE TABLE IF NOT EXISTS climate_risk_workflows (
    id INTEGER PRIMARY KEY,
    risk_type TEXT NOT NULL,
    legal_domains TEXT,
    evidence_needed TEXT
);
