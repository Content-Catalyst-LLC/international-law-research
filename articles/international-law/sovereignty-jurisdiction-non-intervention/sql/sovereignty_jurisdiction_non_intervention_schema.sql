-- Sovereignty, Jurisdiction, and Non-Intervention companion schema

CREATE TABLE IF NOT EXISTS sovereignty_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS sovereignty_jurisdiction_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS sovereignty_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES sovereignty_sources(source_id)
);

CREATE TABLE IF NOT EXISTS intervention_case_notes (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    court_or_institution TEXT,
    year INTEGER,
    doctrinal_focus TEXT,
    power_asymmetry_notes TEXT,
    article_section TEXT,
    url TEXT
);
