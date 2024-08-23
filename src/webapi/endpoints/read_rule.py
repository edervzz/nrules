""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from application.messages import ReadRuleRequest
from application.queries import ReadRuleHandler
from toolkit import Services, Identification
from webapi.models import RuleModel

read_rule_bp = Blueprint("Read Rule", __name__)


@read_rule_bp.get("/t/<tid>/rules/<rule_id>")
def read_rules_endpoint(tid=None, rule_id=None):
    """ Read rules Endpoint """
    tenant_id = int(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rule_id, id_type)
    # tenant_id = int(request.args.get("tid", "0"))

    command = ReadRuleRequest(
        tenant_id,
        rule_id,
        rule_name
    )

    handler = ReadRuleHandler(
        Services.repository,
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    rule = RuleModel(
        result.rule.tenant_id,
        result.rule.id,
        result.rule.name,
        result.rule.expression,
        result.rule.is_exclusive,
        result.rule.version)

    js = json.dumps(rule.__dict__)

    return Response(
        response=js,
        status=200
    )
