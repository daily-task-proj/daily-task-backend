from auth.google_auth import blp as GoogleAuthBlueprint
from resources.user import blp as UserBlueprint
from resources.team import blp as TeamBlueprint
from resources.invite import blp as InviteBlueprint
from resources.team_user import blp as TeamUserBlueprint
from resources.group import blp as GroupBlueprint
from resources.type import blp as TypeBlueprint
from resources.status import blp as StatusBlueprint
from resources.priority import blp as PriorityBlueprint
from resources.difficulty import blp as DifficultyBlueprint
from resources.task_type import blp as TaskTypeBlueprint
from resources.task import blp as TaskBlueprint
from resources.user_task import blp as UserTaskBlueprint
from resources.user_group import blp as UserGroupBlueprint
from resources.task_group import blp as TaskGroupBlueprint
from resources.form_item import blp as FormItemBlueprint
from resources.item import blp as ItemBlueprint
from resources.user_form_item import blp as UserFormItemBlueprint
from resources.daily_limit_time import blp as DailyLimitTimeBlueprint
from resources.daily import blp as DailyBlueprint
from werkzeug.exceptions import UnprocessableEntity


@UserBlueprint.errorhandler(UnprocessableEntity)
@DailyLimitTimeBlueprint.errorhandler(UnprocessableEntity)
@DailyBlueprint.errorhandler(UnprocessableEntity)
def handle_unprocessable_entity_error(error):
    errors = {}

    messages = []
    if error.data:
        errors = error.data.get("messages", {}).get("json", {})
        for field, field_errors in errors.items():
            messages.extend(field_errors)

    if not messages:
        messages = ["Erro de validação desconhecido"]

    return {"messages": messages}, 422


def register_blueprints(api):
    blueprints = [
        GoogleAuthBlueprint,
        UserBlueprint,
        TeamBlueprint,
        InviteBlueprint,
        TeamUserBlueprint,
        GroupBlueprint,
        TypeBlueprint,
        StatusBlueprint,
        PriorityBlueprint,
        DifficultyBlueprint,
        TaskTypeBlueprint,
        TaskBlueprint,
        UserTaskBlueprint,
        UserGroupBlueprint,
        TaskGroupBlueprint,
        FormItemBlueprint,
        ItemBlueprint,
        UserFormItemBlueprint,
        DailyLimitTimeBlueprint,
        DailyBlueprint,
    ]

    for blueprint in blueprints:
        api.register_blueprint(blueprint)
