-- Territory, Borders, and Boundary Disputes companion schema

CREATE TABLE IF NOT EXISTS territory_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS territory_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS territory_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES territory_sources(source_id)
);

CREATE TABLE IF NOT EXISTS boundary_case_notes (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    territory_type TEXT,
    doctrinal_focus TEXT,
    article_section TEXT,
    url TEXT
);

CREATE TABLE IF NOT EXISTS boundary_doctrine_map (
    doctrine_id INTEGER PRIMARY KEY,
    doctrine_name TEXT NOT NULL,
    legal_function TEXT,
    evidentiary_role TEXT,
    justice_tension TEXT,
    article_section TEXT
);
