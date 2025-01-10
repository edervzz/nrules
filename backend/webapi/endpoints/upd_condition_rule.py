""" Update Conditions of Rule """
import json
from flask import Blueprint, request, Response, current_app
from webapi.models import UpdConditionsRuleModel
from application.messages import UpdateConditionsRuleRequest
from application.commands import UpdateConditionsRuleHandler
from toolkit import Identification


upd_condition_rule_bp = Blueprint("Update Conditions by Rule", __name__)


@upd_condition_rule_bp.put("/t/<tid>/rules/<rid>/conditions")
def upd_conditions_rule_endpoint(tid=None, rid=None):
    """ Update Rule's Conditions """

    tenant_id = Identification.get_tenant_safe(tid)
    id_type = request.args.get("idType", "")
    rule_id, rule_name = Identification.get_object(rid, id_type)

    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    save_condition_rule = UpdConditionsRuleModel(json.dumps(json_data))

    command = UpdateConditionsRuleRequest(
        rule_id,
        rule_name,
        save_condition_rule.conditions
    )

    UpdateConditionsRuleHandler(
        current_app.config[str(tenant_id)],
        current_app.config["logger"],
        current_app.config["localizer"]
    ).handler(command)

    return Response(
        response="",
        status=200
    )
