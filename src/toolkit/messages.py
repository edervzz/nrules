""" core messages """


class Codes:
    """ codes """
    en_messages: dict[str, str] = {}
    es_messages: dict[str, str] = {}

    # Read Rule
    RU_READ_002 = "RU-READ-002"
    en_messages[RU_READ_002] = "Rule not found."
    es_messages[RU_READ_002] = "Regla no encontrada."

    RU_READ_001 = "RU-READ-001"
    en_messages[RU_READ_001] = "Rule ID or Rule Name must be provided."
    es_messages[RU_READ_001] = "Id Regla o Nombre Regla es obligatorio."

    # Update Rule
    RU_UPD_006 = "RU-UPD-006"
    en_messages[RU_UPD_006] = "An error happend during expression validation."
    es_messages[RU_UPD_006] = "Un error sucedió durante la validación de la expresión."

    RU_UPD_005 = "RU-UPD-005"
    en_messages[RU_UPD_005] = "Already exists a Rule with same name."
    es_messages[RU_UPD_005] = "Ya existe una Regla con el mismo nombre."

    RU_UPD_004 = "RU-UPD-004"
    en_messages[RU_UPD_004] = "(Internal check) 'Is Exclusive' is badformed."
    es_messages[RU_UPD_004] = "(Internal check) 'Is Exclusive' esta mal formado."

    RU_UPD_003 = "RU-UPD-003"
    en_messages[RU_UPD_003] = "Expression is mandatory."
    es_messages[RU_UPD_003] = "Expresión es obligatoria."

    RU_UPD_002 = "RU-UPD-002"
    en_messages[RU_UPD_002] = "Rule Name must be between 5 and 50 characters."
    es_messages[RU_UPD_002] = "Nombre de Regla debe ser de 5 a 50 caracteres."

    RU_UPD_001 = "RU-UPD-001"
    en_messages[RU_UPD_001] = "Rule Name is mandatory."
    es_messages[RU_UPD_001] = "Nombre de Regla es obligatorio."

    # Create Rule
    RU_CREA_006 = "RU-CREA-006"
    en_messages[RU_CREA_006] = "An error happend during expression validation."
    es_messages[RU_CREA_006] = "Un error sucedió durante la validación de la expresión."

    RU_CREA_005 = "RU-CREA-005"
    en_messages[RU_CREA_005] = "Already exists a Rule with same name."
    es_messages[RU_CREA_005] = "Ya existe una Regla con el mismo nombre."

    RU_CREA_004 = "RU-CREA-004"
    en_messages[RU_CREA_004] = "(Internal check) 'Is Exclusive' is badformed."
    es_messages[RU_CREA_004] = "(Internal check) 'Is Exclusive' esta mal formado."

    RU_CREA_003 = "RU-CREA-003"
    en_messages[RU_CREA_003] = "Expression is mandatory."
    es_messages[RU_CREA_003] = "Expresión es obligatoria."

    RU_CREA_002 = "RU-CREA-002"
    en_messages[RU_CREA_002] = "Rule Name must be between 5 and 50 characters."
    es_messages[RU_CREA_002] = "Nombre de Regla debe ser de 5 a 50 caracteres."

    RU_CREA_001 = "RU-CREA-001"
    en_messages[RU_CREA_001] = "Rule Name is mandatory."
    es_messages[RU_CREA_001] = "Nombre de Regla es obligatorio."

    # Read Workflow
    WF_READ_002 = "WF-READ-002"
    en_messages[WF_READ_002] = "Workflow not found."
    es_messages[WF_READ_002] = "No se encontró Workflow."

    WF_READ_001 = "WF-READ-001"
    en_messages[WF_READ_001] = "Workflow ID or name is mandatory."
    es_messages[WF_READ_001] = "Nombre o ID de 'Workflow' es obligatorio."

    # Create Workflow
    WF_CREA_009 = "WF-CREA-009"
    en_messages[WF_CREA_009] = "Rule with name {} already exists."
    es_messages[WF_CREA_009] = "'Rule' con nombre {} ya existe.",

    WF_CREA_008 = "WF-CREA-008"
    en_messages[WF_CREA_008] = "All Rule Names must be unique."
    es_messages[WF_CREA_008] = "Todos los nombres de 'Rule' debe ser únicos.",

    WF_CREA_007 = "WF-CREA-007"
    en_messages[WF_CREA_007] = "Rules. Operator must be 'AND', 'OR' or empty value."
    es_messages[WF_CREA_007] = "'Rules'. Operador debe ser 'AND', 'OR' or vacío."

    WF_CREA_006 = "WF-CREA-006"
    en_messages[WF_CREA_006] = "At least one rule must be defined."
    es_messages[WF_CREA_006] = "Al menos una 'Rule' debe ser definida."

    WF_CREA_005 = "WF-CREA-005"
    en_messages[WF_CREA_005] = "Rule Name must be between 5 and 50 characters."
    es_messages[WF_CREA_005] = "Nombre de 'Rule' debe ser de 5 a 50 caracteres."

    WF_CREA_004 = "WF-CREA-004"
    en_messages[WF_CREA_004] = "Rules. Name and Expression are mandatory."
    es_messages[WF_CREA_004] = "'Rules'. Nombre y Expresión son obligatorios."

    WF_CREA_003 = "WF-CREA-003"
    en_messages[WF_CREA_003] = "A Workflow already exists with same name."
    es_messages[WF_CREA_003] = "Un 'Workflow' ya existe con el mismo nombre."

    WF_CREA_002 = "WF-CREA-002"
    en_messages[WF_CREA_002] = "Workflow Name must be between 5 and 50 characters."
    es_messages[WF_CREA_002] = "Nombre de 'Workflow' debe ser de 5 a 50 caracteres."

    WF_CREA_001 = "WF-CREA-001"
    en_messages[WF_CREA_001] = "Workflow Name must not be empty."
    es_messages[WF_CREA_001] = "Nombre de 'Workflow' es requerido."
