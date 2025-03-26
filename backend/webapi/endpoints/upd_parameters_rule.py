""" Update Conditions of Rule """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import UpdParametersRuleModel
from application.messages import UpdateParametersRuleRequest
from application.commands import UpdateParamtersRuleHandler
from toolkit import Identification


upd_parameters_rule_bp = Blueprint("UpdateParametersRule", __name__)


@upd_parameters_rule_bp.put("/t/<tid>/rules/<rid>/parameters")
def upd_parameters_rule_endpoint(tid=None, rid=None):
    """ Update Rule's parameters """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("ridType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_condition_rule = UpdParametersRuleModel(json.dumps(json_data))

    command = UpdateParametersRuleRequest(
        rule_id,
        rule_name,
        save_condition_rule.parameters
    )

    UpdateParamtersRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
