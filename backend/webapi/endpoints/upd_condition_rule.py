""" Create a new workflow """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import UpdConditionsRuleModel
from application.messages import UpdateConditionsRuleRequest
from application.commands import UpdateConditionsRuleHandler
from toolkit import Identification


upd_condition_rule_bp = Blueprint("Update Conditions by Rule", __name__)


@upd_condition_rule_bp.put("/t/<tid>/rules/<rid>/conditions")
def upd_conditions_rule_endpoint(tid=None, rid=None):
    """ Update Endpoint """
    Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_kvitems_rule = UpdConditionsRuleModel(json.dumps(json_data))

    command = UpdateConditionsRuleRequest(
        rule_id,
        rule_name,
        save_kvitems_rule.conditions
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
