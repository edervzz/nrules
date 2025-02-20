""" Read all rules paginated """
import json
from flask import Blueprint, Response, request, current_app, session
from flask_cors import cross_origin
from application.messages import ReadAllRulesRequest
from application.queries import ReadAllRulesHandler
from webapi.models import RuleModel

read_all_rule_bp = Blueprint("ReadAllRules", __name__)


@cross_origin
@read_all_rule_bp.get("/t/<tid>/rules")
def read_all_rules_endpoint(tid=None):
    """ Read rules Endpoint """
    page_no = request.args.get("pageNo", "1")
    page_size = request.args.get("pageSize", "10")
    word = request.args.get("word", "")
    tag = request.args.get("tag", "")
    command = ReadAllRulesRequest(
        tid,
        int(page_no),
        int(page_size),
        word,
        tag
    )

    result = ReadAllRulesHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    if result.rules is not None:
        rules = []
        for r in result.rules:
            rule = RuleModel(
                r.id,
                r.name,
                r.rule_type,
                r.strategy,
                r.version,
                True, None, None, None, None)
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
