import click

from globus_cli.login_manager import LoginManager
from globus_cli.parsing import command, mutex_option_group
from globus_cli.termio import FORMAT_TEXT_RECORD, formatted_print

from ._common import task_id_arg

COMMON_FIELDS = [
    ("Label", "label"),
    ("Task ID", "task_id"),
    ("Is Paused", "is_paused"),
    ("Type", "type"),
    ("Directories", "directories"),
    ("Files", "files"),
    ("Status", "status"),
    ("Request Time", "request_time"),
    ("Faults", "faults"),
    ("Total Subtasks", "subtasks_total"),
    ("Subtasks Succeeded", "subtasks_succeeded"),
    ("Subtasks Pending", "subtasks_pending"),
    ("Subtasks Retrying", "subtasks_retrying"),
    ("Subtasks Failed", "subtasks_failed"),
    ("Subtasks Canceled", "subtasks_canceled"),
    ("Subtasks Expired", "subtasks_expired"),
    ("Subtasks with Skipped Errors", "subtasks_skipped_errors"),
]

ACTIVE_FIELDS = [("Deadline", "deadline"), ("Details", "nice_status")]

COMPLETED_FIELDS = [("Completion Time", "completion_time")]

DELETE_FIELDS = [
    ("Endpoint", "source_endpoint_display_name"),
    ("Endpoint ID", "source_endpoint_id"),
]

TRANSFER_FIELDS = [
    ("Source Endpoint", "source_endpoint_display_name"),
    ("Source Endpoint ID", "source_endpoint_id"),
    ("Destination Endpoint", "destination_endpoint_display_name"),
    ("Destination Endpoint ID", "destination_endpoint_id"),
    ("Bytes Transferred", "bytes_transferred"),
    ("Bytes Per Second", "effective_bytes_per_second"),
]

SUCCESSFULL_TRANSFER_FIELDS = [
    ("Source Path", "source_path"),
    ("Destination Path", "destination_path"),
]

SKIPPED_PATHS_FIELDS = [
    ("Source Path", "source_path"),
    ("Destination Path", "destination_path"),
    ("Error Code", "error_code"),
]


def print_successful_transfers(client, task_id):
    from globus_cli.services.transfer import iterable_response_to_dict

    res = client.paginated.task_successful_transfers(task_id).items()
    formatted_print(
        res,
        fields=SUCCESSFULL_TRANSFER_FIELDS,
        json_converter=iterable_response_to_dict,
    )


def print_skipped_errors(client, task_id):
    from globus_cli.services.transfer import iterable_response_to_dict

    res = client.paginated.task_skipped_errors(task_id).items()
    formatted_print(
        res,
        fields=SKIPPED_PATHS_FIELDS,
        json_converter=iterable_response_to_dict,
    )


def print_task_detail(client, task_id):
    res = client.get_task(task_id)
    formatted_print(
        res,
        text_format=FORMAT_TEXT_RECORD,
        fields=(
            COMMON_FIELDS
            + (COMPLETED_FIELDS if res["completion_time"] else ACTIVE_FIELDS)
            + (DELETE_FIELDS if res["type"] == "DELETE" else TRANSFER_FIELDS)
        ),
    )


@command(
    "show",
    short_help="Show detailed information about a task",
    adoc_output="""
When text output is requested, output varies slightly between 'TRANSFER' and
'DELETE' tasks, and between active and completed tasks.

All of the following which apply will be shown:

- 'Task ID'
- 'Type'
- 'Status'
- 'Is Paused'
- 'Label'
- 'Files'
- 'Directories'
- 'Source Endpoint'
- 'Source Endpoint ID'
- 'Destination Endpoint'
- 'Destination Endpoint ID'
- 'Endpoint'
- 'Endpoint ID'
- 'Completion Time'
- 'Deadline'
- 'Details'
- 'Request Time'
- 'Bytes Transferred'
- 'Bytes Per Second'
- 'Faults'
- 'Total Subtasks'
- 'Subtasks Succeeded'
- 'Subtasks Pending'
- 'Subtasks Retrying'
- 'Subtasks Failed'
- 'Subtasks Canceled'
- 'Subtasks Expired'

If *--successful-transfers* is given, the following fields are used:

- 'Source Path'
- 'Destination Path'
""",
    adoc_examples="""Show detailed info about a task as text

[source,bash]
----
$ globus task show TASK_ID
----
""",
)
@task_id_arg
@click.option(
    "--successful-transfers",
    "-t",
    is_flag=True,
    default=False,
    help=(
        "Show files that were transferred as result of this task. "
        "Mutually exclusive with --skipped-errors"
    ),
)
@click.option(
    "--skipped-errors",
    is_flag=True,
    default=False,
    help=(
        "Show paths that were skipped due to errors during this task. "
        "Mutually exclusive with --successful-transfers"
    ),
)
@mutex_option_group("--successful-transfers", "--skipped-errors")
@LoginManager.requires_login(LoginManager.TRANSFER_RS)
def show_task(
    *, login_manager: LoginManager, successful_transfers, skipped_errors, task_id
):
    """
    Print information detailing the status and other info about a task.

    The task may be pending, completed, or in progress.
    """
    transfer_client = login_manager.get_transfer_client()

    if successful_transfers:
        print_successful_transfers(transfer_client, task_id)
    elif skipped_errors:
        print_skipped_errors(transfer_client, task_id)
    else:
        print_task_detail(transfer_client, task_id)
