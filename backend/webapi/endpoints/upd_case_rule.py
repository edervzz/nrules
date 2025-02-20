""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import UpdateCaseModel
from application.messages import UpdateCaseRuleRequest
from application.commands import UpdateCaseRuleHandler
from toolkit import Identification


upd_case_rule_bp = Blueprint("UpdateCasesRule", __name__)


@upd_case_rule_bp.put("/t/<tid>/rules/<rid>/cases")
def upd_case_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    model = UpdateCaseModel(json.dumps(json_data))

    command = UpdateCaseRuleRequest(
        rule_id,
        rule_name,
        model.cases
    )

    UpdateCaseRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
