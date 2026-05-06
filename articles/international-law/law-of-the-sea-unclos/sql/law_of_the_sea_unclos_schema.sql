-- Law of the Sea / UNCLOS companion schema

CREATE TABLE IF NOT EXISTS law_of_the_sea_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS law_of_the_sea_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS law_of_the_sea_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES law_of_the_sea_sources(source_id)
);

CREATE TABLE IF NOT EXISTS maritime_zone_profiles (
    zone_id INTEGER PRIMARY KEY,
    zone_name TEXT NOT NULL,
    maximum_extent_nm INTEGER,
    coastal_state_rights TEXT,
    other_state_rights TEXT,
    key_unclos_articles TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS ocean_governance_case_notes (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    doctrinal_focus TEXT,
    ocean_governance_issue TEXT,
    article_section TEXT,
    url TEXT
);
