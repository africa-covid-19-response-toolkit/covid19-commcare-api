-- CONSTANTS
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUE("TEST_PENDING","001", "TEST_RESULT", "Pending", "Pending test", 0);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUE("TEST_NEGATIVE", "002","TEST_RESULT", "Negative", "Pending test", 0);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUE("TEST_POSITIVE", "003","TEST_RESULT", "Positive", "Pending test", 0);


INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUE("CLINICAL_EVALUATION","020","IDENTIFIED_BY", "Clinical evaluation", "Identified by clinical evaluation", 0);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUE("CONTACT_TRACING","021","IDENTIFIED_BY", "Contact tracing", "Identified by contact tracing", 0);
INSERT INTO CONSTANT_ENUM(ENUM_NAME, ENUM_CODE, ENUM_TYPE, ENUM_LABEL, ENUM_DESC, DISABLED) VALUE("COMMUNITY_SURVEILLANCE","022","IDENTIFIED_BY", "Community surveillance", "Identified by community surveillance", 0);
