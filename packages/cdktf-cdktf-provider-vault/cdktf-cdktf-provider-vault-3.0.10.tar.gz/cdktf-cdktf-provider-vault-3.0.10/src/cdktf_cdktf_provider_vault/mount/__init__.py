'''
# `vault_mount`

Refer to the Terraform Registory for docs: [`vault_mount`](https://www.terraform.io/docs/providers/vault/r/mount).
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


class Mount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.mount.Mount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/mount vault_mount}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        path: builtins.str,
        type: builtins.str,
        allowed_managed_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_request_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_response_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        external_entropy_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        seal_wrap: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/mount vault_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param path: Where the secret backend will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#path Mount#path}
        :param type: Type of the backend, such as 'aws'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#type Mount#type}
        :param allowed_managed_keys: List of managed key registry entry names that the mount in question is allowed to access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#allowed_managed_keys Mount#allowed_managed_keys}
        :param audit_non_hmac_request_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the request data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#audit_non_hmac_request_keys Mount#audit_non_hmac_request_keys}
        :param audit_non_hmac_response_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the response data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#audit_non_hmac_response_keys Mount#audit_non_hmac_response_keys}
        :param default_lease_ttl_seconds: Default lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#default_lease_ttl_seconds Mount#default_lease_ttl_seconds}
        :param description: Human-friendly description of the mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#description Mount#description}
        :param external_entropy_access: Enable the secrets engine to access Vault's external entropy source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#external_entropy_access Mount#external_entropy_access}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#id Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Local mount flag that can be explicitly set to true to enforce local mount in HA environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#local Mount#local}
        :param max_lease_ttl_seconds: Maximum possible lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#max_lease_ttl_seconds Mount#max_lease_ttl_seconds}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#namespace Mount#namespace}
        :param options: Specifies mount type specific options that are passed to the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#options Mount#options}
        :param seal_wrap: Enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#seal_wrap Mount#seal_wrap}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Mount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MountConfig(
            path=path,
            type=type,
            allowed_managed_keys=allowed_managed_keys,
            audit_non_hmac_request_keys=audit_non_hmac_request_keys,
            audit_non_hmac_response_keys=audit_non_hmac_response_keys,
            default_lease_ttl_seconds=default_lease_ttl_seconds,
            description=description,
            external_entropy_access=external_entropy_access,
            id=id,
            local=local,
            max_lease_ttl_seconds=max_lease_ttl_seconds,
            namespace=namespace,
            options=options,
            seal_wrap=seal_wrap,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowedManagedKeys")
    def reset_allowed_managed_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedManagedKeys", []))

    @jsii.member(jsii_name="resetAuditNonHmacRequestKeys")
    def reset_audit_non_hmac_request_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditNonHmacRequestKeys", []))

    @jsii.member(jsii_name="resetAuditNonHmacResponseKeys")
    def reset_audit_non_hmac_response_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditNonHmacResponseKeys", []))

    @jsii.member(jsii_name="resetDefaultLeaseTtlSeconds")
    def reset_default_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalEntropyAccess")
    def reset_external_entropy_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalEntropyAccess", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetMaxLeaseTtlSeconds")
    def reset_max_lease_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLeaseTtlSeconds", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetSealWrap")
    def reset_seal_wrap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSealWrap", []))

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
    @jsii.member(jsii_name="allowedManagedKeysInput")
    def allowed_managed_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedManagedKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacRequestKeysInput")
    def audit_non_hmac_request_keys_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auditNonHmacRequestKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacResponseKeysInput")
    def audit_non_hmac_response_keys_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auditNonHmacResponseKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtlSecondsInput")
    def default_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalEntropyAccessInput")
    def external_entropy_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "externalEntropyAccessInput"))

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
    @jsii.member(jsii_name="maxLeaseTtlSecondsInput")
    def max_lease_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLeaseTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="sealWrapInput")
    def seal_wrap_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sealWrapInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedManagedKeys")
    def allowed_managed_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedManagedKeys"))

    @allowed_managed_keys.setter
    def allowed_managed_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "allowed_managed_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedManagedKeys", value)

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacRequestKeys")
    def audit_non_hmac_request_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "auditNonHmacRequestKeys"))

    @audit_non_hmac_request_keys.setter
    def audit_non_hmac_request_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "audit_non_hmac_request_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNonHmacRequestKeys", value)

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacResponseKeys")
    def audit_non_hmac_response_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "auditNonHmacResponseKeys"))

    @audit_non_hmac_response_keys.setter
    def audit_non_hmac_response_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "audit_non_hmac_response_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNonHmacResponseKeys", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtlSeconds")
    def default_lease_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultLeaseTtlSeconds"))

    @default_lease_ttl_seconds.setter
    def default_lease_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "default_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalEntropyAccess")
    def external_entropy_access(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "externalEntropyAccess"))

    @external_entropy_access.setter
    def external_entropy_access(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "external_entropy_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalEntropyAccess", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "local"))

    @local.setter
    def local(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "local").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "local", value)

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLeaseTtlSeconds"))

    @max_lease_ttl_seconds.setter
    def max_lease_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "max_lease_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLeaseTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="sealWrap")
    def seal_wrap(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sealWrap"))

    @seal_wrap.setter
    def seal_wrap(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "seal_wrap").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sealWrap", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.mount.MountConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "path": "path",
        "type": "type",
        "allowed_managed_keys": "allowedManagedKeys",
        "audit_non_hmac_request_keys": "auditNonHmacRequestKeys",
        "audit_non_hmac_response_keys": "auditNonHmacResponseKeys",
        "default_lease_ttl_seconds": "defaultLeaseTtlSeconds",
        "description": "description",
        "external_entropy_access": "externalEntropyAccess",
        "id": "id",
        "local": "local",
        "max_lease_ttl_seconds": "maxLeaseTtlSeconds",
        "namespace": "namespace",
        "options": "options",
        "seal_wrap": "sealWrap",
    },
)
class MountConfig(cdktf.TerraformMetaArguments):
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
        path: builtins.str,
        type: builtins.str,
        allowed_managed_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_request_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_response_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        external_entropy_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_lease_ttl_seconds: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        seal_wrap: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param path: Where the secret backend will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#path Mount#path}
        :param type: Type of the backend, such as 'aws'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#type Mount#type}
        :param allowed_managed_keys: List of managed key registry entry names that the mount in question is allowed to access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#allowed_managed_keys Mount#allowed_managed_keys}
        :param audit_non_hmac_request_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the request data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#audit_non_hmac_request_keys Mount#audit_non_hmac_request_keys}
        :param audit_non_hmac_response_keys: Specifies the list of keys that will not be HMAC'd by audit devices in the response data object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#audit_non_hmac_response_keys Mount#audit_non_hmac_response_keys}
        :param default_lease_ttl_seconds: Default lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#default_lease_ttl_seconds Mount#default_lease_ttl_seconds}
        :param description: Human-friendly description of the mount. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#description Mount#description}
        :param external_entropy_access: Enable the secrets engine to access Vault's external entropy source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#external_entropy_access Mount#external_entropy_access}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#id Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Local mount flag that can be explicitly set to true to enforce local mount in HA environment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#local Mount#local}
        :param max_lease_ttl_seconds: Maximum possible lease duration for tokens and secrets in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#max_lease_ttl_seconds Mount#max_lease_ttl_seconds}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#namespace Mount#namespace}
        :param options: Specifies mount type specific options that are passed to the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#options Mount#options}
        :param seal_wrap: Enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#seal_wrap Mount#seal_wrap}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(MountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument allowed_managed_keys", value=allowed_managed_keys, expected_type=type_hints["allowed_managed_keys"])
            check_type(argname="argument audit_non_hmac_request_keys", value=audit_non_hmac_request_keys, expected_type=type_hints["audit_non_hmac_request_keys"])
            check_type(argname="argument audit_non_hmac_response_keys", value=audit_non_hmac_response_keys, expected_type=type_hints["audit_non_hmac_response_keys"])
            check_type(argname="argument default_lease_ttl_seconds", value=default_lease_ttl_seconds, expected_type=type_hints["default_lease_ttl_seconds"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_entropy_access", value=external_entropy_access, expected_type=type_hints["external_entropy_access"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument max_lease_ttl_seconds", value=max_lease_ttl_seconds, expected_type=type_hints["max_lease_ttl_seconds"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument seal_wrap", value=seal_wrap, expected_type=type_hints["seal_wrap"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
            "type": type,
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
        if allowed_managed_keys is not None:
            self._values["allowed_managed_keys"] = allowed_managed_keys
        if audit_non_hmac_request_keys is not None:
            self._values["audit_non_hmac_request_keys"] = audit_non_hmac_request_keys
        if audit_non_hmac_response_keys is not None:
            self._values["audit_non_hmac_response_keys"] = audit_non_hmac_response_keys
        if default_lease_ttl_seconds is not None:
            self._values["default_lease_ttl_seconds"] = default_lease_ttl_seconds
        if description is not None:
            self._values["description"] = description
        if external_entropy_access is not None:
            self._values["external_entropy_access"] = external_entropy_access
        if id is not None:
            self._values["id"] = id
        if local is not None:
            self._values["local"] = local
        if max_lease_ttl_seconds is not None:
            self._values["max_lease_ttl_seconds"] = max_lease_ttl_seconds
        if namespace is not None:
            self._values["namespace"] = namespace
        if options is not None:
            self._values["options"] = options
        if seal_wrap is not None:
            self._values["seal_wrap"] = seal_wrap

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
    def path(self) -> builtins.str:
        '''Where the secret backend will be mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#path Mount#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the backend, such as 'aws'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#type Mount#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_managed_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of managed key registry entry names that the mount in question is allowed to access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#allowed_managed_keys Mount#allowed_managed_keys}
        '''
        result = self._values.get("allowed_managed_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_non_hmac_request_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of keys that will not be HMAC'd by audit devices in the request data object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#audit_non_hmac_request_keys Mount#audit_non_hmac_request_keys}
        '''
        result = self._values.get("audit_non_hmac_request_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_non_hmac_response_keys(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the list of keys that will not be HMAC'd by audit devices in the response data object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#audit_non_hmac_response_keys Mount#audit_non_hmac_response_keys}
        '''
        result = self._values.get("audit_non_hmac_response_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Default lease duration for tokens and secrets in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#default_lease_ttl_seconds Mount#default_lease_ttl_seconds}
        '''
        result = self._values.get("default_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-friendly description of the mount.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#description Mount#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_entropy_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the secrets engine to access Vault's external entropy source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#external_entropy_access Mount#external_entropy_access}
        '''
        result = self._values.get("external_entropy_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#id Mount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Local mount flag that can be explicitly set to true to enforce local mount in HA environment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#local Mount#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_lease_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum possible lease duration for tokens and secrets in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#max_lease_ttl_seconds Mount#max_lease_ttl_seconds}
        '''
        result = self._values.get("max_lease_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#namespace Mount#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies mount type specific options that are passed to the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#options Mount#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def seal_wrap(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable seal wrapping for the mount, causing values stored by the mount to be wrapped by the seal's encryption capability.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/mount#seal_wrap Mount#seal_wrap}
        '''
        result = self._values.get("seal_wrap")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Mount",
    "MountConfig",
]

publication.publish()
