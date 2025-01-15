""" Read a Rule """
import json
from flask import Blueprint, request, Response, current_app, session
from application.messages import ReadRuleRequest
from application.queries import ReadRuleHandler
from toolkit import Identification
from webapi.models import RuleModel

read_rule_bp = Blueprint("Read Rule", __name__)


@read_rule_bp.get("/t/<tid>/rules/<rule_id>")
def read_rules_endpoint(tid=None, rule_id=None):
    """ Read rules Endpoint """
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rule_id, id_type)

    command = ReadRuleRequest(
        rule_id,
        rule_name
    )

    result = ReadRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    rule = RuleModel(
        result.rule.id,
        result.rule.name,
        result.rule.rule_type,
        result.rule.strategy,
        result.rule.version,
        result.rule.is_active,
        result.parameters,
        result.cases,
        result.conditions,
        result.kv_items)

    jsonstr = json.dumps(rule.__dict__)

    return Response(
        response=jsonstr,
        status=200,
        content_type="application/json",
    )
