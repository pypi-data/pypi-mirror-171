'''
# `data_opentelekomcloud_vbs_backup_policy_v2`

Refer to the Terraform Registory for docs: [`data_opentelekomcloud_vbs_backup_policy_v2`](https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2).
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


class DataOpentelekomcloudVbsBackupPolicyV2(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2 opentelekomcloud_vbs_backup_policy_v2}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        filter_tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataOpentelekomcloudVbsBackupPolicyV2FilterTags", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policy_resource_count: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2 opentelekomcloud_vbs_backup_policy_v2} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param filter_tags: filter_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#filter_tags DataOpentelekomcloudVbsBackupPolicyV2#filter_tags}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#id DataOpentelekomcloudVbsBackupPolicyV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#name DataOpentelekomcloudVbsBackupPolicyV2#name}.
        :param policy_resource_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#policy_resource_count DataOpentelekomcloudVbsBackupPolicyV2#policy_resource_count}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#region DataOpentelekomcloudVbsBackupPolicyV2#region}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#status DataOpentelekomcloudVbsBackupPolicyV2#status}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataOpentelekomcloudVbsBackupPolicyV2Config(
            filter_tags=filter_tags,
            id=id,
            name=name,
            policy_resource_count=policy_resource_count,
            region=region,
            status=status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFilterTags")
    def put_filter_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataOpentelekomcloudVbsBackupPolicyV2FilterTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2.put_filter_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilterTags", [value]))

    @jsii.member(jsii_name="resetFilterTags")
    def reset_filter_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterTags", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPolicyResourceCount")
    def reset_policy_resource_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyResourceCount", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="filterTags")
    def filter_tags(self) -> "DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList":
        return typing.cast("DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList", jsii.get(self, "filterTags"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequency"))

    @builtins.property
    @jsii.member(jsii_name="remainFirstBackup")
    def remain_first_backup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remainFirstBackup"))

    @builtins.property
    @jsii.member(jsii_name="rententionNum")
    def rentention_num(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rententionNum"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "DataOpentelekomcloudVbsBackupPolicyV2TagsList":
        return typing.cast("DataOpentelekomcloudVbsBackupPolicyV2TagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="filterTagsInput")
    def filter_tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataOpentelekomcloudVbsBackupPolicyV2FilterTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataOpentelekomcloudVbsBackupPolicyV2FilterTags"]]], jsii.get(self, "filterTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyResourceCountInput")
    def policy_resource_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyResourceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyResourceCount")
    def policy_resource_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyResourceCount"))

    @policy_resource_count.setter
    def policy_resource_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2, "policy_resource_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyResourceCount", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "filter_tags": "filterTags",
        "id": "id",
        "name": "name",
        "policy_resource_count": "policyResourceCount",
        "region": "region",
        "status": "status",
    },
)
class DataOpentelekomcloudVbsBackupPolicyV2Config(cdktf.TerraformMetaArguments):
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
        filter_tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DataOpentelekomcloudVbsBackupPolicyV2FilterTags", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        policy_resource_count: typing.Optional[jsii.Number] = None,
        region: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param filter_tags: filter_tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#filter_tags DataOpentelekomcloudVbsBackupPolicyV2#filter_tags}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#id DataOpentelekomcloudVbsBackupPolicyV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#name DataOpentelekomcloudVbsBackupPolicyV2#name}.
        :param policy_resource_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#policy_resource_count DataOpentelekomcloudVbsBackupPolicyV2#policy_resource_count}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#region DataOpentelekomcloudVbsBackupPolicyV2#region}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#status DataOpentelekomcloudVbsBackupPolicyV2#status}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument filter_tags", value=filter_tags, expected_type=type_hints["filter_tags"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_resource_count", value=policy_resource_count, expected_type=type_hints["policy_resource_count"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
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
        if filter_tags is not None:
            self._values["filter_tags"] = filter_tags
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if policy_resource_count is not None:
            self._values["policy_resource_count"] = policy_resource_count
        if region is not None:
            self._values["region"] = region
        if status is not None:
            self._values["status"] = status

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
    def filter_tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataOpentelekomcloudVbsBackupPolicyV2FilterTags"]]]:
        '''filter_tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#filter_tags DataOpentelekomcloudVbsBackupPolicyV2#filter_tags}
        '''
        result = self._values.get("filter_tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DataOpentelekomcloudVbsBackupPolicyV2FilterTags"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#id DataOpentelekomcloudVbsBackupPolicyV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#name DataOpentelekomcloudVbsBackupPolicyV2#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_resource_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#policy_resource_count DataOpentelekomcloudVbsBackupPolicyV2#policy_resource_count}.'''
        result = self._values.get("policy_resource_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#region DataOpentelekomcloudVbsBackupPolicyV2#region}.'''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#status DataOpentelekomcloudVbsBackupPolicyV2#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataOpentelekomcloudVbsBackupPolicyV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2FilterTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "values": "values"},
)
class DataOpentelekomcloudVbsBackupPolicyV2FilterTags:
    def __init__(
        self,
        *,
        key: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#key DataOpentelekomcloudVbsBackupPolicyV2#key}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#values DataOpentelekomcloudVbsBackupPolicyV2#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2FilterTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "values": values,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#key DataOpentelekomcloudVbsBackupPolicyV2#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opentelekomcloud/d/vbs_backup_policy_v2#values DataOpentelekomcloudVbsBackupPolicyV2#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataOpentelekomcloudVbsBackupPolicyV2FilterTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList",
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
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataOpentelekomcloudVbsBackupPolicyV2FilterTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataOpentelekomcloudVbsBackupPolicyV2FilterTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DataOpentelekomcloudVbsBackupPolicyV2FilterTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference",
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
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataOpentelekomcloudVbsBackupPolicyV2FilterTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataOpentelekomcloudVbsBackupPolicyV2FilterTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataOpentelekomcloudVbsBackupPolicyV2FilterTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2Tags",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataOpentelekomcloudVbsBackupPolicyV2Tags:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataOpentelekomcloudVbsBackupPolicyV2Tags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataOpentelekomcloudVbsBackupPolicyV2TagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2TagsList",
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
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2TagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2TagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2TagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2TagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2TagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opentelekomcloud.dataOpentelekomcloudVbsBackupPolicyV2.DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference",
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
            type_hints = typing.get_type_hints(DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataOpentelekomcloudVbsBackupPolicyV2Tags]:
        return typing.cast(typing.Optional[DataOpentelekomcloudVbsBackupPolicyV2Tags], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataOpentelekomcloudVbsBackupPolicyV2Tags],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataOpentelekomcloudVbsBackupPolicyV2",
    "DataOpentelekomcloudVbsBackupPolicyV2Config",
    "DataOpentelekomcloudVbsBackupPolicyV2FilterTags",
    "DataOpentelekomcloudVbsBackupPolicyV2FilterTagsList",
    "DataOpentelekomcloudVbsBackupPolicyV2FilterTagsOutputReference",
    "DataOpentelekomcloudVbsBackupPolicyV2Tags",
    "DataOpentelekomcloudVbsBackupPolicyV2TagsList",
    "DataOpentelekomcloudVbsBackupPolicyV2TagsOutputReference",
]

publication.publish()
