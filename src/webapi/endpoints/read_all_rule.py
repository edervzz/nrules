""" Create a new workflow """
import json
from typing import List
from flask import Blueprint, Response, request
from application.messages import ReadAllRulesRequest
from application.queries import ReadAllRulesHandler
from toolkit import Services
from webapi.models import RuleModel

read_all_rule_bp = Blueprint("Read All Rules", __name__)


@read_all_rule_bp.get("/rules")
def read_all_rules_endpoint(_id=None):
    """ Read rules Endpoint """
    # todo: pagination
    page_no = request.args.get("pageNo", "1")
    page_size = request.args.get("pageSize", "5")
    command = ReadAllRulesRequest(
        int(page_no),
        int(page_size)
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

    jsonobj = []
    if isinstance(rules, list):
        for r in rules:
            if hasattr(r, "__dict__"):
                jsonobj.append(r.__dict__)

    jsonstr = json.dumps(jsonobj)

    return Response(
        response=jsonstr,
        status=200,
        headers=[
            ("Next-Page", f"{result.pagination.next_page}"),
            ("Previous-Page", f"{result.pagination.previous_page}"),
            ("Total-Pages", f"{result.pagination.total_pages}"),
            ("Total-Count", f"{result.pagination.total_count}")
        ]
    )
