PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS regimes (
    regime_key TEXT PRIMARY KEY,
    regime_name TEXT NOT NULL,
    parent_regime TEXT,
    description TEXT,
    priority INTEGER DEFAULT 3,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS treaties (
    treaty_key TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    regime_key TEXT NOT NULL,
    source_type TEXT NOT NULL,
    official_url TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_key) REFERENCES regimes(regime_key)
);

CREATE TABLE IF NOT EXISTS institutions (
    institution_key TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    regime_key TEXT NOT NULL,
    official_url TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_key) REFERENCES regimes(regime_key)
);

CREATE TABLE IF NOT EXISTS cases (
    case_key TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER,
    court_or_body TEXT NOT NULL,
    regime_key TEXT NOT NULL,
    source_type TEXT NOT NULL,
    official_url TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_key) REFERENCES regimes(regime_key)
);

CREATE TABLE IF NOT EXISTS planned_articles (
    slug TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('planned', 'drafting', 'published', 'archived')),
    regime_key TEXT NOT NULL,
    priority INTEGER DEFAULT 3,
    article_type TEXT,
    source_focus TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_key) REFERENCES regimes(regime_key)
);

CREATE TABLE IF NOT EXISTS source_hierarchy (
    source_tier INTEGER NOT NULL,
    source_type TEXT PRIMARY KEY,
    description TEXT NOT NULL,
    preferred_use TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS citation_records (
    citation_key TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author_or_institution TEXT NOT NULL,
    year TEXT,
    source_type TEXT NOT NULL,
    regime_key TEXT,
    official_url TEXT,
    citation_note TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (regime_key) REFERENCES regimes(regime_key),
    FOREIGN KEY (source_type) REFERENCES source_hierarchy(source_type)
);

CREATE INDEX IF NOT EXISTS idx_treaties_regime ON treaties(regime_key);
CREATE INDEX IF NOT EXISTS idx_institutions_regime ON institutions(regime_key);
CREATE INDEX IF NOT EXISTS idx_cases_regime ON cases(regime_key);
CREATE INDEX IF NOT EXISTS idx_cases_year ON cases(year);
CREATE INDEX IF NOT EXISTS idx_planned_articles_regime ON planned_articles(regime_key);
CREATE INDEX IF NOT EXISTS idx_planned_articles_status ON planned_articles(status);
CREATE INDEX IF NOT EXISTS idx_citation_records_regime ON citation_records(regime_key);
CREATE INDEX IF NOT EXISTS idx_citation_records_source_type ON citation_records(source_type);
