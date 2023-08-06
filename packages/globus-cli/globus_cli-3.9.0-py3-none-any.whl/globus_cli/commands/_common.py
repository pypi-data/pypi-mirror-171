from __future__ import annotations

import datetime
import sys
from typing import TYPE_CHECKING

import click

from globus_cli.termio import FORMAT_SILENT, formatted_print

if TYPE_CHECKING:
    from ..services.transfer import CustomTransferClient


def transfer_task_wait_with_io(
    transfer_client: CustomTransferClient,
    meow,
    heartbeat,
    polling_interval,
    timeout,
    task_id,
    timeout_exit_code,
) -> None:
    """
    Options are the core "task wait" options, including the `--meow` easter
    egg.

    This does the core "task wait" loop, including all of the IO.
    It *does exit* on behalf of the caller. (We can enhance with a
    `noabort=True` param or somesuch in the future if necessary.)
    """

    def timed_out(waited_time):
        if timeout is None:
            return False
        else:
            return waited_time >= timeout

    def check_completed():
        completed = transfer_client.task_wait(
            task_id, timeout=polling_interval, polling_interval=polling_interval
        )
        if completed:
            if heartbeat:
                click.echo("", err=True)
            # meowing tasks wake up!
            if meow:
                click.echo(
                    r"""
                  _..
  /}_{\           /.-'
 ( a a )-.___...-'/
 ==._.==         ;
      \ i _..._ /,
      {_;/   {_//""",
                    err=True,
                )

            # TODO: possibly update TransferClient.task_wait so that we don't
            # need to do an extra fetch to get the task status after completion
            res = transfer_client.get_task(task_id)
            formatted_print(res, text_format=FORMAT_SILENT)

            status = res["status"]
            if status == "SUCCEEDED":
                click.get_current_context().exit(0)
            else:
                click.get_current_context().exit(1)

        return completed

    # Tasks start out sleepy
    if meow:
        click.echo(
            r"""
   |\      _,,,---,,_
   /,`.-'`'    -.  ;-;;,_
  |,4-  ) )-,_..;\ (  `'-'
 '---''(_/--'  `-'\_)""",
            err=True,
        )

    waited_time = 0
    while not timed_out(waited_time) and not check_completed():
        if heartbeat:
            click.echo(".", err=True, nl=False)
            sys.stderr.flush()

        waited_time += polling_interval

    # add a trailing newline to heartbeats if we fail
    if heartbeat:
        click.echo("", err=True)

    exit_code = 1
    if timed_out(waited_time):
        click.echo(f"Task has yet to complete after {timeout} seconds", err=True)
        exit_code = timeout_exit_code

    # output json if requested, but nothing for text mode
    res = transfer_client.get_task(task_id)
    formatted_print(res, text_format=FORMAT_SILENT)

    click.get_current_context().exit(exit_code)


def isoformat_to_local(
    utc_str: str | None, localtz: datetime.tzinfo | None = None
) -> str | None:
    if not utc_str:
        return None
    # let this raise ValueError
    date = datetime.datetime.fromisoformat(utc_str)
    if date.tzinfo is None:
        return date.strftime("%Y-%m-%d %H:%M:%S")
    return date.astimezone(tz=localtz).strftime("%Y-%m-%d %H:%M:%S")
