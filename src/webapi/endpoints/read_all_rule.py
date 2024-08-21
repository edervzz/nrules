""" Create a new workflow """
import json
from typing import List
from flask import Blueprint, Response
from application.messages import ReadAllRulesRequest
from application.queries import ReadAllRulesHandler
from toolkit import Services
from webapi.models import RuleModel

read_all_rule_bp = Blueprint("Read All Rules", __name__)


@read_all_rule_bp.get("/rules")
def read_all_rules_endpoint(_id=None):
    """ Read rules Endpoint """
    # todo: pagination
    command = ReadAllRulesRequest(
        1,
        5
    )

    handler = ReadAllRulesHandler(
        Services.repository,
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    if result.rules is not None:
        rules = []
        for r in result.rules:
            rule = RuleModel(
                r.id,
                r.name,
                r.expression,
                r.is_exclusive)
            rules.append(rule)
    else:
        rules = None

    js = json.dumps(rules)

    return Response(
        response=js,
        status=200,
        headers=[
            ("Next-Page", f"{result.pagination.next_page}"),
            ("Previous-Page", f"{result.pagination.previous_page}"),
            ("Total-Pages", f"{result.pagination.total_pages}"),
            ("Total-Count", f"{result.pagination.total_count}")
        ]
    )
