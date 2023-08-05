'''
# `databricks_sql_widget`

Refer to the Terraform Registory for docs: [`databricks_sql_widget`](https://www.terraform.io/docs/providers/databricks/r/sql_widget).
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


class SqlWidget(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidget",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget databricks_sql_widget}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dashboard_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SqlWidgetParameter", typing.Dict[str, typing.Any]]]]] = None,
        position: typing.Optional[typing.Union["SqlWidgetPosition", typing.Dict[str, typing.Any]]] = None,
        text: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        visualization_id: typing.Optional[builtins.str] = None,
        widget_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget databricks_sql_widget} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dashboard_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#dashboard_id SqlWidget#dashboard_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#description SqlWidget#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#id SqlWidget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#parameter SqlWidget#parameter}
        :param position: position block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#position SqlWidget#position}
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#text SqlWidget#text}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.
        :param visualization_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#visualization_id SqlWidget#visualization_id}.
        :param widget_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#widget_id SqlWidget#widget_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidget.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SqlWidgetConfig(
            dashboard_id=dashboard_id,
            description=description,
            id=id,
            parameter=parameter,
            position=position,
            text=text,
            title=title,
            visualization_id=visualization_id,
            widget_id=widget_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SqlWidgetParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidget.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="putPosition")
    def put_position(
        self,
        *,
        size_x: jsii.Number,
        size_y: jsii.Number,
        auto_height: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pos_x: typing.Optional[jsii.Number] = None,
        pos_y: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_x SqlWidget#size_x}.
        :param size_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_y SqlWidget#size_y}.
        :param auto_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#auto_height SqlWidget#auto_height}.
        :param pos_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_x SqlWidget#pos_x}.
        :param pos_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_y SqlWidget#pos_y}.
        '''
        value = SqlWidgetPosition(
            size_x=size_x,
            size_y=size_y,
            auto_height=auto_height,
            pos_x=pos_x,
            pos_y=pos_y,
        )

        return typing.cast(None, jsii.invoke(self, "putPosition", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @jsii.member(jsii_name="resetPosition")
    def reset_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosition", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetVisualizationId")
    def reset_visualization_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisualizationId", []))

    @jsii.member(jsii_name="resetWidgetId")
    def reset_widget_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "SqlWidgetParameterList":
        return typing.cast("SqlWidgetParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> "SqlWidgetPositionOutputReference":
        return typing.cast("SqlWidgetPositionOutputReference", jsii.get(self, "position"))

    @builtins.property
    @jsii.member(jsii_name="dashboardIdInput")
    def dashboard_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlWidgetParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlWidgetParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional["SqlWidgetPosition"]:
        return typing.cast(typing.Optional["SqlWidgetPosition"], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="visualizationIdInput")
    def visualization_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visualizationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetIdInput")
    def widget_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "widgetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dashboardId"))

    @dashboard_id.setter
    def dashboard_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "dashboard_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="visualizationId")
    def visualization_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visualizationId"))

    @visualization_id.setter
    def visualization_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "visualization_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visualizationId", value)

    @builtins.property
    @jsii.member(jsii_name="widgetId")
    def widget_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "widgetId"))

    @widget_id.setter
    def widget_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidget, "widget_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "widgetId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidgetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dashboard_id": "dashboardId",
        "description": "description",
        "id": "id",
        "parameter": "parameter",
        "position": "position",
        "text": "text",
        "title": "title",
        "visualization_id": "visualizationId",
        "widget_id": "widgetId",
    },
)
class SqlWidgetConfig(cdktf.TerraformMetaArguments):
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
        dashboard_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SqlWidgetParameter", typing.Dict[str, typing.Any]]]]] = None,
        position: typing.Optional[typing.Union["SqlWidgetPosition", typing.Dict[str, typing.Any]]] = None,
        text: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        visualization_id: typing.Optional[builtins.str] = None,
        widget_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dashboard_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#dashboard_id SqlWidget#dashboard_id}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#description SqlWidget#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#id SqlWidget#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#parameter SqlWidget#parameter}
        :param position: position block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#position SqlWidget#position}
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#text SqlWidget#text}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.
        :param visualization_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#visualization_id SqlWidget#visualization_id}.
        :param widget_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#widget_id SqlWidget#widget_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(position, dict):
            position = SqlWidgetPosition(**position)
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidgetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument visualization_id", value=visualization_id, expected_type=type_hints["visualization_id"])
            check_type(argname="argument widget_id", value=widget_id, expected_type=type_hints["widget_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dashboard_id": dashboard_id,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if parameter is not None:
            self._values["parameter"] = parameter
        if position is not None:
            self._values["position"] = position
        if text is not None:
            self._values["text"] = text
        if title is not None:
            self._values["title"] = title
        if visualization_id is not None:
            self._values["visualization_id"] = visualization_id
        if widget_id is not None:
            self._values["widget_id"] = widget_id

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
    def dashboard_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#dashboard_id SqlWidget#dashboard_id}.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#description SqlWidget#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#id SqlWidget#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlWidgetParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#parameter SqlWidget#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SqlWidgetParameter"]]], result)

    @builtins.property
    def position(self) -> typing.Optional["SqlWidgetPosition"]:
        '''position block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#position SqlWidget#position}
        '''
        result = self._values.get("position")
        return typing.cast(typing.Optional["SqlWidgetPosition"], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#text SqlWidget#text}.'''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visualization_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#visualization_id SqlWidget#visualization_id}.'''
        result = self._values.get("visualization_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def widget_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#widget_id SqlWidget#widget_id}.'''
        result = self._values.get("widget_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlWidgetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidgetParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "map_to": "mapTo",
        "title": "title",
        "value": "value",
        "values": "values",
    },
)
class SqlWidgetParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        map_to: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#name SqlWidget#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#type SqlWidget#type}.
        :param map_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#map_to SqlWidget#map_to}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#value SqlWidget#value}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#values SqlWidget#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidgetParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument map_to", value=map_to, expected_type=type_hints["map_to"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if map_to is not None:
            self._values["map_to"] = map_to
        if title is not None:
            self._values["title"] = title
        if value is not None:
            self._values["value"] = value
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#name SqlWidget#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#type SqlWidget#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def map_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#map_to SqlWidget#map_to}.'''
        result = self._values.get("map_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#title SqlWidget#title}.'''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#value SqlWidget#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#values SqlWidget#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlWidgetParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlWidgetParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidgetParameterList",
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
            type_hints = typing.get_type_hints(SqlWidgetParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SqlWidgetParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidgetParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SqlWidgetParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SqlWidgetParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SqlWidgetParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SqlWidgetParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SqlWidgetParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidgetParameterOutputReference",
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
            type_hints = typing.get_type_hints(SqlWidgetParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMapTo")
    def reset_map_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapTo", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="mapToInput")
    def map_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mapToInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="mapTo")
    def map_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mapTo"))

    @map_to.setter
    def map_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "map_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapTo", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SqlWidgetParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SqlWidgetParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SqlWidgetParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidgetPosition",
    jsii_struct_bases=[],
    name_mapping={
        "size_x": "sizeX",
        "size_y": "sizeY",
        "auto_height": "autoHeight",
        "pos_x": "posX",
        "pos_y": "posY",
    },
)
class SqlWidgetPosition:
    def __init__(
        self,
        *,
        size_x: jsii.Number,
        size_y: jsii.Number,
        auto_height: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pos_x: typing.Optional[jsii.Number] = None,
        pos_y: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param size_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_x SqlWidget#size_x}.
        :param size_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_y SqlWidget#size_y}.
        :param auto_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#auto_height SqlWidget#auto_height}.
        :param pos_x: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_x SqlWidget#pos_x}.
        :param pos_y: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_y SqlWidget#pos_y}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidgetPosition.__init__)
            check_type(argname="argument size_x", value=size_x, expected_type=type_hints["size_x"])
            check_type(argname="argument size_y", value=size_y, expected_type=type_hints["size_y"])
            check_type(argname="argument auto_height", value=auto_height, expected_type=type_hints["auto_height"])
            check_type(argname="argument pos_x", value=pos_x, expected_type=type_hints["pos_x"])
            check_type(argname="argument pos_y", value=pos_y, expected_type=type_hints["pos_y"])
        self._values: typing.Dict[str, typing.Any] = {
            "size_x": size_x,
            "size_y": size_y,
        }
        if auto_height is not None:
            self._values["auto_height"] = auto_height
        if pos_x is not None:
            self._values["pos_x"] = pos_x
        if pos_y is not None:
            self._values["pos_y"] = pos_y

    @builtins.property
    def size_x(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_x SqlWidget#size_x}.'''
        result = self._values.get("size_x")
        assert result is not None, "Required property 'size_x' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def size_y(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#size_y SqlWidget#size_y}.'''
        result = self._values.get("size_y")
        assert result is not None, "Required property 'size_y' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def auto_height(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#auto_height SqlWidget#auto_height}.'''
        result = self._values.get("auto_height")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pos_x(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_x SqlWidget#pos_x}.'''
        result = self._values.get("pos_x")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pos_y(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/sql_widget#pos_y SqlWidget#pos_y}.'''
        result = self._values.get("pos_y")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlWidgetPosition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SqlWidgetPositionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.sqlWidget.SqlWidgetPositionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SqlWidgetPositionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoHeight")
    def reset_auto_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoHeight", []))

    @jsii.member(jsii_name="resetPosX")
    def reset_pos_x(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosX", []))

    @jsii.member(jsii_name="resetPosY")
    def reset_pos_y(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosY", []))

    @builtins.property
    @jsii.member(jsii_name="autoHeightInput")
    def auto_height_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="posXInput")
    def pos_x_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "posXInput"))

    @builtins.property
    @jsii.member(jsii_name="posYInput")
    def pos_y_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "posYInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeXInput")
    def size_x_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeXInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeYInput")
    def size_y_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeYInput"))

    @builtins.property
    @jsii.member(jsii_name="autoHeight")
    def auto_height(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoHeight"))

    @auto_height.setter
    def auto_height(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetPositionOutputReference, "auto_height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoHeight", value)

    @builtins.property
    @jsii.member(jsii_name="posX")
    def pos_x(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "posX"))

    @pos_x.setter
    def pos_x(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetPositionOutputReference, "pos_x").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posX", value)

    @builtins.property
    @jsii.member(jsii_name="posY")
    def pos_y(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "posY"))

    @pos_y.setter
    def pos_y(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetPositionOutputReference, "pos_y").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posY", value)

    @builtins.property
    @jsii.member(jsii_name="sizeX")
    def size_x(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeX"))

    @size_x.setter
    def size_x(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetPositionOutputReference, "size_x").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeX", value)

    @builtins.property
    @jsii.member(jsii_name="sizeY")
    def size_y(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeY"))

    @size_y.setter
    def size_y(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetPositionOutputReference, "size_y").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeY", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SqlWidgetPosition]:
        return typing.cast(typing.Optional[SqlWidgetPosition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SqlWidgetPosition]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SqlWidgetPositionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SqlWidget",
    "SqlWidgetConfig",
    "SqlWidgetParameter",
    "SqlWidgetParameterList",
    "SqlWidgetParameterOutputReference",
    "SqlWidgetPosition",
    "SqlWidgetPositionOutputReference",
]

publication.publish()
