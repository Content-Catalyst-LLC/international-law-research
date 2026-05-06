-- International Courts and Tribunals companion schema

CREATE TABLE IF NOT EXISTS adjudication_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS adjudication_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS adjudication_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES adjudication_sources(source_id)
);

CREATE TABLE IF NOT EXISTS tribunal_profiles (
    tribunal_id INTEGER PRIMARY KEY,
    tribunal_name TEXT NOT NULL,
    tribunal_type TEXT,
    subject_matter TEXT,
    jurisdiction_basis TEXT,
    access_notes TEXT,
    enforcement_notes TEXT,
    url TEXT
);
