-- Support schema for International Trade Law and the Legal Order of Global Commerce.
-- This schema is intentionally lightweight and article-specific.

CREATE TABLE IF NOT EXISTS trade_law_architecture (
    area TEXT PRIMARY KEY,
    core_question TEXT NOT NULL,
    legal_tools TEXT NOT NULL,
    governance_tension TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS wto_agreement_matrix (
    agreement TEXT PRIMARY KEY,
    short_name TEXT NOT NULL,
    main_function TEXT NOT NULL,
    article_use TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dispute_settlement_matrix (
    stage TEXT PRIMARY KEY,
    legal_function TEXT NOT NULL,
    practical_issue TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS regulatory_autonomy_matrix (
    policy_area TEXT PRIMARY KEY,
    trade_law_pressure TEXT NOT NULL,
    autonomy_question TEXT NOT NULL
);
