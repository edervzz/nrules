""" Create a new workflow """
import json
from flask import Blueprint, Response, request, current_app
from flask_cors import cross_origin
from application.messages import ReadAllRulesRequest
from application.queries import ReadAllRulesHandler
from webapi.models import RuleModel

read_all_rule_bp = Blueprint("Read All Rules", __name__)


@cross_origin
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
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    )

    result = handler.handler(command)

    if result.rules is not None:
        rules = []
        for r in result.rules:
            rule = RuleModel(
                tenant_id,
                r.id,
                r.name,
                r.rule_type,
                r.strategy,
                r.kvs_id_nok,
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
        content_type="application/json",
        headers=[
            ("Next-Page", f"{result.pagination.next_page}"),
            ("Previous-Page", f"{result.pagination.previous_page}"),
            ("Total-Pages", f"{result.pagination.total_pages}"),
            ("Total-Count", f"{result.pagination.total_count}"),
        ]
    )
