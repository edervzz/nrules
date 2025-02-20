""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import UpdConditionsRuleModel
from application.messages import UpdateConditionsRuleRequest
from application.commands import UpdateConditionsRuleHandler
from toolkit import Identification


upd_condition_rule_bp = Blueprint("UpdateConditionsRule", __name__)


@upd_condition_rule_bp.put("/t/<tid>/rules/<rid>/cases/<cid>/conditions")
def upd_conditions_rule_endpoint(tid=None, rid=None, cid=None):
    """ Update Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    upd_conditions_rule = UpdConditionsRuleModel(json.dumps(json_data), cid)

    command = UpdateConditionsRuleRequest(
        rule_id,
        rule_name,
        upd_conditions_rule.conditions
    )

    UpdateConditionsRuleHandler(
        current_app.config[tid],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
