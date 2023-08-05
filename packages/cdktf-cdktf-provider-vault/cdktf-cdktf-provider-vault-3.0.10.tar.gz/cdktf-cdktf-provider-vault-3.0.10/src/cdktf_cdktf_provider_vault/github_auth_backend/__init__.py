'''
# `vault_github_auth_backend`

Refer to the Terraform Registory for docs: [`vault_github_auth_backend`](https://www.terraform.io/docs/providers/vault/r/github_auth_backend).
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


class GithubAuthBackend(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.githubAuthBackend.GithubAuthBackend",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend vault_github_auth_backend}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        organization: builtins.str,
        base_url: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        organization_id: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        token_bound_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_explicit_max_ttl: typing.Optional[jsii.Number] = None,
        token_max_ttl: typing.Optional[jsii.Number] = None,
        token_no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_num_uses: typing.Optional[jsii.Number] = None,
        token_period: typing.Optional[jsii.Number] = None,
        token_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_ttl: typing.Optional[jsii.Number] = None,
        token_type: typing.Optional[builtins.str] = None,
        tune: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GithubAuthBackendTune", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend vault_github_auth_backend} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param organization: The organization users must be part of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#organization GithubAuthBackend#organization}
        :param base_url: The API endpoint to use. Useful if you are running GitHub Enterprise or an API-compatible authentication server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#base_url GithubAuthBackend#base_url}
        :param description: Specifies the description of the mount. This overrides the current stored value, if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#description GithubAuthBackend#description}
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#disable_remount GithubAuthBackend#disable_remount}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#id GithubAuthBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#namespace GithubAuthBackend#namespace}
        :param organization_id: The ID of the organization users must be part of. Vault will attempt to fetch and set this value if it is not provided (vault-1.10+) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#organization_id GithubAuthBackend#organization_id}
        :param path: Path where the auth backend is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#path GithubAuthBackend#path}
        :param token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_bound_cidrs GithubAuthBackend#token_bound_cidrs}
        :param token_explicit_max_ttl: Generated Token's Explicit Maximum TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_explicit_max_ttl GithubAuthBackend#token_explicit_max_ttl}
        :param token_max_ttl: The maximum lifetime of the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_max_ttl GithubAuthBackend#token_max_ttl}
        :param token_no_default_policy: If true, the 'default' policy will not automatically be added to generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_no_default_policy GithubAuthBackend#token_no_default_policy}
        :param token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_num_uses GithubAuthBackend#token_num_uses}
        :param token_period: Generated Token's Period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_period GithubAuthBackend#token_period}
        :param token_policies: Generated Token's Policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_policies GithubAuthBackend#token_policies}
        :param token_ttl: The initial ttl of the token to generate in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_ttl GithubAuthBackend#token_ttl}
        :param token_type: The type of token to generate, service or batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_type GithubAuthBackend#token_type}
        :param tune: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#tune GithubAuthBackend#tune}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackend.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GithubAuthBackendConfig(
            organization=organization,
            base_url=base_url,
            description=description,
            disable_remount=disable_remount,
            id=id,
            namespace=namespace,
            organization_id=organization_id,
            path=path,
            token_bound_cidrs=token_bound_cidrs,
            token_explicit_max_ttl=token_explicit_max_ttl,
            token_max_ttl=token_max_ttl,
            token_no_default_policy=token_no_default_policy,
            token_num_uses=token_num_uses,
            token_period=token_period,
            token_policies=token_policies,
            token_ttl=token_ttl,
            token_type=token_type,
            tune=tune,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTune")
    def put_tune(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GithubAuthBackendTune", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackend.put_tune)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTune", [value]))

    @jsii.member(jsii_name="resetBaseUrl")
    def reset_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseUrl", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableRemount")
    def reset_disable_remount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRemount", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetOrganizationId")
    def reset_organization_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetTokenBoundCidrs")
    def reset_token_bound_cidrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenBoundCidrs", []))

    @jsii.member(jsii_name="resetTokenExplicitMaxTtl")
    def reset_token_explicit_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenExplicitMaxTtl", []))

    @jsii.member(jsii_name="resetTokenMaxTtl")
    def reset_token_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenMaxTtl", []))

    @jsii.member(jsii_name="resetTokenNoDefaultPolicy")
    def reset_token_no_default_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNoDefaultPolicy", []))

    @jsii.member(jsii_name="resetTokenNumUses")
    def reset_token_num_uses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNumUses", []))

    @jsii.member(jsii_name="resetTokenPeriod")
    def reset_token_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenPeriod", []))

    @jsii.member(jsii_name="resetTokenPolicies")
    def reset_token_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenPolicies", []))

    @jsii.member(jsii_name="resetTokenTtl")
    def reset_token_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenTtl", []))

    @jsii.member(jsii_name="resetTokenType")
    def reset_token_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenType", []))

    @jsii.member(jsii_name="resetTune")
    def reset_tune(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTune", []))

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
    @jsii.member(jsii_name="tune")
    def tune(self) -> "GithubAuthBackendTuneList":
        return typing.cast("GithubAuthBackendTuneList", jsii.get(self, "tune"))

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRemountInput")
    def disable_remount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableRemountInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationIdInput")
    def organization_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "organizationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenBoundCidrsInput")
    def token_bound_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenBoundCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenExplicitMaxTtlInput")
    def token_explicit_max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenExplicitMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenMaxTtlInput")
    def token_max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNoDefaultPolicyInput")
    def token_no_default_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tokenNoDefaultPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNumUsesInput")
    def token_num_uses_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenNumUsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenPeriodInput")
    def token_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenPoliciesInput")
    def token_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTtlInput")
    def token_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tuneInput")
    def tune_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GithubAuthBackendTune"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GithubAuthBackendTune"]]], jsii.get(self, "tuneInput"))

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "base_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableRemount")
    def disable_remount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRemount"))

    @disable_remount.setter
    def disable_remount(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "disable_remount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRemount", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationId")
    def organization_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "organizationId"))

    @organization_id.setter
    def organization_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "organization_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationId", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="tokenBoundCidrs")
    def token_bound_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenBoundCidrs"))

    @token_bound_cidrs.setter
    def token_bound_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_bound_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenBoundCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="tokenExplicitMaxTtl")
    def token_explicit_max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenExplicitMaxTtl"))

    @token_explicit_max_ttl.setter
    def token_explicit_max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_explicit_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenExplicitMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenMaxTtl")
    def token_max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenMaxTtl"))

    @token_max_ttl.setter
    def token_max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNoDefaultPolicy")
    def token_no_default_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tokenNoDefaultPolicy"))

    @token_no_default_policy.setter
    def token_no_default_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_no_default_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNoDefaultPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNumUses")
    def token_num_uses(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenNumUses"))

    @token_num_uses.setter
    def token_num_uses(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_num_uses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNumUses", value)

    @builtins.property
    @jsii.member(jsii_name="tokenPeriod")
    def token_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenPeriod"))

    @token_period.setter
    def token_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tokenPolicies")
    def token_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenPolicies"))

    @token_policies.setter
    def token_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="tokenTtl")
    def token_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenTtl"))

    @token_ttl.setter
    def token_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackend, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.githubAuthBackend.GithubAuthBackendConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "organization": "organization",
        "base_url": "baseUrl",
        "description": "description",
        "disable_remount": "disableRemount",
        "id": "id",
        "namespace": "namespace",
        "organization_id": "organizationId",
        "path": "path",
        "token_bound_cidrs": "tokenBoundCidrs",
        "token_explicit_max_ttl": "tokenExplicitMaxTtl",
        "token_max_ttl": "tokenMaxTtl",
        "token_no_default_policy": "tokenNoDefaultPolicy",
        "token_num_uses": "tokenNumUses",
        "token_period": "tokenPeriod",
        "token_policies": "tokenPolicies",
        "token_ttl": "tokenTtl",
        "token_type": "tokenType",
        "tune": "tune",
    },
)
class GithubAuthBackendConfig(cdktf.TerraformMetaArguments):
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
        organization: builtins.str,
        base_url: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        organization_id: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        token_bound_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_explicit_max_ttl: typing.Optional[jsii.Number] = None,
        token_max_ttl: typing.Optional[jsii.Number] = None,
        token_no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_num_uses: typing.Optional[jsii.Number] = None,
        token_period: typing.Optional[jsii.Number] = None,
        token_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_ttl: typing.Optional[jsii.Number] = None,
        token_type: typing.Optional[builtins.str] = None,
        tune: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GithubAuthBackendTune", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param organization: The organization users must be part of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#organization GithubAuthBackend#organization}
        :param base_url: The API endpoint to use. Useful if you are running GitHub Enterprise or an API-compatible authentication server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#base_url GithubAuthBackend#base_url}
        :param description: Specifies the description of the mount. This overrides the current stored value, if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#description GithubAuthBackend#description}
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#disable_remount GithubAuthBackend#disable_remount}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#id GithubAuthBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#namespace GithubAuthBackend#namespace}
        :param organization_id: The ID of the organization users must be part of. Vault will attempt to fetch and set this value if it is not provided (vault-1.10+) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#organization_id GithubAuthBackend#organization_id}
        :param path: Path where the auth backend is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#path GithubAuthBackend#path}
        :param token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_bound_cidrs GithubAuthBackend#token_bound_cidrs}
        :param token_explicit_max_ttl: Generated Token's Explicit Maximum TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_explicit_max_ttl GithubAuthBackend#token_explicit_max_ttl}
        :param token_max_ttl: The maximum lifetime of the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_max_ttl GithubAuthBackend#token_max_ttl}
        :param token_no_default_policy: If true, the 'default' policy will not automatically be added to generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_no_default_policy GithubAuthBackend#token_no_default_policy}
        :param token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_num_uses GithubAuthBackend#token_num_uses}
        :param token_period: Generated Token's Period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_period GithubAuthBackend#token_period}
        :param token_policies: Generated Token's Policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_policies GithubAuthBackend#token_policies}
        :param token_ttl: The initial ttl of the token to generate in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_ttl GithubAuthBackend#token_ttl}
        :param token_type: The type of token to generate, service or batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_type GithubAuthBackend#token_type}
        :param tune: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#tune GithubAuthBackend#tune}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackendConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_remount", value=disable_remount, expected_type=type_hints["disable_remount"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument organization_id", value=organization_id, expected_type=type_hints["organization_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument token_bound_cidrs", value=token_bound_cidrs, expected_type=type_hints["token_bound_cidrs"])
            check_type(argname="argument token_explicit_max_ttl", value=token_explicit_max_ttl, expected_type=type_hints["token_explicit_max_ttl"])
            check_type(argname="argument token_max_ttl", value=token_max_ttl, expected_type=type_hints["token_max_ttl"])
            check_type(argname="argument token_no_default_policy", value=token_no_default_policy, expected_type=type_hints["token_no_default_policy"])
            check_type(argname="argument token_num_uses", value=token_num_uses, expected_type=type_hints["token_num_uses"])
            check_type(argname="argument token_period", value=token_period, expected_type=type_hints["token_period"])
            check_type(argname="argument token_policies", value=token_policies, expected_type=type_hints["token_policies"])
            check_type(argname="argument token_ttl", value=token_ttl, expected_type=type_hints["token_ttl"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
            check_type(argname="argument tune", value=tune, expected_type=type_hints["tune"])
        self._values: typing.Dict[str, typing.Any] = {
            "organization": organization,
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
        if base_url is not None:
            self._values["base_url"] = base_url
        if description is not None:
            self._values["description"] = description
        if disable_remount is not None:
            self._values["disable_remount"] = disable_remount
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if organization_id is not None:
            self._values["organization_id"] = organization_id
        if path is not None:
            self._values["path"] = path
        if token_bound_cidrs is not None:
            self._values["token_bound_cidrs"] = token_bound_cidrs
        if token_explicit_max_ttl is not None:
            self._values["token_explicit_max_ttl"] = token_explicit_max_ttl
        if token_max_ttl is not None:
            self._values["token_max_ttl"] = token_max_ttl
        if token_no_default_policy is not None:
            self._values["token_no_default_policy"] = token_no_default_policy
        if token_num_uses is not None:
            self._values["token_num_uses"] = token_num_uses
        if token_period is not None:
            self._values["token_period"] = token_period
        if token_policies is not None:
            self._values["token_policies"] = token_policies
        if token_ttl is not None:
            self._values["token_ttl"] = token_ttl
        if token_type is not None:
            self._values["token_type"] = token_type
        if tune is not None:
            self._values["tune"] = tune

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
    def organization(self) -> builtins.str:
        '''The organization users must be part of.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#organization GithubAuthBackend#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_url(self) -> typing.Optional[builtins.str]:
        '''The API endpoint to use. Useful if you are running GitHub Enterprise or an API-compatible authentication server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#base_url GithubAuthBackend#base_url}
        '''
        result = self._values.get("base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Specifies the description of the mount. This overrides the current stored value, if any.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#description GithubAuthBackend#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_remount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set, opts out of mount migration on path updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#disable_remount GithubAuthBackend#disable_remount}
        '''
        result = self._values.get("disable_remount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#id GithubAuthBackend#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#namespace GithubAuthBackend#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the organization users must be part of.

        Vault will attempt to fetch and set this value if it is not provided (vault-1.10+)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#organization_id GithubAuthBackend#organization_id}
        '''
        result = self._values.get("organization_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path where the auth backend is mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#path GithubAuthBackend#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_bound_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the blocks of IP addresses which are allowed to use the generated token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_bound_cidrs GithubAuthBackend#token_bound_cidrs}
        '''
        result = self._values.get("token_bound_cidrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_explicit_max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Generated Token's Explicit Maximum TTL in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_explicit_max_ttl GithubAuthBackend#token_explicit_max_ttl}
        '''
        result = self._values.get("token_explicit_max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_max_ttl(self) -> typing.Optional[jsii.Number]:
        '''The maximum lifetime of the generated token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_max_ttl GithubAuthBackend#token_max_ttl}
        '''
        result = self._values.get("token_max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_no_default_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the 'default' policy will not automatically be added to generated tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_no_default_policy GithubAuthBackend#token_no_default_policy}
        '''
        result = self._values.get("token_no_default_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token_num_uses(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times a token may be used, a value of zero means unlimited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_num_uses GithubAuthBackend#token_num_uses}
        '''
        result = self._values.get("token_num_uses")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_period(self) -> typing.Optional[jsii.Number]:
        '''Generated Token's Period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_period GithubAuthBackend#token_period}
        '''
        result = self._values.get("token_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Generated Token's Policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_policies GithubAuthBackend#token_policies}
        '''
        result = self._values.get("token_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_ttl(self) -> typing.Optional[jsii.Number]:
        '''The initial ttl of the token to generate in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_ttl GithubAuthBackend#token_ttl}
        '''
        result = self._values.get("token_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_type(self) -> typing.Optional[builtins.str]:
        '''The type of token to generate, service or batch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_type GithubAuthBackend#token_type}
        '''
        result = self._values.get("token_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tune(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GithubAuthBackendTune"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#tune GithubAuthBackend#tune}.'''
        result = self._values.get("tune")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GithubAuthBackendTune"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubAuthBackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.githubAuthBackend.GithubAuthBackendTune",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_response_headers": "allowedResponseHeaders",
        "audit_non_hmac_request_keys": "auditNonHmacRequestKeys",
        "audit_non_hmac_response_keys": "auditNonHmacResponseKeys",
        "default_lease_ttl": "defaultLeaseTtl",
        "listing_visibility": "listingVisibility",
        "max_lease_ttl": "maxLeaseTtl",
        "passthrough_request_headers": "passthroughRequestHeaders",
        "token_type": "tokenType",
    },
)
class GithubAuthBackendTune:
    def __init__(
        self,
        *,
        allowed_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_request_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        audit_non_hmac_response_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_lease_ttl: typing.Optional[builtins.str] = None,
        listing_visibility: typing.Optional[builtins.str] = None,
        max_lease_ttl: typing.Optional[builtins.str] = None,
        passthrough_request_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_response_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#allowed_response_headers GithubAuthBackend#allowed_response_headers}.
        :param audit_non_hmac_request_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#audit_non_hmac_request_keys GithubAuthBackend#audit_non_hmac_request_keys}.
        :param audit_non_hmac_response_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#audit_non_hmac_response_keys GithubAuthBackend#audit_non_hmac_response_keys}.
        :param default_lease_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#default_lease_ttl GithubAuthBackend#default_lease_ttl}.
        :param listing_visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#listing_visibility GithubAuthBackend#listing_visibility}.
        :param max_lease_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#max_lease_ttl GithubAuthBackend#max_lease_ttl}.
        :param passthrough_request_headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#passthrough_request_headers GithubAuthBackend#passthrough_request_headers}.
        :param token_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_type GithubAuthBackend#token_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackendTune.__init__)
            check_type(argname="argument allowed_response_headers", value=allowed_response_headers, expected_type=type_hints["allowed_response_headers"])
            check_type(argname="argument audit_non_hmac_request_keys", value=audit_non_hmac_request_keys, expected_type=type_hints["audit_non_hmac_request_keys"])
            check_type(argname="argument audit_non_hmac_response_keys", value=audit_non_hmac_response_keys, expected_type=type_hints["audit_non_hmac_response_keys"])
            check_type(argname="argument default_lease_ttl", value=default_lease_ttl, expected_type=type_hints["default_lease_ttl"])
            check_type(argname="argument listing_visibility", value=listing_visibility, expected_type=type_hints["listing_visibility"])
            check_type(argname="argument max_lease_ttl", value=max_lease_ttl, expected_type=type_hints["max_lease_ttl"])
            check_type(argname="argument passthrough_request_headers", value=passthrough_request_headers, expected_type=type_hints["passthrough_request_headers"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_response_headers is not None:
            self._values["allowed_response_headers"] = allowed_response_headers
        if audit_non_hmac_request_keys is not None:
            self._values["audit_non_hmac_request_keys"] = audit_non_hmac_request_keys
        if audit_non_hmac_response_keys is not None:
            self._values["audit_non_hmac_response_keys"] = audit_non_hmac_response_keys
        if default_lease_ttl is not None:
            self._values["default_lease_ttl"] = default_lease_ttl
        if listing_visibility is not None:
            self._values["listing_visibility"] = listing_visibility
        if max_lease_ttl is not None:
            self._values["max_lease_ttl"] = max_lease_ttl
        if passthrough_request_headers is not None:
            self._values["passthrough_request_headers"] = passthrough_request_headers
        if token_type is not None:
            self._values["token_type"] = token_type

    @builtins.property
    def allowed_response_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#allowed_response_headers GithubAuthBackend#allowed_response_headers}.'''
        result = self._values.get("allowed_response_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_non_hmac_request_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#audit_non_hmac_request_keys GithubAuthBackend#audit_non_hmac_request_keys}.'''
        result = self._values.get("audit_non_hmac_request_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def audit_non_hmac_response_keys(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#audit_non_hmac_response_keys GithubAuthBackend#audit_non_hmac_response_keys}.'''
        result = self._values.get("audit_non_hmac_response_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_lease_ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#default_lease_ttl GithubAuthBackend#default_lease_ttl}.'''
        result = self._values.get("default_lease_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def listing_visibility(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#listing_visibility GithubAuthBackend#listing_visibility}.'''
        result = self._values.get("listing_visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_lease_ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#max_lease_ttl GithubAuthBackend#max_lease_ttl}.'''
        result = self._values.get("max_lease_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passthrough_request_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#passthrough_request_headers GithubAuthBackend#passthrough_request_headers}.'''
        result = self._values.get("passthrough_request_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/github_auth_backend#token_type GithubAuthBackend#token_type}.'''
        result = self._values.get("token_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubAuthBackendTune(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GithubAuthBackendTuneList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.githubAuthBackend.GithubAuthBackendTuneList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackendTuneList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GithubAuthBackendTuneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackendTuneList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GithubAuthBackendTuneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GithubAuthBackendTune]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GithubAuthBackendTune]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GithubAuthBackendTune]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GithubAuthBackendTuneOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.githubAuthBackend.GithubAuthBackendTuneOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GithubAuthBackendTuneOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowedResponseHeaders")
    def reset_allowed_response_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedResponseHeaders", []))

    @jsii.member(jsii_name="resetAuditNonHmacRequestKeys")
    def reset_audit_non_hmac_request_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditNonHmacRequestKeys", []))

    @jsii.member(jsii_name="resetAuditNonHmacResponseKeys")
    def reset_audit_non_hmac_response_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuditNonHmacResponseKeys", []))

    @jsii.member(jsii_name="resetDefaultLeaseTtl")
    def reset_default_lease_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLeaseTtl", []))

    @jsii.member(jsii_name="resetListingVisibility")
    def reset_listing_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListingVisibility", []))

    @jsii.member(jsii_name="resetMaxLeaseTtl")
    def reset_max_lease_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLeaseTtl", []))

    @jsii.member(jsii_name="resetPassthroughRequestHeaders")
    def reset_passthrough_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassthroughRequestHeaders", []))

    @jsii.member(jsii_name="resetTokenType")
    def reset_token_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenType", []))

    @builtins.property
    @jsii.member(jsii_name="allowedResponseHeadersInput")
    def allowed_response_headers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedResponseHeadersInput"))

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
    @jsii.member(jsii_name="defaultLeaseTtlInput")
    def default_lease_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLeaseTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="listingVisibilityInput")
    def listing_visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listingVisibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtlInput")
    def max_lease_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxLeaseTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="passthroughRequestHeadersInput")
    def passthrough_request_headers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "passthroughRequestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedResponseHeaders")
    def allowed_response_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedResponseHeaders"))

    @allowed_response_headers.setter
    def allowed_response_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "allowed_response_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedResponseHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacRequestKeys")
    def audit_non_hmac_request_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "auditNonHmacRequestKeys"))

    @audit_non_hmac_request_keys.setter
    def audit_non_hmac_request_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "audit_non_hmac_request_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNonHmacRequestKeys", value)

    @builtins.property
    @jsii.member(jsii_name="auditNonHmacResponseKeys")
    def audit_non_hmac_response_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "auditNonHmacResponseKeys"))

    @audit_non_hmac_response_keys.setter
    def audit_non_hmac_response_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "audit_non_hmac_response_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNonHmacResponseKeys", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLeaseTtl")
    def default_lease_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLeaseTtl"))

    @default_lease_ttl.setter
    def default_lease_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "default_lease_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLeaseTtl", value)

    @builtins.property
    @jsii.member(jsii_name="listingVisibility")
    def listing_visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listingVisibility"))

    @listing_visibility.setter
    def listing_visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "listing_visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listingVisibility", value)

    @builtins.property
    @jsii.member(jsii_name="maxLeaseTtl")
    def max_lease_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxLeaseTtl"))

    @max_lease_ttl.setter
    def max_lease_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "max_lease_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLeaseTtl", value)

    @builtins.property
    @jsii.member(jsii_name="passthroughRequestHeaders")
    def passthrough_request_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "passthroughRequestHeaders"))

    @passthrough_request_headers.setter
    def passthrough_request_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "passthrough_request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passthroughRequestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GithubAuthBackendTune, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GithubAuthBackendTune, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GithubAuthBackendTune, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GithubAuthBackendTuneOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GithubAuthBackend",
    "GithubAuthBackendConfig",
    "GithubAuthBackendTune",
    "GithubAuthBackendTuneList",
    "GithubAuthBackendTuneOutputReference",
]

publication.publish()
