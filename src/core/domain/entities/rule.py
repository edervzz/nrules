""" _summary_ """


class Rule:
    """_summary_"""

    def __init__(self, expression: str):
        self.params = []
        self.expression: str = expression

    def check_expression(self) -> bool:
        """verify an expression"""

        return True

    def get_next_component(self):
        """ get next component from expression """
        expression = self.expression
        # find the first variable, means up to first space
        cursor_index = expression.find(" ")
        variable = expression[0:cursor_index]
        operator = ""
        # next, find the first operator
        for _ in range(1):
            start_oper = expression.find(" = ", cursor_index, cursor_index+3)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 1]
                cursor_index = start_oper + 2
                break

            start_oper = expression.find(" > ", cursor_index, cursor_index+3)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 1]
                cursor_index = start_oper + 2
                break

            start_oper = expression.find(" < ", cursor_index, cursor_index+3)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 1]
                cursor_index = start_oper + 2
                break

            start_oper = expression.find(" >= ", cursor_index, cursor_index+4)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 2]
                cursor_index = start_oper + 3
                break

            start_oper = expression.find(" <= ", cursor_index, cursor_index+4)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 2]
                cursor_index = start_oper + 3
                break

            start_oper = expression.find(" <> ", cursor_index, cursor_index+4)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 2]
                cursor_index = start_oper + 3
                break

            start_oper = expression.find(" IN ", cursor_index, cursor_index+4)
            if (start_oper != -1):
                start_oper += 1
                operator = expression[start_oper:start_oper + 2]
                cursor_index = start_oper + 3
                break

        value = ""
        if (expression.find("\"", cursor_index, cursor_index+1) != -1):
            # should be a text
            start_text = expression.find("\"", cursor_index, cursor_index+1)
            end_text = expression.find("\" ", cursor_index+1) + 1
            value = expression[cursor_index:end_text]
            cursor_index = end_text + 1
        elif expression.find("true ", cursor_index, cursor_index+6) != -1:
            # should be true
            value = expression[cursor_index:cursor_index+4]
            cursor_index = cursor_index+5
        elif expression.find("false ", cursor_index, cursor_index+6) != -1:
            # should be false
            value = expression[cursor_index:cursor_index+5]
            cursor_index = cursor_index+6
        else:
            # should be numeric
            print("")

        print(variable, operator, value)
        print(cursor_index)
