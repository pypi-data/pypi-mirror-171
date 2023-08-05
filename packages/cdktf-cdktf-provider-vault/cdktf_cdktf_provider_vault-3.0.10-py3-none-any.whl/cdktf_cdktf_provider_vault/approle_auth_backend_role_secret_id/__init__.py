'''
# `vault_approle_auth_backend_role_secret_id`

Refer to the Terraform Registory for docs: [`vault_approle_auth_backend_role_secret_id`](https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id).
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


class ApproleAuthBackendRoleSecretId(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.approleAuthBackendRoleSecretId.ApproleAuthBackendRoleSecretId",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id vault_approle_auth_backend_role_secret_id}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        role_name: builtins.str,
        backend: typing.Optional[builtins.str] = None,
        cidr_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        with_wrapped_accessor: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        wrapping_ttl: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id vault_approle_auth_backend_role_secret_id} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param role_name: Name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#role_name ApproleAuthBackendRoleSecretId#role_name}
        :param backend: Unique name of the auth backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#backend ApproleAuthBackendRoleSecretId#backend}
        :param cidr_list: List of CIDR blocks that can log in using the SecretID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#cidr_list ApproleAuthBackendRoleSecretId#cidr_list}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#id ApproleAuthBackendRoleSecretId#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: JSON-encoded secret data to write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#metadata ApproleAuthBackendRoleSecretId#metadata}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#namespace ApproleAuthBackendRoleSecretId#namespace}
        :param secret_id: The SecretID to be managed. If not specified, Vault auto-generates one. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#secret_id ApproleAuthBackendRoleSecretId#secret_id}
        :param with_wrapped_accessor: Use the wrapped secret-id accessor as the id of this resource. If false, a fresh secret-id will be regenerated whenever the wrapping token is expired or invalidated through unwrapping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#with_wrapped_accessor ApproleAuthBackendRoleSecretId#with_wrapped_accessor}
        :param wrapping_ttl: The TTL duration of the wrapped SecretID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#wrapping_ttl ApproleAuthBackendRoleSecretId#wrapping_ttl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApproleAuthBackendRoleSecretId.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApproleAuthBackendRoleSecretIdConfig(
            role_name=role_name,
            backend=backend,
            cidr_list=cidr_list,
            id=id,
            metadata=metadata,
            namespace=namespace,
            secret_id=secret_id,
            with_wrapped_accessor=with_wrapped_accessor,
            wrapping_ttl=wrapping_ttl,
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

    @jsii.member(jsii_name="resetCidrList")
    def reset_cidr_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrList", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetSecretId")
    def reset_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretId", []))

    @jsii.member(jsii_name="resetWithWrappedAccessor")
    def reset_with_wrapped_accessor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithWrappedAccessor", []))

    @jsii.member(jsii_name="resetWrappingTtl")
    def reset_wrapping_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWrappingTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessor")
    def accessor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessor"))

    @builtins.property
    @jsii.member(jsii_name="wrappingAccessor")
    def wrapping_accessor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wrappingAccessor"))

    @builtins.property
    @jsii.member(jsii_name="wrappingToken")
    def wrapping_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wrappingToken"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrListInput")
    def cidr_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrListInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="withWrappedAccessorInput")
    def with_wrapped_accessor_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withWrappedAccessorInput"))

    @builtins.property
    @jsii.member(jsii_name="wrappingTtlInput")
    def wrapping_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wrappingTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="cidrList")
    def cidr_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cidrList"))

    @cidr_list.setter
    def cidr_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "cidr_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrList", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretId", value)

    @builtins.property
    @jsii.member(jsii_name="withWrappedAccessor")
    def with_wrapped_accessor(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withWrappedAccessor"))

    @with_wrapped_accessor.setter
    def with_wrapped_accessor(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "with_wrapped_accessor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withWrappedAccessor", value)

    @builtins.property
    @jsii.member(jsii_name="wrappingTtl")
    def wrapping_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wrappingTtl"))

    @wrapping_ttl.setter
    def wrapping_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApproleAuthBackendRoleSecretId, "wrapping_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrappingTtl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.approleAuthBackendRoleSecretId.ApproleAuthBackendRoleSecretIdConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "role_name": "roleName",
        "backend": "backend",
        "cidr_list": "cidrList",
        "id": "id",
        "metadata": "metadata",
        "namespace": "namespace",
        "secret_id": "secretId",
        "with_wrapped_accessor": "withWrappedAccessor",
        "wrapping_ttl": "wrappingTtl",
    },
)
class ApproleAuthBackendRoleSecretIdConfig(cdktf.TerraformMetaArguments):
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
        role_name: builtins.str,
        backend: typing.Optional[builtins.str] = None,
        cidr_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        secret_id: typing.Optional[builtins.str] = None,
        with_wrapped_accessor: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        wrapping_ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param role_name: Name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#role_name ApproleAuthBackendRoleSecretId#role_name}
        :param backend: Unique name of the auth backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#backend ApproleAuthBackendRoleSecretId#backend}
        :param cidr_list: List of CIDR blocks that can log in using the SecretID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#cidr_list ApproleAuthBackendRoleSecretId#cidr_list}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#id ApproleAuthBackendRoleSecretId#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: JSON-encoded secret data to write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#metadata ApproleAuthBackendRoleSecretId#metadata}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#namespace ApproleAuthBackendRoleSecretId#namespace}
        :param secret_id: The SecretID to be managed. If not specified, Vault auto-generates one. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#secret_id ApproleAuthBackendRoleSecretId#secret_id}
        :param with_wrapped_accessor: Use the wrapped secret-id accessor as the id of this resource. If false, a fresh secret-id will be regenerated whenever the wrapping token is expired or invalidated through unwrapping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#with_wrapped_accessor ApproleAuthBackendRoleSecretId#with_wrapped_accessor}
        :param wrapping_ttl: The TTL duration of the wrapped SecretID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#wrapping_ttl ApproleAuthBackendRoleSecretId#wrapping_ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ApproleAuthBackendRoleSecretIdConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument cidr_list", value=cidr_list, expected_type=type_hints["cidr_list"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            check_type(argname="argument with_wrapped_accessor", value=with_wrapped_accessor, expected_type=type_hints["with_wrapped_accessor"])
            check_type(argname="argument wrapping_ttl", value=wrapping_ttl, expected_type=type_hints["wrapping_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "role_name": role_name,
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
        if cidr_list is not None:
            self._values["cidr_list"] = cidr_list
        if id is not None:
            self._values["id"] = id
        if metadata is not None:
            self._values["metadata"] = metadata
        if namespace is not None:
            self._values["namespace"] = namespace
        if secret_id is not None:
            self._values["secret_id"] = secret_id
        if with_wrapped_accessor is not None:
            self._values["with_wrapped_accessor"] = with_wrapped_accessor
        if wrapping_ttl is not None:
            self._values["wrapping_ttl"] = wrapping_ttl

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
    def role_name(self) -> builtins.str:
        '''Name of the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#role_name ApproleAuthBackendRoleSecretId#role_name}
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backend(self) -> typing.Optional[builtins.str]:
        '''Unique name of the auth backend to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#backend ApproleAuthBackendRoleSecretId#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cidr_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of CIDR blocks that can log in using the SecretID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#cidr_list ApproleAuthBackendRoleSecretId#cidr_list}
        '''
        result = self._values.get("cidr_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#id ApproleAuthBackendRoleSecretId#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        '''JSON-encoded secret data to write.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#metadata ApproleAuthBackendRoleSecretId#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#namespace ApproleAuthBackendRoleSecretId#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_id(self) -> typing.Optional[builtins.str]:
        '''The SecretID to be managed. If not specified, Vault auto-generates one.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#secret_id ApproleAuthBackendRoleSecretId#secret_id}
        '''
        result = self._values.get("secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def with_wrapped_accessor(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use the wrapped secret-id accessor as the id of this resource.

        If false, a fresh secret-id will be regenerated whenever the wrapping token is expired or invalidated through unwrapping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#with_wrapped_accessor ApproleAuthBackendRoleSecretId#with_wrapped_accessor}
        '''
        result = self._values.get("with_wrapped_accessor")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def wrapping_ttl(self) -> typing.Optional[builtins.str]:
        '''The TTL duration of the wrapped SecretID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id#wrapping_ttl ApproleAuthBackendRoleSecretId#wrapping_ttl}
        '''
        result = self._values.get("wrapping_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApproleAuthBackendRoleSecretIdConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApproleAuthBackendRoleSecretId",
    "ApproleAuthBackendRoleSecretIdConfig",
]

publication.publish()
