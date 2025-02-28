""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import NewNodeModel
from application.messages import CreateNodeRuleRequest
from application.commands import CreateNodeRuleHandler
from toolkit import Identification


new_node_rule_bp = Blueprint("NewNodesRule", __name__)


@new_node_rule_bp.post("/t/<tid>/rules/<rid>/nodes")
def new_node_rule_endpoint(tid=None, rid=None):
    """ New Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("ridType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    model = NewNodeModel(json.dumps(json_data))

    command = CreateNodeRuleRequest(
        rule_id,
        rule_name,
        model.parent_node_id,
        model.assign_node_to
    )

    CreateNodeRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
