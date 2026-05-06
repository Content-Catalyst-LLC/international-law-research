-- Statehood, Recognition, and Legal Personality companion schema

CREATE TABLE IF NOT EXISTS statehood_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS statehood_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS statehood_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES statehood_sources(source_id)
);

CREATE TABLE IF NOT EXISTS status_case_notes (
    case_id INTEGER PRIMARY KEY,
    entity_name TEXT NOT NULL,
    issue_type TEXT,
    legal_status_notes TEXT,
    institutional_status_notes TEXT,
    article_section TEXT,
    url TEXT
);
