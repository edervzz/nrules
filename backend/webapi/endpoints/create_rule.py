""" Create a new Rule """
import json
from flask import Blueprint, request, Response, current_app, session
from flask_cors import cross_origin
from webapi.models import NewRuleModel
from application.messages import CreateRuleRequest
from application.commands import CreateRuleHandler
from toolkit import Identification


new_rule_bp = Blueprint("NewRule", __name__)


@cross_origin
@new_rule_bp.post("/t/<tid>/rules")
def new_rules_endpoint(tid=None):
    """ New rules Endpoint """
    Identification.get_tenant_safe(tid)
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_rules = NewRuleModel(json.dumps(json_data))

    command = CreateRuleRequest(
        new_rules.rule,
        new_rules.parameters,
        new_rules.tags
    )

    result = CreateRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=201,
        headers=[
            ("Item", f"/t/{tid}/rules/{result.id}"),
        ]
    )
