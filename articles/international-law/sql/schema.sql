-- International Law research schema

CREATE TABLE IF NOT EXISTS legal_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS article_roadmap (
    article_id INTEGER PRIMARY KEY,
    article_title TEXT NOT NULL,
    article_slug TEXT NOT NULL,
    status TEXT NOT NULL,
    domain TEXT,
    description TEXT,
    url TEXT
);

CREATE TABLE IF NOT EXISTS article_source_links (
    link_id INTEGER PRIMARY KEY,
    article_id INTEGER NOT NULL,
    source_id INTEGER NOT NULL,
    relationship_type TEXT,
    notes TEXT,
    FOREIGN KEY(article_id) REFERENCES article_roadmap(article_id),
    FOREIGN KEY(source_id) REFERENCES legal_sources(source_id)
);
