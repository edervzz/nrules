""" Create a new workflow """
import json
from flask import Blueprint, request, Response
from webapi.models import NewTenantModel
from application.messages import CreateTenantRequest
from application.commands import CreateTenantHandler
from toolkit import Services

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
        Services.tenancy_repository,
        Services.logger,
        Services.localizer
    ).handler(command)

    return Response(
        response=json.dumps(result.__dict__),
        status=200
    )
