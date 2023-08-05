'''
# `opentelekomcloud_lb_listener_v3`

Refer to the Terraform Registory for docs: [`opentelekomcloud_lb_listener_v3`](https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3).
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


class LbListenerV3(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.lbListenerV3.LbListenerV3",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3 opentelekomcloud_lb_listener_v3}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        loadbalancer_id: builtins.str,
        protocol: builtins.str,
        protocol_port: jsii.Number,
        admin_state_up: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_ca_tls_container_ref: typing.Optional[builtins.str] = None,
        client_timeout: typing.Optional[jsii.Number] = None,
        default_pool_id: typing.Optional[builtins.str] = None,
        default_tls_container_ref: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        http2_enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        insert_headers: typing.Optional[typing.Union["LbListenerV3InsertHeaders", typing.Dict[str, typing.Any]]] = None,
        keep_alive_timeout: typing.Optional[jsii.Number] = None,
        member_retry_enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        member_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        sni_container_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tls_ciphers_policy: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3 opentelekomcloud_lb_listener_v3} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#loadbalancer_id LbListenerV3#loadbalancer_id}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#protocol LbListenerV3#protocol}.
        :param protocol_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#protocol_port LbListenerV3#protocol_port}.
        :param admin_state_up: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#admin_state_up LbListenerV3#admin_state_up}.
        :param client_ca_tls_container_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#client_ca_tls_container_ref LbListenerV3#client_ca_tls_container_ref}.
        :param client_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#client_timeout LbListenerV3#client_timeout}.
        :param default_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#default_pool_id LbListenerV3#default_pool_id}.
        :param default_tls_container_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#default_tls_container_ref LbListenerV3#default_tls_container_ref}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#description LbListenerV3#description}.
        :param http2_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#http2_enable LbListenerV3#http2_enable}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#id LbListenerV3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insert_headers: insert_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#insert_headers LbListenerV3#insert_headers}
        :param keep_alive_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#keep_alive_timeout LbListenerV3#keep_alive_timeout}.
        :param member_retry_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#member_retry_enable LbListenerV3#member_retry_enable}.
        :param member_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#member_timeout LbListenerV3#member_timeout}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#name LbListenerV3#name}.
        :param sni_container_refs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#sni_container_refs LbListenerV3#sni_container_refs}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#tags LbListenerV3#tags}.
        :param tls_ciphers_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#tls_ciphers_policy LbListenerV3#tls_ciphers_policy}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LbListenerV3.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LbListenerV3Config(
            loadbalancer_id=loadbalancer_id,
            protocol=protocol,
            protocol_port=protocol_port,
            admin_state_up=admin_state_up,
            client_ca_tls_container_ref=client_ca_tls_container_ref,
            client_timeout=client_timeout,
            default_pool_id=default_pool_id,
            default_tls_container_ref=default_tls_container_ref,
            description=description,
            http2_enable=http2_enable,
            id=id,
            insert_headers=insert_headers,
            keep_alive_timeout=keep_alive_timeout,
            member_retry_enable=member_retry_enable,
            member_timeout=member_timeout,
            name=name,
            sni_container_refs=sni_container_refs,
            tags=tags,
            tls_ciphers_policy=tls_ciphers_policy,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInsertHeaders")
    def put_insert_headers(
        self,
        *,
        forwarded_for_port: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarded_host: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarded_port: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forward_elb_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param forwarded_for_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_for_port LbListenerV3#forwarded_for_port}.
        :param forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_host LbListenerV3#forwarded_host}.
        :param forwarded_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_port LbListenerV3#forwarded_port}.
        :param forward_elb_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forward_elb_ip LbListenerV3#forward_elb_ip}.
        '''
        value = LbListenerV3InsertHeaders(
            forwarded_for_port=forwarded_for_port,
            forwarded_host=forwarded_host,
            forwarded_port=forwarded_port,
            forward_elb_ip=forward_elb_ip,
        )

        return typing.cast(None, jsii.invoke(self, "putInsertHeaders", [value]))

    @jsii.member(jsii_name="resetAdminStateUp")
    def reset_admin_state_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminStateUp", []))

    @jsii.member(jsii_name="resetClientCaTlsContainerRef")
    def reset_client_ca_tls_container_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCaTlsContainerRef", []))

    @jsii.member(jsii_name="resetClientTimeout")
    def reset_client_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTimeout", []))

    @jsii.member(jsii_name="resetDefaultPoolId")
    def reset_default_pool_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPoolId", []))

    @jsii.member(jsii_name="resetDefaultTlsContainerRef")
    def reset_default_tls_container_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTlsContainerRef", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHttp2Enable")
    def reset_http2_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2Enable", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInsertHeaders")
    def reset_insert_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsertHeaders", []))

    @jsii.member(jsii_name="resetKeepAliveTimeout")
    def reset_keep_alive_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepAliveTimeout", []))

    @jsii.member(jsii_name="resetMemberRetryEnable")
    def reset_member_retry_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberRetryEnable", []))

    @jsii.member(jsii_name="resetMemberTimeout")
    def reset_member_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberTimeout", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSniContainerRefs")
    def reset_sni_container_refs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSniContainerRefs", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTlsCiphersPolicy")
    def reset_tls_ciphers_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCiphersPolicy", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="insertHeaders")
    def insert_headers(self) -> "LbListenerV3InsertHeadersOutputReference":
        return typing.cast("LbListenerV3InsertHeadersOutputReference", jsii.get(self, "insertHeaders"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="adminStateUpInput")
    def admin_state_up_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adminStateUpInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCaTlsContainerRefInput")
    def client_ca_tls_container_ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCaTlsContainerRefInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTimeoutInput")
    def client_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPoolIdInput")
    def default_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTlsContainerRefInput")
    def default_tls_container_ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTlsContainerRefInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="http2EnableInput")
    def http2_enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "http2EnableInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="insertHeadersInput")
    def insert_headers_input(self) -> typing.Optional["LbListenerV3InsertHeaders"]:
        return typing.cast(typing.Optional["LbListenerV3InsertHeaders"], jsii.get(self, "insertHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="keepAliveTimeoutInput")
    def keep_alive_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keepAliveTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="loadbalancerIdInput")
    def loadbalancer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadbalancerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="memberRetryEnableInput")
    def member_retry_enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "memberRetryEnableInput"))

    @builtins.property
    @jsii.member(jsii_name="memberTimeoutInput")
    def member_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memberTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolPortInput")
    def protocol_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "protocolPortInput"))

    @builtins.property
    @jsii.member(jsii_name="sniContainerRefsInput")
    def sni_container_refs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sniContainerRefsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCiphersPolicyInput")
    def tls_ciphers_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCiphersPolicyInput"))

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
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "admin_state_up").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminStateUp", value)

    @builtins.property
    @jsii.member(jsii_name="clientCaTlsContainerRef")
    def client_ca_tls_container_ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCaTlsContainerRef"))

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "client_ca_tls_container_ref").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCaTlsContainerRef", value)

    @builtins.property
    @jsii.member(jsii_name="clientTimeout")
    def client_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientTimeout"))

    @client_timeout.setter
    def client_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "client_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="defaultPoolId")
    def default_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPoolId"))

    @default_pool_id.setter
    def default_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "default_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTlsContainerRef")
    def default_tls_container_ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTlsContainerRef"))

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "default_tls_container_ref").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTlsContainerRef", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="http2Enable")
    def http2_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "http2Enable"))

    @http2_enable.setter
    def http2_enable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "http2_enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "http2Enable", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="keepAliveTimeout")
    def keep_alive_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keepAliveTimeout"))

    @keep_alive_timeout.setter
    def keep_alive_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "keep_alive_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAliveTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="loadbalancerId")
    def loadbalancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadbalancerId"))

    @loadbalancer_id.setter
    def loadbalancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "loadbalancer_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadbalancerId", value)

    @builtins.property
    @jsii.member(jsii_name="memberRetryEnable")
    def member_retry_enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "memberRetryEnable"))

    @member_retry_enable.setter
    def member_retry_enable(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "member_retry_enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberRetryEnable", value)

    @builtins.property
    @jsii.member(jsii_name="memberTimeout")
    def member_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memberTimeout"))

    @member_timeout.setter
    def member_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "member_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="protocolPort")
    def protocol_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "protocolPort"))

    @protocol_port.setter
    def protocol_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "protocol_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolPort", value)

    @builtins.property
    @jsii.member(jsii_name="sniContainerRefs")
    def sni_container_refs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sniContainerRefs"))

    @sni_container_refs.setter
    def sni_container_refs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "sni_container_refs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sniContainerRefs", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCiphersPolicy")
    def tls_ciphers_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCiphersPolicy"))

    @tls_ciphers_policy.setter
    def tls_ciphers_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3, "tls_ciphers_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCiphersPolicy", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.lbListenerV3.LbListenerV3Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "loadbalancer_id": "loadbalancerId",
        "protocol": "protocol",
        "protocol_port": "protocolPort",
        "admin_state_up": "adminStateUp",
        "client_ca_tls_container_ref": "clientCaTlsContainerRef",
        "client_timeout": "clientTimeout",
        "default_pool_id": "defaultPoolId",
        "default_tls_container_ref": "defaultTlsContainerRef",
        "description": "description",
        "http2_enable": "http2Enable",
        "id": "id",
        "insert_headers": "insertHeaders",
        "keep_alive_timeout": "keepAliveTimeout",
        "member_retry_enable": "memberRetryEnable",
        "member_timeout": "memberTimeout",
        "name": "name",
        "sni_container_refs": "sniContainerRefs",
        "tags": "tags",
        "tls_ciphers_policy": "tlsCiphersPolicy",
    },
)
class LbListenerV3Config(cdktf.TerraformMetaArguments):
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
        loadbalancer_id: builtins.str,
        protocol: builtins.str,
        protocol_port: jsii.Number,
        admin_state_up: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        client_ca_tls_container_ref: typing.Optional[builtins.str] = None,
        client_timeout: typing.Optional[jsii.Number] = None,
        default_pool_id: typing.Optional[builtins.str] = None,
        default_tls_container_ref: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        http2_enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        insert_headers: typing.Optional[typing.Union["LbListenerV3InsertHeaders", typing.Dict[str, typing.Any]]] = None,
        keep_alive_timeout: typing.Optional[jsii.Number] = None,
        member_retry_enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        member_timeout: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        sni_container_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tls_ciphers_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param loadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#loadbalancer_id LbListenerV3#loadbalancer_id}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#protocol LbListenerV3#protocol}.
        :param protocol_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#protocol_port LbListenerV3#protocol_port}.
        :param admin_state_up: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#admin_state_up LbListenerV3#admin_state_up}.
        :param client_ca_tls_container_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#client_ca_tls_container_ref LbListenerV3#client_ca_tls_container_ref}.
        :param client_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#client_timeout LbListenerV3#client_timeout}.
        :param default_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#default_pool_id LbListenerV3#default_pool_id}.
        :param default_tls_container_ref: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#default_tls_container_ref LbListenerV3#default_tls_container_ref}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#description LbListenerV3#description}.
        :param http2_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#http2_enable LbListenerV3#http2_enable}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#id LbListenerV3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insert_headers: insert_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#insert_headers LbListenerV3#insert_headers}
        :param keep_alive_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#keep_alive_timeout LbListenerV3#keep_alive_timeout}.
        :param member_retry_enable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#member_retry_enable LbListenerV3#member_retry_enable}.
        :param member_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#member_timeout LbListenerV3#member_timeout}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#name LbListenerV3#name}.
        :param sni_container_refs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#sni_container_refs LbListenerV3#sni_container_refs}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#tags LbListenerV3#tags}.
        :param tls_ciphers_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#tls_ciphers_policy LbListenerV3#tls_ciphers_policy}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(insert_headers, dict):
            insert_headers = LbListenerV3InsertHeaders(**insert_headers)
        if __debug__:
            type_hints = typing.get_type_hints(LbListenerV3Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument loadbalancer_id", value=loadbalancer_id, expected_type=type_hints["loadbalancer_id"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument protocol_port", value=protocol_port, expected_type=type_hints["protocol_port"])
            check_type(argname="argument admin_state_up", value=admin_state_up, expected_type=type_hints["admin_state_up"])
            check_type(argname="argument client_ca_tls_container_ref", value=client_ca_tls_container_ref, expected_type=type_hints["client_ca_tls_container_ref"])
            check_type(argname="argument client_timeout", value=client_timeout, expected_type=type_hints["client_timeout"])
            check_type(argname="argument default_pool_id", value=default_pool_id, expected_type=type_hints["default_pool_id"])
            check_type(argname="argument default_tls_container_ref", value=default_tls_container_ref, expected_type=type_hints["default_tls_container_ref"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument http2_enable", value=http2_enable, expected_type=type_hints["http2_enable"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument insert_headers", value=insert_headers, expected_type=type_hints["insert_headers"])
            check_type(argname="argument keep_alive_timeout", value=keep_alive_timeout, expected_type=type_hints["keep_alive_timeout"])
            check_type(argname="argument member_retry_enable", value=member_retry_enable, expected_type=type_hints["member_retry_enable"])
            check_type(argname="argument member_timeout", value=member_timeout, expected_type=type_hints["member_timeout"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sni_container_refs", value=sni_container_refs, expected_type=type_hints["sni_container_refs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tls_ciphers_policy", value=tls_ciphers_policy, expected_type=type_hints["tls_ciphers_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "loadbalancer_id": loadbalancer_id,
            "protocol": protocol,
            "protocol_port": protocol_port,
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
        if client_ca_tls_container_ref is not None:
            self._values["client_ca_tls_container_ref"] = client_ca_tls_container_ref
        if client_timeout is not None:
            self._values["client_timeout"] = client_timeout
        if default_pool_id is not None:
            self._values["default_pool_id"] = default_pool_id
        if default_tls_container_ref is not None:
            self._values["default_tls_container_ref"] = default_tls_container_ref
        if description is not None:
            self._values["description"] = description
        if http2_enable is not None:
            self._values["http2_enable"] = http2_enable
        if id is not None:
            self._values["id"] = id
        if insert_headers is not None:
            self._values["insert_headers"] = insert_headers
        if keep_alive_timeout is not None:
            self._values["keep_alive_timeout"] = keep_alive_timeout
        if member_retry_enable is not None:
            self._values["member_retry_enable"] = member_retry_enable
        if member_timeout is not None:
            self._values["member_timeout"] = member_timeout
        if name is not None:
            self._values["name"] = name
        if sni_container_refs is not None:
            self._values["sni_container_refs"] = sni_container_refs
        if tags is not None:
            self._values["tags"] = tags
        if tls_ciphers_policy is not None:
            self._values["tls_ciphers_policy"] = tls_ciphers_policy

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
    def loadbalancer_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#loadbalancer_id LbListenerV3#loadbalancer_id}.'''
        result = self._values.get("loadbalancer_id")
        assert result is not None, "Required property 'loadbalancer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#protocol LbListenerV3#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#protocol_port LbListenerV3#protocol_port}.'''
        result = self._values.get("protocol_port")
        assert result is not None, "Required property 'protocol_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def admin_state_up(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#admin_state_up LbListenerV3#admin_state_up}.'''
        result = self._values.get("admin_state_up")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def client_ca_tls_container_ref(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#client_ca_tls_container_ref LbListenerV3#client_ca_tls_container_ref}.'''
        result = self._values.get("client_ca_tls_container_ref")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#client_timeout LbListenerV3#client_timeout}.'''
        result = self._values.get("client_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_pool_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#default_pool_id LbListenerV3#default_pool_id}.'''
        result = self._values.get("default_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_tls_container_ref(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#default_tls_container_ref LbListenerV3#default_tls_container_ref}.'''
        result = self._values.get("default_tls_container_ref")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#description LbListenerV3#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2_enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#http2_enable LbListenerV3#http2_enable}.'''
        result = self._values.get("http2_enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#id LbListenerV3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insert_headers(self) -> typing.Optional["LbListenerV3InsertHeaders"]:
        '''insert_headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#insert_headers LbListenerV3#insert_headers}
        '''
        result = self._values.get("insert_headers")
        return typing.cast(typing.Optional["LbListenerV3InsertHeaders"], result)

    @builtins.property
    def keep_alive_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#keep_alive_timeout LbListenerV3#keep_alive_timeout}.'''
        result = self._values.get("keep_alive_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def member_retry_enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#member_retry_enable LbListenerV3#member_retry_enable}.'''
        result = self._values.get("member_retry_enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def member_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#member_timeout LbListenerV3#member_timeout}.'''
        result = self._values.get("member_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#name LbListenerV3#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sni_container_refs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#sni_container_refs LbListenerV3#sni_container_refs}.'''
        result = self._values.get("sni_container_refs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#tags LbListenerV3#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tls_ciphers_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#tls_ciphers_policy LbListenerV3#tls_ciphers_policy}.'''
        result = self._values.get("tls_ciphers_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerV3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.lbListenerV3.LbListenerV3InsertHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "forwarded_for_port": "forwardedForPort",
        "forwarded_host": "forwardedHost",
        "forwarded_port": "forwardedPort",
        "forward_elb_ip": "forwardElbIp",
    },
)
class LbListenerV3InsertHeaders:
    def __init__(
        self,
        *,
        forwarded_for_port: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarded_host: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarded_port: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forward_elb_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param forwarded_for_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_for_port LbListenerV3#forwarded_for_port}.
        :param forwarded_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_host LbListenerV3#forwarded_host}.
        :param forwarded_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_port LbListenerV3#forwarded_port}.
        :param forward_elb_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forward_elb_ip LbListenerV3#forward_elb_ip}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LbListenerV3InsertHeaders.__init__)
            check_type(argname="argument forwarded_for_port", value=forwarded_for_port, expected_type=type_hints["forwarded_for_port"])
            check_type(argname="argument forwarded_host", value=forwarded_host, expected_type=type_hints["forwarded_host"])
            check_type(argname="argument forwarded_port", value=forwarded_port, expected_type=type_hints["forwarded_port"])
            check_type(argname="argument forward_elb_ip", value=forward_elb_ip, expected_type=type_hints["forward_elb_ip"])
        self._values: typing.Dict[str, typing.Any] = {}
        if forwarded_for_port is not None:
            self._values["forwarded_for_port"] = forwarded_for_port
        if forwarded_host is not None:
            self._values["forwarded_host"] = forwarded_host
        if forwarded_port is not None:
            self._values["forwarded_port"] = forwarded_port
        if forward_elb_ip is not None:
            self._values["forward_elb_ip"] = forward_elb_ip

    @builtins.property
    def forwarded_for_port(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_for_port LbListenerV3#forwarded_for_port}.'''
        result = self._values.get("forwarded_for_port")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarded_host(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_host LbListenerV3#forwarded_host}.'''
        result = self._values.get("forwarded_host")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarded_port(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forwarded_port LbListenerV3#forwarded_port}.'''
        result = self._values.get("forwarded_port")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forward_elb_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/lb_listener_v3#forward_elb_ip LbListenerV3#forward_elb_ip}.'''
        result = self._values.get("forward_elb_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LbListenerV3InsertHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LbListenerV3InsertHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.lbListenerV3.LbListenerV3InsertHeadersOutputReference",
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
            type_hints = typing.get_type_hints(LbListenerV3InsertHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetForwardedForPort")
    def reset_forwarded_for_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedForPort", []))

    @jsii.member(jsii_name="resetForwardedHost")
    def reset_forwarded_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedHost", []))

    @jsii.member(jsii_name="resetForwardedPort")
    def reset_forwarded_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardedPort", []))

    @jsii.member(jsii_name="resetForwardElbIp")
    def reset_forward_elb_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardElbIp", []))

    @builtins.property
    @jsii.member(jsii_name="forwardedForPortInput")
    def forwarded_for_port_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forwardedForPortInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedHostInput")
    def forwarded_host_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forwardedHostInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedPortInput")
    def forwarded_port_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forwardedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardElbIpInput")
    def forward_elb_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forwardElbIpInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardedForPort")
    def forwarded_for_port(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forwardedForPort"))

    @forwarded_for_port.setter
    def forwarded_for_port(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3InsertHeadersOutputReference, "forwarded_for_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardedForPort", value)

    @builtins.property
    @jsii.member(jsii_name="forwardedHost")
    def forwarded_host(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forwardedHost"))

    @forwarded_host.setter
    def forwarded_host(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3InsertHeadersOutputReference, "forwarded_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardedHost", value)

    @builtins.property
    @jsii.member(jsii_name="forwardedPort")
    def forwarded_port(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forwardedPort"))

    @forwarded_port.setter
    def forwarded_port(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3InsertHeadersOutputReference, "forwarded_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardedPort", value)

    @builtins.property
    @jsii.member(jsii_name="forwardElbIp")
    def forward_elb_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forwardElbIp"))

    @forward_elb_ip.setter
    def forward_elb_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3InsertHeadersOutputReference, "forward_elb_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardElbIp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LbListenerV3InsertHeaders]:
        return typing.cast(typing.Optional[LbListenerV3InsertHeaders], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LbListenerV3InsertHeaders]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LbListenerV3InsertHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LbListenerV3",
    "LbListenerV3Config",
    "LbListenerV3InsertHeaders",
    "LbListenerV3InsertHeadersOutputReference",
]

publication.publish()
