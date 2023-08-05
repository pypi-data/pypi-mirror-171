'''
# `data_vault_transform_decode`

Refer to the Terraform Registory for docs: [`data_vault_transform_decode`](https://www.terraform.io/docs/providers/vault/d/transform_decode).
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


class DataVaultTransformDecode(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.dataVaultTransformDecode.DataVaultTransformDecode",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/d/transform_decode vault_transform_decode}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        path: builtins.str,
        role_name: builtins.str,
        batch_input: typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        batch_results: typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        decoded_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        transformation: typing.Optional[builtins.str] = None,
        tweak: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/d/transform_decode vault_transform_decode} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param path: Path to backend from which to retrieve data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#path DataVaultTransformDecode#path}
        :param role_name: The name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#role_name DataVaultTransformDecode#role_name}
        :param batch_input: Specifies a list of items to be decoded in a single batch. If this parameter is set, the top-level parameters 'value', 'transformation' and 'tweak' will be ignored. Each batch item within the list can specify these parameters instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#batch_input DataVaultTransformDecode#batch_input}
        :param batch_results: The result of decoding batch_input. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#batch_results DataVaultTransformDecode#batch_results}
        :param decoded_value: The result of decoding a value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#decoded_value DataVaultTransformDecode#decoded_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#id DataVaultTransformDecode#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#namespace DataVaultTransformDecode#namespace}
        :param transformation: The transformation to perform. If no value is provided and the role contains a single transformation, this value will be inferred from the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#transformation DataVaultTransformDecode#transformation}
        :param tweak: The tweak value to use. Only applicable for FPE transformations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#tweak DataVaultTransformDecode#tweak}
        :param value: The value in which to decode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#value DataVaultTransformDecode#value}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVaultTransformDecode.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataVaultTransformDecodeConfig(
            path=path,
            role_name=role_name,
            batch_input=batch_input,
            batch_results=batch_results,
            decoded_value=decoded_value,
            id=id,
            namespace=namespace,
            transformation=transformation,
            tweak=tweak,
            value=value,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBatchInput")
    def reset_batch_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchInput", []))

    @jsii.member(jsii_name="resetBatchResults")
    def reset_batch_results(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBatchResults", []))

    @jsii.member(jsii_name="resetDecodedValue")
    def reset_decoded_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecodedValue", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetTransformation")
    def reset_transformation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransformation", []))

    @jsii.member(jsii_name="resetTweak")
    def reset_tweak(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTweak", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="batchInputInput")
    def batch_input_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "batchInputInput"))

    @builtins.property
    @jsii.member(jsii_name="batchResultsInput")
    def batch_results_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "batchResultsInput"))

    @builtins.property
    @jsii.member(jsii_name="decodedValueInput")
    def decoded_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "decodedValueInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="transformationInput")
    def transformation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transformationInput"))

    @builtins.property
    @jsii.member(jsii_name="tweakInput")
    def tweak_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tweakInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="batchInput")
    def batch_input(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "batchInput"))

    @batch_input.setter
    def batch_input(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "batch_input").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchInput", value)

    @builtins.property
    @jsii.member(jsii_name="batchResults")
    def batch_results(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "batchResults"))

    @batch_results.setter
    def batch_results(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "batch_results").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "batchResults", value)

    @builtins.property
    @jsii.member(jsii_name="decodedValue")
    def decoded_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decodedValue"))

    @decoded_value.setter
    def decoded_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "decoded_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decodedValue", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="transformation")
    def transformation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "transformation"))

    @transformation.setter
    def transformation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "transformation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformation", value)

    @builtins.property
    @jsii.member(jsii_name="tweak")
    def tweak(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tweak"))

    @tweak.setter
    def tweak(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "tweak").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tweak", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultTransformDecode, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.dataVaultTransformDecode.DataVaultTransformDecodeConfig",
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
        "role_name": "roleName",
        "batch_input": "batchInput",
        "batch_results": "batchResults",
        "decoded_value": "decodedValue",
        "id": "id",
        "namespace": "namespace",
        "transformation": "transformation",
        "tweak": "tweak",
        "value": "value",
    },
)
class DataVaultTransformDecodeConfig(cdktf.TerraformMetaArguments):
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
        role_name: builtins.str,
        batch_input: typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        batch_results: typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        decoded_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        transformation: typing.Optional[builtins.str] = None,
        tweak: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param path: Path to backend from which to retrieve data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#path DataVaultTransformDecode#path}
        :param role_name: The name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#role_name DataVaultTransformDecode#role_name}
        :param batch_input: Specifies a list of items to be decoded in a single batch. If this parameter is set, the top-level parameters 'value', 'transformation' and 'tweak' will be ignored. Each batch item within the list can specify these parameters instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#batch_input DataVaultTransformDecode#batch_input}
        :param batch_results: The result of decoding batch_input. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#batch_results DataVaultTransformDecode#batch_results}
        :param decoded_value: The result of decoding a value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#decoded_value DataVaultTransformDecode#decoded_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#id DataVaultTransformDecode#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#namespace DataVaultTransformDecode#namespace}
        :param transformation: The transformation to perform. If no value is provided and the role contains a single transformation, this value will be inferred from the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#transformation DataVaultTransformDecode#transformation}
        :param tweak: The tweak value to use. Only applicable for FPE transformations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#tweak DataVaultTransformDecode#tweak}
        :param value: The value in which to decode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#value DataVaultTransformDecode#value}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataVaultTransformDecodeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument batch_input", value=batch_input, expected_type=type_hints["batch_input"])
            check_type(argname="argument batch_results", value=batch_results, expected_type=type_hints["batch_results"])
            check_type(argname="argument decoded_value", value=decoded_value, expected_type=type_hints["decoded_value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument transformation", value=transformation, expected_type=type_hints["transformation"])
            check_type(argname="argument tweak", value=tweak, expected_type=type_hints["tweak"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
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
        if batch_input is not None:
            self._values["batch_input"] = batch_input
        if batch_results is not None:
            self._values["batch_results"] = batch_results
        if decoded_value is not None:
            self._values["decoded_value"] = decoded_value
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if transformation is not None:
            self._values["transformation"] = transformation
        if tweak is not None:
            self._values["tweak"] = tweak
        if value is not None:
            self._values["value"] = value

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
        '''Path to backend from which to retrieve data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#path DataVaultTransformDecode#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''The name of the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#role_name DataVaultTransformDecode#role_name}
        '''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def batch_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''Specifies a list of items to be decoded in a single batch.

        If this parameter is set, the top-level parameters 'value', 'transformation' and 'tweak' will be ignored. Each batch item within the list can specify these parameters instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#batch_input DataVaultTransformDecode#batch_input}
        '''
        result = self._values.get("batch_input")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def batch_results(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''The result of decoding batch_input.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#batch_results DataVaultTransformDecode#batch_results}
        '''
        result = self._values.get("batch_results")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def decoded_value(self) -> typing.Optional[builtins.str]:
        '''The result of decoding a value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#decoded_value DataVaultTransformDecode#decoded_value}
        '''
        result = self._values.get("decoded_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#id DataVaultTransformDecode#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#namespace DataVaultTransformDecode#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transformation(self) -> typing.Optional[builtins.str]:
        '''The transformation to perform.

        If no value is provided and the role contains a single transformation, this value will be inferred from the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#transformation DataVaultTransformDecode#transformation}
        '''
        result = self._values.get("transformation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tweak(self) -> typing.Optional[builtins.str]:
        '''The tweak value to use. Only applicable for FPE transformations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#tweak DataVaultTransformDecode#tweak}
        '''
        result = self._values.get("tweak")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value in which to decode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/transform_decode#value DataVaultTransformDecode#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVaultTransformDecodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataVaultTransformDecode",
    "DataVaultTransformDecodeConfig",
]

publication.publish()
