-- Sources of International Law companion schema

CREATE TABLE IF NOT EXISTS source_law_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS source_law_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    source_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS source_law_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES source_law_sources(source_id)
);

CREATE TABLE IF NOT EXISTS source_law_article_sections (
    section_id INTEGER PRIMARY KEY,
    section_anchor TEXT NOT NULL,
    section_title TEXT NOT NULL,
    doctrinal_focus TEXT,
    source_focus TEXT,
    critical_focus TEXT
);
