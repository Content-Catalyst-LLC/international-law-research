CREATE TABLE IF NOT EXISTS future_domains (
    id INTEGER PRIMARY KEY,
    domain TEXT NOT NULL,
    core_pressure TEXT,
    legal_questions TEXT,
    likely_governance_forms TEXT
);

CREATE TABLE IF NOT EXISTS future_scenarios (
    id INTEGER PRIMARY KEY,
    scenario TEXT NOT NULL,
    description TEXT,
    legal_markers TEXT,
    risk TEXT
);

CREATE TABLE IF NOT EXISTS planetary_crisis_issues (
    id INTEGER PRIMARY KEY,
    issue TEXT NOT NULL,
    legal_question TEXT,
    affected_interests TEXT,
    potential_legal_pathways TEXT
);

CREATE TABLE IF NOT EXISTS lawyer_workflow_steps (
    id INTEGER PRIMARY KEY,
    step_number INTEGER,
    task TEXT NOT NULL,
    key_question TEXT,
    output TEXT
);
