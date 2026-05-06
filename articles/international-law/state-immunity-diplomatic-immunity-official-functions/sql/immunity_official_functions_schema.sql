-- State Immunity, Diplomatic Immunity, and Official Functions companion schema

CREATE TABLE IF NOT EXISTS immunity_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS immunity_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS immunity_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES immunity_sources(source_id)
);

CREATE TABLE IF NOT EXISTS immunity_case_notes (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    doctrinal_focus TEXT,
    accountability_tension TEXT,
    article_section TEXT,
    url TEXT
);

CREATE TABLE IF NOT EXISTS immunity_categories (
    category_id INTEGER PRIMARY KEY,
    immunity_type TEXT NOT NULL,
    protected_entity_or_function TEXT,
    duration TEXT,
    scope TEXT,
    key_exceptions_or_limits TEXT,
    key_sources TEXT
);
