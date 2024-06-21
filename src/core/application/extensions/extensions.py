
""" Extensions """
from domain.entities.expression_component import ExpressionComponent


class ExpressionExtensions:
    """ Extensions for expressions """

    @staticmethod
    def transform_expression(expression_original: str) -> str:
        """ Transform a expression into single components  """
        # obj.asdf >= false AND qwer = true OR rtyu = "hello" AND lkjj = 9898

        # obj.asdf >= false<OP>qwer = true<OP>rtyu = "hello"<OP>lkjj = 9898
        # obj.asdf >= false<&&>qwer = true<||>rtyu = "hello"<&&>lkjj = 9898

        # obj.asdf<IO>false<OP>qwer<IO>true<OP>rtyu<IO>"hello"<OP>lkjj<IO>9898
        # obj.asdf<GE>false<&&>qwer<EQ>true<||>rtyu<EQ>"hello"<&&>lkjj<EQ>9898

        # obj.asdf, GE, false       => true
        # qwer,     GE, true        => true
        # rtyu,     GE, "hello"     => false
        # lkjj,     EQ, 9898        => true

        # <&&>
        # <||>
        # <&&>

        AND = "<&&>"
        OR = "<||>"
        EQ = "<EQ>"
        NE = "<NE>"
        GT = "<GT>"
        GE = "<GE>"
        LT = "<LT>"
        LE = "<LE>"
        IN = "<IN>"
        expression_original = expression_original.strip()
        expression_translated = expression_original
        expression_translated = expression_translated.replace(" AND ", AND)
        expression_translated = expression_translated.replace(" OR ", OR)
        expression_translated = expression_translated.replace(" = ", EQ)
        expression_translated = expression_translated.replace(" <> ", NE)
        expression_translated = expression_translated.replace(" > ", GT)
        expression_translated = expression_translated.replace(" >= ", GE)
        expression_translated = expression_translated.replace(" < ", LT)
        expression_translated = expression_translated.replace(" <= ", LE)
        expression_translated = expression_translated.replace(" IN ", IN)

        OPER = "<OP>"
        INNER_OPER = "<IO>"
        expression_var_value = expression_original
        expression_var_value = expression_var_value.replace(" AND ", OPER)
        expression_var_value = expression_var_value.replace(" OR ", OPER)
        expression_var_value = expression_var_value.replace(" = ", INNER_OPER)
        expression_var_value = expression_var_value.replace(" <> ", INNER_OPER)
        expression_var_value = expression_var_value.replace(" > ", INNER_OPER)
        expression_var_value = expression_var_value.replace(" >= ", INNER_OPER)
        expression_var_value = expression_var_value.replace(" < ", INNER_OPER)
        expression_var_value = expression_var_value.replace(" <= ", INNER_OPER)
        expression_var_value = expression_var_value.replace(" IN ", INNER_OPER)

        components = [ExpressionComponent]

        cursor = 0

        # collect variable
        variable_end = expression_var_value.find(
            INNER_OPER,
            cursor,
            len(expression_var_value)
        )
        variable = expression_translated[cursor:variable_end]
        cursor = variable_end
        # collect operator
        operator_start = expression_var_value.find(
            INNER_OPER,
            cursor,
            len(expression_var_value)
        )
        operator_end = operator_start + 4
        operator = expression_translated[operator_start:operator_end]
        cursor = operator_end
        # value collector
        value_end = expression_var_value.find(
            OPER,
            cursor,
            len(expression_var_value)
        )
        if value_end != -1:
            value = expression_translated[cursor:value_end]
        else:
            value_end = expression_var_value.find(
                INNER_OPER,
                cursor,
                len(expression_var_value)
            )
            if value_end == -1:
                value = expression_translated[operator_start:]
            else:
                value = None

        item = ExpressionComponent(variable, operator, value)
        components.append(item)


def get_next_component(expression: str):
    """ Get next component from expression \n
        e.g.: obj.asdf >= false AND qwer = true OR rtyu = "hello" AND lkjj = 9898
    """

    expression = expression.strip()
    expression += "."
    # find the first variable, means up to first space
    cursor_index = expression.find(" ")
    variable = expression[0:cursor_index]
    # next, find the first operator
    operator = ""
    for _ in range(1):
        operidx = expression.find(" = ", cursor_index, cursor_index+3)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 1]
            cursor_index = operidx + 2
            break

        operidx = expression.find(
            " > ", cursor_index, cursor_index+3)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 1]
            cursor_index = operidx + 2
            break

        operidx = expression.find(
            " < ", cursor_index, cursor_index+3)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 1]
            cursor_index = operidx + 2
            break

        operidx = expression.find(
            " >= ", cursor_index, cursor_index+4)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 2]
            cursor_index = operidx + 3
            break

        operidx = expression.find(
            " <= ", cursor_index, cursor_index+4)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 2]
            cursor_index = operidx + 3
            break

        operidx = expression.find(
            " <> ", cursor_index, cursor_index+4)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 2]
            cursor_index = operidx + 3
            break

        operidx = expression.find(
            " IN ", cursor_index, cursor_index+4)
        if (operidx != -1):
            operidx += 1
            operator = expression[operidx:operidx + 2]
            cursor_index = operidx + 3
            break

    value = ""
    if (expression.find("\"", cursor_index, cursor_index+1) != -1):
        # should be a text
        start_text = expression.find("\"", cursor_index, cursor_index+1)
        end_text = expression.find("\" ", cursor_index+1) + 1
        if end_text == -1:
            end_text = expression.find("\".", cursor_index+1) + 1
        value = expression[start_text:end_text]
        cursor_index = end_text + 1
    elif expression.find("true", cursor_index, cursor_index+6) != -1:
        start_text = expression.find("true ", cursor_index, cursor_index+1)
        end_text = expression.find("\" ", cursor_index+1) + 1
        if end_text == -1:
            end_text = expression.find("\".", cursor_index+1) + 1
        # should be true
        value = expression[cursor_index:cursor_index+4]
        cursor_index = cursor_index+5
    elif expression.find("false", cursor_index, cursor_index+6) != -1:
        # should be false
        value = expression[cursor_index:cursor_index+5]
        cursor_index = cursor_index+6
    else:
        # should be numeric
        start_number = cursor_index
        end_number = expression.find(" ", cursor_index, cursor_index)
        if (end_number == -1):
            end_number = cursor_index
        value = expression[start_number:end_number]
        cursor_index = end_text + 1

    print(variable, operator, value)
    print(cursor_index)
