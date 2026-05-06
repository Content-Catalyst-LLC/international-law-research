-- Public vs Private International Law companion schema

CREATE TABLE IF NOT EXISTS public_private_sources (
    source_id INTEGER PRIMARY KEY,
    source_title TEXT NOT NULL,
    source_type TEXT NOT NULL,
    institution TEXT,
    year INTEGER,
    url TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS public_private_concepts (
    concept_id INTEGER PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_category TEXT,
    description TEXT,
    article_section TEXT
);

CREATE TABLE IF NOT EXISTS public_private_quote_log (
    quote_id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    legal_excerpt TEXT NOT NULL,
    source_location TEXT,
    article_section TEXT,
    editorial_purpose TEXT,
    FOREIGN KEY(source_id) REFERENCES public_private_sources(source_id)
);

CREATE TABLE IF NOT EXISTS comparison_points (
    point_id INTEGER PRIMARY KEY,
    comparison_dimension TEXT NOT NULL,
    public_international_law TEXT,
    private_international_law TEXT,
    overlap_or_tension TEXT,
    article_section TEXT
);
