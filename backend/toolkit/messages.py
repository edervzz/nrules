""" core messages """


class Codes:
    """ codes """
    en_messages: dict[str, str] = {}
    es_messages: dict[str, str] = {}

    RUNNER_004 = "RUNNER-004"
    en_messages[RUNNER_004] = "KVS {} not found."
    es_messages[RUNNER_004] = "KVS {}, no encontrada."

    RUNNER_003 = "RUNNER-003 "
    en_messages[RUNNER_003] = "Rule {} not found."
    es_messages[RUNNER_003] = "Regla {}, no encontrada."

    RUNNER_002 = "RUNNER-002 "
    en_messages[RUNNER_002] = "Component {}, not found into payload."
    es_messages[RUNNER_002] = "Se requiere el componente '{}', dentro de la solicitud."

    RUNNER_001 = "RUNNER-001"
    en_messages[RUNNER_001] = "Rule name and ID must not be empty."
    es_messages[RUNNER_001] = "Nombre o ID de regla son obligatorios."

    KVI_CREA_010 = "KVI-CREA-010"
    en_messages[KVI_CREA_010] = "Duplicated Keys are not allowed."
    es_messages[KVI_CREA_010] = "Keys duplicadas no están permitidas."

    KVI_CREA_009 = "KVI-CREA-009"
    en_messages[KVI_CREA_009] = "KV Item Calculation value must be 'ADD' or 'MOD'."
    es_messages[KVI_CREA_009] = "El valor de cálculo del KV Item debe ser 'ADD' o  'MOD'."

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

    KV_READ_003 = "KVI-READ-003"
    en_messages[KV_READ_003] = "KV Items not found."
    es_messages[KV_READ_003] = "No se encontrado Items del KV."

    KV_READ_002 = "KVI-READ-002"
    en_messages[KV_READ_002] = "KV ID not found."
    es_messages[KV_READ_002] = "KV ID no encontrado."

    KV_READ_001 = "KVI-READ-001"
    en_messages[KV_READ_001] = "KV ID must not be empty."
    es_messages[KV_READ_001] = "KV ID debe proporcionarse."

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
    RU_READ_006 = "RU-READ-006"
    en_messages[RU_READ_006] = "Rule's Key is mandatory."
    es_messages[RU_READ_006] = "Clave de búsqueda es obligatorio."

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

    # Save Rule's Conditions
    COND_SAVE_010 = "COND-SAVE-010"
    en_messages[COND_SAVE_010] = "Condition '{}' must be consistent between parameter and condition."
    es_messages[COND_SAVE_010] = "Condition '{}' debe ser consistente entre el parámetro y condición."

    COND_SAVE_009 = "COND-SAVE-009"
    en_messages[COND_SAVE_009] = "Parameters not found for this rule."
    es_messages[COND_SAVE_009] = "No se encontraron parámetros para esta Regla."

    COND_SAVE_008 = "COND-SAVE-008"
    en_messages[COND_SAVE_008] = "Rule not found."
    es_messages[COND_SAVE_008] = "Regla no encontrada."

    COND_SAVE_007 = "COND-SAVE-007"
    en_messages[COND_SAVE_007] = "Rule ID or Rule Name must be provided."
    es_messages[COND_SAVE_007] = "Id Regla o Nombre Regla es obligatorio."

    COND_SAVE_006 = "COND-SAVE-006"
    en_messages[COND_SAVE_006] = "For type of DATE, operator must be: ['=', '<>', '>', '<', '>=', '<=', 'BT', 'NB']"
    es_messages[COND_SAVE_006] = "Para tipos DATE, operador debe ser: ['=', '<>', '>', '<', '>=', '<=', 'BT', 'NB']"

    COND_SAVE_005 = "COND-SAVE-005"
    en_messages[COND_SAVE_005] = "For type of NUMERIC, operator must be: ['=', '<>', '>', '<', '>=', '<=', 'IN', 'NI', 'BT', 'NB']"
    es_messages[COND_SAVE_005] = "Para tipos NUMERIC, operador debe ser: ['=', '<>', '>', '<', '>=', '<=', 'IN', 'NI', 'BT', 'NB']"

    COND_SAVE_004 = "COND-SAVE-004"
    en_messages[COND_SAVE_004] = "For type of STRING, operator must be: ['=', '<>', 'IN', 'NI']"
    es_messages[COND_SAVE_004] = "Para tipos STRING, operador debe ser: ['=', '<>', 'IN', 'NI']"

    COND_SAVE_003 = "COND-SAVE-003"
    en_messages[COND_SAVE_003] = "Operator must be: ['=', '<>', '>', '<', '>=', '<=', 'IN', 'NI', 'BT', 'NB']"
    es_messages[COND_SAVE_003] = "Operador debe ser: ['=', '<>', '>', '<', '>=', '<=', 'IN', 'NI', 'BT', 'NB']"

    COND_SAVE_002 = "COND-SAVE-002"
    en_messages[COND_SAVE_002] = "The type of Condition must be: ['STRING', 'NUMERIC', 'DATE']"
    es_messages[COND_SAVE_002] = "El tipo de la condición debe ser: ['STRING', 'NUMERIC', 'DATE']"

    COND_SAVE_001 = "COND-SAVE-001"
    en_messages[COND_SAVE_001] = "All variables are mandatory"
    es_messages[COND_SAVE_001] = "Todas las variables son obligatorias."

    # Update Parameter
    PARAM_UPD_006 = "PARAM-UPD-006"
    en_messages[PARAM_UPD_006] = "Parameter '{}' cannot determine its use for."
    es_messages[PARAM_UPD_006] = "Parámetro '{}' no puede determinarse su uso.."

    PARAM_UPD_005 = "PARAM-UPD-005"
    en_messages[PARAM_UPD_005] = "Parameter '{}' not found."
    es_messages[PARAM_UPD_005] = "Parámetro '{}' no encontrado."

    PARAM_UPD_004 = "PARAM-UPD-004"
    en_messages[PARAM_UPD_004] = "Parameters must not be in different lists."
    es_messages[PARAM_UPD_004] = "Ningún parámetro puede estar en diferentes listas."

    PARAM_UPD_003 = "PARAM-UPD-003"
    en_messages[PARAM_UPD_003] = "All Parameters must not be duplicated."
    es_messages[PARAM_UPD_003] = "Ningún parámetero puede estar duplicado."

    PARAM_UPD_002 = "PARAM-UPD-002"
    en_messages[PARAM_UPD_002] = "Rule ID or Rule Name must be provided."
    es_messages[PARAM_UPD_002] = "Id Regla o Nombre Regla es obligatorio."

    PARAM_UPD_001 = "PARAM-UPD-001"
    en_messages[PARAM_UPD_001] = "Exists more than one parameter with same key '{}'."
    es_messages[PARAM_UPD_001] = "Existe mas de una parámetro con la misma key '{}'."

    # Update Rule
    RU_UPD_011 = "RU-UPD-011"
    en_messages[RU_UPD_011] = "Strategy must be EARLY / BASE / ALL."
    es_messages[RU_UPD_011] = "La estrategia debe ser EARLY / BASE / ALL."

    RU_UPD_010 = "RU-UPD-010"
    en_messages[RU_UPD_010] = "Rule Type must be 'MATRIX'."
    es_messages[RU_UPD_010] = "Tipo Regla deber ser 'MATRIX'."

    RU_UPD_009 = "RU-UPD-009"
    en_messages[RU_UPD_009] = "Rule Type is mandatory."
    es_messages[RU_UPD_009] = "Tipo de Regla es obligatorio."

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

    # Condition
    COND_001 = "COND-001"
    en_messages[COND_001] = "Condition's Value cannot be converted to '{}'."
    es_messages[COND_001] = "El Valor de la Condición no puede ser convertido a '{}'"

    # Parameter
    PARAM_004 = "PARAM-004"
    en_messages[PARAM_004] = "Output Parameter '{}' typeof must be: [JSON, STRING, NUMERIC, DATE]."
    es_messages[PARAM_004] = "Parámetro de Salida '{}' typeof debe ser: [JSON, STRING, NUMERIC, DATE]."

    PARAM_003 = "PARAM-003"
    en_messages[PARAM_003] = "Condition Parameter '{}' typeof must be: [STRING, NUMERIC, DATE]."
    es_messages[PARAM_003] = "Parámetro de Condición '{}' typeof debe ser: [STRING, NUMERIC, DATE]."

    PARAM_002 = "PARAM-002"
    en_messages[PARAM_002] = "Parameter '{}' use for must be: [CONDITION, OUTPUT]."
    es_messages[PARAM_002] = "Uso de parámetro '{}' debe ser: [CONDITION, OUTPUT]."

    PARAM_001 = "PARAM-001"
    en_messages[PARAM_001] = "Parameter's fields are mandatory."
    es_messages[PARAM_001] = "Complete todos los campos de los parámetros."

    # Rule
    RULE_005 = "RULE-005"
    en_messages[RULE_005] = "Rule Name must be between 5 and 50 characters."
    es_messages[RULE_005] = "Nombre de Regla debe ser de 5 a 50 caracteres."

    RULE_004 = "RULE-004"
    en_messages[RULE_004] = "Strategy must be EARLY / BASIC / ALL."
    es_messages[RULE_004] = "La estrategia debe ser EARLY / BASIC / ALL."

    RULE_003 = "RULE-003"
    en_messages[RULE_003] = "Rule Type must be 'MATRIX'."
    es_messages[RULE_003] = "Tipo Regla deber ser 'MATRIX'."

    RULE_002 = "RULE-002"
    en_messages[RULE_002] = "Rule Type must be provided."
    es_messages[RULE_002] = "Tipo de Regla es obligatorio."

    RULE_001 = "RULE-001"
    en_messages[RULE_001] = "Rule Name is mandatory."
    es_messages[RULE_001] = "Nombre de Regla es obligatorio."

    # Create Rule
    RU_CREA_013 = "RU-CREA-013"
    en_messages[RU_CREA_013] = "All paramter's name must be unique."
    es_messages[RU_CREA_013] = "Todos los nombres de los parámetros deben ser únicos."

    RU_CREA_010 = "RU-CREA-010"
    en_messages[RU_CREA_010] = "Rule, KVS {} not found."
    es_messages[RU_CREA_010] = "Regla, KVS {} no encontrado."

    RU_CREA_009 = "RU-CREA-009"
    en_messages[RU_CREA_009] = "Condition {}, KVS {} not found."
    es_messages[RU_CREA_009] = "Condición {}, KVS {} no encontrado."

    RU_CREA_007 = "RU-CREA-007"
    en_messages[RU_CREA_007] = "At least one conditions is required."
    es_messages[RU_CREA_007] = "Al menos se requiere una condición."

    RU_CREA_006 = "RU-CREA-006"
    en_messages[RU_CREA_006] = "ExpVal: {}."
    es_messages[RU_CREA_006] = "ExpVal: {}."

    RU_CREA_005 = "RU-CREA-005"
    en_messages[RU_CREA_005] = "Already exists a Rule with same name."
    es_messages[RU_CREA_005] = "Ya existe una Regla con el mismo nombre."

    RU_CREA_003 = "RU-CREA-003"
    en_messages[RU_CREA_003] = "Expression is mandatory."
    es_messages[RU_CREA_003] = "Expresión es obligatoria."

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
