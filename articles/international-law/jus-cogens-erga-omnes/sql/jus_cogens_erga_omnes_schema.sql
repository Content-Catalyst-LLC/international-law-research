-- Jus Cogens and Erga Omnes companion schema

CREATE TABLE IF NOT EXISTS jus_cogens_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS jus_cogens_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS jus_cogens_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES jus_cogens_sources(source_id)
);

CREATE TABLE IF NOT EXISTS jus_cogens_legal_consequences (
    consequence_id INTEGER PRIMARY KEY,
    consequence_name TEXT NOT NULL,
    legal_basis TEXT,
    description TEXT,
    affected_actors TEXT
);
