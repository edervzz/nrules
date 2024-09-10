
""" Extensions """
from typing import List
from toolkit import Validator
from toolkit.localization import Localizer, Codes
from domain.entities.expression_component import ExpressionComponent


class ExpressionValidator(Validator):
    """ Extensions for expressions """

    def __init__(self, localizer: Localizer):
        super().__init__()
        self._localizer = localizer
        self.expression_original = ""
        self._and = "<&&>"
        self._or = "<||>"
        self._eq = "<EQ>"
        self._ne = "<NE>"
        self._gt = "<GT>"
        self._ge = "<GE>"
        self._lt = "<LT>"
        self._le = "<LE>"
        self._in = "<IN>"
        self._oper = "<OP>"
        self._inoper = "<IO>"
        self.components: List[ExpressionComponent] = []
        self.operators = []

    def __validate__(self, request: str):
        """ Run request validations 
        obj.asdf >= false AND qwer = true OR rtyu = "hello" AND lkjj = 9898 \n
        obj.asdf >= false<OP>qwer = true<OP>rtyu = "hello"<OP>lkjj = 9898 \n
        obj.asdf >= false<&&>qwer = true<||>rtyu = "hello"<&&>lkjj = 9898 \n
        obj.asdf<IO>false<OP>qwer<IO>true<OP>rtyu<IO>"hello"<OP>lkjj<IO>9898 \n
        obj.asdf<GE>false<&&>qwer<EQ>true<||>rtyu<EQ>"hello"<&&>lkjj<EQ>9898 \n
        obj.asdf, GE, false       => true \n
        qwer,     GE, true        => true \n
        rtyu,     GE, "hello"     => false \n
        lkjj,     EQ, 9898        => true \n
        """
        self.expression_original = request.strip()
        components: List[ExpressionComponent] = []
        operators: List[str] = []
        translated = self.__create_translate()
        var_value = self.__create_var_value()
        length = len(var_value)
        cursor_exp = 0
        is_end_expression = False

        while (not is_end_expression):
            # collect operator
            if len(components) != 0:
                if var_value.find(self._oper, cursor_exp, length) == -1:
                    raise self.as_error(
                        Codes.RU_CREA_006,
                        self._localizer.get(
                            Codes.RU_CREA_006, request, "operator not found")
                    )
                else:
                    oper_start = var_value.find(
                        self._oper, cursor_exp, length)
                    oper_end = oper_start + 4
                    operator = translated[oper_start:oper_end]
                    operators.append(operator)
                    cursor_exp = oper_end
            # collect variable
            if var_value.find(self._inoper, cursor_exp, length) == -1:
                raise self.as_error(
                    Codes.RU_CREA_006,
                    self._localizer.get(
                        Codes.RU_CREA_006, request, "variable not found")
                )
            variable_end = var_value.find(self._inoper, cursor_exp, length)
            variable = translated[cursor_exp:variable_end]
            cursor_exp = variable_end
            # collect inner operator
            if var_value.find(self._inoper, cursor_exp, length) == -1:
                raise self.as_error(
                    Codes.RU_CREA_006,
                    self._localizer.get(
                        Codes.RU_CREA_006, request, "inner operator not found")
                )
            inner_oper_start = var_value.find(self._inoper, cursor_exp, length)
            inner_oper_end = inner_oper_start + 4
            inner_oper = translated[inner_oper_start:inner_oper_end]
            cursor_exp = inner_oper_end
            # collect value
            value_end = var_value.find(self._oper, cursor_exp, length)
            if value_end == -1:
                # confirm no more inner operators forward
                value_end = var_value.find(self._inoper, cursor_exp, length)
                if value_end == -1:
                    value = translated[inner_oper_start:]
                    is_end_expression = True
                else:
                    raise self.as_error(
                        Codes.RU_CREA_006,
                        self._localizer.get(
                            Codes.RU_CREA_006, request, "inner operator at end of expression")
                    )
            else:
                value = translated[cursor_exp:value_end]

            item = ExpressionComponent(variable, inner_oper, value)
            # move cursor
            cursor_exp = value_end

            components.append(item)

        if len(components) > 0:
            self.components = components
        if len(operators) > 0 and len(operators) == len(components) - 1:
            self.operators = operators

    def __create_translate(self) -> str:
        translated = self.expression_original
        translated = translated.replace(" AND ", self._and)
        translated = translated.replace(" OR ", self._or)
        translated = translated.replace(" = ", self._eq)
        translated = translated.replace(" <> ", self._ne)
        translated = translated.replace(" > ", self._gt)
        translated = translated.replace(" >= ", self._ge)
        translated = translated.replace(" < ", self._lt)
        translated = translated.replace(" <= ", self._le)
        translated = translated.replace(" IN ", self._in)

        return translated

    def __create_var_value(self) -> str:
        var_value = self.expression_original
        var_value = var_value.replace(" AND ", self._oper)
        var_value = var_value.replace(" OR ", self._oper)
        var_value = var_value.replace(" = ", self._inoper)
        var_value = var_value.replace(" <> ", self._inoper)
        var_value = var_value.replace(" > ", self._inoper)
        var_value = var_value.replace(" >= ", self._inoper)
        var_value = var_value.replace(" < ", self._inoper)
        var_value = var_value.replace(" <= ", self._inoper)
        var_value = var_value.replace(" IN ", self._inoper)

        return var_value
