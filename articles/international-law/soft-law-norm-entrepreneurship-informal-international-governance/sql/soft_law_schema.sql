CREATE TABLE IF NOT EXISTS soft_law_instruments (
    id INTEGER PRIMARY KEY,
    instrument_name TEXT NOT NULL,
    instrument_type TEXT NOT NULL,
    adopting_body TEXT,
    year_adopted INTEGER,
    legal_form TEXT,
    governance_domain TEXT,
    binding_status TEXT DEFAULT 'non-binding',
    legal_effect_pathway TEXT
);

CREATE TABLE IF NOT EXISTS norm_entrepreneurship_stages (
    id INTEGER PRIMARY KEY,
    stage_name TEXT NOT NULL,
    description TEXT,
    key_actors TEXT,
    legal_significance TEXT
);

CREATE TABLE IF NOT EXISTS informal_governance_risks (
    id INTEGER PRIMARY KEY,
    risk_type TEXT NOT NULL,
    description TEXT,
    example_context TEXT,
    lawyer_facing_question TEXT
);
