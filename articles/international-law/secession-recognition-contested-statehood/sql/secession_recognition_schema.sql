CREATE TABLE IF NOT EXISTS secession_recognition_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS secession_recognition_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept TEXT NOT NULL,
    category TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS contested_statehood_examples (
    example_id INTEGER PRIMARY KEY,
    entity TEXT NOT NULL,
    issue TEXT,
    type TEXT,
    legal_frame TEXT
);
