'''
# `vsphere_datastore_cluster`

Refer to the Terraform Registory for docs: [`vsphere_datastore_cluster`](https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster).
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


class DatastoreCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.datastoreCluster.DatastoreCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster vsphere_datastore_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datacenter_id: builtins.str,
        name: builtins.str,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        sdrs_advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sdrs_automation_level: typing.Optional[builtins.str] = None,
        sdrs_default_intra_vm_affinity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sdrs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sdrs_free_space_threshold: typing.Optional[jsii.Number] = None,
        sdrs_free_space_threshold_mode: typing.Optional[builtins.str] = None,
        sdrs_free_space_utilization_difference: typing.Optional[jsii.Number] = None,
        sdrs_io_balance_automation_level: typing.Optional[builtins.str] = None,
        sdrs_io_latency_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_load_balance_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sdrs_io_load_imbalance_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_reservable_iops_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_reservable_percent_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_reservable_threshold_mode: typing.Optional[builtins.str] = None,
        sdrs_load_balance_interval: typing.Optional[jsii.Number] = None,
        sdrs_policy_enforcement_automation_level: typing.Optional[builtins.str] = None,
        sdrs_rule_enforcement_automation_level: typing.Optional[builtins.str] = None,
        sdrs_space_balance_automation_level: typing.Optional[builtins.str] = None,
        sdrs_space_utilization_threshold: typing.Optional[jsii.Number] = None,
        sdrs_vm_evacuation_automation_level: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster vsphere_datastore_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datacenter_id: The managed object ID of the datacenter to put the datastore cluster in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#datacenter_id DatastoreCluster#datacenter_id}
        :param name: Name for the new storage pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#name DatastoreCluster#name}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#custom_attributes DatastoreCluster#custom_attributes}
        :param folder: The name of the folder to locate the datastore cluster in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#folder DatastoreCluster#folder}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#id DatastoreCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sdrs_advanced_options: Advanced configuration options for storage DRS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_advanced_options DatastoreCluster#sdrs_advanced_options}
        :param sdrs_automation_level: The default automation level for all virtual machines in this storage cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_automation_level DatastoreCluster#sdrs_automation_level}
        :param sdrs_default_intra_vm_affinity: When true, storage DRS keeps VMDKs for individual VMs on the same datastore by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_default_intra_vm_affinity DatastoreCluster#sdrs_default_intra_vm_affinity}
        :param sdrs_enabled: Enable storage DRS for this datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_enabled DatastoreCluster#sdrs_enabled}
        :param sdrs_free_space_threshold: The threshold, in GB, that storage DRS uses to make decisions to migrate VMs out of a datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_threshold DatastoreCluster#sdrs_free_space_threshold}
        :param sdrs_free_space_threshold_mode: The free space threshold to use. When set to utilization, drs_space_utilization_threshold is used, and when set to freeSpace, drs_free_space_threshold is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_threshold_mode DatastoreCluster#sdrs_free_space_threshold_mode}
        :param sdrs_free_space_utilization_difference: The threshold, in percent, of difference between space utilization in datastores before storage DRS makes decisions to balance the space. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_utilization_difference DatastoreCluster#sdrs_free_space_utilization_difference}
        :param sdrs_io_balance_automation_level: Overrides the default automation settings when correcting I/O load imbalances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_balance_automation_level DatastoreCluster#sdrs_io_balance_automation_level}
        :param sdrs_io_latency_threshold: The I/O latency threshold, in milliseconds, that storage DRS uses to make recommendations to move disks from this datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_latency_threshold DatastoreCluster#sdrs_io_latency_threshold}
        :param sdrs_io_load_balance_enabled: Enable I/O load balancing for this datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_load_balance_enabled DatastoreCluster#sdrs_io_load_balance_enabled}
        :param sdrs_io_load_imbalance_threshold: The difference between load in datastores in the cluster before storage DRS makes recommendations to balance the load. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_load_imbalance_threshold DatastoreCluster#sdrs_io_load_imbalance_threshold}
        :param sdrs_io_reservable_iops_threshold: The threshold of reservable IOPS of all virtual machines on the datastore before storage DRS makes recommendations to move VMs off of a datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_iops_threshold DatastoreCluster#sdrs_io_reservable_iops_threshold}
        :param sdrs_io_reservable_percent_threshold: The threshold, in percent, of actual estimated performance of the datastore (in IOPS) that storage DRS uses to make recommendations to move VMs off of a datastore when the total reservable IOPS exceeds the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_percent_threshold DatastoreCluster#sdrs_io_reservable_percent_threshold}
        :param sdrs_io_reservable_threshold_mode: The reservable IOPS threshold to use, percent in the event of automatic, or manual threshold in the event of manual. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_threshold_mode DatastoreCluster#sdrs_io_reservable_threshold_mode}
        :param sdrs_load_balance_interval: The storage DRS poll interval, in minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_load_balance_interval DatastoreCluster#sdrs_load_balance_interval}
        :param sdrs_policy_enforcement_automation_level: Overrides the default automation settings when correcting storage and VM policy violations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_policy_enforcement_automation_level DatastoreCluster#sdrs_policy_enforcement_automation_level}
        :param sdrs_rule_enforcement_automation_level: Overrides the default automation settings when correcting affinity rule violations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_rule_enforcement_automation_level DatastoreCluster#sdrs_rule_enforcement_automation_level}
        :param sdrs_space_balance_automation_level: Overrides the default automation settings when correcting disk space imbalances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_space_balance_automation_level DatastoreCluster#sdrs_space_balance_automation_level}
        :param sdrs_space_utilization_threshold: The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_space_utilization_threshold DatastoreCluster#sdrs_space_utilization_threshold}
        :param sdrs_vm_evacuation_automation_level: Overrides the default automation settings when generating recommendations for datastore evacuation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_vm_evacuation_automation_level DatastoreCluster#sdrs_vm_evacuation_automation_level}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#tags DatastoreCluster#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatastoreCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatastoreClusterConfig(
            datacenter_id=datacenter_id,
            name=name,
            custom_attributes=custom_attributes,
            folder=folder,
            id=id,
            sdrs_advanced_options=sdrs_advanced_options,
            sdrs_automation_level=sdrs_automation_level,
            sdrs_default_intra_vm_affinity=sdrs_default_intra_vm_affinity,
            sdrs_enabled=sdrs_enabled,
            sdrs_free_space_threshold=sdrs_free_space_threshold,
            sdrs_free_space_threshold_mode=sdrs_free_space_threshold_mode,
            sdrs_free_space_utilization_difference=sdrs_free_space_utilization_difference,
            sdrs_io_balance_automation_level=sdrs_io_balance_automation_level,
            sdrs_io_latency_threshold=sdrs_io_latency_threshold,
            sdrs_io_load_balance_enabled=sdrs_io_load_balance_enabled,
            sdrs_io_load_imbalance_threshold=sdrs_io_load_imbalance_threshold,
            sdrs_io_reservable_iops_threshold=sdrs_io_reservable_iops_threshold,
            sdrs_io_reservable_percent_threshold=sdrs_io_reservable_percent_threshold,
            sdrs_io_reservable_threshold_mode=sdrs_io_reservable_threshold_mode,
            sdrs_load_balance_interval=sdrs_load_balance_interval,
            sdrs_policy_enforcement_automation_level=sdrs_policy_enforcement_automation_level,
            sdrs_rule_enforcement_automation_level=sdrs_rule_enforcement_automation_level,
            sdrs_space_balance_automation_level=sdrs_space_balance_automation_level,
            sdrs_space_utilization_threshold=sdrs_space_utilization_threshold,
            sdrs_vm_evacuation_automation_level=sdrs_vm_evacuation_automation_level,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCustomAttributes")
    def reset_custom_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAttributes", []))

    @jsii.member(jsii_name="resetFolder")
    def reset_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFolder", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSdrsAdvancedOptions")
    def reset_sdrs_advanced_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsAdvancedOptions", []))

    @jsii.member(jsii_name="resetSdrsAutomationLevel")
    def reset_sdrs_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsAutomationLevel", []))

    @jsii.member(jsii_name="resetSdrsDefaultIntraVmAffinity")
    def reset_sdrs_default_intra_vm_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsDefaultIntraVmAffinity", []))

    @jsii.member(jsii_name="resetSdrsEnabled")
    def reset_sdrs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsEnabled", []))

    @jsii.member(jsii_name="resetSdrsFreeSpaceThreshold")
    def reset_sdrs_free_space_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsFreeSpaceThreshold", []))

    @jsii.member(jsii_name="resetSdrsFreeSpaceThresholdMode")
    def reset_sdrs_free_space_threshold_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsFreeSpaceThresholdMode", []))

    @jsii.member(jsii_name="resetSdrsFreeSpaceUtilizationDifference")
    def reset_sdrs_free_space_utilization_difference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsFreeSpaceUtilizationDifference", []))

    @jsii.member(jsii_name="resetSdrsIoBalanceAutomationLevel")
    def reset_sdrs_io_balance_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoBalanceAutomationLevel", []))

    @jsii.member(jsii_name="resetSdrsIoLatencyThreshold")
    def reset_sdrs_io_latency_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoLatencyThreshold", []))

    @jsii.member(jsii_name="resetSdrsIoLoadBalanceEnabled")
    def reset_sdrs_io_load_balance_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoLoadBalanceEnabled", []))

    @jsii.member(jsii_name="resetSdrsIoLoadImbalanceThreshold")
    def reset_sdrs_io_load_imbalance_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoLoadImbalanceThreshold", []))

    @jsii.member(jsii_name="resetSdrsIoReservableIopsThreshold")
    def reset_sdrs_io_reservable_iops_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoReservableIopsThreshold", []))

    @jsii.member(jsii_name="resetSdrsIoReservablePercentThreshold")
    def reset_sdrs_io_reservable_percent_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoReservablePercentThreshold", []))

    @jsii.member(jsii_name="resetSdrsIoReservableThresholdMode")
    def reset_sdrs_io_reservable_threshold_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsIoReservableThresholdMode", []))

    @jsii.member(jsii_name="resetSdrsLoadBalanceInterval")
    def reset_sdrs_load_balance_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsLoadBalanceInterval", []))

    @jsii.member(jsii_name="resetSdrsPolicyEnforcementAutomationLevel")
    def reset_sdrs_policy_enforcement_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsPolicyEnforcementAutomationLevel", []))

    @jsii.member(jsii_name="resetSdrsRuleEnforcementAutomationLevel")
    def reset_sdrs_rule_enforcement_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsRuleEnforcementAutomationLevel", []))

    @jsii.member(jsii_name="resetSdrsSpaceBalanceAutomationLevel")
    def reset_sdrs_space_balance_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsSpaceBalanceAutomationLevel", []))

    @jsii.member(jsii_name="resetSdrsSpaceUtilizationThreshold")
    def reset_sdrs_space_utilization_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsSpaceUtilizationThreshold", []))

    @jsii.member(jsii_name="resetSdrsVmEvacuationAutomationLevel")
    def reset_sdrs_vm_evacuation_automation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSdrsVmEvacuationAutomationLevel", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsAdvancedOptionsInput")
    def sdrs_advanced_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sdrsAdvancedOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsAutomationLevelInput")
    def sdrs_automation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsDefaultIntraVmAffinityInput")
    def sdrs_default_intra_vm_affinity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sdrsDefaultIntraVmAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsEnabledInput")
    def sdrs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sdrsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsFreeSpaceThresholdInput")
    def sdrs_free_space_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsFreeSpaceThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsFreeSpaceThresholdModeInput")
    def sdrs_free_space_threshold_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsFreeSpaceThresholdModeInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsFreeSpaceUtilizationDifferenceInput")
    def sdrs_free_space_utilization_difference_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsFreeSpaceUtilizationDifferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoBalanceAutomationLevelInput")
    def sdrs_io_balance_automation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsIoBalanceAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoLatencyThresholdInput")
    def sdrs_io_latency_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsIoLatencyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoLoadBalanceEnabledInput")
    def sdrs_io_load_balance_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sdrsIoLoadBalanceEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoLoadImbalanceThresholdInput")
    def sdrs_io_load_imbalance_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsIoLoadImbalanceThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoReservableIopsThresholdInput")
    def sdrs_io_reservable_iops_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsIoReservableIopsThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoReservablePercentThresholdInput")
    def sdrs_io_reservable_percent_threshold_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsIoReservablePercentThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsIoReservableThresholdModeInput")
    def sdrs_io_reservable_threshold_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsIoReservableThresholdModeInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsLoadBalanceIntervalInput")
    def sdrs_load_balance_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsLoadBalanceIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsPolicyEnforcementAutomationLevelInput")
    def sdrs_policy_enforcement_automation_level_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsPolicyEnforcementAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsRuleEnforcementAutomationLevelInput")
    def sdrs_rule_enforcement_automation_level_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsRuleEnforcementAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsSpaceBalanceAutomationLevelInput")
    def sdrs_space_balance_automation_level_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsSpaceBalanceAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsSpaceUtilizationThresholdInput")
    def sdrs_space_utilization_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sdrsSpaceUtilizationThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sdrsVmEvacuationAutomationLevelInput")
    def sdrs_vm_evacuation_automation_level_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sdrsVmEvacuationAutomationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributes")
    def custom_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customAttributes"))

    @custom_attributes.setter
    def custom_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "custom_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "folder").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsAdvancedOptions")
    def sdrs_advanced_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sdrsAdvancedOptions"))

    @sdrs_advanced_options.setter
    def sdrs_advanced_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_advanced_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsAdvancedOptions", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsAutomationLevel")
    def sdrs_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsAutomationLevel"))

    @sdrs_automation_level.setter
    def sdrs_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsDefaultIntraVmAffinity")
    def sdrs_default_intra_vm_affinity(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sdrsDefaultIntraVmAffinity"))

    @sdrs_default_intra_vm_affinity.setter
    def sdrs_default_intra_vm_affinity(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_default_intra_vm_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsDefaultIntraVmAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsEnabled")
    def sdrs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sdrsEnabled"))

    @sdrs_enabled.setter
    def sdrs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsFreeSpaceThreshold")
    def sdrs_free_space_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsFreeSpaceThreshold"))

    @sdrs_free_space_threshold.setter
    def sdrs_free_space_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_free_space_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsFreeSpaceThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsFreeSpaceThresholdMode")
    def sdrs_free_space_threshold_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsFreeSpaceThresholdMode"))

    @sdrs_free_space_threshold_mode.setter
    def sdrs_free_space_threshold_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_free_space_threshold_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsFreeSpaceThresholdMode", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsFreeSpaceUtilizationDifference")
    def sdrs_free_space_utilization_difference(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsFreeSpaceUtilizationDifference"))

    @sdrs_free_space_utilization_difference.setter
    def sdrs_free_space_utilization_difference(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_free_space_utilization_difference").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsFreeSpaceUtilizationDifference", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoBalanceAutomationLevel")
    def sdrs_io_balance_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsIoBalanceAutomationLevel"))

    @sdrs_io_balance_automation_level.setter
    def sdrs_io_balance_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_balance_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoBalanceAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoLatencyThreshold")
    def sdrs_io_latency_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsIoLatencyThreshold"))

    @sdrs_io_latency_threshold.setter
    def sdrs_io_latency_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_latency_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoLatencyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoLoadBalanceEnabled")
    def sdrs_io_load_balance_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sdrsIoLoadBalanceEnabled"))

    @sdrs_io_load_balance_enabled.setter
    def sdrs_io_load_balance_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_load_balance_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoLoadBalanceEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoLoadImbalanceThreshold")
    def sdrs_io_load_imbalance_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsIoLoadImbalanceThreshold"))

    @sdrs_io_load_imbalance_threshold.setter
    def sdrs_io_load_imbalance_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_load_imbalance_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoLoadImbalanceThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoReservableIopsThreshold")
    def sdrs_io_reservable_iops_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsIoReservableIopsThreshold"))

    @sdrs_io_reservable_iops_threshold.setter
    def sdrs_io_reservable_iops_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_reservable_iops_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoReservableIopsThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoReservablePercentThreshold")
    def sdrs_io_reservable_percent_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsIoReservablePercentThreshold"))

    @sdrs_io_reservable_percent_threshold.setter
    def sdrs_io_reservable_percent_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_reservable_percent_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoReservablePercentThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsIoReservableThresholdMode")
    def sdrs_io_reservable_threshold_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsIoReservableThresholdMode"))

    @sdrs_io_reservable_threshold_mode.setter
    def sdrs_io_reservable_threshold_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_io_reservable_threshold_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsIoReservableThresholdMode", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsLoadBalanceInterval")
    def sdrs_load_balance_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsLoadBalanceInterval"))

    @sdrs_load_balance_interval.setter
    def sdrs_load_balance_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_load_balance_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsLoadBalanceInterval", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsPolicyEnforcementAutomationLevel")
    def sdrs_policy_enforcement_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsPolicyEnforcementAutomationLevel"))

    @sdrs_policy_enforcement_automation_level.setter
    def sdrs_policy_enforcement_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_policy_enforcement_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsPolicyEnforcementAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsRuleEnforcementAutomationLevel")
    def sdrs_rule_enforcement_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsRuleEnforcementAutomationLevel"))

    @sdrs_rule_enforcement_automation_level.setter
    def sdrs_rule_enforcement_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_rule_enforcement_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsRuleEnforcementAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsSpaceBalanceAutomationLevel")
    def sdrs_space_balance_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsSpaceBalanceAutomationLevel"))

    @sdrs_space_balance_automation_level.setter
    def sdrs_space_balance_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_space_balance_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsSpaceBalanceAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsSpaceUtilizationThreshold")
    def sdrs_space_utilization_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sdrsSpaceUtilizationThreshold"))

    @sdrs_space_utilization_threshold.setter
    def sdrs_space_utilization_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_space_utilization_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsSpaceUtilizationThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sdrsVmEvacuationAutomationLevel")
    def sdrs_vm_evacuation_automation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sdrsVmEvacuationAutomationLevel"))

    @sdrs_vm_evacuation_automation_level.setter
    def sdrs_vm_evacuation_automation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "sdrs_vm_evacuation_automation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sdrsVmEvacuationAutomationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatastoreCluster, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.datastoreCluster.DatastoreClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datacenter_id": "datacenterId",
        "name": "name",
        "custom_attributes": "customAttributes",
        "folder": "folder",
        "id": "id",
        "sdrs_advanced_options": "sdrsAdvancedOptions",
        "sdrs_automation_level": "sdrsAutomationLevel",
        "sdrs_default_intra_vm_affinity": "sdrsDefaultIntraVmAffinity",
        "sdrs_enabled": "sdrsEnabled",
        "sdrs_free_space_threshold": "sdrsFreeSpaceThreshold",
        "sdrs_free_space_threshold_mode": "sdrsFreeSpaceThresholdMode",
        "sdrs_free_space_utilization_difference": "sdrsFreeSpaceUtilizationDifference",
        "sdrs_io_balance_automation_level": "sdrsIoBalanceAutomationLevel",
        "sdrs_io_latency_threshold": "sdrsIoLatencyThreshold",
        "sdrs_io_load_balance_enabled": "sdrsIoLoadBalanceEnabled",
        "sdrs_io_load_imbalance_threshold": "sdrsIoLoadImbalanceThreshold",
        "sdrs_io_reservable_iops_threshold": "sdrsIoReservableIopsThreshold",
        "sdrs_io_reservable_percent_threshold": "sdrsIoReservablePercentThreshold",
        "sdrs_io_reservable_threshold_mode": "sdrsIoReservableThresholdMode",
        "sdrs_load_balance_interval": "sdrsLoadBalanceInterval",
        "sdrs_policy_enforcement_automation_level": "sdrsPolicyEnforcementAutomationLevel",
        "sdrs_rule_enforcement_automation_level": "sdrsRuleEnforcementAutomationLevel",
        "sdrs_space_balance_automation_level": "sdrsSpaceBalanceAutomationLevel",
        "sdrs_space_utilization_threshold": "sdrsSpaceUtilizationThreshold",
        "sdrs_vm_evacuation_automation_level": "sdrsVmEvacuationAutomationLevel",
        "tags": "tags",
    },
)
class DatastoreClusterConfig(cdktf.TerraformMetaArguments):
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
        datacenter_id: builtins.str,
        name: builtins.str,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        sdrs_advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sdrs_automation_level: typing.Optional[builtins.str] = None,
        sdrs_default_intra_vm_affinity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sdrs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sdrs_free_space_threshold: typing.Optional[jsii.Number] = None,
        sdrs_free_space_threshold_mode: typing.Optional[builtins.str] = None,
        sdrs_free_space_utilization_difference: typing.Optional[jsii.Number] = None,
        sdrs_io_balance_automation_level: typing.Optional[builtins.str] = None,
        sdrs_io_latency_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_load_balance_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sdrs_io_load_imbalance_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_reservable_iops_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_reservable_percent_threshold: typing.Optional[jsii.Number] = None,
        sdrs_io_reservable_threshold_mode: typing.Optional[builtins.str] = None,
        sdrs_load_balance_interval: typing.Optional[jsii.Number] = None,
        sdrs_policy_enforcement_automation_level: typing.Optional[builtins.str] = None,
        sdrs_rule_enforcement_automation_level: typing.Optional[builtins.str] = None,
        sdrs_space_balance_automation_level: typing.Optional[builtins.str] = None,
        sdrs_space_utilization_threshold: typing.Optional[jsii.Number] = None,
        sdrs_vm_evacuation_automation_level: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datacenter_id: The managed object ID of the datacenter to put the datastore cluster in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#datacenter_id DatastoreCluster#datacenter_id}
        :param name: Name for the new storage pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#name DatastoreCluster#name}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#custom_attributes DatastoreCluster#custom_attributes}
        :param folder: The name of the folder to locate the datastore cluster in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#folder DatastoreCluster#folder}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#id DatastoreCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sdrs_advanced_options: Advanced configuration options for storage DRS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_advanced_options DatastoreCluster#sdrs_advanced_options}
        :param sdrs_automation_level: The default automation level for all virtual machines in this storage cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_automation_level DatastoreCluster#sdrs_automation_level}
        :param sdrs_default_intra_vm_affinity: When true, storage DRS keeps VMDKs for individual VMs on the same datastore by default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_default_intra_vm_affinity DatastoreCluster#sdrs_default_intra_vm_affinity}
        :param sdrs_enabled: Enable storage DRS for this datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_enabled DatastoreCluster#sdrs_enabled}
        :param sdrs_free_space_threshold: The threshold, in GB, that storage DRS uses to make decisions to migrate VMs out of a datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_threshold DatastoreCluster#sdrs_free_space_threshold}
        :param sdrs_free_space_threshold_mode: The free space threshold to use. When set to utilization, drs_space_utilization_threshold is used, and when set to freeSpace, drs_free_space_threshold is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_threshold_mode DatastoreCluster#sdrs_free_space_threshold_mode}
        :param sdrs_free_space_utilization_difference: The threshold, in percent, of difference between space utilization in datastores before storage DRS makes decisions to balance the space. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_utilization_difference DatastoreCluster#sdrs_free_space_utilization_difference}
        :param sdrs_io_balance_automation_level: Overrides the default automation settings when correcting I/O load imbalances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_balance_automation_level DatastoreCluster#sdrs_io_balance_automation_level}
        :param sdrs_io_latency_threshold: The I/O latency threshold, in milliseconds, that storage DRS uses to make recommendations to move disks from this datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_latency_threshold DatastoreCluster#sdrs_io_latency_threshold}
        :param sdrs_io_load_balance_enabled: Enable I/O load balancing for this datastore cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_load_balance_enabled DatastoreCluster#sdrs_io_load_balance_enabled}
        :param sdrs_io_load_imbalance_threshold: The difference between load in datastores in the cluster before storage DRS makes recommendations to balance the load. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_load_imbalance_threshold DatastoreCluster#sdrs_io_load_imbalance_threshold}
        :param sdrs_io_reservable_iops_threshold: The threshold of reservable IOPS of all virtual machines on the datastore before storage DRS makes recommendations to move VMs off of a datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_iops_threshold DatastoreCluster#sdrs_io_reservable_iops_threshold}
        :param sdrs_io_reservable_percent_threshold: The threshold, in percent, of actual estimated performance of the datastore (in IOPS) that storage DRS uses to make recommendations to move VMs off of a datastore when the total reservable IOPS exceeds the threshold. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_percent_threshold DatastoreCluster#sdrs_io_reservable_percent_threshold}
        :param sdrs_io_reservable_threshold_mode: The reservable IOPS threshold to use, percent in the event of automatic, or manual threshold in the event of manual. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_threshold_mode DatastoreCluster#sdrs_io_reservable_threshold_mode}
        :param sdrs_load_balance_interval: The storage DRS poll interval, in minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_load_balance_interval DatastoreCluster#sdrs_load_balance_interval}
        :param sdrs_policy_enforcement_automation_level: Overrides the default automation settings when correcting storage and VM policy violations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_policy_enforcement_automation_level DatastoreCluster#sdrs_policy_enforcement_automation_level}
        :param sdrs_rule_enforcement_automation_level: Overrides the default automation settings when correcting affinity rule violations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_rule_enforcement_automation_level DatastoreCluster#sdrs_rule_enforcement_automation_level}
        :param sdrs_space_balance_automation_level: Overrides the default automation settings when correcting disk space imbalances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_space_balance_automation_level DatastoreCluster#sdrs_space_balance_automation_level}
        :param sdrs_space_utilization_threshold: The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a datastore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_space_utilization_threshold DatastoreCluster#sdrs_space_utilization_threshold}
        :param sdrs_vm_evacuation_automation_level: Overrides the default automation settings when generating recommendations for datastore evacuation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_vm_evacuation_automation_level DatastoreCluster#sdrs_vm_evacuation_automation_level}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#tags DatastoreCluster#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DatastoreClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sdrs_advanced_options", value=sdrs_advanced_options, expected_type=type_hints["sdrs_advanced_options"])
            check_type(argname="argument sdrs_automation_level", value=sdrs_automation_level, expected_type=type_hints["sdrs_automation_level"])
            check_type(argname="argument sdrs_default_intra_vm_affinity", value=sdrs_default_intra_vm_affinity, expected_type=type_hints["sdrs_default_intra_vm_affinity"])
            check_type(argname="argument sdrs_enabled", value=sdrs_enabled, expected_type=type_hints["sdrs_enabled"])
            check_type(argname="argument sdrs_free_space_threshold", value=sdrs_free_space_threshold, expected_type=type_hints["sdrs_free_space_threshold"])
            check_type(argname="argument sdrs_free_space_threshold_mode", value=sdrs_free_space_threshold_mode, expected_type=type_hints["sdrs_free_space_threshold_mode"])
            check_type(argname="argument sdrs_free_space_utilization_difference", value=sdrs_free_space_utilization_difference, expected_type=type_hints["sdrs_free_space_utilization_difference"])
            check_type(argname="argument sdrs_io_balance_automation_level", value=sdrs_io_balance_automation_level, expected_type=type_hints["sdrs_io_balance_automation_level"])
            check_type(argname="argument sdrs_io_latency_threshold", value=sdrs_io_latency_threshold, expected_type=type_hints["sdrs_io_latency_threshold"])
            check_type(argname="argument sdrs_io_load_balance_enabled", value=sdrs_io_load_balance_enabled, expected_type=type_hints["sdrs_io_load_balance_enabled"])
            check_type(argname="argument sdrs_io_load_imbalance_threshold", value=sdrs_io_load_imbalance_threshold, expected_type=type_hints["sdrs_io_load_imbalance_threshold"])
            check_type(argname="argument sdrs_io_reservable_iops_threshold", value=sdrs_io_reservable_iops_threshold, expected_type=type_hints["sdrs_io_reservable_iops_threshold"])
            check_type(argname="argument sdrs_io_reservable_percent_threshold", value=sdrs_io_reservable_percent_threshold, expected_type=type_hints["sdrs_io_reservable_percent_threshold"])
            check_type(argname="argument sdrs_io_reservable_threshold_mode", value=sdrs_io_reservable_threshold_mode, expected_type=type_hints["sdrs_io_reservable_threshold_mode"])
            check_type(argname="argument sdrs_load_balance_interval", value=sdrs_load_balance_interval, expected_type=type_hints["sdrs_load_balance_interval"])
            check_type(argname="argument sdrs_policy_enforcement_automation_level", value=sdrs_policy_enforcement_automation_level, expected_type=type_hints["sdrs_policy_enforcement_automation_level"])
            check_type(argname="argument sdrs_rule_enforcement_automation_level", value=sdrs_rule_enforcement_automation_level, expected_type=type_hints["sdrs_rule_enforcement_automation_level"])
            check_type(argname="argument sdrs_space_balance_automation_level", value=sdrs_space_balance_automation_level, expected_type=type_hints["sdrs_space_balance_automation_level"])
            check_type(argname="argument sdrs_space_utilization_threshold", value=sdrs_space_utilization_threshold, expected_type=type_hints["sdrs_space_utilization_threshold"])
            check_type(argname="argument sdrs_vm_evacuation_automation_level", value=sdrs_vm_evacuation_automation_level, expected_type=type_hints["sdrs_vm_evacuation_automation_level"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "datacenter_id": datacenter_id,
            "name": name,
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
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if folder is not None:
            self._values["folder"] = folder
        if id is not None:
            self._values["id"] = id
        if sdrs_advanced_options is not None:
            self._values["sdrs_advanced_options"] = sdrs_advanced_options
        if sdrs_automation_level is not None:
            self._values["sdrs_automation_level"] = sdrs_automation_level
        if sdrs_default_intra_vm_affinity is not None:
            self._values["sdrs_default_intra_vm_affinity"] = sdrs_default_intra_vm_affinity
        if sdrs_enabled is not None:
            self._values["sdrs_enabled"] = sdrs_enabled
        if sdrs_free_space_threshold is not None:
            self._values["sdrs_free_space_threshold"] = sdrs_free_space_threshold
        if sdrs_free_space_threshold_mode is not None:
            self._values["sdrs_free_space_threshold_mode"] = sdrs_free_space_threshold_mode
        if sdrs_free_space_utilization_difference is not None:
            self._values["sdrs_free_space_utilization_difference"] = sdrs_free_space_utilization_difference
        if sdrs_io_balance_automation_level is not None:
            self._values["sdrs_io_balance_automation_level"] = sdrs_io_balance_automation_level
        if sdrs_io_latency_threshold is not None:
            self._values["sdrs_io_latency_threshold"] = sdrs_io_latency_threshold
        if sdrs_io_load_balance_enabled is not None:
            self._values["sdrs_io_load_balance_enabled"] = sdrs_io_load_balance_enabled
        if sdrs_io_load_imbalance_threshold is not None:
            self._values["sdrs_io_load_imbalance_threshold"] = sdrs_io_load_imbalance_threshold
        if sdrs_io_reservable_iops_threshold is not None:
            self._values["sdrs_io_reservable_iops_threshold"] = sdrs_io_reservable_iops_threshold
        if sdrs_io_reservable_percent_threshold is not None:
            self._values["sdrs_io_reservable_percent_threshold"] = sdrs_io_reservable_percent_threshold
        if sdrs_io_reservable_threshold_mode is not None:
            self._values["sdrs_io_reservable_threshold_mode"] = sdrs_io_reservable_threshold_mode
        if sdrs_load_balance_interval is not None:
            self._values["sdrs_load_balance_interval"] = sdrs_load_balance_interval
        if sdrs_policy_enforcement_automation_level is not None:
            self._values["sdrs_policy_enforcement_automation_level"] = sdrs_policy_enforcement_automation_level
        if sdrs_rule_enforcement_automation_level is not None:
            self._values["sdrs_rule_enforcement_automation_level"] = sdrs_rule_enforcement_automation_level
        if sdrs_space_balance_automation_level is not None:
            self._values["sdrs_space_balance_automation_level"] = sdrs_space_balance_automation_level
        if sdrs_space_utilization_threshold is not None:
            self._values["sdrs_space_utilization_threshold"] = sdrs_space_utilization_threshold
        if sdrs_vm_evacuation_automation_level is not None:
            self._values["sdrs_vm_evacuation_automation_level"] = sdrs_vm_evacuation_automation_level
        if tags is not None:
            self._values["tags"] = tags

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
    def datacenter_id(self) -> builtins.str:
        '''The managed object ID of the datacenter to put the datastore cluster in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#datacenter_id DatastoreCluster#datacenter_id}
        '''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name for the new storage pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#name DatastoreCluster#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of custom attributes to set on this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#custom_attributes DatastoreCluster#custom_attributes}
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''The name of the folder to locate the datastore cluster in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#folder DatastoreCluster#folder}
        '''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#id DatastoreCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_advanced_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Advanced configuration options for storage DRS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_advanced_options DatastoreCluster#sdrs_advanced_options}
        '''
        result = self._values.get("sdrs_advanced_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def sdrs_automation_level(self) -> typing.Optional[builtins.str]:
        '''The default automation level for all virtual machines in this storage cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_automation_level DatastoreCluster#sdrs_automation_level}
        '''
        result = self._values.get("sdrs_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_default_intra_vm_affinity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, storage DRS keeps VMDKs for individual VMs on the same datastore by default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_default_intra_vm_affinity DatastoreCluster#sdrs_default_intra_vm_affinity}
        '''
        result = self._values.get("sdrs_default_intra_vm_affinity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sdrs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable storage DRS for this datastore cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_enabled DatastoreCluster#sdrs_enabled}
        '''
        result = self._values.get("sdrs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sdrs_free_space_threshold(self) -> typing.Optional[jsii.Number]:
        '''The threshold, in GB, that storage DRS uses to make decisions to migrate VMs out of a datastore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_threshold DatastoreCluster#sdrs_free_space_threshold}
        '''
        result = self._values.get("sdrs_free_space_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_free_space_threshold_mode(self) -> typing.Optional[builtins.str]:
        '''The free space threshold to use.

        When set to utilization, drs_space_utilization_threshold is used, and when set to freeSpace, drs_free_space_threshold is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_threshold_mode DatastoreCluster#sdrs_free_space_threshold_mode}
        '''
        result = self._values.get("sdrs_free_space_threshold_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_free_space_utilization_difference(self) -> typing.Optional[jsii.Number]:
        '''The threshold, in percent, of difference between space utilization in datastores before storage DRS makes decisions to balance the space.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_free_space_utilization_difference DatastoreCluster#sdrs_free_space_utilization_difference}
        '''
        result = self._values.get("sdrs_free_space_utilization_difference")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_io_balance_automation_level(self) -> typing.Optional[builtins.str]:
        '''Overrides the default automation settings when correcting I/O load imbalances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_balance_automation_level DatastoreCluster#sdrs_io_balance_automation_level}
        '''
        result = self._values.get("sdrs_io_balance_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_io_latency_threshold(self) -> typing.Optional[jsii.Number]:
        '''The I/O latency threshold, in milliseconds, that storage DRS uses to make recommendations to move disks from this datastore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_latency_threshold DatastoreCluster#sdrs_io_latency_threshold}
        '''
        result = self._values.get("sdrs_io_latency_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_io_load_balance_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable I/O load balancing for this datastore cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_load_balance_enabled DatastoreCluster#sdrs_io_load_balance_enabled}
        '''
        result = self._values.get("sdrs_io_load_balance_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sdrs_io_load_imbalance_threshold(self) -> typing.Optional[jsii.Number]:
        '''The difference between load in datastores in the cluster before storage DRS makes recommendations to balance the load.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_load_imbalance_threshold DatastoreCluster#sdrs_io_load_imbalance_threshold}
        '''
        result = self._values.get("sdrs_io_load_imbalance_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_io_reservable_iops_threshold(self) -> typing.Optional[jsii.Number]:
        '''The threshold of reservable IOPS of all virtual machines on the datastore before storage DRS makes recommendations to move VMs off of a datastore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_iops_threshold DatastoreCluster#sdrs_io_reservable_iops_threshold}
        '''
        result = self._values.get("sdrs_io_reservable_iops_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_io_reservable_percent_threshold(self) -> typing.Optional[jsii.Number]:
        '''The threshold, in percent, of actual estimated performance of the datastore (in IOPS) that storage DRS uses to make recommendations to move VMs off of a datastore when the total reservable IOPS exceeds the threshold.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_percent_threshold DatastoreCluster#sdrs_io_reservable_percent_threshold}
        '''
        result = self._values.get("sdrs_io_reservable_percent_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_io_reservable_threshold_mode(self) -> typing.Optional[builtins.str]:
        '''The reservable IOPS threshold to use, percent in the event of automatic, or manual threshold in the event of manual.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_io_reservable_threshold_mode DatastoreCluster#sdrs_io_reservable_threshold_mode}
        '''
        result = self._values.get("sdrs_io_reservable_threshold_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_load_balance_interval(self) -> typing.Optional[jsii.Number]:
        '''The storage DRS poll interval, in minutes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_load_balance_interval DatastoreCluster#sdrs_load_balance_interval}
        '''
        result = self._values.get("sdrs_load_balance_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_policy_enforcement_automation_level(self) -> typing.Optional[builtins.str]:
        '''Overrides the default automation settings when correcting storage and VM policy violations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_policy_enforcement_automation_level DatastoreCluster#sdrs_policy_enforcement_automation_level}
        '''
        result = self._values.get("sdrs_policy_enforcement_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_rule_enforcement_automation_level(self) -> typing.Optional[builtins.str]:
        '''Overrides the default automation settings when correcting affinity rule violations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_rule_enforcement_automation_level DatastoreCluster#sdrs_rule_enforcement_automation_level}
        '''
        result = self._values.get("sdrs_rule_enforcement_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_space_balance_automation_level(self) -> typing.Optional[builtins.str]:
        '''Overrides the default automation settings when correcting disk space imbalances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_space_balance_automation_level DatastoreCluster#sdrs_space_balance_automation_level}
        '''
        result = self._values.get("sdrs_space_balance_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sdrs_space_utilization_threshold(self) -> typing.Optional[jsii.Number]:
        '''The threshold, in percent of used space, that storage DRS uses to make decisions to migrate VMs out of a datastore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_space_utilization_threshold DatastoreCluster#sdrs_space_utilization_threshold}
        '''
        result = self._values.get("sdrs_space_utilization_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sdrs_vm_evacuation_automation_level(self) -> typing.Optional[builtins.str]:
        '''Overrides the default automation settings when generating recommendations for datastore evacuation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#sdrs_vm_evacuation_automation_level DatastoreCluster#sdrs_vm_evacuation_automation_level}
        '''
        result = self._values.get("sdrs_vm_evacuation_automation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tag IDs to apply to this object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/datastore_cluster#tags DatastoreCluster#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastoreClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatastoreCluster",
    "DatastoreClusterConfig",
]

publication.publish()
