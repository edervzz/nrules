""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from application.messages import ReadRuleRequest
from application.queries import ReadRuleHandler
from toolkit import Services, Identification
from webapi.models import RuleModel

read_rule_bp = Blueprint("Read Rule", __name__)


@read_rule_bp.get("/rules/<_id>")
def read_rules_endpoint(_id=None):
    """ Read rules Endpoint """
    id_type = request.args.get("idType")
    rule_id, rule_name = Identification.get(_id, id_type)

    command = ReadRuleRequest(
        rule_id,
        rule_name
    )

    handler = ReadRuleHandler(
        Services.repository,
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    rule = RuleModel(result.rule.name, result.rule.expression,
                     result.rule.is_exclusive)

    js = json.dumps(rule.__dict__)

    return Response(
        response=js,
        status=200
    )
