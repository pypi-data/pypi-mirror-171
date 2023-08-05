'''
# `opentelekomcloud_lb_monitor_v3`

Refer to the Terraform Registory for docs: [`opentelekomcloud_lb_monitor_v3`](https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3).
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


class LbMonitorV3(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.lbMonitorV3.LbMonitorV3",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3 opentelekomcloud_lb_monitor_v3}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        delay: jsii.Number,
        max_retries: jsii.Number,
        pool_id: builtins.str,
        timeout: jsii.Number,
        type: builtins.str,
        admin_state_up: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        expected_codes: typing.Optional[builtins.str] = None,
        http_method: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_retries_down: typing.Optional[jsii.Number] = None,
        monitor_port: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        url_path: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3 opentelekomcloud_lb_monitor_v3} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#delay LbMonitorV3#delay}.
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#max_retries LbMonitorV3#max_retries}.
        :param pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#pool_id LbMonitorV3#pool_id}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#timeout LbMonitorV3#timeout}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#type LbMonitorV3#type}.
        :param admin_state_up: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#admin_state_up LbMonitorV3#admin_state_up}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#domain_name LbMonitorV3#domain_name}.
        :param expected_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#expected_codes LbMonitorV3#expected_codes}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#http_method LbMonitorV3#http_method}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#id LbMonitorV3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_retries_down: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#max_retries_down LbMonitorV3#max_retries_down}.
        :param monitor_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#monitor_port LbMonitorV3#monitor_port}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#name LbMonitorV3#name}.
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#project_id LbMonitorV3#project_id}.
        :param url_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#url_path LbMonitorV3#url_path}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LbMonitorV3.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbMonitorV3Config(
            delay=delay,
            max_retries=max_retries,
            pool_id=pool_id,
            timeout=timeout,
            type=type,
            admin_state_up=admin_state_up,
            domain_name=domain_name,
            expected_codes=expected_codes,
            http_method=http_method,
            id=id,
            max_retries_down=max_retries_down,
            monitor_port=monitor_port,
            name=name,
            project_id=project_id,
            url_path=url_path,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAdminStateUp")
    def reset_admin_state_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminStateUp", []))

    @jsii.member(jsii_name="resetDomainName")
    def reset_domain_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainName", []))

    @jsii.member(jsii_name="resetExpectedCodes")
    def reset_expected_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedCodes", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxRetriesDown")
    def reset_max_retries_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetriesDown", []))

    @jsii.member(jsii_name="resetMonitorPort")
    def reset_monitor_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorPort", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetUrlPath")
    def reset_url_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlPath", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="adminStateUpInput")
    def admin_state_up_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adminStateUpInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedCodesInput")
    def expected_codes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesDownInput")
    def max_retries_down_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesDownInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorPortInput")
    def monitor_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monitorPortInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIdInput")
    def pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlPathInput")
    def url_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlPathInput"))

    @builtins.property
    @jsii.member(jsii_name="adminStateUp")
    def admin_state_up(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "adminStateUp"))

    @admin_state_up.setter
    def admin_state_up(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "admin_state_up").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminStateUp", value)

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "delay"))

    @delay.setter
    def delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delay", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="expectedCodes")
    def expected_codes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expectedCodes"))

    @expected_codes.setter
    def expected_codes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "expected_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedCodes", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "max_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetriesDown")
    def max_retries_down(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetriesDown"))

    @max_retries_down.setter
    def max_retries_down(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "max_retries_down").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetriesDown", value)

    @builtins.property
    @jsii.member(jsii_name="monitorPort")
    def monitor_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monitorPort"))

    @monitor_port.setter
    def monitor_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "monitor_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitorPort", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="poolId")
    def pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "poolId"))

    @pool_id.setter
    def pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="urlPath")
    def url_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlPath"))

    @url_path.setter
    def url_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbMonitorV3, "url_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlPath", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.lbMonitorV3.LbMonitorV3Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "delay": "delay",
        "max_retries": "maxRetries",
        "pool_id": "poolId",
        "timeout": "timeout",
        "type": "type",
        "admin_state_up": "adminStateUp",
        "domain_name": "domainName",
        "expected_codes": "expectedCodes",
        "http_method": "httpMethod",
        "id": "id",
        "max_retries_down": "maxRetriesDown",
        "monitor_port": "monitorPort",
        "name": "name",
        "project_id": "projectId",
        "url_path": "urlPath",
    },
)
class LbMonitorV3Config(cdktf.TerraformMetaArguments):
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
        delay: jsii.Number,
        max_retries: jsii.Number,
        pool_id: builtins.str,
        timeout: jsii.Number,
        type: builtins.str,
        admin_state_up: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        domain_name: typing.Optional[builtins.str] = None,
        expected_codes: typing.Optional[builtins.str] = None,
        http_method: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_retries_down: typing.Optional[jsii.Number] = None,
        monitor_port: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        url_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param delay: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#delay LbMonitorV3#delay}.
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#max_retries LbMonitorV3#max_retries}.
        :param pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#pool_id LbMonitorV3#pool_id}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#timeout LbMonitorV3#timeout}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#type LbMonitorV3#type}.
        :param admin_state_up: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#admin_state_up LbMonitorV3#admin_state_up}.
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#domain_name LbMonitorV3#domain_name}.
        :param expected_codes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#expected_codes LbMonitorV3#expected_codes}.
        :param http_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#http_method LbMonitorV3#http_method}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#id LbMonitorV3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_retries_down: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#max_retries_down LbMonitorV3#max_retries_down}.
        :param monitor_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#monitor_port LbMonitorV3#monitor_port}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#name LbMonitorV3#name}.
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#project_id LbMonitorV3#project_id}.
        :param url_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#url_path LbMonitorV3#url_path}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LbMonitorV3Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument admin_state_up", value=admin_state_up, expected_type=type_hints["admin_state_up"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument expected_codes", value=expected_codes, expected_type=type_hints["expected_codes"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_retries_down", value=max_retries_down, expected_type=type_hints["max_retries_down"])
            check_type(argname="argument monitor_port", value=monitor_port, expected_type=type_hints["monitor_port"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument url_path", value=url_path, expected_type=type_hints["url_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "delay": delay,
            "max_retries": max_retries,
            "pool_id": pool_id,
            "timeout": timeout,
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
        if admin_state_up is not None:
            self._values["admin_state_up"] = admin_state_up
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if expected_codes is not None:
            self._values["expected_codes"] = expected_codes
        if http_method is not None:
            self._values["http_method"] = http_method
        if id is not None:
            self._values["id"] = id
        if max_retries_down is not None:
            self._values["max_retries_down"] = max_retries_down
        if monitor_port is not None:
            self._values["monitor_port"] = monitor_port
        if name is not None:
            self._values["name"] = name
        if project_id is not None:
            self._values["project_id"] = project_id
        if url_path is not None:
            self._values["url_path"] = url_path

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
    def delay(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#delay LbMonitorV3#delay}.'''
        result = self._values.get("delay")
        assert result is not None, "Required property 'delay' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_retries(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#max_retries LbMonitorV3#max_retries}.'''
        result = self._values.get("max_retries")
        assert result is not None, "Required property 'max_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#pool_id LbMonitorV3#pool_id}.'''
        result = self._values.get("pool_id")
        assert result is not None, "Required property 'pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#timeout LbMonitorV3#timeout}.'''
        result = self._values.get("timeout")
        assert result is not None, "Required property 'timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#type LbMonitorV3#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_state_up(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#admin_state_up LbMonitorV3#admin_state_up}.'''
        result = self._values.get("admin_state_up")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#domain_name LbMonitorV3#domain_name}.'''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expected_codes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#expected_codes LbMonitorV3#expected_codes}.'''
        result = self._values.get("expected_codes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#http_method LbMonitorV3#http_method}.'''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#id LbMonitorV3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_retries_down(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#max_retries_down LbMonitorV3#max_retries_down}.'''
        result = self._values.get("max_retries_down")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monitor_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#monitor_port LbMonitorV3#monitor_port}.'''
        result = self._values.get("monitor_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#name LbMonitorV3#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#project_id LbMonitorV3#project_id}.'''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_monitor_v3#url_path LbMonitorV3#url_path}.'''
        result = self._values.get("url_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbMonitorV3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LbMonitorV3",
    "LbMonitorV3Config",
]

publication.publish()
