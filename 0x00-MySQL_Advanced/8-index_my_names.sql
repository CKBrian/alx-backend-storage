
-- creates an index idx_name_first on the table names and the first letter of name.
-- ALTER TABLE names ADD first_letter VARCHAR(1);
-- UPDATE names SET first_letter = LEFT(name, 1);
CREATE INDEX idx_name_first ON names(name, score);