# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_partnercenter


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_bundle.custom#{}', client_factory=cf_partnercenter)

    with commands_loader.command_group('partnercenter marketplace bundle', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_command('verify', 'verify_bundle', supports_no_wait=True, table_transformer=None)
        g.custom_command('build', 'build_bundle', supports_no_wait=True, table_transformer=None)
        g.custom_command('delete', 'delete_bundle', confirmation=True, supports_no_wait=True)
        g.custom_show_command('show', 'get_bundle', table_transformer=None)
        g.custom_command('list', 'list_bundle', table_transformer=None)
