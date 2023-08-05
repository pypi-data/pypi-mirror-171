'''
# `vault_aws_auth_backend_client`

Refer to the Terraform Registory for docs: [`vault_aws_auth_backend_client`](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client).
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


class AwsAuthBackendClient(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.awsAuthBackendClient.AwsAuthBackendClient",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client vault_aws_auth_backend_client}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        access_key: typing.Optional[builtins.str] = None,
        backend: typing.Optional[builtins.str] = None,
        ec2_endpoint: typing.Optional[builtins.str] = None,
        iam_endpoint: typing.Optional[builtins.str] = None,
        iam_server_id_header_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        sts_endpoint: typing.Optional[builtins.str] = None,
        sts_region: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client vault_aws_auth_backend_client} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_key: AWS Access key with permissions to query AWS APIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#access_key AwsAuthBackendClient#access_key}
        :param backend: Unique name of the auth backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#backend AwsAuthBackendClient#backend}
        :param ec2_endpoint: URL to override the default generated endpoint for making AWS EC2 API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#ec2_endpoint AwsAuthBackendClient#ec2_endpoint}
        :param iam_endpoint: URL to override the default generated endpoint for making AWS IAM API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#iam_endpoint AwsAuthBackendClient#iam_endpoint}
        :param iam_server_id_header_value: The value to require in the X-Vault-AWS-IAM-Server-ID header as part of GetCallerIdentity requests that are used in the iam auth method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#iam_server_id_header_value AwsAuthBackendClient#iam_server_id_header_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#id AwsAuthBackendClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#namespace AwsAuthBackendClient#namespace}
        :param secret_key: AWS Secret key with permissions to query AWS APIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#secret_key AwsAuthBackendClient#secret_key}
        :param sts_endpoint: URL to override the default generated endpoint for making AWS STS API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#sts_endpoint AwsAuthBackendClient#sts_endpoint}
        :param sts_region: Region to override the default region for making AWS STS API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#sts_region AwsAuthBackendClient#sts_region}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AwsAuthBackendClient.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AwsAuthBackendClientConfig(
            access_key=access_key,
            backend=backend,
            ec2_endpoint=ec2_endpoint,
            iam_endpoint=iam_endpoint,
            iam_server_id_header_value=iam_server_id_header_value,
            id=id,
            namespace=namespace,
            secret_key=secret_key,
            sts_endpoint=sts_endpoint,
            sts_region=sts_region,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetEc2Endpoint")
    def reset_ec2_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2Endpoint", []))

    @jsii.member(jsii_name="resetIamEndpoint")
    def reset_iam_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamEndpoint", []))

    @jsii.member(jsii_name="resetIamServerIdHeaderValue")
    def reset_iam_server_id_header_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamServerIdHeaderValue", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="resetStsEndpoint")
    def reset_sts_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStsEndpoint", []))

    @jsii.member(jsii_name="resetStsRegion")
    def reset_sts_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStsRegion", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2EndpointInput")
    def ec2_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2EndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="iamEndpointInput")
    def iam_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="iamServerIdHeaderValueInput")
    def iam_server_id_header_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamServerIdHeaderValueInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="stsEndpointInput")
    def sts_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stsEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="stsRegionInput")
    def sts_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="ec2Endpoint")
    def ec2_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ec2Endpoint"))

    @ec2_endpoint.setter
    def ec2_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "ec2_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2Endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="iamEndpoint")
    def iam_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamEndpoint"))

    @iam_endpoint.setter
    def iam_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "iam_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="iamServerIdHeaderValue")
    def iam_server_id_header_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamServerIdHeaderValue"))

    @iam_server_id_header_value.setter
    def iam_server_id_header_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "iam_server_id_header_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamServerIdHeaderValue", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="stsEndpoint")
    def sts_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stsEndpoint"))

    @sts_endpoint.setter
    def sts_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "sts_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stsEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="stsRegion")
    def sts_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stsRegion"))

    @sts_region.setter
    def sts_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendClient, "sts_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stsRegion", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.awsAuthBackendClient.AwsAuthBackendClientConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access_key": "accessKey",
        "backend": "backend",
        "ec2_endpoint": "ec2Endpoint",
        "iam_endpoint": "iamEndpoint",
        "iam_server_id_header_value": "iamServerIdHeaderValue",
        "id": "id",
        "namespace": "namespace",
        "secret_key": "secretKey",
        "sts_endpoint": "stsEndpoint",
        "sts_region": "stsRegion",
    },
)
class AwsAuthBackendClientConfig(cdktf.TerraformMetaArguments):
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
        access_key: typing.Optional[builtins.str] = None,
        backend: typing.Optional[builtins.str] = None,
        ec2_endpoint: typing.Optional[builtins.str] = None,
        iam_endpoint: typing.Optional[builtins.str] = None,
        iam_server_id_header_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        sts_endpoint: typing.Optional[builtins.str] = None,
        sts_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param access_key: AWS Access key with permissions to query AWS APIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#access_key AwsAuthBackendClient#access_key}
        :param backend: Unique name of the auth backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#backend AwsAuthBackendClient#backend}
        :param ec2_endpoint: URL to override the default generated endpoint for making AWS EC2 API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#ec2_endpoint AwsAuthBackendClient#ec2_endpoint}
        :param iam_endpoint: URL to override the default generated endpoint for making AWS IAM API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#iam_endpoint AwsAuthBackendClient#iam_endpoint}
        :param iam_server_id_header_value: The value to require in the X-Vault-AWS-IAM-Server-ID header as part of GetCallerIdentity requests that are used in the iam auth method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#iam_server_id_header_value AwsAuthBackendClient#iam_server_id_header_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#id AwsAuthBackendClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#namespace AwsAuthBackendClient#namespace}
        :param secret_key: AWS Secret key with permissions to query AWS APIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#secret_key AwsAuthBackendClient#secret_key}
        :param sts_endpoint: URL to override the default generated endpoint for making AWS STS API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#sts_endpoint AwsAuthBackendClient#sts_endpoint}
        :param sts_region: Region to override the default region for making AWS STS API calls. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#sts_region AwsAuthBackendClient#sts_region}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AwsAuthBackendClientConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument ec2_endpoint", value=ec2_endpoint, expected_type=type_hints["ec2_endpoint"])
            check_type(argname="argument iam_endpoint", value=iam_endpoint, expected_type=type_hints["iam_endpoint"])
            check_type(argname="argument iam_server_id_header_value", value=iam_server_id_header_value, expected_type=type_hints["iam_server_id_header_value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument sts_endpoint", value=sts_endpoint, expected_type=type_hints["sts_endpoint"])
            check_type(argname="argument sts_region", value=sts_region, expected_type=type_hints["sts_region"])
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
        if access_key is not None:
            self._values["access_key"] = access_key
        if backend is not None:
            self._values["backend"] = backend
        if ec2_endpoint is not None:
            self._values["ec2_endpoint"] = ec2_endpoint
        if iam_endpoint is not None:
            self._values["iam_endpoint"] = iam_endpoint
        if iam_server_id_header_value is not None:
            self._values["iam_server_id_header_value"] = iam_server_id_header_value
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if sts_endpoint is not None:
            self._values["sts_endpoint"] = sts_endpoint
        if sts_region is not None:
            self._values["sts_region"] = sts_region

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
    def access_key(self) -> typing.Optional[builtins.str]:
        '''AWS Access key with permissions to query AWS APIs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#access_key AwsAuthBackendClient#access_key}
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend(self) -> typing.Optional[builtins.str]:
        '''Unique name of the auth backend to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#backend AwsAuthBackendClient#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_endpoint(self) -> typing.Optional[builtins.str]:
        '''URL to override the default generated endpoint for making AWS EC2 API calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#ec2_endpoint AwsAuthBackendClient#ec2_endpoint}
        '''
        result = self._values.get("ec2_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_endpoint(self) -> typing.Optional[builtins.str]:
        '''URL to override the default generated endpoint for making AWS IAM API calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#iam_endpoint AwsAuthBackendClient#iam_endpoint}
        '''
        result = self._values.get("iam_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_server_id_header_value(self) -> typing.Optional[builtins.str]:
        '''The value to require in the X-Vault-AWS-IAM-Server-ID header as part of GetCallerIdentity requests that are used in the iam auth method.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#iam_server_id_header_value AwsAuthBackendClient#iam_server_id_header_value}
        '''
        result = self._values.get("iam_server_id_header_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#id AwsAuthBackendClient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#namespace AwsAuthBackendClient#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''AWS Secret key with permissions to query AWS APIs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#secret_key AwsAuthBackendClient#secret_key}
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sts_endpoint(self) -> typing.Optional[builtins.str]:
        '''URL to override the default generated endpoint for making AWS STS API calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#sts_endpoint AwsAuthBackendClient#sts_endpoint}
        '''
        result = self._values.get("sts_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sts_region(self) -> typing.Optional[builtins.str]:
        '''Region to override the default region for making AWS STS API calls.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_client#sts_region AwsAuthBackendClient#sts_region}
        '''
        result = self._values.get("sts_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsAuthBackendClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsAuthBackendClient",
    "AwsAuthBackendClientConfig",
]

publication.publish()
