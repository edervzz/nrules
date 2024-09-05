""" core messages """


class Codes:
    """ codes """
    en_messages: dict[str, str] = {}
    es_messages: dict[str, str] = {}

    ACTION_CREA_006 = "ACTION-CREA-006"
    en_messages[ACTION_CREA_006] = "KVS no encontrado."
    es_messages[ACTION_CREA_006] = "KVS ID not found."

    ACTION_CREA_005 = "ACTION-CREA-005"
    en_messages[ACTION_CREA_005] = "Ruleset no encontrado."
    es_messages[ACTION_CREA_005] = "Ruleset ID not found."

    ACTION_CREA_004 = "ACTION-CREA-004"
    en_messages[ACTION_CREA_004] = "Nombre de Actión no debe repetirse."
    es_messages[ACTION_CREA_004] = "Action's Name already exists."

    ACTION_CREA_003 = "ACTION-CREA-003"
    en_messages[ACTION_CREA_003] = "Actión no existe."
    es_messages[ACTION_CREA_003] = "Action do not exists."

    ACTION_CREA_002 = "ACTION-CREA-002"
    en_messages[ACTION_CREA_002] = "Just Ruleset or KVS must be declared."
    es_messages[ACTION_CREA_002] = "Un Ruleset o un KVS debe ser indicado."

    ACTION_CREA_001 = "ACTION-CREA-001"
    en_messages[ACTION_CREA_001] = "Action Name must be between 5 and 50 characters."
    es_messages[ACTION_CREA_001] = "Nombre de Action debe ser de 5 a 50 caracteres."

    KVI_CREA_008 = "KVI-CREA-008"
    en_messages[KVI_CREA_008] = "List must not be empty."
    es_messages[KVI_CREA_008] = "La lista no debe estar vacía."

    KVI_CREA_007 = "KVI-CREA-007"
    en_messages[KVI_CREA_007] = "KV Parent ID not found."
    es_messages[KVI_CREA_007] = "KV padre no fue encontrado."

    KVI_CREA_006 = "KVI-CREA-006"
    en_messages[KVI_CREA_006] = "Type Of must not be greater than 50 characteres."
    es_messages[KVI_CREA_006] = "Tipo debe tener un máximo de 50 caracteres."

    KVI_CREA_005 = "KVI-CREA-005"
    en_messages[KVI_CREA_005] = "Value must not be greater than 500 characteres."
    es_messages[KVI_CREA_005] = "Valor debe tener un máximo de 500 caracteres."

    KVI_CREA_004 = "KVI-CREA-004"
    en_messages[KVI_CREA_004] = "Value must not be empty."
    es_messages[KVI_CREA_004] = "Valor es obligatorio."

    KVI_CREA_003 = "KVI-CREA-003"
    en_messages[KVI_CREA_003] = "KV Parent ID must not be empty."
    es_messages[KVI_CREA_003] = "ID padre es obligatorio."

    KVI_CREA_002 = "KVI-CREA-002"
    en_messages[KVI_CREA_002] = "KV Item Name must be between 5 and 50 characters."
    es_messages[KVI_CREA_002] = "Nombre de KV Item debe ser de 5 a 50 caracteres."

    KVI_CREA_001 = "KVI-CREA-001"
    en_messages[KVI_CREA_001] = "Nombre de KV Item es obligatorio."
    es_messages[KVI_CREA_001] = "KV Item Name must not be empty."

    KV_CREA_003 = "KV-CREA-003"
    en_messages[KV_CREA_003] = "KVS already exists."
    es_messages[KV_CREA_003] = "KVS ya existe."

    KV_CREA_002 = "KV-CREA-002"
    en_messages[KV_CREA_002] = "KVS Name must be between 5 and 50 characters."
    es_messages[KV_CREA_002] = "Nombre de KVS debe ser de 5 a 50 caracteres."

    KV_CREA_001 = "KV-CREA-001"
    en_messages[KV_CREA_001] = "KVS Name is mandatory."
    es_messages[KV_CREA_001] = "Nombre de KVS es obligatorio."

    # Create Container
    CO_CREA_004 = "CO-CREA-004"
    en_messages[CO_CREA_004] = "(Internal check) 'Is Full' is badformed."
    es_messages[CO_CREA_004] = "(Internal check) 'Is Full' está mal formado."

    CO_CREA_003 = "CO-CREA-003"
    en_messages[CO_CREA_003] = "(Internal check) 'Is Node' is badformed."
    es_messages[CO_CREA_003] = "(Internal check) 'Is Node' está mal formado."

    CO_CREA_002 = "CO-CREA-002"
    en_messages[CO_CREA_002] = "Container Name must be between 5 and 50 characters."
    es_messages[CO_CREA_002] = "Container de Regla debe ser de 5 a 50 caracteres."

    CO_CREA_001 = "CO-CREA-001"
    en_messages[CO_CREA_001] = "Container Name is mandatory."
    es_messages[CO_CREA_001] = "Nombre de Contenedor es obligatorio."

    # Create Tenant
    TE_CREA_004 = "TE-CREA-004"
    en_messages[TE_CREA_004] = "Tenant Name already exists."
    es_messages[TE_CREA_004] = "Nombre de Tenant ya existe."

    TE_CREA_003 = "TE-CREA-003"
    en_messages[TE_CREA_003] = "Tenant ID already exists."
    es_messages[TE_CREA_003] = "ID de Tenant ya existe."

    TE_CREA_002 = "TE-CREA-002"
    en_messages[TE_CREA_002] = "Tenant Name must be between 5 and 50 characteres."
    es_messages[TE_CREA_002] = "Nombre de Tenant debe ser entre 5 y 50 caracteres."

    TE_CREA_001 = "TE-CREA-001"
    en_messages[TE_CREA_001] = "Tenant ID must be between 1 and 99."
    es_messages[TE_CREA_001] = "Id Tenant debe ser entre 1 y 99."

    # Read Rule
    RU_READ_005 = "RU-READ-005"
    en_messages[RU_READ_005] = "Rules not found."
    es_messages[RU_READ_005] = "No se encontraron Reglas."

    RU_READ_004 = "RU-READ-004"
    en_messages[RU_READ_004] = "Page Size must not be negative."
    es_messages[RU_READ_004] = "Tamaño de Pagina no debe ser negativo."

    RU_READ_003 = "RU-READ-003"
    en_messages[RU_READ_003] = "Page Number must not be negative."
    es_messages[RU_READ_003] = "Número de Pagina no debe ser negativo."

    RU_READ_002 = "RU-READ-002"
    en_messages[RU_READ_002] = "Rule not found."
    es_messages[RU_READ_002] = "Regla no encontrada."

    RU_READ_001 = "RU-READ-001"
    en_messages[RU_READ_001] = "Rule ID or Rule Name must be provided."
    es_messages[RU_READ_001] = "Id Regla o Nombre Regla es obligatorio."

    # Update Rule
    RU_UPD_008 = "RU-UPD-008"
    en_messages[RU_UPD_008] = "Rule ID or Rule Name must be provided."
    es_messages[RU_UPD_008] = "Id Regla o Nombre Regla es obligatorio."

    RU_UPD_007 = "RU-UPD-007"
    en_messages[RU_UPD_007] = "Rule not found."
    es_messages[RU_UPD_007] = "No se encontró Regla."

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
    en_messages[WF_CREA_004] = "Type Of must be 'BASE' or 'FULL' or 'NODE'."
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

    OBJ_UPD_001 = "OBJ_UPD_001"
    en_messages[OBJ_UPD_001] = "No modificactions."
    es_messages[OBJ_UPD_001] = "Sin modificaciones."
