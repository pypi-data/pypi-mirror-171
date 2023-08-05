'''
# `vault_raft_autopilot`

Refer to the Terraform Registory for docs: [`vault_raft_autopilot`](https://www.terraform.io/docs/providers/vault/r/raft_autopilot).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class RaftAutopilot(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.raftAutopilot.RaftAutopilot",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot vault_raft_autopilot}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cleanup_dead_servers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dead_server_last_contact_threshold: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_contact_threshold: typing.Optional[builtins.str] = None,
        max_trailing_logs: typing.Optional[jsii.Number] = None,
        min_quorum: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        server_stabilization_time: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot vault_raft_autopilot} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cleanup_dead_servers: Specifies whether to remove dead server nodes periodically or when a new server joins. This requires that min-quorum is also set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#cleanup_dead_servers RaftAutopilot#cleanup_dead_servers}
        :param dead_server_last_contact_threshold: Limit the amount of time a server can go without leader contact before being considered failed. This only takes effect when cleanup_dead_servers is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#dead_server_last_contact_threshold RaftAutopilot#dead_server_last_contact_threshold}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#id RaftAutopilot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_contact_threshold: Limit the amount of time a server can go without leader contact before being considered unhealthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#last_contact_threshold RaftAutopilot#last_contact_threshold}
        :param max_trailing_logs: Maximum number of log entries in the Raft log that a server can be behind its leader before being considered unhealthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#max_trailing_logs RaftAutopilot#max_trailing_logs}
        :param min_quorum: Minimum number of servers allowed in a cluster before autopilot can prune dead servers. This should at least be 3. Applicable only for voting nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#min_quorum RaftAutopilot#min_quorum}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#namespace RaftAutopilot#namespace}
        :param server_stabilization_time: Minimum amount of time a server must be stable in the 'healthy' state before being added to the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#server_stabilization_time RaftAutopilot#server_stabilization_time}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RaftAutopilot.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RaftAutopilotConfig(
            cleanup_dead_servers=cleanup_dead_servers,
            dead_server_last_contact_threshold=dead_server_last_contact_threshold,
            id=id,
            last_contact_threshold=last_contact_threshold,
            max_trailing_logs=max_trailing_logs,
            min_quorum=min_quorum,
            namespace=namespace,
            server_stabilization_time=server_stabilization_time,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCleanupDeadServers")
    def reset_cleanup_dead_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCleanupDeadServers", []))

    @jsii.member(jsii_name="resetDeadServerLastContactThreshold")
    def reset_dead_server_last_contact_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadServerLastContactThreshold", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLastContactThreshold")
    def reset_last_contact_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastContactThreshold", []))

    @jsii.member(jsii_name="resetMaxTrailingLogs")
    def reset_max_trailing_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTrailingLogs", []))

    @jsii.member(jsii_name="resetMinQuorum")
    def reset_min_quorum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinQuorum", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetServerStabilizationTime")
    def reset_server_stabilization_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerStabilizationTime", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cleanupDeadServersInput")
    def cleanup_dead_servers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cleanupDeadServersInput"))

    @builtins.property
    @jsii.member(jsii_name="deadServerLastContactThresholdInput")
    def dead_server_last_contact_threshold_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deadServerLastContactThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lastContactThresholdInput")
    def last_contact_threshold_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastContactThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTrailingLogsInput")
    def max_trailing_logs_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTrailingLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="minQuorumInput")
    def min_quorum_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minQuorumInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="serverStabilizationTimeInput")
    def server_stabilization_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverStabilizationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="cleanupDeadServers")
    def cleanup_dead_servers(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cleanupDeadServers"))

    @cleanup_dead_servers.setter
    def cleanup_dead_servers(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "cleanup_dead_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cleanupDeadServers", value)

    @builtins.property
    @jsii.member(jsii_name="deadServerLastContactThreshold")
    def dead_server_last_contact_threshold(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deadServerLastContactThreshold"))

    @dead_server_last_contact_threshold.setter
    def dead_server_last_contact_threshold(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "dead_server_last_contact_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadServerLastContactThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lastContactThreshold")
    def last_contact_threshold(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastContactThreshold"))

    @last_contact_threshold.setter
    def last_contact_threshold(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "last_contact_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastContactThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="maxTrailingLogs")
    def max_trailing_logs(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTrailingLogs"))

    @max_trailing_logs.setter
    def max_trailing_logs(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "max_trailing_logs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTrailingLogs", value)

    @builtins.property
    @jsii.member(jsii_name="minQuorum")
    def min_quorum(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minQuorum"))

    @min_quorum.setter
    def min_quorum(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "min_quorum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minQuorum", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="serverStabilizationTime")
    def server_stabilization_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverStabilizationTime"))

    @server_stabilization_time.setter
    def server_stabilization_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RaftAutopilot, "server_stabilization_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverStabilizationTime", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.raftAutopilot.RaftAutopilotConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cleanup_dead_servers": "cleanupDeadServers",
        "dead_server_last_contact_threshold": "deadServerLastContactThreshold",
        "id": "id",
        "last_contact_threshold": "lastContactThreshold",
        "max_trailing_logs": "maxTrailingLogs",
        "min_quorum": "minQuorum",
        "namespace": "namespace",
        "server_stabilization_time": "serverStabilizationTime",
    },
)
class RaftAutopilotConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        cleanup_dead_servers: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dead_server_last_contact_threshold: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        last_contact_threshold: typing.Optional[builtins.str] = None,
        max_trailing_logs: typing.Optional[jsii.Number] = None,
        min_quorum: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        server_stabilization_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cleanup_dead_servers: Specifies whether to remove dead server nodes periodically or when a new server joins. This requires that min-quorum is also set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#cleanup_dead_servers RaftAutopilot#cleanup_dead_servers}
        :param dead_server_last_contact_threshold: Limit the amount of time a server can go without leader contact before being considered failed. This only takes effect when cleanup_dead_servers is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#dead_server_last_contact_threshold RaftAutopilot#dead_server_last_contact_threshold}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#id RaftAutopilot#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param last_contact_threshold: Limit the amount of time a server can go without leader contact before being considered unhealthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#last_contact_threshold RaftAutopilot#last_contact_threshold}
        :param max_trailing_logs: Maximum number of log entries in the Raft log that a server can be behind its leader before being considered unhealthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#max_trailing_logs RaftAutopilot#max_trailing_logs}
        :param min_quorum: Minimum number of servers allowed in a cluster before autopilot can prune dead servers. This should at least be 3. Applicable only for voting nodes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#min_quorum RaftAutopilot#min_quorum}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#namespace RaftAutopilot#namespace}
        :param server_stabilization_time: Minimum amount of time a server must be stable in the 'healthy' state before being added to the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#server_stabilization_time RaftAutopilot#server_stabilization_time}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RaftAutopilotConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cleanup_dead_servers", value=cleanup_dead_servers, expected_type=type_hints["cleanup_dead_servers"])
            check_type(argname="argument dead_server_last_contact_threshold", value=dead_server_last_contact_threshold, expected_type=type_hints["dead_server_last_contact_threshold"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument last_contact_threshold", value=last_contact_threshold, expected_type=type_hints["last_contact_threshold"])
            check_type(argname="argument max_trailing_logs", value=max_trailing_logs, expected_type=type_hints["max_trailing_logs"])
            check_type(argname="argument min_quorum", value=min_quorum, expected_type=type_hints["min_quorum"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument server_stabilization_time", value=server_stabilization_time, expected_type=type_hints["server_stabilization_time"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if cleanup_dead_servers is not None:
            self._values["cleanup_dead_servers"] = cleanup_dead_servers
        if dead_server_last_contact_threshold is not None:
            self._values["dead_server_last_contact_threshold"] = dead_server_last_contact_threshold
        if id is not None:
            self._values["id"] = id
        if last_contact_threshold is not None:
            self._values["last_contact_threshold"] = last_contact_threshold
        if max_trailing_logs is not None:
            self._values["max_trailing_logs"] = max_trailing_logs
        if min_quorum is not None:
            self._values["min_quorum"] = min_quorum
        if namespace is not None:
            self._values["namespace"] = namespace
        if server_stabilization_time is not None:
            self._values["server_stabilization_time"] = server_stabilization_time

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def cleanup_dead_servers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to remove dead server nodes periodically or when a new server joins.

        This requires that min-quorum is also set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#cleanup_dead_servers RaftAutopilot#cleanup_dead_servers}
        '''
        result = self._values.get("cleanup_dead_servers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dead_server_last_contact_threshold(self) -> typing.Optional[builtins.str]:
        '''Limit the amount of time a server can go without leader contact before being considered failed.

        This only takes effect when cleanup_dead_servers is set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#dead_server_last_contact_threshold RaftAutopilot#dead_server_last_contact_threshold}
        '''
        result = self._values.get("dead_server_last_contact_threshold")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#id RaftAutopilot#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_contact_threshold(self) -> typing.Optional[builtins.str]:
        '''Limit the amount of time a server can go without leader contact before being considered unhealthy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#last_contact_threshold RaftAutopilot#last_contact_threshold}
        '''
        result = self._values.get("last_contact_threshold")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_trailing_logs(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of log entries in the Raft log that a server can be behind its leader before being considered unhealthy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#max_trailing_logs RaftAutopilot#max_trailing_logs}
        '''
        result = self._values.get("max_trailing_logs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_quorum(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of servers allowed in a cluster before autopilot can prune dead servers.

        This should at least be 3. Applicable only for voting nodes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#min_quorum RaftAutopilot#min_quorum}
        '''
        result = self._values.get("min_quorum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#namespace RaftAutopilot#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_stabilization_time(self) -> typing.Optional[builtins.str]:
        '''Minimum amount of time a server must be stable in the 'healthy' state before being added to the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/raft_autopilot#server_stabilization_time RaftAutopilot#server_stabilization_time}
        '''
        result = self._values.get("server_stabilization_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RaftAutopilotConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RaftAutopilot",
    "RaftAutopilotConfig",
]

publication.publish()
