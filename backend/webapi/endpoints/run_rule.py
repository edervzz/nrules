""" Run Rule """
import json
from flask import Blueprint, request, Response, current_app, session
from application.messages import RunRuleRequest
from application.commands import RunRuleHandler
from webapi.models import RunRule


run_rule_bp = Blueprint("RunRule", __name__)


@run_rule_bp.post("/t/<tid>/run/rule/<rid>")
def run_rule_endpoint(tid: int = 0, rid: int = 0):
    """ Run rules Endpoint """

    rule_id = request.args.get("ridType", 0)
    json_data = request.json
    if json_data is None:
        return

    js = json.dumps(json_data)
    data = json.loads(js)

    payload = any
    if "data" in data:
        payload = data["data"]

    command = RunRuleRequest(
        rid,
        "",
        rule_id,
        payload
    )

    result = RunRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    res = RunRule(result.ok, result.rule_results, result.trace)

    data = res.to_json()
    return Response(
        response=data,
        status=200,
        content_type="application/json"
    )
