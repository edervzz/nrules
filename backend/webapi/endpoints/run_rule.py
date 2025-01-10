""" Run Rule """
import json
from flask import Blueprint, request, Response, current_app
from application.messages import RunRuleRequest
from application.commands import RunRuleHandler
from webapi.models import RunRule


run_rule_bp = Blueprint("Run Rule", __name__)


@run_rule_bp.post("/t/<tid>/run/rule/<rid>")
def run_rule_endpoint(tid: int = 0, rid: int = 0):
    """ Run rules Endpoint """

    kvs_id = request.args.get("kvsId", 0)
    json_data = request.json
    if json_data is None:
        return

    js = json.dumps(json_data)
    data = json.loads(js)

    if "data" in data:
        payload = data["data"]

    command = RunRuleRequest(
        rid,
        "",
        kvs_id,
        payload
    )

    result = RunRuleHandler(
        current_app.config[str(tid)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    res = RunRule(result.ok, result.rule_results, result.trace)

    data = res.to_json()
    return Response(
        response=data,
        status=200,
        content_type="application/json"
    )
