""" core messages """


class Codes:
    """ codes """
    en_messages: dict[str, str] = {}
    es_messages: dict[str, str] = {}

    # Runner
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

    # Update KV Items
    KVI_UPD_003 = "KVI-UPD-003"
    en_messages[KVI_UPD_003] = "All parameters must exists."
    es_messages[KVI_UPD_003] = "Todos los parámetros deben existir."

    KVI_UPD_002 = "KVI-UPD-002"
    en_messages[KVI_UPD_002] = "Nothing to update."
    es_messages[KVI_UPD_002] = "Nada que actualizar."

    KVI_UPD_001 = "KVI-UPD-001"
    en_messages[KVI_UPD_001] = "Rule's ID or Name are mandatory."
    es_messages[KVI_UPD_001] = "Id o nombre de Regla es obligatorio."

    # Create KV Items
    KVI_CREA_006 = "KVI-CREA-006"
    en_messages[KVI_CREA_006] = "Any new parameter must not exists."
    es_messages[KVI_CREA_006] = "Ningún nuevo parametro debe existir."

    KVI_CREA_005 = "KVI-CREA-005"
    en_messages[KVI_CREA_005] = "Rule not found."
    es_messages[KVI_CREA_005] = "Regla no encontrada."

    KVI_CREA_004 = "KVI-CREA-004"
    en_messages[KVI_CREA_004] = "Total of Parameters must be equal to total of KV Items."
    es_messages[KVI_CREA_004] = "El total de Parámetros debe ser igual al total de KV Items."

    KVI_CREA_003 = "KVI-CREA-003"
    en_messages[KVI_CREA_003] = "All Parameters must be unique."
    es_messages[KVI_CREA_003] = "Todos los Parametros deben ser únicos."

    KVI_CREA_002 = "KVI-CREA-002"
    en_messages[KVI_CREA_002] = "Nothing to update."
    es_messages[KVI_CREA_002] = "Nada que actualizar."

    KVI_CREA_001 = "KVI-CREA-001"
    en_messages[KVI_CREA_001] = "Rule's ID or Name are mandatory."
    es_messages[KVI_CREA_001] = "Id o nombre de Regla es obligatorio."

    # Read KV Item
    KV_READ_003 = "KVI-READ-003"
    en_messages[KV_READ_003] = "KV Items not found."
    es_messages[KV_READ_003] = "No se encontrado Items del KV."

    KV_READ_002 = "KVI-READ-002"
    en_messages[KV_READ_002] = "KV ID not found."
    es_messages[KV_READ_002] = "KV ID no encontrado."

    KV_READ_001 = "KVI-READ-001"
    en_messages[KV_READ_001] = "KV ID must not be empty."
    es_messages[KV_READ_001] = "KV ID debe proporcionarse."

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

    # Create Rule's Parameters
    COND_CREA_015 = "COND-CREA-015"
    en_messages[COND_CREA_015] = "Total of Parameters must be equal to total of Conditions."
    es_messages[COND_CREA_015] = "El total de Parámetros debe ser igual al total de Condiciones."

    COND_CREA_014 = "COND-CREA-014"
    en_messages[COND_CREA_014] = "Nothing to update."
    es_messages[COND_CREA_014] = "Nada que actualizar."

    COND_CREA_013 = "COND-CREA-013"
    en_messages[COND_CREA_013] = "All parameters to update must be exists."
    es_messages[COND_CREA_013] = "Todos los parametros para actualización, debe existir."

    COND_CREA_012 = "COND-SAVE-012"
    en_messages[COND_CREA_012] = "Any new parameter must not be exists."
    es_messages[COND_CREA_012] = "Ningún nuevo parametro debe existir."

    COND_CREA_011 = "COND-CREA-011"
    en_messages[COND_CREA_011] = "At least one Parameter must have been created during Rule creation."
    es_messages[COND_CREA_011] = "Al menos un Parámetro debío crearse durante la creación de la Regla."

    COND_CREA_010 = "COND-CREA-010"
    en_messages[COND_CREA_010] = "Condition '{}' must be consistent between parameter and condition."
    es_messages[COND_CREA_010] = "Condition '{}' debe ser consistente entre el parámetro y condición."

    COND_CREA_009 = "COND-CREA-009"
    en_messages[COND_CREA_009] = "Parameters not found for this rule."
    es_messages[COND_CREA_009] = "No se encontraron parámetros para esta Regla."

    COND_CREA_008 = "COND-CREA-008"
    en_messages[COND_CREA_008] = "Rule not found."
    es_messages[COND_CREA_008] = "Regla no encontrada."

    COND_CREA_007 = "COND-CREA-007"
    en_messages[COND_CREA_007] = "Rule's ID or Name are mandatory."
    es_messages[COND_CREA_007] = "Id o nombre de Regla es obligatorio."

    COND_CREA_006 = "COND-CREA-006"
    en_messages[COND_CREA_006] = "At least one Case must have been created during Rule creation."
    es_messages[COND_CREA_006] = "Al menos un Caso debío crearse durante la creación de la Regla."

    COND_CREA_005 = "COND-CREA-005"
    en_messages[COND_CREA_005] = "All Parameters must be unique."
    es_messages[COND_CREA_005] = "Todos los Parametros deben ser únicos."

    COND_CREA_004 = "COND-CREA-004"
    en_messages[COND_CREA_004] = "Type JSON is not available for Conditions."
    es_messages[COND_CREA_004] = "El tipo 'JSON' no esta disponible para Conditiones."

    COND_CREA_003 = "COND-CREA-003"
    en_messages[COND_CREA_003] = "Use for field must be 'CONDITION' or 'OUTPUT'"
    es_messages[COND_CREA_003] = "Campo 'Uso' debe ser 'CONDITION' or 'OUTPUT'"

    COND_CREA_002 = "COND-CREA-002"
    en_messages[COND_CREA_002] = "Type of Condition must be 'STRING' or 'NUMERIC' or 'DATE' or 'JSON'"
    es_messages[COND_CREA_002] = "El tipo del Condición debe ser 'STRING' o 'NUMERIC' o 'DATE' o 'JSON'"

    COND_CREA_001 = "COND-CREA-001"
    en_messages[COND_CREA_001] = "'Variable' field are mandatory"
    es_messages[COND_CREA_001] = "Campo 'variable' es obligatorio."

    # Update Condition
    COND_UPD_005 = "COND-UPD-005"
    en_messages[COND_UPD_005] = "All parameters to update must be exists."
    es_messages[COND_UPD_005] = "Todos los parametros para actualización, debe existir."

    COND_UPD_004 = "COND-UPD-004"
    en_messages[COND_UPD_004] = "Total of Parameters must be equal to total of Conditions."
    es_messages[COND_UPD_004] = "El total de Parámetros debe ser igual al total de Condiciones."

    COND_UPD_003 = "COND-UPD-003"
    en_messages[COND_UPD_003] = "All Parameters must be unique."
    es_messages[COND_UPD_003] = "Todos los Parametros deben ser únicos."

    COND_UPD_002 = "COND-UPD-002"
    en_messages[COND_UPD_002] = "Nothing to update."
    es_messages[COND_UPD_002] = "Nada que actualizar."

    COND_UPD_001 = "COND-UPD-001"
    en_messages[COND_UPD_001] = "Rule's ID or Name are mandatory."
    es_messages[COND_UPD_001] = "Id o nombre de Regla es obligatorio."

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

    # KV Item
    KVI_005 = "KVI-005"
    en_messages[KVI_005] = "Type Of must not be greater than 50 characteres."
    es_messages[KVI_005] = "Tipo debe tener un máximo de 50 caracteres."

    KVI_004 = "KVI-004"
    en_messages[KVI_004] = "Value must be between 1 and 500 characteres."
    es_messages[KVI_004] = "Valor debe tener una longitud entre 1 y 500 caracteres."

    KVI_003 = "KVI-003"
    en_messages[KVI_003] = "KV Item Name must be between 5 and 50 characters."
    es_messages[KVI_003] = "Nombre de KV Item debe ser de 5 a 50 caracteres."

    KVI_002 = "KVI-002"
    en_messages[KVI_002] = "Nombre de KV Item es obligatorio."
    es_messages[KVI_002] = "KV Item Name must not be empty."

    KVI_001 = "KVI-001"
    en_messages[KVI_001] = "KV Item's Value '{}' cannot be converted to '{}'."
    es_messages[KVI_001] = "El Valor del KV Item '{}' no puede ser convertido a '{}'"

    # Condition
    COND_004 = "COND-004"
    en_messages[COND_004] = "Condition's Value '{}' cannot be converted to '{}'."
    es_messages[COND_004] = "El Valor de la Condición '{}' no puede ser convertido a '{}'"

    COND_003 = "COND-003"
    en_messages[COND_003] = "Type of Condition must be 'STRING' or 'NUMERIC' or 'DATE'"
    es_messages[COND_003] = "El tipo del Condición debe ser 'STRING' o 'NUMERIC' o 'DATE'"

    COND_002 = "COND-002"
    en_messages[COND_002] = "Parameter's Operator is mandatory."
    es_messages[COND_002] = "El Operador del parámetro es obligatorio."

    COND_001 = "COND-001"
    en_messages[COND_001] = "Variable name is mandatory."
    es_messages[COND_001] = "Nombre de Variable es obligatorio."

    # Parameter
    PARAM_005 = "PARAM-005"
    en_messages[PARAM_005] = "Parameter length must be between 5 and 50 characteres."
    es_messages[PARAM_005] = "La longitud de los Parámetros debe ser entre 5 y 50 caracteres."

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

    # Update Object
    OBJ_UPD_001 = "OBJ_UPD_001"
    en_messages[OBJ_UPD_001] = "No modificactions."
    es_messages[OBJ_UPD_001] = "Sin modificaciones."

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
