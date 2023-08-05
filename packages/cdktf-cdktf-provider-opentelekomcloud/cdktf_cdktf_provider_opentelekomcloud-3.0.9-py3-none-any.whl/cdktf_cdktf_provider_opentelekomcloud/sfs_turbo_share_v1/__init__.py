'''
# `opentelekomcloud_sfs_turbo_share_v1`

Refer to the Terraform Registory for docs: [`opentelekomcloud_sfs_turbo_share_v1`](https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1).
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


class SfsTurboShareV1(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.sfsTurboShareV1.SfsTurboShareV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1 opentelekomcloud_sfs_turbo_share_v1}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        availability_zone: builtins.str,
        name: builtins.str,
        security_group_id: builtins.str,
        size: jsii.Number,
        subnet_id: builtins.str,
        vpc_id: builtins.str,
        crypt_key_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        share_proto: typing.Optional[builtins.str] = None,
        share_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SfsTurboShareV1Timeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1 opentelekomcloud_sfs_turbo_share_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#availability_zone SfsTurboShareV1#availability_zone}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#name SfsTurboShareV1#name}.
        :param security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#security_group_id SfsTurboShareV1#security_group_id}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#size SfsTurboShareV1#size}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#subnet_id SfsTurboShareV1#subnet_id}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#vpc_id SfsTurboShareV1#vpc_id}.
        :param crypt_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#crypt_key_id SfsTurboShareV1#crypt_key_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#id SfsTurboShareV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#region SfsTurboShareV1#region}.
        :param share_proto: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#share_proto SfsTurboShareV1#share_proto}.
        :param share_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#share_type SfsTurboShareV1#share_type}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#timeouts SfsTurboShareV1#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SfsTurboShareV1.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SfsTurboShareV1Config(
            availability_zone=availability_zone,
            name=name,
            security_group_id=security_group_id,
            size=size,
            subnet_id=subnet_id,
            vpc_id=vpc_id,
            crypt_key_id=crypt_key_id,
            id=id,
            region=region,
            share_proto=share_proto,
            share_type=share_type,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#create SfsTurboShareV1#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#delete SfsTurboShareV1#delete}.
        '''
        value = SfsTurboShareV1Timeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCryptKeyId")
    def reset_crypt_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCryptKeyId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetShareProto")
    def reset_share_proto(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareProto", []))

    @jsii.member(jsii_name="resetShareType")
    def reset_share_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareType", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="availableCapacity")
    def available_capacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availableCapacity"))

    @builtins.property
    @jsii.member(jsii_name="exportLocation")
    def export_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exportLocation"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SfsTurboShareV1TimeoutsOutputReference":
        return typing.cast("SfsTurboShareV1TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneInput")
    def availability_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="cryptKeyIdInput")
    def crypt_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cryptKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdInput")
    def security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="shareProtoInput")
    def share_proto_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareProtoInput"))

    @builtins.property
    @jsii.member(jsii_name="shareTypeInput")
    def share_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SfsTurboShareV1Timeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SfsTurboShareV1Timeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "availability_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="cryptKeyId")
    def crypt_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cryptKeyId"))

    @crypt_key_id.setter
    def crypt_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "crypt_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cryptKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupId"))

    @security_group_id.setter
    def security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "security_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="shareProto")
    def share_proto(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareProto"))

    @share_proto.setter
    def share_proto(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "share_proto").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareProto", value)

    @builtins.property
    @jsii.member(jsii_name="shareType")
    def share_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareType"))

    @share_type.setter
    def share_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "share_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareType", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1, "vpc_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.sfsTurboShareV1.SfsTurboShareV1Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "availability_zone": "availabilityZone",
        "name": "name",
        "security_group_id": "securityGroupId",
        "size": "size",
        "subnet_id": "subnetId",
        "vpc_id": "vpcId",
        "crypt_key_id": "cryptKeyId",
        "id": "id",
        "region": "region",
        "share_proto": "shareProto",
        "share_type": "shareType",
        "timeouts": "timeouts",
    },
)
class SfsTurboShareV1Config(cdktf.TerraformMetaArguments):
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
        availability_zone: builtins.str,
        name: builtins.str,
        security_group_id: builtins.str,
        size: jsii.Number,
        subnet_id: builtins.str,
        vpc_id: builtins.str,
        crypt_key_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        share_proto: typing.Optional[builtins.str] = None,
        share_type: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SfsTurboShareV1Timeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param availability_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#availability_zone SfsTurboShareV1#availability_zone}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#name SfsTurboShareV1#name}.
        :param security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#security_group_id SfsTurboShareV1#security_group_id}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#size SfsTurboShareV1#size}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#subnet_id SfsTurboShareV1#subnet_id}.
        :param vpc_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#vpc_id SfsTurboShareV1#vpc_id}.
        :param crypt_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#crypt_key_id SfsTurboShareV1#crypt_key_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#id SfsTurboShareV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#region SfsTurboShareV1#region}.
        :param share_proto: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#share_proto SfsTurboShareV1#share_proto}.
        :param share_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#share_type SfsTurboShareV1#share_type}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#timeouts SfsTurboShareV1#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SfsTurboShareV1Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SfsTurboShareV1Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument crypt_key_id", value=crypt_key_id, expected_type=type_hints["crypt_key_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument share_proto", value=share_proto, expected_type=type_hints["share_proto"])
            check_type(argname="argument share_type", value=share_type, expected_type=type_hints["share_type"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "availability_zone": availability_zone,
            "name": name,
            "security_group_id": security_group_id,
            "size": size,
            "subnet_id": subnet_id,
            "vpc_id": vpc_id,
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
        if crypt_key_id is not None:
            self._values["crypt_key_id"] = crypt_key_id
        if id is not None:
            self._values["id"] = id
        if region is not None:
            self._values["region"] = region
        if share_proto is not None:
            self._values["share_proto"] = share_proto
        if share_type is not None:
            self._values["share_type"] = share_type
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def availability_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#availability_zone SfsTurboShareV1#availability_zone}.'''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#name SfsTurboShareV1#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#security_group_id SfsTurboShareV1#security_group_id}.'''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#size SfsTurboShareV1#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#subnet_id SfsTurboShareV1#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#vpc_id SfsTurboShareV1#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def crypt_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#crypt_key_id SfsTurboShareV1#crypt_key_id}.'''
        result = self._values.get("crypt_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#id SfsTurboShareV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#region SfsTurboShareV1#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def share_proto(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#share_proto SfsTurboShareV1#share_proto}.'''
        result = self._values.get("share_proto")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def share_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#share_type SfsTurboShareV1#share_type}.'''
        result = self._values.get("share_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SfsTurboShareV1Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#timeouts SfsTurboShareV1#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SfsTurboShareV1Timeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SfsTurboShareV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.sfsTurboShareV1.SfsTurboShareV1Timeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class SfsTurboShareV1Timeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#create SfsTurboShareV1#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#delete SfsTurboShareV1#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SfsTurboShareV1Timeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#create SfsTurboShareV1#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/r/sfs_turbo_share_v1#delete SfsTurboShareV1#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SfsTurboShareV1Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SfsTurboShareV1TimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.sfsTurboShareV1.SfsTurboShareV1TimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SfsTurboShareV1TimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1TimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1TimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SfsTurboShareV1Timeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SfsTurboShareV1Timeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SfsTurboShareV1Timeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SfsTurboShareV1TimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SfsTurboShareV1",
    "SfsTurboShareV1Config",
    "SfsTurboShareV1Timeouts",
    "SfsTurboShareV1TimeoutsOutputReference",
]

publication.publish()
