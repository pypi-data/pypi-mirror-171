'''
# `vault_consul_secret_backend_role`

Refer to the Terraform Registory for docs: [`vault_consul_secret_backend_role`](https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role).
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


class ConsulSecretBackendRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.consulSecretBackendRole.ConsulSecretBackendRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role vault_consul_secret_backend_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        backend: typing.Optional[builtins.str] = None,
        consul_namespace: typing.Optional[builtins.str] = None,
        consul_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        consul_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        partition: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_type: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role vault_consul_secret_backend_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of an existing role against which to create this Consul credential. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#name ConsulSecretBackendRole#name}
        :param backend: The path of the Consul Secret Backend the role belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#backend ConsulSecretBackendRole#backend}
        :param consul_namespace: The Consul namespace that the token will be created in. Applicable for Vault 1.10+ and Consul 1.7+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_namespace ConsulSecretBackendRole#consul_namespace}
        :param consul_policies: List of Consul policies to associate with this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_policies ConsulSecretBackendRole#consul_policies}
        :param consul_roles: Set of Consul roles to attach to the token. Applicable for Vault 1.10+ with Consul 1.5+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_roles ConsulSecretBackendRole#consul_roles}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#id ConsulSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Indicates that the token should not be replicated globally and instead be local to the current datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#local ConsulSecretBackendRole#local}
        :param max_ttl: Maximum TTL for leases associated with this role, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#max_ttl ConsulSecretBackendRole#max_ttl}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#namespace ConsulSecretBackendRole#namespace}
        :param node_identities: Set of Consul node identities to attach to the token. Applicable for Vault 1.11+ with Consul 1.8+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#node_identities ConsulSecretBackendRole#node_identities}
        :param partition: The Consul admin partition that the token will be created in. Applicable for Vault 1.10+ and Consul 1.11+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#partition ConsulSecretBackendRole#partition}
        :param policies: List of Consul policies to associate with this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#policies ConsulSecretBackendRole#policies}
        :param service_identities: Set of Consul service identities to attach to the token. Applicable for Vault 1.11+ with Consul 1.5+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#service_identities ConsulSecretBackendRole#service_identities}
        :param token_type: Specifies the type of token to create when using this role. Valid values are "client" or "management". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#token_type ConsulSecretBackendRole#token_type}
        :param ttl: Specifies the TTL for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#ttl ConsulSecretBackendRole#ttl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulSecretBackendRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConsulSecretBackendRoleConfig(
            name=name,
            backend=backend,
            consul_namespace=consul_namespace,
            consul_policies=consul_policies,
            consul_roles=consul_roles,
            id=id,
            local=local,
            max_ttl=max_ttl,
            namespace=namespace,
            node_identities=node_identities,
            partition=partition,
            policies=policies,
            service_identities=service_identities,
            token_type=token_type,
            ttl=ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetConsulNamespace")
    def reset_consul_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulNamespace", []))

    @jsii.member(jsii_name="resetConsulPolicies")
    def reset_consul_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulPolicies", []))

    @jsii.member(jsii_name="resetConsulRoles")
    def reset_consul_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsulRoles", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetNodeIdentities")
    def reset_node_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeIdentities", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @jsii.member(jsii_name="resetServiceIdentities")
    def reset_service_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceIdentities", []))

    @jsii.member(jsii_name="resetTokenType")
    def reset_token_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenType", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="consulNamespaceInput")
    def consul_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "consulNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="consulPoliciesInput")
    def consul_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "consulPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="consulRolesInput")
    def consul_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "consulRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeIdentitiesInput")
    def node_identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodeIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceIdentitiesInput")
    def service_identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serviceIdentitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="consulNamespace")
    def consul_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consulNamespace"))

    @consul_namespace.setter
    def consul_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "consul_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="consulPolicies")
    def consul_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "consulPolicies"))

    @consul_policies.setter
    def consul_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "consul_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="consulRoles")
    def consul_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "consulRoles"))

    @consul_roles.setter
    def consul_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "consul_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consulRoles", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "local"))

    @local.setter
    def local(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "local").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "local", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="nodeIdentities")
    def node_identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nodeIdentities"))

    @node_identities.setter
    def node_identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "node_identities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeIdentities", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="serviceIdentities")
    def service_identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "serviceIdentities"))

    @service_identities.setter
    def service_identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "service_identities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIdentities", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulSecretBackendRole, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.consulSecretBackendRole.ConsulSecretBackendRoleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "backend": "backend",
        "consul_namespace": "consulNamespace",
        "consul_policies": "consulPolicies",
        "consul_roles": "consulRoles",
        "id": "id",
        "local": "local",
        "max_ttl": "maxTtl",
        "namespace": "namespace",
        "node_identities": "nodeIdentities",
        "partition": "partition",
        "policies": "policies",
        "service_identities": "serviceIdentities",
        "token_type": "tokenType",
        "ttl": "ttl",
    },
)
class ConsulSecretBackendRoleConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        backend: typing.Optional[builtins.str] = None,
        consul_namespace: typing.Optional[builtins.str] = None,
        consul_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        consul_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        partition: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_type: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of an existing role against which to create this Consul credential. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#name ConsulSecretBackendRole#name}
        :param backend: The path of the Consul Secret Backend the role belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#backend ConsulSecretBackendRole#backend}
        :param consul_namespace: The Consul namespace that the token will be created in. Applicable for Vault 1.10+ and Consul 1.7+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_namespace ConsulSecretBackendRole#consul_namespace}
        :param consul_policies: List of Consul policies to associate with this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_policies ConsulSecretBackendRole#consul_policies}
        :param consul_roles: Set of Consul roles to attach to the token. Applicable for Vault 1.10+ with Consul 1.5+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_roles ConsulSecretBackendRole#consul_roles}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#id ConsulSecretBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Indicates that the token should not be replicated globally and instead be local to the current datacenter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#local ConsulSecretBackendRole#local}
        :param max_ttl: Maximum TTL for leases associated with this role, in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#max_ttl ConsulSecretBackendRole#max_ttl}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#namespace ConsulSecretBackendRole#namespace}
        :param node_identities: Set of Consul node identities to attach to the token. Applicable for Vault 1.11+ with Consul 1.8+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#node_identities ConsulSecretBackendRole#node_identities}
        :param partition: The Consul admin partition that the token will be created in. Applicable for Vault 1.10+ and Consul 1.11+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#partition ConsulSecretBackendRole#partition}
        :param policies: List of Consul policies to associate with this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#policies ConsulSecretBackendRole#policies}
        :param service_identities: Set of Consul service identities to attach to the token. Applicable for Vault 1.11+ with Consul 1.5+. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#service_identities ConsulSecretBackendRole#service_identities}
        :param token_type: Specifies the type of token to create when using this role. Valid values are "client" or "management". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#token_type ConsulSecretBackendRole#token_type}
        :param ttl: Specifies the TTL for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#ttl ConsulSecretBackendRole#ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ConsulSecretBackendRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument consul_namespace", value=consul_namespace, expected_type=type_hints["consul_namespace"])
            check_type(argname="argument consul_policies", value=consul_policies, expected_type=type_hints["consul_policies"])
            check_type(argname="argument consul_roles", value=consul_roles, expected_type=type_hints["consul_roles"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument node_identities", value=node_identities, expected_type=type_hints["node_identities"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument service_identities", value=service_identities, expected_type=type_hints["service_identities"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
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
        if backend is not None:
            self._values["backend"] = backend
        if consul_namespace is not None:
            self._values["consul_namespace"] = consul_namespace
        if consul_policies is not None:
            self._values["consul_policies"] = consul_policies
        if consul_roles is not None:
            self._values["consul_roles"] = consul_roles
        if id is not None:
            self._values["id"] = id
        if local is not None:
            self._values["local"] = local
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if namespace is not None:
            self._values["namespace"] = namespace
        if node_identities is not None:
            self._values["node_identities"] = node_identities
        if partition is not None:
            self._values["partition"] = partition
        if policies is not None:
            self._values["policies"] = policies
        if service_identities is not None:
            self._values["service_identities"] = service_identities
        if token_type is not None:
            self._values["token_type"] = token_type
        if ttl is not None:
            self._values["ttl"] = ttl

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
    def name(self) -> builtins.str:
        '''The name of an existing role against which to create this Consul credential.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#name ConsulSecretBackendRole#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backend(self) -> typing.Optional[builtins.str]:
        '''The path of the Consul Secret Backend the role belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#backend ConsulSecretBackendRole#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consul_namespace(self) -> typing.Optional[builtins.str]:
        '''The Consul namespace that the token will be created in. Applicable for Vault 1.10+ and Consul 1.7+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_namespace ConsulSecretBackendRole#consul_namespace}
        '''
        result = self._values.get("consul_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consul_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Consul policies to associate with this role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_policies ConsulSecretBackendRole#consul_policies}
        '''
        result = self._values.get("consul_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def consul_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of Consul roles to attach to the token. Applicable for Vault 1.10+ with Consul 1.5+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#consul_roles ConsulSecretBackendRole#consul_roles}
        '''
        result = self._values.get("consul_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#id ConsulSecretBackendRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates that the token should not be replicated globally and instead be local to the current datacenter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#local ConsulSecretBackendRole#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Maximum TTL for leases associated with this role, in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#max_ttl ConsulSecretBackendRole#max_ttl}
        '''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#namespace ConsulSecretBackendRole#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of Consul node identities to attach to the token. Applicable for Vault 1.11+ with Consul 1.8+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#node_identities ConsulSecretBackendRole#node_identities}
        '''
        result = self._values.get("node_identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''The Consul admin partition that the token will be created in. Applicable for Vault 1.10+ and Consul 1.11+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#partition ConsulSecretBackendRole#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of Consul policies to associate with this role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#policies ConsulSecretBackendRole#policies}
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of Consul service identities to attach to the token. Applicable for Vault 1.11+ with Consul 1.5+.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#service_identities ConsulSecretBackendRole#service_identities}
        '''
        result = self._values.get("service_identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of token to create when using this role. Valid values are "client" or "management".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#token_type ConsulSecretBackendRole#token_type}
        '''
        result = self._values.get("token_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the TTL for this role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/consul_secret_backend_role#ttl ConsulSecretBackendRole#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsulSecretBackendRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConsulSecretBackendRole",
    "ConsulSecretBackendRoleConfig",
]

publication.publish()
