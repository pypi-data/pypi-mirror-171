'''
# `vault_identity_group_member_entity_ids`

Refer to the Terraform Registory for docs: [`vault_identity_group_member_entity_ids`](https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids).
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


class IdentityGroupMemberEntityIds(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.identityGroupMemberEntityIds.IdentityGroupMemberEntityIds",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids vault_identity_group_member_entity_ids}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        group_id: builtins.str,
        exclusive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        member_entity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids vault_identity_group_member_entity_ids} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_id: ID of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#group_id IdentityGroupMemberEntityIds#group_id}
        :param exclusive: Should the resource manage member entity ids exclusively? Beware of race conditions when disabling exclusive management. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#exclusive IdentityGroupMemberEntityIds#exclusive}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#id IdentityGroupMemberEntityIds#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param member_entity_ids: Entity IDs to be assigned as group members. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#member_entity_ids IdentityGroupMemberEntityIds#member_entity_ids}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#namespace IdentityGroupMemberEntityIds#namespace}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IdentityGroupMemberEntityIds.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IdentityGroupMemberEntityIdsConfig(
            group_id=group_id,
            exclusive=exclusive,
            id=id,
            member_entity_ids=member_entity_ids,
            namespace=namespace,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetExclusive")
    def reset_exclusive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusive", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMemberEntityIds")
    def reset_member_entity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberEntityIds", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @builtins.property
    @jsii.member(jsii_name="exclusiveInput")
    def exclusive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "exclusiveInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="memberEntityIdsInput")
    def member_entity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "memberEntityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusive")
    def exclusive(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exclusive"))

    @exclusive.setter
    def exclusive(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityGroupMemberEntityIds, "exclusive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusive", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityGroupMemberEntityIds, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityGroupMemberEntityIds, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="memberEntityIds")
    def member_entity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "memberEntityIds"))

    @member_entity_ids.setter
    def member_entity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityGroupMemberEntityIds, "member_entity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberEntityIds", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityGroupMemberEntityIds, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.identityGroupMemberEntityIds.IdentityGroupMemberEntityIdsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_id": "groupId",
        "exclusive": "exclusive",
        "id": "id",
        "member_entity_ids": "memberEntityIds",
        "namespace": "namespace",
    },
)
class IdentityGroupMemberEntityIdsConfig(cdktf.TerraformMetaArguments):
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
        group_id: builtins.str,
        exclusive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        member_entity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group_id: ID of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#group_id IdentityGroupMemberEntityIds#group_id}
        :param exclusive: Should the resource manage member entity ids exclusively? Beware of race conditions when disabling exclusive management. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#exclusive IdentityGroupMemberEntityIds#exclusive}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#id IdentityGroupMemberEntityIds#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param member_entity_ids: Entity IDs to be assigned as group members. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#member_entity_ids IdentityGroupMemberEntityIds#member_entity_ids}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#namespace IdentityGroupMemberEntityIds#namespace}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(IdentityGroupMemberEntityIdsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument exclusive", value=exclusive, expected_type=type_hints["exclusive"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument member_entity_ids", value=member_entity_ids, expected_type=type_hints["member_entity_ids"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_id": group_id,
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
        if exclusive is not None:
            self._values["exclusive"] = exclusive
        if id is not None:
            self._values["id"] = id
        if member_entity_ids is not None:
            self._values["member_entity_ids"] = member_entity_ids
        if namespace is not None:
            self._values["namespace"] = namespace

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
    def group_id(self) -> builtins.str:
        '''ID of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#group_id IdentityGroupMemberEntityIds#group_id}
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the resource manage member entity ids  exclusively? Beware of race conditions when disabling exclusive management.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#exclusive IdentityGroupMemberEntityIds#exclusive}
        '''
        result = self._values.get("exclusive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#id IdentityGroupMemberEntityIds#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def member_entity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Entity IDs to be assigned as group members.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#member_entity_ids IdentityGroupMemberEntityIds#member_entity_ids}
        '''
        result = self._values.get("member_entity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_group_member_entity_ids#namespace IdentityGroupMemberEntityIds#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityGroupMemberEntityIdsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IdentityGroupMemberEntityIds",
    "IdentityGroupMemberEntityIdsConfig",
]

publication.publish()
