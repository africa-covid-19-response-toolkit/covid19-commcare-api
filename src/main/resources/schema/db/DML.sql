-- CONSTANTS
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('TEST_PENDING','1001', 'TEST_RESULT', 'Pending', 'Pending test', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('TEST_NEGATIVE', '1002','TEST_RESULT', 'Negative', 'Pending test', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('TEST_POSITIVE', '1003','TEST_RESULT', 'Positive', 'Pending test', false);


INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('CLINICAL_EVALUATION','1020','IDENTIFIED_BY', 'Clinical evaluation', 'Identified by clinical evaluation', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('CONTACT_TRACING','1021','IDENTIFIED_BY', 'Contact tracing', 'Identified by contact tracing', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('COMMUNITY_SURVEILLANCE','1022','IDENTIFIED_BY', 'Community surveillance', 'Identified by community surveillance', false);


INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('PUI_INFO','1040','QUESTIONNIER_CATEGORY', 'PUI Information', 'Information about Person under investigation', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('SYMPTOMS','1041','QUESTIONNIER_CATEGORY', 'Symptoms', 'Symptoms', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('EXISTING_CONDITION','1042','QUESTIONNIER_CATEGORY', 'Existing condition', 'Existing condition', false);


INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('STABLE','1060','STATUS', 'PUI Status stable.', '', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('CRITICAL','1061','STATUS', 'PUI Status critical.', '', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('DECEASED','1062','STATUS', 'PUI Status deceased.', '', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('RECOVERED','1063','STATUS', 'PUI Status recovered.', '', false);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUES('NA','1064','STATUS', 'Not available', '', false);