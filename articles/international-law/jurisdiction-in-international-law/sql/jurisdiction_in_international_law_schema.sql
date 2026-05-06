-- Jurisdiction in International Law companion schema

CREATE TABLE IF NOT EXISTS jurisdiction_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS jurisdiction_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS jurisdiction_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES jurisdiction_sources(source_id)
);

CREATE TABLE IF NOT EXISTS jurisdiction_bases (
    basis_id INTEGER PRIMARY KEY,
    jurisdiction_basis TEXT NOT NULL,
    connecting_factor TEXT,
    ordinary_use TEXT,
    risks_or_limits TEXT,
    key_sources TEXT
);

CREATE TABLE IF NOT EXISTS jurisdiction_case_notes (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    doctrinal_focus TEXT,
    jurisdictional_issue TEXT,
    article_section TEXT,
    url TEXT
);
