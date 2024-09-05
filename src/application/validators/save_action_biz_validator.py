"""_summary_
    """
from toolkit import Validator, Localizer, Codes
from domain.entities import Action
from domain.ports import CoreRepository
from application.messages import SaveActionRequest


class SaveActionBizValidator(Validator):
    """ Save Action Validator """

    def __init__(self, localizer: Localizer, repo: CoreRepository):
        super().__init__()
        self.repo = repo
        self.local = localizer

    def __validate__(self, request: SaveActionRequest):
        # update
        if request.id > 0:
            action = self.repo.action.read(request.id)
            if action is None:
                raise self.as_not_found(
                    Codes.ACTION_CREA_003,
                    self.local.get(Codes.ACTION_CREA_003))

            action2 = self.repo.action.read_by_external_id(request.name)
            if action2 is not None:
                raise self.as_not_found(
                    Codes.ACTION_CREA_003,
                    self.local.get(Codes.ACTION_CREA_003))

            request.is_update = True
            request.action = action
            request.action.name = request.name
            request.action.ruleset_id = request.ruleset_id
            request.action.kv_id = request.kv_id
            request.action.version += 1
        else:
            action = self.repo.action.read_by_external_id(request.name)
            # Insert
            if action is None:
                request.action = Action()
                request.name = request.name
            # update
            else:
                request.is_update = True
                request.action = action

            request.action.ruleset_id = request.ruleset_id
            request.action.kv_id = request.kv_id
            request.action.version = 1

        if request.run_check:
            if request.action.ruleset_id != 0:
                ruleset = self.repo.ruleset.read(request.action.ruleset_id)
                if ruleset is None:
                    raise self.as_not_found(
                        Codes.ACTION_CREA_005,
                        self.local.get(Codes.ACTION_CREA_005))

            if request.action.kv_id != 0:
                kvs = self.repo.kvs.read(request.action.kv_id)
                if kvs is None:
                    raise self.as_not_found(
                        Codes.ACTION_CREA_006,
                        self.local.get(Codes.ACTION_CREA_006))
