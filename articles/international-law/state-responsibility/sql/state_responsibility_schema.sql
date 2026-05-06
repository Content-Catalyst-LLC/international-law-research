-- State Responsibility companion schema

CREATE TABLE IF NOT EXISTS state_responsibility_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS state_responsibility_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS state_responsibility_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES state_responsibility_sources(source_id)
);

CREATE TABLE IF NOT EXISTS state_responsibility_case_notes (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    court TEXT,
    year INTEGER,
    doctrinal_focus TEXT,
    article_section TEXT,
    url TEXT
);
