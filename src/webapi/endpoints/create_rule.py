""" Creaet a new Rule """
import json
from flask import Blueprint, request
from webapi.models.new_rule import NewRule, NewRuleResult



new_rule = Blueprint("New Rule", __name__)


@new_rule.post("/rule")
def new_rule_endpoint():
    """ endpoint """
    request_data: NewRule = request.get_json()

    result = NewRuleResult(123)
    jsonstring = json.dumps(result.__dict__)
    return jsonstring, 201
