PRAGMA foreign_keys = ON;

.mode csv
.import --skip 1 data/regimes.csv regimes
.import --skip 1 data/treaties.csv treaties
.import --skip 1 data/institutions.csv institutions
.import --skip 1 data/cases.csv cases
.import --skip 1 data/planned-articles.csv planned_articles

INSERT OR REPLACE INTO source_hierarchy (source_tier, source_type, description, preferred_use) VALUES
(1, 'primary_treaty', 'Treaty, convention, protocol, covenant, or charter text from an authoritative source.', 'Use for binding treaty frameworks and treaty interpretation.'),
(1, 'court_statute', 'Statute or founding instrument of an international court or tribunal.', 'Use for jurisdiction, institutional authority, and procedural foundations.'),
(1, 'judgment', 'Judgment from an international court or tribunal.', 'Use for judicial interpretation, dispute settlement, and doctrinal development.'),
(1, 'advisory_opinion', 'Advisory opinion from an international court or tribunal.', 'Use for authoritative legal reasoning outside contentious disputes.'),
(1, 'provisional_measures', 'Provisional measures order or equivalent procedural decision.', 'Use for urgent protection, jurisdictional thresholds, and interim obligations.'),
(1, 'declaration', 'Formal international declaration or resolution with major normative significance.', 'Use for foundational statements, soft law, and normative development.'),
(2, 'institutional_guidance', 'Official institutional commentary, database, report, or guidance.', 'Use for authoritative institutional interpretation and practice.'),
(2, 'un_document', 'UN report, resolution, repertory entry, or institutional record.', 'Use for UN practice, interpretation, and institutional development.'),
(3, 'scholarly_book', 'Academic monograph, treatise, or edited volume.', 'Use for interpretation, historical context, and scholarly debate.'),
(3, 'scholarly_article', 'Peer-reviewed article or specialist legal scholarship.', 'Use for argument, analysis, and doctrinal criticism.'),
(4, 'critical_scholarship', 'Postcolonial, feminist, TWAIL, Indigenous, historical, or political economy critique.', 'Use for power analysis, historical injustice, and structural critique.');
