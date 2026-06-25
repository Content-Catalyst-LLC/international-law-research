CREATE TABLE IF NOT EXISTS gender_violence_issue_areas (
    id INTEGER PRIMARY KEY,
    issue_area TEXT NOT NULL,
    legal_framework TEXT,
    public_private_dimension TEXT,
    core_rights TEXT,
    example_context TEXT
);

CREATE TABLE IF NOT EXISTS due_diligence_duties (
    id INTEGER PRIMARY KEY,
    duty_stage TEXT NOT NULL,
    description TEXT,
    legal_question TEXT,
    example_evidence TEXT
);

CREATE TABLE IF NOT EXISTS procedural_risks (
    id INTEGER PRIMARY KEY,
    risk_type TEXT NOT NULL,
    description TEXT,
    legal_consequence TEXT,
    lawyer_facing_question TEXT
);

CREATE TABLE IF NOT EXISTS primary_authorities (
    id INTEGER PRIMARY KEY,
    authority_name TEXT NOT NULL,
    authority_type TEXT,
    year INTEGER,
    legal_domain TEXT,
    relevance TEXT
);
