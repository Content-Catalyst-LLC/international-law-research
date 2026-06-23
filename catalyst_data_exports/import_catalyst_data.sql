-- Catalyst Data import for International Law research exports
-- Usage from the catalyst-data SQLite shell after .read schema.sql:
--   .mode csv
--   .import --skip 1 catalyst_data_exports/sources.csv staging_sources
-- Or use the generated import_catalyst_data.py loader for a safer import.

PRAGMA foreign_keys = ON;

-- This file documents the table mapping. Use python/import_catalyst_data.py
-- for actual CSV ingestion because it handles stable IDs and duplicate URLs.

-- catalyst_data_exports/sources.csv -> sources(name, url, license, retrieved_at, note)
-- catalyst_data_exports/legal_instruments.csv -> legal_instruments(instrument_type, title, short_citation, adopted_on, url, source_id)
-- catalyst_data_exports/tags.csv -> tags(kind, name)
-- catalyst_data_exports/instrument_topics.csv -> instrument_topics(instrument_id, tag_id)
