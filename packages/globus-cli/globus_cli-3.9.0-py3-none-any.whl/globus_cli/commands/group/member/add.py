import click

from globus_cli.login_manager import LoginManager
from globus_cli.parsing import IdentityType, ParsedIdentity, command
from globus_cli.termio import FORMAT_TEXT_RECORD, formatted_print
from globus_cli.types import FIELD_LIST_T

ADD_USER_FIELDS: FIELD_LIST_T = [
    ("Group ID", "group_id"),
    ("Added User ID", "identity_id"),
    ("Added User Username", "username"),
]


@command("add", short_help="Add a member to a group")
@click.argument("group_id", type=click.UUID)
@click.argument("user", type=IdentityType())
@click.option(
    "--role",
    type=click.Choice(("member", "manager", "admin")),
    default="member",
    help="The role for the added user",
    show_default=True,
)
@LoginManager.requires_login(LoginManager.GROUPS_RS)
def member_add(
    *, group_id: str, user: ParsedIdentity, role: str, login_manager: LoginManager
):
    """
    Add a member to a group.

    The USER argument may be an identity ID or username (whereas the group must be
    specified with an ID).
    """
    auth_client = login_manager.get_auth_client()
    groups_client = login_manager.get_groups_client()
    identity_id = auth_client.maybe_lookup_identity_id(user.value)
    if not identity_id:
        raise click.UsageError(f"Couldn't determine identity from user value: {user}")
    actions = {"add": [{"identity_id": identity_id, "role": role}]}
    response = groups_client.batch_membership_action(group_id, actions)
    # If this call failed to return an added user, figure out an error to show
    if not response.get("add", None):
        try:
            raise ValueError(response["errors"]["add"][0]["detail"])
        except (IndexError, KeyError):
            raise ValueError("Could not add user to group")
    formatted_print(
        response,
        text_format=FORMAT_TEXT_RECORD,
        fields=ADD_USER_FIELDS,
        response_key=lambda data: data["add"][0],
    )
