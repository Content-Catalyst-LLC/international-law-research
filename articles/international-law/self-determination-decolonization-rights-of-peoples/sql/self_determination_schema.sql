CREATE TABLE IF NOT EXISTS self_determination_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS self_determination_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept TEXT NOT NULL,
    category TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS self_determination_cases (
    case_id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    people_or_territory TEXT,
    doctrinal_focus TEXT,
    url TEXT
);
