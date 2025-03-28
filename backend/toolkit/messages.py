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

    RU_CREA_006 = "RU-CREA-006"  # todo
    en_messages[RU_CREA_006] = "ExpVal: {}."
    es_messages[RU_CREA_006] = "ExpVal: {}."\

    # Inventory ################################################################
    INV_CREA_001 = "INV-CREA-001"
    en_messages[INV_CREA_001] = "Rule is not modified."
    es_messages[INV_CREA_001] = "La Regla no tiene modificaciones."

    # Node ################################################################
    NODE_CREA_004 = "NODE-CREA-004"
    en_messages[NODE_CREA_004] = "Nodes only works for rule type 'TREE'."
    es_messages[NODE_CREA_004] = "Los nodos solo aplican a reglas tipo 'TREE'."

    NODE_CREA_003 = "NODE-CREA-003"
    en_messages[NODE_CREA_003] = "Parent Node must be exists."
    es_messages[NODE_CREA_003] = "Nodo padre no encontrado."

    NODE_CREA_002 = "NODE-CREA-002"
    en_messages[NODE_CREA_002] = "Node Assigment must be 'LEFT' or 'RIGHT'."
    es_messages[NODE_CREA_002] = "Asignación de Nodo debe ser 'LEFT' o 'RIGHT'."

    NODE_CREA_001 = "NODE-CREA-001"
    en_messages[NODE_CREA_001] = "Parent Node and assignment is required."
    es_messages[NODE_CREA_001] = "Nodo padre y asignación es requerido."

    # Check Rule ################################################################
    CHK_RULE_003 = "CHK-RULE-003"
    en_messages[CHK_RULE_003] = "Case # {}, KV-Item: {}, cannot be used as {}."
    es_messages[CHK_RULE_003] = "Caso #{}, KV-Item: {}, no puede ser usada como {}."

    CHK_RULE_002 = "CHK-RULE-002"
    en_messages[CHK_RULE_002] = "Case # {}, Condition: {}, cannot be used as {}."
    es_messages[CHK_RULE_002] = "Caso #{}, Condición: {}, no puede ser usada como {}."

    CHK_RULE_001 = "CHK-RULE-001"
    en_messages[CHK_RULE_001] = "For check rules must have Cases, Conditions, KV-Items."
    es_messages[CHK_RULE_001] = "Para verificar regla se deben tener Casos, Condiciones y KV-Items."

    # Create Case ################################################################
    CASE_CREA_001 = "CASE-CREA-001"
    en_messages[CASE_CREA_001] = "Rules type TREE cannot create Cases directly."
    es_messages[CASE_CREA_001] = "Las reglas tipo 'TREE' no pueden crear Casos directamente."

    # Update Case ################################################################
    CASE_UPD_005 = "CASE-UPD-005"
    en_messages[CASE_UPD_005] = "Case default cannot change position."
    es_messages[CASE_UPD_005] = "El caso por defecto no puede cambiar de posición."

    CASE_UPD_004 = "CASE-UPD-004"
    en_messages[CASE_UPD_004] = "Case not found."
    es_messages[CASE_UPD_004] = "No se encontró caso."

    CASE_UPD_003 = "CASE-UPD-003"
    en_messages[CASE_UPD_003] = "Positions must not be duplicaded."
    es_messages[CASE_UPD_003] = "Las posiciones no deben duplicarse."

    CASE_UPD_002 = "CASE-UPD-002"
    en_messages[CASE_UPD_002] = "Position must not be empty."
    es_messages[CASE_UPD_002] = "La Posición no debe estar vacía."

    CASE_UPD_001 = "CASE-UPD-001"
    en_messages[CASE_UPD_001] = "Case ID must not be empty."
    es_messages[CASE_UPD_001] = "ID de Case no debe estar vacío."

    # Update Condition ################################################################
    COND_UPD_003 = "COND-UPD-003"
    en_messages[COND_UPD_003] = "Condition '{}' not found."
    es_messages[COND_UPD_003] = "Condición '{}' no encontrada."

    COND_UPD_002 = "COND-UPD-002"
    en_messages[COND_UPD_002] = "Items must be unique."
    es_messages[COND_UPD_002] = "Los elemenos deben ser únicos."

    COND_UPD_001 = "COND-UPD-001"
    en_messages[COND_UPD_001] = "Nothing to update."
    es_messages[COND_UPD_001] = "Nada que actualizar."

    # Update KV Items ################################################################
    KVI_UPD_003 = "KVI-UPD-003"
    en_messages[KVI_UPD_003] = "All KV Items must exists."
    es_messages[KVI_UPD_003] = "Todos los KV Items deben existir."

    KVI_UPD_002 = "KVI-UPD-002"
    en_messages[KVI_UPD_002] = "Nothing to update."
    es_messages[KVI_UPD_002] = "Nada que actualizar."

    KVI_UPD_001 = "KVI-UPD-001"
    en_messages[KVI_UPD_001] = "Rule's ID or Name are mandatory."
    es_messages[KVI_UPD_001] = "Id o nombre de Regla es obligatorio."

    # Read KV Item ################################################################
    KV_READ_003 = "KVI-READ-003"
    en_messages[KV_READ_003] = "KV Items not found."
    es_messages[KV_READ_003] = "No se encontrado Items del KV."

    KV_READ_002 = "KVI-READ-002"
    en_messages[KV_READ_002] = "KV ID not found."
    es_messages[KV_READ_002] = "KV ID no encontrado."

    KV_READ_001 = "KVI-READ-001"
    en_messages[KV_READ_001] = "KV ID must not be empty."
    es_messages[KV_READ_001] = "KV ID debe proporcionarse."

    # Read Rule ################################################################
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

    # Create parameter ################################################################
    PARAM_CREA_004 = "PARAM-CREA-004"
    en_messages[PARAM_CREA_004] = "Nothing to update."
    es_messages[PARAM_CREA_004] = "Nada que actualizar."

    PARAM_CREA_003 = "PARAM-SAVE-003"
    en_messages[PARAM_CREA_003] = "Any new parameter must not be exists."
    es_messages[PARAM_CREA_003] = "Ningún nuevo parametro debe existir."

    PARAM_CREA_002 = "PARAM-CREA-002"
    en_messages[PARAM_CREA_002] = "Rule's ID or Name are mandatory."
    es_messages[PARAM_CREA_002] = "Id o nombre de Regla es obligatorio."

    PARAM_CREA_001 = "PARAM-CREA-001"
    en_messages[PARAM_CREA_001] = "All Parameters must be unique."
    es_messages[PARAM_CREA_001] = "Todos los Parametros deben ser únicos."

    # Update Parameter ################################################################
    PARAM_UPD_006 = "PARAM-UPD-006"
    en_messages[PARAM_UPD_006] = "KV Item '{}' not found."
    es_messages[PARAM_UPD_006] = "KV ITem '{}' no encontrado."

    PARAM_UPD_005 = "PARAM-UPD-005"
    en_messages[PARAM_UPD_005] = "Condition '{}' not found."
    es_messages[PARAM_UPD_005] = "La Condición '{}' no encontrada."

    PARAM_UPD_004 = "PARAM-UPD-004"
    en_messages[PARAM_UPD_004] = "All parameters to update must exists."
    es_messages[PARAM_UPD_004] = "Todos los parametros para actualización, debe existir."

    PARAM_UPD_003 = "PARAM-UPD-003"
    en_messages[PARAM_UPD_003] = "All Parameters must be unique."
    es_messages[PARAM_UPD_003] = "Todos los Parametros deben ser únicos."

    PARAM_UPD_002 = "PARAM-UPD-002"
    en_messages[PARAM_UPD_002] = "Nothing to update."
    es_messages[PARAM_UPD_002] = "Nada que actualizar."

    PARAM_UPD_001 = "PARAM-UPD-001"
    en_messages[PARAM_UPD_001] = "Rule's ID or Name are mandatory."
    es_messages[PARAM_UPD_001] = "Id o nombre de Regla es obligatorio."

    # Rule Create ################################################################
    RU_CREA_002 = "RU-CREA-002"
    en_messages[RU_CREA_002] = "All paramter's name must be unique."
    es_messages[RU_CREA_002] = "Todos los nombres de los parámetros deben ser únicos."

    RU_CREA_001 = "RU-CREA-001"
    en_messages[RU_CREA_001] = "Already exists a Rule with same name."
    es_messages[RU_CREA_001] = "Ya existe una Regla con el mismo nombre."

    # Rule Update ################################################################
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

    # Entities #################################################################
    # KV Item
    KVI_006 = "KVI-006"
    en_messages[KVI_006] = "Case ID is required."
    es_messages[KVI_006] = "ID de Caso es requerido."

    KVI_004 = "KVI-004"
    en_messages[KVI_004] = "Value must be between 1 and 500 characteres."
    es_messages[KVI_004] = "Valor debe tener una longitud entre 1 y 500 caracteres."

    KVI_003 = "KVI-003"
    en_messages[KVI_003] = "KV Item Name must be between 5 and 50 characters."
    es_messages[KVI_003] = "Nombre de KV Item debe ser de 5 a 50 caracteres."

    KVI_002 = "KVI-002"
    en_messages[KVI_002] = "Nombre de KV Item es obligatorio."
    es_messages[KVI_002] = "KV Item Name must not be empty."

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
    en_messages[RULE_003] = "Rule Type must be 'CASE'."
    es_messages[RULE_003] = "Tipo Regla deber ser 'CASE'."

    RULE_002 = "RULE-002"
    en_messages[RULE_002] = "Rule Type must be provided."
    es_messages[RULE_002] = "Tipo de Regla es obligatorio."

    RULE_001 = "RULE-001"
    en_messages[RULE_001] = "Rule Name is mandatory."
    es_messages[RULE_001] = "Nombre de Regla es obligatorio."

    # Object ########################################################################
    # Update Object
    OBJ_UPD_001 = "OBJ_UPD_001"
    en_messages[OBJ_UPD_001] = "No modificactions."
    es_messages[OBJ_UPD_001] = "Sin modificaciones."

    # Tenant ########################################################################
    # Create
    TE_CREA_003 = "TE-CREA-003"
    en_messages[TE_CREA_003] = "Tenant ID already exists."
    es_messages[TE_CREA_003] = "ID de Tenant ya existe."

    TE_CREA_002 = "TE-CREA-002"
    en_messages[TE_CREA_002] = "Tenant Name must be between 5 and 50 characteres."
    es_messages[TE_CREA_002] = "Nombre de Tenant debe ser entre 5 y 50 caracteres."

    TE_CREA_001 = "TE-CREA-001"
    en_messages[TE_CREA_001] = "Tenant ID must be between 1 and 99."
    es_messages[TE_CREA_001] = "Id Tenant debe ser entre 1 y 99."
