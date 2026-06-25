CREATE TABLE IF NOT EXISTS investment_treaty_doctrines (
  doctrine TEXT PRIMARY KEY,
  core_question TEXT,
  typical_claim TEXT,
  regulatory_sovereignty_issue TEXT
);

CREATE TABLE IF NOT EXISTS isds_procedure_matrix (
  stage TEXT PRIMARY KEY,
  legal_function TEXT,
  key_documents TEXT,
  practice_risk TEXT
);

CREATE TABLE IF NOT EXISTS regulatory_sovereignty_risk_matrix (
  policy_area TEXT PRIMARY KEY,
  common_investor_claim TEXT,
  state_defense TEXT,
  governance_question TEXT
);

CREATE TABLE IF NOT EXISTS reform_pathways (
  reform_pathway TEXT PRIMARY KEY,
  main_goal TEXT,
  example_tools TEXT,
  limits TEXT
);
