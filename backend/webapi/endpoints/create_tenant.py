""" Create a new tenant """
import json
from flask import Blueprint, request, Response, current_app, session
from webapi.models import NewTenantModel
from application.messages import CreateTenantRequest
from application.commands import CreateTenantHandler

new_tenant_bp = Blueprint("New Tenant", __name__)


@new_tenant_bp.post("/tenants")
def new_tenant_endpoint():
    """ New Tenant Endpoint """
    json_data = request.get_json(silent=True)
    if json_data is None:
        return

    new_tenant = NewTenantModel(json.dumps(json_data))

    command = CreateTenantRequest(
        new_tenant.tenant_id,
        new_tenant.tenant_name,
        new_tenant.option_dev,
        new_tenant.option_test,
        new_tenant.option_prod
    )

    result = CreateTenantHandler(
        current_app.config["tenancy_repository"],
        current_app.config["logger"],
        current_app.config[session["localizer"]]
    ).handler(command)

    return Response(
        response=json.dumps(result.__dict__),
        status=200,
        mimetype="application/json"
    )
