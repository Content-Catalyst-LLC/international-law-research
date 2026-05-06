-- Fragmentation and Coherence companion schema

CREATE TABLE IF NOT EXISTS fragmentation_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS fragmentation_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS fragmentation_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES fragmentation_sources(source_id)
);

CREATE TABLE IF NOT EXISTS regime_interaction_notes (
    note_id INTEGER PRIMARY KEY,
    regime_a TEXT NOT NULL,
    regime_b TEXT NOT NULL,
    interaction_type TEXT,
    doctrinal_tool TEXT,
    power_asymmetry_notes TEXT
);
