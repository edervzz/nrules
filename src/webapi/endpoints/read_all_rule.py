""" Create a new workflow """
import json
from flask import Blueprint, Response, request
from application.messages import ReadAllRulesRequest
from application.queries import ReadAllRulesHandler
from toolkit import Services
from webapi.models import RuleModel

read_all_rule_bp = Blueprint("Read All Rules", __name__)


@read_all_rule_bp.get("/t/<tid>/rules")
def read_all_rules_endpoint(tid=None):
    """ Read rules Endpoint """
    tenant_id = int(tid)
    page_no = request.args.get("pageNo", "1")
    page_size = request.args.get("pageSize", "5")
    command = ReadAllRulesRequest(
        tenant_id,
        int(page_no),
        int(page_size)
    )

    handler = ReadAllRulesHandler(
        Services.core_repositories[tid],
        Services.logger,
        Services.localizer
    )

    result = handler.handler(command)

    if result.rules is not None:
        rules = []
        for r in result.rules:
            rule = RuleModel(
                tenant_id,
                r.id,
                r.name,
                r.expression,
                r.is_exclusive,
                r.version)
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
