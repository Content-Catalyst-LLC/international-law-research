-- Customary International Law companion schema

CREATE TABLE IF NOT EXISTS customary_law_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS customary_law_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS customary_law_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES customary_law_sources(source_id)
);

CREATE TABLE IF NOT EXISTS customary_law_evidence_types (
    evidence_id INTEGER PRIMARY KEY,
    evidence_type TEXT NOT NULL,
    related_element TEXT,
    description TEXT,
    example_materials TEXT
);
