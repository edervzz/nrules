""" Create a new inventory """
from flask import Blueprint, request, Response, current_app, session
from application.messages import CreateInventoryRuleRequest
from application.commands import CreateInventoryRuleHandler
from toolkit import Identification


new_inventory_rule_bp = Blueprint("NewInventoryRule", __name__)


@new_inventory_rule_bp.post("/t/<tid>/rules/<rid>/inventory")
def new_inventory_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("ridType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    command = CreateInventoryRuleRequest(
        rule_id,
        rule_name
    )

    CreateInventoryRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
