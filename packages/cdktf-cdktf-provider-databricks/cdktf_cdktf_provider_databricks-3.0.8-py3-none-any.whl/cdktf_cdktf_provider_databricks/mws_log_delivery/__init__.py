'''
# `databricks_mws_log_delivery`

Refer to the Terraform Registory for docs: [`databricks_mws_log_delivery`](https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery).
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


class MwsLogDelivery(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mwsLogDelivery.MwsLogDelivery",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery databricks_mws_log_delivery}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        credentials_id: builtins.str,
        log_type: builtins.str,
        output_format: builtins.str,
        storage_configuration_id: builtins.str,
        config_id: typing.Optional[builtins.str] = None,
        config_name: typing.Optional[builtins.str] = None,
        delivery_path_prefix: typing.Optional[builtins.str] = None,
        delivery_start_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        workspace_ids_filter: typing.Optional[typing.Sequence[jsii.Number]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery databricks_mws_log_delivery} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#account_id MwsLogDelivery#account_id}.
        :param credentials_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#credentials_id MwsLogDelivery#credentials_id}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#log_type MwsLogDelivery#log_type}.
        :param output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#output_format MwsLogDelivery#output_format}.
        :param storage_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#storage_configuration_id MwsLogDelivery#storage_configuration_id}.
        :param config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#config_id MwsLogDelivery#config_id}.
        :param config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#config_name MwsLogDelivery#config_name}.
        :param delivery_path_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#delivery_path_prefix MwsLogDelivery#delivery_path_prefix}.
        :param delivery_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#delivery_start_time MwsLogDelivery#delivery_start_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#id MwsLogDelivery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#status MwsLogDelivery#status}.
        :param workspace_ids_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#workspace_ids_filter MwsLogDelivery#workspace_ids_filter}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MwsLogDelivery.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MwsLogDeliveryConfig(
            account_id=account_id,
            credentials_id=credentials_id,
            log_type=log_type,
            output_format=output_format,
            storage_configuration_id=storage_configuration_id,
            config_id=config_id,
            config_name=config_name,
            delivery_path_prefix=delivery_path_prefix,
            delivery_start_time=delivery_start_time,
            id=id,
            status=status,
            workspace_ids_filter=workspace_ids_filter,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetConfigId")
    def reset_config_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigId", []))

    @jsii.member(jsii_name="resetConfigName")
    def reset_config_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigName", []))

    @jsii.member(jsii_name="resetDeliveryPathPrefix")
    def reset_delivery_path_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryPathPrefix", []))

    @jsii.member(jsii_name="resetDeliveryStartTime")
    def reset_delivery_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStartTime", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetWorkspaceIdsFilter")
    def reset_workspace_ids_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceIdsFilter", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configNameInput")
    def config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configNameInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsIdInput")
    def credentials_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryPathPrefixInput")
    def delivery_path_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryPathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStartTimeInput")
    def delivery_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatInput")
    def output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationIdInput")
    def storage_configuration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageConfigurationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdsFilterInput")
    def workspace_ids_filter_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "workspaceIdsFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "config_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="configName")
    def config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configName"))

    @config_name.setter
    def config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "config_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configName", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsId")
    def credentials_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsId"))

    @credentials_id.setter
    def credentials_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "credentials_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsId", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryPathPrefix")
    def delivery_path_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryPathPrefix"))

    @delivery_path_prefix.setter
    def delivery_path_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "delivery_path_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryPathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStartTime")
    def delivery_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStartTime"))

    @delivery_start_time.setter
    def delivery_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "delivery_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "log_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "output_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationId")
    def storage_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageConfigurationId"))

    @storage_configuration_id.setter
    def storage_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "storage_configuration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageConfigurationId", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceIdsFilter")
    def workspace_ids_filter(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "workspaceIdsFilter"))

    @workspace_ids_filter.setter
    def workspace_ids_filter(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MwsLogDelivery, "workspace_ids_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceIdsFilter", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mwsLogDelivery.MwsLogDeliveryConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "credentials_id": "credentialsId",
        "log_type": "logType",
        "output_format": "outputFormat",
        "storage_configuration_id": "storageConfigurationId",
        "config_id": "configId",
        "config_name": "configName",
        "delivery_path_prefix": "deliveryPathPrefix",
        "delivery_start_time": "deliveryStartTime",
        "id": "id",
        "status": "status",
        "workspace_ids_filter": "workspaceIdsFilter",
    },
)
class MwsLogDeliveryConfig(cdktf.TerraformMetaArguments):
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
        account_id: builtins.str,
        credentials_id: builtins.str,
        log_type: builtins.str,
        output_format: builtins.str,
        storage_configuration_id: builtins.str,
        config_id: typing.Optional[builtins.str] = None,
        config_name: typing.Optional[builtins.str] = None,
        delivery_path_prefix: typing.Optional[builtins.str] = None,
        delivery_start_time: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        workspace_ids_filter: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#account_id MwsLogDelivery#account_id}.
        :param credentials_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#credentials_id MwsLogDelivery#credentials_id}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#log_type MwsLogDelivery#log_type}.
        :param output_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#output_format MwsLogDelivery#output_format}.
        :param storage_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#storage_configuration_id MwsLogDelivery#storage_configuration_id}.
        :param config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#config_id MwsLogDelivery#config_id}.
        :param config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#config_name MwsLogDelivery#config_name}.
        :param delivery_path_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#delivery_path_prefix MwsLogDelivery#delivery_path_prefix}.
        :param delivery_start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#delivery_start_time MwsLogDelivery#delivery_start_time}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#id MwsLogDelivery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#status MwsLogDelivery#status}.
        :param workspace_ids_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#workspace_ids_filter MwsLogDelivery#workspace_ids_filter}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(MwsLogDeliveryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument credentials_id", value=credentials_id, expected_type=type_hints["credentials_id"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument storage_configuration_id", value=storage_configuration_id, expected_type=type_hints["storage_configuration_id"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument config_name", value=config_name, expected_type=type_hints["config_name"])
            check_type(argname="argument delivery_path_prefix", value=delivery_path_prefix, expected_type=type_hints["delivery_path_prefix"])
            check_type(argname="argument delivery_start_time", value=delivery_start_time, expected_type=type_hints["delivery_start_time"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument workspace_ids_filter", value=workspace_ids_filter, expected_type=type_hints["workspace_ids_filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "credentials_id": credentials_id,
            "log_type": log_type,
            "output_format": output_format,
            "storage_configuration_id": storage_configuration_id,
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
        if config_id is not None:
            self._values["config_id"] = config_id
        if config_name is not None:
            self._values["config_name"] = config_name
        if delivery_path_prefix is not None:
            self._values["delivery_path_prefix"] = delivery_path_prefix
        if delivery_start_time is not None:
            self._values["delivery_start_time"] = delivery_start_time
        if id is not None:
            self._values["id"] = id
        if status is not None:
            self._values["status"] = status
        if workspace_ids_filter is not None:
            self._values["workspace_ids_filter"] = workspace_ids_filter

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
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#account_id MwsLogDelivery#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credentials_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#credentials_id MwsLogDelivery#credentials_id}.'''
        result = self._values.get("credentials_id")
        assert result is not None, "Required property 'credentials_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#log_type MwsLogDelivery#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#output_format MwsLogDelivery#output_format}.'''
        result = self._values.get("output_format")
        assert result is not None, "Required property 'output_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_configuration_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#storage_configuration_id MwsLogDelivery#storage_configuration_id}.'''
        result = self._values.get("storage_configuration_id")
        assert result is not None, "Required property 'storage_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#config_id MwsLogDelivery#config_id}.'''
        result = self._values.get("config_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#config_name MwsLogDelivery#config_name}.'''
        result = self._values.get("config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_path_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#delivery_path_prefix MwsLogDelivery#delivery_path_prefix}.'''
        result = self._values.get("delivery_path_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#delivery_start_time MwsLogDelivery#delivery_start_time}.'''
        result = self._values.get("delivery_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#id MwsLogDelivery#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#status MwsLogDelivery#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_ids_filter(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mws_log_delivery#workspace_ids_filter MwsLogDelivery#workspace_ids_filter}.'''
        result = self._values.get("workspace_ids_filter")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MwsLogDeliveryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MwsLogDelivery",
    "MwsLogDeliveryConfig",
]

publication.publish()
