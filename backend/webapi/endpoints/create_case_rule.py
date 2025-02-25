""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import NewCaseModel
from application.messages import CreateCaseRuleRequest
from application.commands import CreateCaseRuleHandler
from toolkit import Identification


new_case_rule_bp = Blueprint("NewCasesRule", __name__)


@new_case_rule_bp.post("/t/<tid>/rules/<rid>/cases")
def new_case_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("ridType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    model = NewCaseModel(json.dumps(json_data))

    command = CreateCaseRuleRequest(
        rule_id,
        rule_name,
        model.case
    )

    CreateCaseRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
