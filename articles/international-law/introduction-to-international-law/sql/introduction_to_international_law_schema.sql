-- Introduction to International Law companion schema

CREATE TABLE IF NOT EXISTS international_law_intro_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS international_law_intro_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS international_law_intro_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES international_law_intro_sources(source_id)
);

CREATE TABLE IF NOT EXISTS source_taxonomy (
    taxonomy_id INTEGER PRIMARY KEY,
    source_name TEXT NOT NULL,
    source_category TEXT,
    definition TEXT,
    example TEXT,
    article_section TEXT
);
