from typing import Any

from globus_cli.login_manager import LoginManager
from globus_cli.parsing import command
from globus_cli.termio import formatted_print

from ._common import group_create_and_update_params


@group_create_and_update_params(create=True)
@command("create")
@LoginManager.requires_login(LoginManager.GROUPS_RS)
def group_create(*, login_manager: LoginManager, **kwargs: Any):
    """Create a new group"""
    groups_client = login_manager.get_groups_client()

    response = groups_client.create_group(kwargs)
    group_id = response["id"]

    formatted_print(response, simple_text=f"Group {group_id} created successfully")
