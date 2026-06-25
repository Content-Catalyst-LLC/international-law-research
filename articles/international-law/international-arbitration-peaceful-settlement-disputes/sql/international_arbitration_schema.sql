CREATE TABLE IF NOT EXISTS arbitration_forms (
    id INTEGER PRIMARY KEY,
    form TEXT NOT NULL,
    parties TEXT,
    source_of_authority TEXT,
    typical_disputes TEXT,
    distinctive_feature TEXT
);

CREATE TABLE IF NOT EXISTS consent_jurisdiction_sources (
    id INTEGER PRIMARY KEY,
    consent_source TEXT NOT NULL,
    typical_use TEXT,
    jurisdictional_questions TEXT,
    practice_note TEXT
);

CREATE TABLE IF NOT EXISTS procedure_enforcement_stages (
    id INTEGER PRIMARY KEY,
    stage TEXT NOT NULL,
    core_issue TEXT,
    legal_question TEXT,
    output TEXT
);

CREATE TABLE IF NOT EXISTS article_sequence_patch (
    id INTEGER PRIMARY KEY,
    position TEXT NOT NULL,
    slug TEXT NOT NULL,
    title TEXT NOT NULL,
    navigation_note TEXT
);
