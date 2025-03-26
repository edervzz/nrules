""" Check Rule """
from flask import Blueprint, request, Response, current_app, session
from application.messages import CheckRuleRequest
from application.commands import CheckRuleHandler
from toolkit import Identification


check_rule_bp = Blueprint("CheckRule", __name__)


@check_rule_bp.post("/t/<tid>/rules/<rid>/check")
def check_rule_endpoint(tid: int = 0, rid: int = 0):
    """ Check rules Endpoint """

    id_type = request.args.get("ridType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    command = CheckRuleRequest(
        rule_id,
        rule_name
    )

    CheckRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        status=200,
        content_type="application/json"
    )
