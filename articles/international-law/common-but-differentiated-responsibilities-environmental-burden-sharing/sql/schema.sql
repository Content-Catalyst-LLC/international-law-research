CREATE TABLE IF NOT EXISTS cbdr_authorities (
  id INTEGER PRIMARY KEY,
  type TEXT NOT NULL,
  title TEXT NOT NULL,
  year INTEGER,
  institution_or_source TEXT,
  url TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS cbdr_doctrine (
  id INTEGER PRIMARY KEY,
  concept TEXT NOT NULL,
  legal_location TEXT,
  core_question TEXT,
  burden_sharing_function TEXT,
  lawyer_facing_use TEXT
);

CREATE TABLE IF NOT EXISTS burden_sharing_mechanisms (
  id INTEGER PRIMARY KEY,
  mechanism TEXT NOT NULL,
  legal_context TEXT,
  what_it_allocates TEXT,
  distribution_issue TEXT,
  implementation_challenge TEXT
);
