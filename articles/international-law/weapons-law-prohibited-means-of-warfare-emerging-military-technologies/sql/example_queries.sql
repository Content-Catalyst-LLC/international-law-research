-- Example query: identify legal questions across weapons categories
SELECT category, legal_question, lawyer_task
FROM weapons_law_matrix
ORDER BY category;

-- Example query: map Article 36 stages to evidence needs
SELECT stage, review_question, evidence
FROM article_36_review_matrix;

-- Example query: emerging-technology review focus
SELECT technology, core_issue, review_focus
FROM emerging_military_technologies_matrix
ORDER BY technology;
