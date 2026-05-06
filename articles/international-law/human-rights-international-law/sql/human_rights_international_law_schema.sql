-- Human Rights in International Law companion schema

CREATE TABLE IF NOT EXISTS human_rights_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS human_rights_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS human_rights_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES human_rights_sources(source_id)
);

CREATE TABLE IF NOT EXISTS human_rights_treaty_profiles (
    treaty_id INTEGER PRIMARY KEY,
    treaty_name TEXT NOT NULL,
    year_adopted INTEGER,
    monitoring_body TEXT,
    rights_focus TEXT,
    complaint_mechanism_notes TEXT,
    url TEXT
);
