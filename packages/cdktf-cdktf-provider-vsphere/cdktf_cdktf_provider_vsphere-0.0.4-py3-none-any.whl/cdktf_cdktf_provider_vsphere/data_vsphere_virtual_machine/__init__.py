'''
# `data_vsphere_virtual_machine`

Refer to the Terraform Registory for docs: [`data_vsphere_virtual_machine`](https://www.terraform.io/docs/providers/vsphere/d/virtual_machine).
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


class DataVsphereVirtualMachine(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine vsphere_virtual_machine}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        alternate_guest_name: typing.Optional[builtins.str] = None,
        annotation: typing.Optional[builtins.str] = None,
        boot_delay: typing.Optional[jsii.Number] = None,
        boot_retry_delay: typing.Optional[jsii.Number] = None,
        boot_retry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_hot_add_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_hot_remove_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_limit: typing.Optional[jsii.Number] = None,
        cpu_performance_counters_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_reservation: typing.Optional[jsii.Number] = None,
        cpu_share_count: typing.Optional[jsii.Number] = None,
        cpu_share_level: typing.Optional[builtins.str] = None,
        datacenter_id: typing.Optional[builtins.str] = None,
        efi_secure_boot_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_disk_uuid: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ept_rvi_mode: typing.Optional[builtins.str] = None,
        extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        firmware: typing.Optional[builtins.str] = None,
        guest_id: typing.Optional[builtins.str] = None,
        hardware_version: typing.Optional[jsii.Number] = None,
        hv_mode: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ide_controller_scan_count: typing.Optional[jsii.Number] = None,
        latency_sensitivity: typing.Optional[builtins.str] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_hot_add_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        memory_reservation: typing.Optional[jsii.Number] = None,
        memory_share_count: typing.Optional[jsii.Number] = None,
        memory_share_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        nested_hv_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        num_cores_per_socket: typing.Optional[jsii.Number] = None,
        num_cpus: typing.Optional[jsii.Number] = None,
        replace_trigger: typing.Optional[builtins.str] = None,
        run_tools_scripts_after_power_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_after_resume: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_before_guest_reboot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_before_guest_shutdown: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_before_guest_standby: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sata_controller_scan_count: typing.Optional[jsii.Number] = None,
        scsi_controller_scan_count: typing.Optional[jsii.Number] = None,
        storage_policy_id: typing.Optional[builtins.str] = None,
        swap_placement_policy: typing.Optional[builtins.str] = None,
        sync_time_with_host: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sync_time_with_host_periodically: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tools_upgrade_policy: typing.Optional[builtins.str] = None,
        uuid: typing.Optional[builtins.str] = None,
        vapp: typing.Optional[typing.Union["DataVsphereVirtualMachineVapp", typing.Dict[str, typing.Any]]] = None,
        vbs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vvtd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine vsphere_virtual_machine} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alternate_guest_name: The guest name for the operating system when guest_id is otherGuest or otherGuest64. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#alternate_guest_name DataVsphereVirtualMachine#alternate_guest_name}
        :param annotation: User-provided description of the virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#annotation DataVsphereVirtualMachine#annotation}
        :param boot_delay: The number of milliseconds to wait before starting the boot sequence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_delay DataVsphereVirtualMachine#boot_delay}
        :param boot_retry_delay: The number of milliseconds to wait before retrying the boot sequence. This only valid if boot_retry_enabled is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_retry_delay DataVsphereVirtualMachine#boot_retry_delay}
        :param boot_retry_enabled: If set to true, a virtual machine that fails to boot will try again after the delay defined in boot_retry_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_retry_enabled DataVsphereVirtualMachine#boot_retry_enabled}
        :param cpu_hot_add_enabled: Allow CPUs to be added to this virtual machine while it is running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_hot_add_enabled DataVsphereVirtualMachine#cpu_hot_add_enabled}
        :param cpu_hot_remove_enabled: Allow CPUs to be added to this virtual machine while it is running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_hot_remove_enabled DataVsphereVirtualMachine#cpu_hot_remove_enabled}
        :param cpu_limit: The maximum amount of memory (in MB) or CPU (in MHz) that this virtual machine can consume, regardless of available resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_limit DataVsphereVirtualMachine#cpu_limit}
        :param cpu_performance_counters_enabled: Enable CPU performance counters on this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_performance_counters_enabled DataVsphereVirtualMachine#cpu_performance_counters_enabled}
        :param cpu_reservation: The amount of memory (in MB) or CPU (in MHz) that this virtual machine is guaranteed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_reservation DataVsphereVirtualMachine#cpu_reservation}
        :param cpu_share_count: The amount of shares to allocate to cpu for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_share_count DataVsphereVirtualMachine#cpu_share_count}
        :param cpu_share_level: The allocation level for cpu resources. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_share_level DataVsphereVirtualMachine#cpu_share_level}
        :param datacenter_id: The managed object ID of the datacenter the virtual machine is in. This is not required when using ESXi directly, or if there is only one datacenter in your infrastructure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#datacenter_id DataVsphereVirtualMachine#datacenter_id}
        :param efi_secure_boot_enabled: When the boot type set in firmware is efi, this enables EFI secure boot. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#efi_secure_boot_enabled DataVsphereVirtualMachine#efi_secure_boot_enabled}
        :param enable_disk_uuid: Expose the UUIDs of attached virtual disks to the virtual machine, allowing access to them in the guest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#enable_disk_uuid DataVsphereVirtualMachine#enable_disk_uuid}
        :param enable_logging: Enable logging on this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#enable_logging DataVsphereVirtualMachine#enable_logging}
        :param ept_rvi_mode: The EPT/RVI (hardware memory virtualization) setting for this virtual machine. Can be one of automatic, on, or off. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#ept_rvi_mode DataVsphereVirtualMachine#ept_rvi_mode}
        :param extra_config: Extra configuration data for this virtual machine. Can be used to supply advanced parameters not normally in configuration, such as instance metadata, or configuration data for OVF images. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#extra_config DataVsphereVirtualMachine#extra_config}
        :param firmware: The firmware interface to use on the virtual machine. Can be one of bios or efi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#firmware DataVsphereVirtualMachine#firmware}
        :param guest_id: The guest ID for the operating system. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#guest_id DataVsphereVirtualMachine#guest_id}
        :param hardware_version: The hardware version for the virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#hardware_version DataVsphereVirtualMachine#hardware_version}
        :param hv_mode: The (non-nested) hardware virtualization setting for this virtual machine. Can be one of hvAuto, hvOn, or hvOff. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#hv_mode DataVsphereVirtualMachine#hv_mode}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#id DataVsphereVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ide_controller_scan_count: The number of IDE controllers to scan for disk sizes and controller types on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#ide_controller_scan_count DataVsphereVirtualMachine#ide_controller_scan_count}
        :param latency_sensitivity: Controls the scheduling delay of the virtual machine. Use a higher sensitivity for applications that require lower latency, such as VOIP, media player applications, or applications that require frequent access to mouse or keyboard devices. Can be one of low, normal, medium, or high. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#latency_sensitivity DataVsphereVirtualMachine#latency_sensitivity}
        :param memory: The size of the virtual machine's memory, in MB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory DataVsphereVirtualMachine#memory}
        :param memory_hot_add_enabled: Allow memory to be added to this virtual machine while it is running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_hot_add_enabled DataVsphereVirtualMachine#memory_hot_add_enabled}
        :param memory_limit: The maximum amount of memory (in MB) or CPU (in MHz) that this virtual machine can consume, regardless of available resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_limit DataVsphereVirtualMachine#memory_limit}
        :param memory_reservation: The amount of memory (in MB) or CPU (in MHz) that this virtual machine is guaranteed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_reservation DataVsphereVirtualMachine#memory_reservation}
        :param memory_share_count: The amount of shares to allocate to memory for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_share_count DataVsphereVirtualMachine#memory_share_count}
        :param memory_share_level: The allocation level for memory resources. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_share_level DataVsphereVirtualMachine#memory_share_level}
        :param name: The name of this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#name DataVsphereVirtualMachine#name}
        :param nested_hv_enabled: Enable nested hardware virtualization on this virtual machine, facilitating nested virtualization in the guest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#nested_hv_enabled DataVsphereVirtualMachine#nested_hv_enabled}
        :param num_cores_per_socket: The number of cores to distribute amongst the CPUs in this virtual machine. If specified, the value supplied to num_cpus must be evenly divisible by this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#num_cores_per_socket DataVsphereVirtualMachine#num_cores_per_socket}
        :param num_cpus: The number of virtual processors to assign to this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#num_cpus DataVsphereVirtualMachine#num_cpus}
        :param replace_trigger: Triggers replacement of resource whenever it changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#replace_trigger DataVsphereVirtualMachine#replace_trigger}
        :param run_tools_scripts_after_power_on: Enable the run of scripts after virtual machine power-on when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_after_power_on DataVsphereVirtualMachine#run_tools_scripts_after_power_on}
        :param run_tools_scripts_after_resume: Enable the run of scripts after virtual machine resume when when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_after_resume DataVsphereVirtualMachine#run_tools_scripts_after_resume}
        :param run_tools_scripts_before_guest_reboot: Enable the run of scripts before guest operating system reboot when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_reboot DataVsphereVirtualMachine#run_tools_scripts_before_guest_reboot}
        :param run_tools_scripts_before_guest_shutdown: Enable the run of scripts before guest operating system shutdown when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_shutdown DataVsphereVirtualMachine#run_tools_scripts_before_guest_shutdown}
        :param run_tools_scripts_before_guest_standby: Enable the run of scripts before guest operating system standby when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_standby DataVsphereVirtualMachine#run_tools_scripts_before_guest_standby}
        :param sata_controller_scan_count: The number of SATA controllers to scan for disk sizes and controller types on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sata_controller_scan_count DataVsphereVirtualMachine#sata_controller_scan_count}
        :param scsi_controller_scan_count: The number of SCSI controllers to scan for disk sizes and controller types on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#scsi_controller_scan_count DataVsphereVirtualMachine#scsi_controller_scan_count}
        :param storage_policy_id: The ID of the storage policy to assign to the virtual machine home directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#storage_policy_id DataVsphereVirtualMachine#storage_policy_id}
        :param swap_placement_policy: The swap file placement policy for this virtual machine. Can be one of inherit, hostLocal, or vmDirectory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#swap_placement_policy DataVsphereVirtualMachine#swap_placement_policy}
        :param sync_time_with_host: Enable guest clock synchronization with the host. On vSphere 7.0 U1 and above, with only this setting the clock is synchronized on startup and resume. Requires VMware Tools to be installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sync_time_with_host DataVsphereVirtualMachine#sync_time_with_host}
        :param sync_time_with_host_periodically: Enable periodic clock synchronization with the host. Supported only on vSphere 7.0 U1 and above. On prior versions setting ``sync_time_with_host`` is enough for periodic synchronization. Requires VMware Tools to be installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sync_time_with_host_periodically DataVsphereVirtualMachine#sync_time_with_host_periodically}
        :param tools_upgrade_policy: Set the upgrade policy for VMware Tools. Can be one of ``manual`` or ``upgradeAtPowerCycle``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#tools_upgrade_policy DataVsphereVirtualMachine#tools_upgrade_policy}
        :param uuid: The UUID of the virtual machine. Also exposed as the ID of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#uuid DataVsphereVirtualMachine#uuid}
        :param vapp: vapp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vapp DataVsphereVirtualMachine#vapp}
        :param vbs_enabled: Flag to specify if Virtualization-based security is enabled for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vbs_enabled DataVsphereVirtualMachine#vbs_enabled}
        :param vvtd_enabled: Flag to specify if I/O MMU virtualization, also called Intel Virtualization Technology for Directed I/O (VT-d) and AMD I/O Virtualization (AMD-Vi or IOMMU), is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vvtd_enabled DataVsphereVirtualMachine#vvtd_enabled}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereVirtualMachine.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataVsphereVirtualMachineConfig(
            alternate_guest_name=alternate_guest_name,
            annotation=annotation,
            boot_delay=boot_delay,
            boot_retry_delay=boot_retry_delay,
            boot_retry_enabled=boot_retry_enabled,
            cpu_hot_add_enabled=cpu_hot_add_enabled,
            cpu_hot_remove_enabled=cpu_hot_remove_enabled,
            cpu_limit=cpu_limit,
            cpu_performance_counters_enabled=cpu_performance_counters_enabled,
            cpu_reservation=cpu_reservation,
            cpu_share_count=cpu_share_count,
            cpu_share_level=cpu_share_level,
            datacenter_id=datacenter_id,
            efi_secure_boot_enabled=efi_secure_boot_enabled,
            enable_disk_uuid=enable_disk_uuid,
            enable_logging=enable_logging,
            ept_rvi_mode=ept_rvi_mode,
            extra_config=extra_config,
            firmware=firmware,
            guest_id=guest_id,
            hardware_version=hardware_version,
            hv_mode=hv_mode,
            id=id,
            ide_controller_scan_count=ide_controller_scan_count,
            latency_sensitivity=latency_sensitivity,
            memory=memory,
            memory_hot_add_enabled=memory_hot_add_enabled,
            memory_limit=memory_limit,
            memory_reservation=memory_reservation,
            memory_share_count=memory_share_count,
            memory_share_level=memory_share_level,
            name=name,
            nested_hv_enabled=nested_hv_enabled,
            num_cores_per_socket=num_cores_per_socket,
            num_cpus=num_cpus,
            replace_trigger=replace_trigger,
            run_tools_scripts_after_power_on=run_tools_scripts_after_power_on,
            run_tools_scripts_after_resume=run_tools_scripts_after_resume,
            run_tools_scripts_before_guest_reboot=run_tools_scripts_before_guest_reboot,
            run_tools_scripts_before_guest_shutdown=run_tools_scripts_before_guest_shutdown,
            run_tools_scripts_before_guest_standby=run_tools_scripts_before_guest_standby,
            sata_controller_scan_count=sata_controller_scan_count,
            scsi_controller_scan_count=scsi_controller_scan_count,
            storage_policy_id=storage_policy_id,
            swap_placement_policy=swap_placement_policy,
            sync_time_with_host=sync_time_with_host,
            sync_time_with_host_periodically=sync_time_with_host_periodically,
            tools_upgrade_policy=tools_upgrade_policy,
            uuid=uuid,
            vapp=vapp,
            vbs_enabled=vbs_enabled,
            vvtd_enabled=vvtd_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putVapp")
    def put_vapp(
        self,
        *,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param properties: A map of customizable vApp properties and their values. Allows customization of VMs cloned from OVF templates which have customizable vApp properties. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#properties DataVsphereVirtualMachine#properties}
        '''
        value = DataVsphereVirtualMachineVapp(properties=properties)

        return typing.cast(None, jsii.invoke(self, "putVapp", [value]))

    @jsii.member(jsii_name="resetAlternateGuestName")
    def reset_alternate_guest_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternateGuestName", []))

    @jsii.member(jsii_name="resetAnnotation")
    def reset_annotation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotation", []))

    @jsii.member(jsii_name="resetBootDelay")
    def reset_boot_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDelay", []))

    @jsii.member(jsii_name="resetBootRetryDelay")
    def reset_boot_retry_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootRetryDelay", []))

    @jsii.member(jsii_name="resetBootRetryEnabled")
    def reset_boot_retry_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootRetryEnabled", []))

    @jsii.member(jsii_name="resetCpuHotAddEnabled")
    def reset_cpu_hot_add_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuHotAddEnabled", []))

    @jsii.member(jsii_name="resetCpuHotRemoveEnabled")
    def reset_cpu_hot_remove_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuHotRemoveEnabled", []))

    @jsii.member(jsii_name="resetCpuLimit")
    def reset_cpu_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuLimit", []))

    @jsii.member(jsii_name="resetCpuPerformanceCountersEnabled")
    def reset_cpu_performance_counters_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPerformanceCountersEnabled", []))

    @jsii.member(jsii_name="resetCpuReservation")
    def reset_cpu_reservation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuReservation", []))

    @jsii.member(jsii_name="resetCpuShareCount")
    def reset_cpu_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuShareCount", []))

    @jsii.member(jsii_name="resetCpuShareLevel")
    def reset_cpu_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuShareLevel", []))

    @jsii.member(jsii_name="resetDatacenterId")
    def reset_datacenter_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenterId", []))

    @jsii.member(jsii_name="resetEfiSecureBootEnabled")
    def reset_efi_secure_boot_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfiSecureBootEnabled", []))

    @jsii.member(jsii_name="resetEnableDiskUuid")
    def reset_enable_disk_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDiskUuid", []))

    @jsii.member(jsii_name="resetEnableLogging")
    def reset_enable_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogging", []))

    @jsii.member(jsii_name="resetEptRviMode")
    def reset_ept_rvi_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEptRviMode", []))

    @jsii.member(jsii_name="resetExtraConfig")
    def reset_extra_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfig", []))

    @jsii.member(jsii_name="resetFirmware")
    def reset_firmware(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirmware", []))

    @jsii.member(jsii_name="resetGuestId")
    def reset_guest_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestId", []))

    @jsii.member(jsii_name="resetHardwareVersion")
    def reset_hardware_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHardwareVersion", []))

    @jsii.member(jsii_name="resetHvMode")
    def reset_hv_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHvMode", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdeControllerScanCount")
    def reset_ide_controller_scan_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdeControllerScanCount", []))

    @jsii.member(jsii_name="resetLatencySensitivity")
    def reset_latency_sensitivity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatencySensitivity", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetMemoryHotAddEnabled")
    def reset_memory_hot_add_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryHotAddEnabled", []))

    @jsii.member(jsii_name="resetMemoryLimit")
    def reset_memory_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryLimit", []))

    @jsii.member(jsii_name="resetMemoryReservation")
    def reset_memory_reservation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryReservation", []))

    @jsii.member(jsii_name="resetMemoryShareCount")
    def reset_memory_share_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryShareCount", []))

    @jsii.member(jsii_name="resetMemoryShareLevel")
    def reset_memory_share_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryShareLevel", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNestedHvEnabled")
    def reset_nested_hv_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNestedHvEnabled", []))

    @jsii.member(jsii_name="resetNumCoresPerSocket")
    def reset_num_cores_per_socket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumCoresPerSocket", []))

    @jsii.member(jsii_name="resetNumCpus")
    def reset_num_cpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumCpus", []))

    @jsii.member(jsii_name="resetReplaceTrigger")
    def reset_replace_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplaceTrigger", []))

    @jsii.member(jsii_name="resetRunToolsScriptsAfterPowerOn")
    def reset_run_tools_scripts_after_power_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunToolsScriptsAfterPowerOn", []))

    @jsii.member(jsii_name="resetRunToolsScriptsAfterResume")
    def reset_run_tools_scripts_after_resume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunToolsScriptsAfterResume", []))

    @jsii.member(jsii_name="resetRunToolsScriptsBeforeGuestReboot")
    def reset_run_tools_scripts_before_guest_reboot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunToolsScriptsBeforeGuestReboot", []))

    @jsii.member(jsii_name="resetRunToolsScriptsBeforeGuestShutdown")
    def reset_run_tools_scripts_before_guest_shutdown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunToolsScriptsBeforeGuestShutdown", []))

    @jsii.member(jsii_name="resetRunToolsScriptsBeforeGuestStandby")
    def reset_run_tools_scripts_before_guest_standby(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunToolsScriptsBeforeGuestStandby", []))

    @jsii.member(jsii_name="resetSataControllerScanCount")
    def reset_sata_controller_scan_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSataControllerScanCount", []))

    @jsii.member(jsii_name="resetScsiControllerScanCount")
    def reset_scsi_controller_scan_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScsiControllerScanCount", []))

    @jsii.member(jsii_name="resetStoragePolicyId")
    def reset_storage_policy_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoragePolicyId", []))

    @jsii.member(jsii_name="resetSwapPlacementPolicy")
    def reset_swap_placement_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSwapPlacementPolicy", []))

    @jsii.member(jsii_name="resetSyncTimeWithHost")
    def reset_sync_time_with_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncTimeWithHost", []))

    @jsii.member(jsii_name="resetSyncTimeWithHostPeriodically")
    def reset_sync_time_with_host_periodically(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncTimeWithHostPeriodically", []))

    @jsii.member(jsii_name="resetToolsUpgradePolicy")
    def reset_tools_upgrade_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToolsUpgradePolicy", []))

    @jsii.member(jsii_name="resetUuid")
    def reset_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUuid", []))

    @jsii.member(jsii_name="resetVapp")
    def reset_vapp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVapp", []))

    @jsii.member(jsii_name="resetVbsEnabled")
    def reset_vbs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVbsEnabled", []))

    @jsii.member(jsii_name="resetVvtdEnabled")
    def reset_vvtd_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVvtdEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="changeVersion")
    def change_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "changeVersion"))

    @builtins.property
    @jsii.member(jsii_name="defaultIpAddress")
    def default_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="disks")
    def disks(self) -> "DataVsphereVirtualMachineDisksList":
        return typing.cast("DataVsphereVirtualMachineDisksList", jsii.get(self, "disks"))

    @builtins.property
    @jsii.member(jsii_name="guestIpAddresses")
    def guest_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "guestIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(self) -> "DataVsphereVirtualMachineNetworkInterfacesList":
        return typing.cast("DataVsphereVirtualMachineNetworkInterfacesList", jsii.get(self, "networkInterfaces"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceTypes")
    def network_interface_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceTypes"))

    @builtins.property
    @jsii.member(jsii_name="scsiBusSharing")
    def scsi_bus_sharing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scsiBusSharing"))

    @builtins.property
    @jsii.member(jsii_name="scsiType")
    def scsi_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scsiType"))

    @builtins.property
    @jsii.member(jsii_name="vapp")
    def vapp(self) -> "DataVsphereVirtualMachineVappOutputReference":
        return typing.cast("DataVsphereVirtualMachineVappOutputReference", jsii.get(self, "vapp"))

    @builtins.property
    @jsii.member(jsii_name="vappTransport")
    def vapp_transport(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vappTransport"))

    @builtins.property
    @jsii.member(jsii_name="alternateGuestNameInput")
    def alternate_guest_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alternateGuestNameInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationInput")
    def annotation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "annotationInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDelayInput")
    def boot_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="bootRetryDelayInput")
    def boot_retry_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bootRetryDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="bootRetryEnabledInput")
    def boot_retry_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bootRetryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuHotAddEnabledInput")
    def cpu_hot_add_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cpuHotAddEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuHotRemoveEnabledInput")
    def cpu_hot_remove_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cpuHotRemoveEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuLimitInput")
    def cpu_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuPerformanceCountersEnabledInput")
    def cpu_performance_counters_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cpuPerformanceCountersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuReservationInput")
    def cpu_reservation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuReservationInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuShareCountInput")
    def cpu_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuShareLevelInput")
    def cpu_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="efiSecureBootEnabledInput")
    def efi_secure_boot_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "efiSecureBootEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDiskUuidInput")
    def enable_disk_uuid_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableDiskUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="eptRviModeInput")
    def ept_rvi_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eptRviModeInput"))

    @builtins.property
    @jsii.member(jsii_name="extraConfigInput")
    def extra_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extraConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="firmwareInput")
    def firmware_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firmwareInput"))

    @builtins.property
    @jsii.member(jsii_name="guestIdInput")
    def guest_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guestIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hardwareVersionInput")
    def hardware_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hardwareVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="hvModeInput")
    def hv_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hvModeInput"))

    @builtins.property
    @jsii.member(jsii_name="ideControllerScanCountInput")
    def ide_controller_scan_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ideControllerScanCountInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="latencySensitivityInput")
    def latency_sensitivity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latencySensitivityInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryHotAddEnabledInput")
    def memory_hot_add_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "memoryHotAddEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryLimitInput")
    def memory_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryReservationInput")
    def memory_reservation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryReservationInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryShareCountInput")
    def memory_share_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryShareCountInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryShareLevelInput")
    def memory_share_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryShareLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nestedHvEnabledInput")
    def nested_hv_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "nestedHvEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="numCoresPerSocketInput")
    def num_cores_per_socket_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numCoresPerSocketInput"))

    @builtins.property
    @jsii.member(jsii_name="numCpusInput")
    def num_cpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numCpusInput"))

    @builtins.property
    @jsii.member(jsii_name="replaceTriggerInput")
    def replace_trigger_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replaceTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsAfterPowerOnInput")
    def run_tools_scripts_after_power_on_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runToolsScriptsAfterPowerOnInput"))

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsAfterResumeInput")
    def run_tools_scripts_after_resume_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runToolsScriptsAfterResumeInput"))

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsBeforeGuestRebootInput")
    def run_tools_scripts_before_guest_reboot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runToolsScriptsBeforeGuestRebootInput"))

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsBeforeGuestShutdownInput")
    def run_tools_scripts_before_guest_shutdown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runToolsScriptsBeforeGuestShutdownInput"))

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsBeforeGuestStandbyInput")
    def run_tools_scripts_before_guest_standby_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runToolsScriptsBeforeGuestStandbyInput"))

    @builtins.property
    @jsii.member(jsii_name="sataControllerScanCountInput")
    def sata_controller_scan_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sataControllerScanCountInput"))

    @builtins.property
    @jsii.member(jsii_name="scsiControllerScanCountInput")
    def scsi_controller_scan_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scsiControllerScanCountInput"))

    @builtins.property
    @jsii.member(jsii_name="storagePolicyIdInput")
    def storage_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storagePolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="swapPlacementPolicyInput")
    def swap_placement_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "swapPlacementPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="syncTimeWithHostInput")
    def sync_time_with_host_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "syncTimeWithHostInput"))

    @builtins.property
    @jsii.member(jsii_name="syncTimeWithHostPeriodicallyInput")
    def sync_time_with_host_periodically_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "syncTimeWithHostPeriodicallyInput"))

    @builtins.property
    @jsii.member(jsii_name="toolsUpgradePolicyInput")
    def tools_upgrade_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "toolsUpgradePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="uuidInput")
    def uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uuidInput"))

    @builtins.property
    @jsii.member(jsii_name="vappInput")
    def vapp_input(self) -> typing.Optional["DataVsphereVirtualMachineVapp"]:
        return typing.cast(typing.Optional["DataVsphereVirtualMachineVapp"], jsii.get(self, "vappInput"))

    @builtins.property
    @jsii.member(jsii_name="vbsEnabledInput")
    def vbs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vbsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="vvtdEnabledInput")
    def vvtd_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vvtdEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="alternateGuestName")
    def alternate_guest_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alternateGuestName"))

    @alternate_guest_name.setter
    def alternate_guest_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "alternate_guest_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alternateGuestName", value)

    @builtins.property
    @jsii.member(jsii_name="annotation")
    def annotation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "annotation"))

    @annotation.setter
    def annotation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "annotation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotation", value)

    @builtins.property
    @jsii.member(jsii_name="bootDelay")
    def boot_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootDelay"))

    @boot_delay.setter
    def boot_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "boot_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootDelay", value)

    @builtins.property
    @jsii.member(jsii_name="bootRetryDelay")
    def boot_retry_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootRetryDelay"))

    @boot_retry_delay.setter
    def boot_retry_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "boot_retry_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootRetryDelay", value)

    @builtins.property
    @jsii.member(jsii_name="bootRetryEnabled")
    def boot_retry_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bootRetryEnabled"))

    @boot_retry_enabled.setter
    def boot_retry_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "boot_retry_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootRetryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cpuHotAddEnabled")
    def cpu_hot_add_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cpuHotAddEnabled"))

    @cpu_hot_add_enabled.setter
    def cpu_hot_add_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_hot_add_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuHotAddEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cpuHotRemoveEnabled")
    def cpu_hot_remove_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cpuHotRemoveEnabled"))

    @cpu_hot_remove_enabled.setter
    def cpu_hot_remove_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_hot_remove_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuHotRemoveEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cpuLimit")
    def cpu_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuLimit"))

    @cpu_limit.setter
    def cpu_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuLimit", value)

    @builtins.property
    @jsii.member(jsii_name="cpuPerformanceCountersEnabled")
    def cpu_performance_counters_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cpuPerformanceCountersEnabled"))

    @cpu_performance_counters_enabled.setter
    def cpu_performance_counters_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_performance_counters_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPerformanceCountersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cpuReservation")
    def cpu_reservation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuReservation"))

    @cpu_reservation.setter
    def cpu_reservation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_reservation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuReservation", value)

    @builtins.property
    @jsii.member(jsii_name="cpuShareCount")
    def cpu_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuShareCount"))

    @cpu_share_count.setter
    def cpu_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="cpuShareLevel")
    def cpu_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuShareLevel"))

    @cpu_share_level.setter
    def cpu_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "cpu_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="efiSecureBootEnabled")
    def efi_secure_boot_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "efiSecureBootEnabled"))

    @efi_secure_boot_enabled.setter
    def efi_secure_boot_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "efi_secure_boot_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "efiSecureBootEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="enableDiskUuid")
    def enable_disk_uuid(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableDiskUuid"))

    @enable_disk_uuid.setter
    def enable_disk_uuid(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "enable_disk_uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDiskUuid", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogging")
    def enable_logging(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogging"))

    @enable_logging.setter
    def enable_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "enable_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

    @builtins.property
    @jsii.member(jsii_name="eptRviMode")
    def ept_rvi_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eptRviMode"))

    @ept_rvi_mode.setter
    def ept_rvi_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "ept_rvi_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eptRviMode", value)

    @builtins.property
    @jsii.member(jsii_name="extraConfig")
    def extra_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraConfig"))

    @extra_config.setter
    def extra_config(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "extra_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConfig", value)

    @builtins.property
    @jsii.member(jsii_name="firmware")
    def firmware(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firmware"))

    @firmware.setter
    def firmware(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "firmware").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmware", value)

    @builtins.property
    @jsii.member(jsii_name="guestId")
    def guest_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guestId"))

    @guest_id.setter
    def guest_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "guest_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guestId", value)

    @builtins.property
    @jsii.member(jsii_name="hardwareVersion")
    def hardware_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hardwareVersion"))

    @hardware_version.setter
    def hardware_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "hardware_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hardwareVersion", value)

    @builtins.property
    @jsii.member(jsii_name="hvMode")
    def hv_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hvMode"))

    @hv_mode.setter
    def hv_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "hv_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hvMode", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ideControllerScanCount")
    def ide_controller_scan_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ideControllerScanCount"))

    @ide_controller_scan_count.setter
    def ide_controller_scan_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "ide_controller_scan_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ideControllerScanCount", value)

    @builtins.property
    @jsii.member(jsii_name="latencySensitivity")
    def latency_sensitivity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latencySensitivity"))

    @latency_sensitivity.setter
    def latency_sensitivity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "latency_sensitivity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latencySensitivity", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="memoryHotAddEnabled")
    def memory_hot_add_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "memoryHotAddEnabled"))

    @memory_hot_add_enabled.setter
    def memory_hot_add_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "memory_hot_add_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryHotAddEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="memoryLimit")
    def memory_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryLimit"))

    @memory_limit.setter
    def memory_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "memory_limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryLimit", value)

    @builtins.property
    @jsii.member(jsii_name="memoryReservation")
    def memory_reservation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryReservation"))

    @memory_reservation.setter
    def memory_reservation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "memory_reservation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryReservation", value)

    @builtins.property
    @jsii.member(jsii_name="memoryShareCount")
    def memory_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryShareCount"))

    @memory_share_count.setter
    def memory_share_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "memory_share_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryShareCount", value)

    @builtins.property
    @jsii.member(jsii_name="memoryShareLevel")
    def memory_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memoryShareLevel"))

    @memory_share_level.setter
    def memory_share_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "memory_share_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryShareLevel", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nestedHvEnabled")
    def nested_hv_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nestedHvEnabled"))

    @nested_hv_enabled.setter
    def nested_hv_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "nested_hv_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nestedHvEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="numCoresPerSocket")
    def num_cores_per_socket(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numCoresPerSocket"))

    @num_cores_per_socket.setter
    def num_cores_per_socket(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "num_cores_per_socket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numCoresPerSocket", value)

    @builtins.property
    @jsii.member(jsii_name="numCpus")
    def num_cpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numCpus"))

    @num_cpus.setter
    def num_cpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "num_cpus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numCpus", value)

    @builtins.property
    @jsii.member(jsii_name="replaceTrigger")
    def replace_trigger(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replaceTrigger"))

    @replace_trigger.setter
    def replace_trigger(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "replace_trigger").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replaceTrigger", value)

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsAfterPowerOn")
    def run_tools_scripts_after_power_on(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runToolsScriptsAfterPowerOn"))

    @run_tools_scripts_after_power_on.setter
    def run_tools_scripts_after_power_on(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "run_tools_scripts_after_power_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runToolsScriptsAfterPowerOn", value)

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsAfterResume")
    def run_tools_scripts_after_resume(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runToolsScriptsAfterResume"))

    @run_tools_scripts_after_resume.setter
    def run_tools_scripts_after_resume(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "run_tools_scripts_after_resume").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runToolsScriptsAfterResume", value)

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsBeforeGuestReboot")
    def run_tools_scripts_before_guest_reboot(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runToolsScriptsBeforeGuestReboot"))

    @run_tools_scripts_before_guest_reboot.setter
    def run_tools_scripts_before_guest_reboot(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "run_tools_scripts_before_guest_reboot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runToolsScriptsBeforeGuestReboot", value)

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsBeforeGuestShutdown")
    def run_tools_scripts_before_guest_shutdown(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runToolsScriptsBeforeGuestShutdown"))

    @run_tools_scripts_before_guest_shutdown.setter
    def run_tools_scripts_before_guest_shutdown(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "run_tools_scripts_before_guest_shutdown").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runToolsScriptsBeforeGuestShutdown", value)

    @builtins.property
    @jsii.member(jsii_name="runToolsScriptsBeforeGuestStandby")
    def run_tools_scripts_before_guest_standby(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "runToolsScriptsBeforeGuestStandby"))

    @run_tools_scripts_before_guest_standby.setter
    def run_tools_scripts_before_guest_standby(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "run_tools_scripts_before_guest_standby").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runToolsScriptsBeforeGuestStandby", value)

    @builtins.property
    @jsii.member(jsii_name="sataControllerScanCount")
    def sata_controller_scan_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sataControllerScanCount"))

    @sata_controller_scan_count.setter
    def sata_controller_scan_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "sata_controller_scan_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sataControllerScanCount", value)

    @builtins.property
    @jsii.member(jsii_name="scsiControllerScanCount")
    def scsi_controller_scan_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scsiControllerScanCount"))

    @scsi_controller_scan_count.setter
    def scsi_controller_scan_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "scsi_controller_scan_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scsiControllerScanCount", value)

    @builtins.property
    @jsii.member(jsii_name="storagePolicyId")
    def storage_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storagePolicyId"))

    @storage_policy_id.setter
    def storage_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "storage_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagePolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="swapPlacementPolicy")
    def swap_placement_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "swapPlacementPolicy"))

    @swap_placement_policy.setter
    def swap_placement_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "swap_placement_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "swapPlacementPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="syncTimeWithHost")
    def sync_time_with_host(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "syncTimeWithHost"))

    @sync_time_with_host.setter
    def sync_time_with_host(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "sync_time_with_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncTimeWithHost", value)

    @builtins.property
    @jsii.member(jsii_name="syncTimeWithHostPeriodically")
    def sync_time_with_host_periodically(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "syncTimeWithHostPeriodically"))

    @sync_time_with_host_periodically.setter
    def sync_time_with_host_periodically(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "sync_time_with_host_periodically").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncTimeWithHostPeriodically", value)

    @builtins.property
    @jsii.member(jsii_name="toolsUpgradePolicy")
    def tools_upgrade_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "toolsUpgradePolicy"))

    @tools_upgrade_policy.setter
    def tools_upgrade_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "tools_upgrade_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toolsUpgradePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @uuid.setter
    def uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uuid", value)

    @builtins.property
    @jsii.member(jsii_name="vbsEnabled")
    def vbs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vbsEnabled"))

    @vbs_enabled.setter
    def vbs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "vbs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vbsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="vvtdEnabled")
    def vvtd_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vvtdEnabled"))

    @vvtd_enabled.setter
    def vvtd_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachine, "vvtd_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vvtdEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "alternate_guest_name": "alternateGuestName",
        "annotation": "annotation",
        "boot_delay": "bootDelay",
        "boot_retry_delay": "bootRetryDelay",
        "boot_retry_enabled": "bootRetryEnabled",
        "cpu_hot_add_enabled": "cpuHotAddEnabled",
        "cpu_hot_remove_enabled": "cpuHotRemoveEnabled",
        "cpu_limit": "cpuLimit",
        "cpu_performance_counters_enabled": "cpuPerformanceCountersEnabled",
        "cpu_reservation": "cpuReservation",
        "cpu_share_count": "cpuShareCount",
        "cpu_share_level": "cpuShareLevel",
        "datacenter_id": "datacenterId",
        "efi_secure_boot_enabled": "efiSecureBootEnabled",
        "enable_disk_uuid": "enableDiskUuid",
        "enable_logging": "enableLogging",
        "ept_rvi_mode": "eptRviMode",
        "extra_config": "extraConfig",
        "firmware": "firmware",
        "guest_id": "guestId",
        "hardware_version": "hardwareVersion",
        "hv_mode": "hvMode",
        "id": "id",
        "ide_controller_scan_count": "ideControllerScanCount",
        "latency_sensitivity": "latencySensitivity",
        "memory": "memory",
        "memory_hot_add_enabled": "memoryHotAddEnabled",
        "memory_limit": "memoryLimit",
        "memory_reservation": "memoryReservation",
        "memory_share_count": "memoryShareCount",
        "memory_share_level": "memoryShareLevel",
        "name": "name",
        "nested_hv_enabled": "nestedHvEnabled",
        "num_cores_per_socket": "numCoresPerSocket",
        "num_cpus": "numCpus",
        "replace_trigger": "replaceTrigger",
        "run_tools_scripts_after_power_on": "runToolsScriptsAfterPowerOn",
        "run_tools_scripts_after_resume": "runToolsScriptsAfterResume",
        "run_tools_scripts_before_guest_reboot": "runToolsScriptsBeforeGuestReboot",
        "run_tools_scripts_before_guest_shutdown": "runToolsScriptsBeforeGuestShutdown",
        "run_tools_scripts_before_guest_standby": "runToolsScriptsBeforeGuestStandby",
        "sata_controller_scan_count": "sataControllerScanCount",
        "scsi_controller_scan_count": "scsiControllerScanCount",
        "storage_policy_id": "storagePolicyId",
        "swap_placement_policy": "swapPlacementPolicy",
        "sync_time_with_host": "syncTimeWithHost",
        "sync_time_with_host_periodically": "syncTimeWithHostPeriodically",
        "tools_upgrade_policy": "toolsUpgradePolicy",
        "uuid": "uuid",
        "vapp": "vapp",
        "vbs_enabled": "vbsEnabled",
        "vvtd_enabled": "vvtdEnabled",
    },
)
class DataVsphereVirtualMachineConfig(cdktf.TerraformMetaArguments):
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
        alternate_guest_name: typing.Optional[builtins.str] = None,
        annotation: typing.Optional[builtins.str] = None,
        boot_delay: typing.Optional[jsii.Number] = None,
        boot_retry_delay: typing.Optional[jsii.Number] = None,
        boot_retry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_hot_add_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_hot_remove_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_limit: typing.Optional[jsii.Number] = None,
        cpu_performance_counters_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cpu_reservation: typing.Optional[jsii.Number] = None,
        cpu_share_count: typing.Optional[jsii.Number] = None,
        cpu_share_level: typing.Optional[builtins.str] = None,
        datacenter_id: typing.Optional[builtins.str] = None,
        efi_secure_boot_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_disk_uuid: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ept_rvi_mode: typing.Optional[builtins.str] = None,
        extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        firmware: typing.Optional[builtins.str] = None,
        guest_id: typing.Optional[builtins.str] = None,
        hardware_version: typing.Optional[jsii.Number] = None,
        hv_mode: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ide_controller_scan_count: typing.Optional[jsii.Number] = None,
        latency_sensitivity: typing.Optional[builtins.str] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_hot_add_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        memory_reservation: typing.Optional[jsii.Number] = None,
        memory_share_count: typing.Optional[jsii.Number] = None,
        memory_share_level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        nested_hv_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        num_cores_per_socket: typing.Optional[jsii.Number] = None,
        num_cpus: typing.Optional[jsii.Number] = None,
        replace_trigger: typing.Optional[builtins.str] = None,
        run_tools_scripts_after_power_on: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_after_resume: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_before_guest_reboot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_before_guest_shutdown: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        run_tools_scripts_before_guest_standby: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sata_controller_scan_count: typing.Optional[jsii.Number] = None,
        scsi_controller_scan_count: typing.Optional[jsii.Number] = None,
        storage_policy_id: typing.Optional[builtins.str] = None,
        swap_placement_policy: typing.Optional[builtins.str] = None,
        sync_time_with_host: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sync_time_with_host_periodically: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tools_upgrade_policy: typing.Optional[builtins.str] = None,
        uuid: typing.Optional[builtins.str] = None,
        vapp: typing.Optional[typing.Union["DataVsphereVirtualMachineVapp", typing.Dict[str, typing.Any]]] = None,
        vbs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vvtd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param alternate_guest_name: The guest name for the operating system when guest_id is otherGuest or otherGuest64. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#alternate_guest_name DataVsphereVirtualMachine#alternate_guest_name}
        :param annotation: User-provided description of the virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#annotation DataVsphereVirtualMachine#annotation}
        :param boot_delay: The number of milliseconds to wait before starting the boot sequence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_delay DataVsphereVirtualMachine#boot_delay}
        :param boot_retry_delay: The number of milliseconds to wait before retrying the boot sequence. This only valid if boot_retry_enabled is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_retry_delay DataVsphereVirtualMachine#boot_retry_delay}
        :param boot_retry_enabled: If set to true, a virtual machine that fails to boot will try again after the delay defined in boot_retry_delay. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_retry_enabled DataVsphereVirtualMachine#boot_retry_enabled}
        :param cpu_hot_add_enabled: Allow CPUs to be added to this virtual machine while it is running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_hot_add_enabled DataVsphereVirtualMachine#cpu_hot_add_enabled}
        :param cpu_hot_remove_enabled: Allow CPUs to be added to this virtual machine while it is running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_hot_remove_enabled DataVsphereVirtualMachine#cpu_hot_remove_enabled}
        :param cpu_limit: The maximum amount of memory (in MB) or CPU (in MHz) that this virtual machine can consume, regardless of available resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_limit DataVsphereVirtualMachine#cpu_limit}
        :param cpu_performance_counters_enabled: Enable CPU performance counters on this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_performance_counters_enabled DataVsphereVirtualMachine#cpu_performance_counters_enabled}
        :param cpu_reservation: The amount of memory (in MB) or CPU (in MHz) that this virtual machine is guaranteed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_reservation DataVsphereVirtualMachine#cpu_reservation}
        :param cpu_share_count: The amount of shares to allocate to cpu for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_share_count DataVsphereVirtualMachine#cpu_share_count}
        :param cpu_share_level: The allocation level for cpu resources. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_share_level DataVsphereVirtualMachine#cpu_share_level}
        :param datacenter_id: The managed object ID of the datacenter the virtual machine is in. This is not required when using ESXi directly, or if there is only one datacenter in your infrastructure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#datacenter_id DataVsphereVirtualMachine#datacenter_id}
        :param efi_secure_boot_enabled: When the boot type set in firmware is efi, this enables EFI secure boot. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#efi_secure_boot_enabled DataVsphereVirtualMachine#efi_secure_boot_enabled}
        :param enable_disk_uuid: Expose the UUIDs of attached virtual disks to the virtual machine, allowing access to them in the guest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#enable_disk_uuid DataVsphereVirtualMachine#enable_disk_uuid}
        :param enable_logging: Enable logging on this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#enable_logging DataVsphereVirtualMachine#enable_logging}
        :param ept_rvi_mode: The EPT/RVI (hardware memory virtualization) setting for this virtual machine. Can be one of automatic, on, or off. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#ept_rvi_mode DataVsphereVirtualMachine#ept_rvi_mode}
        :param extra_config: Extra configuration data for this virtual machine. Can be used to supply advanced parameters not normally in configuration, such as instance metadata, or configuration data for OVF images. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#extra_config DataVsphereVirtualMachine#extra_config}
        :param firmware: The firmware interface to use on the virtual machine. Can be one of bios or efi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#firmware DataVsphereVirtualMachine#firmware}
        :param guest_id: The guest ID for the operating system. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#guest_id DataVsphereVirtualMachine#guest_id}
        :param hardware_version: The hardware version for the virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#hardware_version DataVsphereVirtualMachine#hardware_version}
        :param hv_mode: The (non-nested) hardware virtualization setting for this virtual machine. Can be one of hvAuto, hvOn, or hvOff. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#hv_mode DataVsphereVirtualMachine#hv_mode}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#id DataVsphereVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ide_controller_scan_count: The number of IDE controllers to scan for disk sizes and controller types on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#ide_controller_scan_count DataVsphereVirtualMachine#ide_controller_scan_count}
        :param latency_sensitivity: Controls the scheduling delay of the virtual machine. Use a higher sensitivity for applications that require lower latency, such as VOIP, media player applications, or applications that require frequent access to mouse or keyboard devices. Can be one of low, normal, medium, or high. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#latency_sensitivity DataVsphereVirtualMachine#latency_sensitivity}
        :param memory: The size of the virtual machine's memory, in MB. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory DataVsphereVirtualMachine#memory}
        :param memory_hot_add_enabled: Allow memory to be added to this virtual machine while it is running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_hot_add_enabled DataVsphereVirtualMachine#memory_hot_add_enabled}
        :param memory_limit: The maximum amount of memory (in MB) or CPU (in MHz) that this virtual machine can consume, regardless of available resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_limit DataVsphereVirtualMachine#memory_limit}
        :param memory_reservation: The amount of memory (in MB) or CPU (in MHz) that this virtual machine is guaranteed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_reservation DataVsphereVirtualMachine#memory_reservation}
        :param memory_share_count: The amount of shares to allocate to memory for a custom share level. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_share_count DataVsphereVirtualMachine#memory_share_count}
        :param memory_share_level: The allocation level for memory resources. Can be one of high, low, normal, or custom. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_share_level DataVsphereVirtualMachine#memory_share_level}
        :param name: The name of this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#name DataVsphereVirtualMachine#name}
        :param nested_hv_enabled: Enable nested hardware virtualization on this virtual machine, facilitating nested virtualization in the guest. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#nested_hv_enabled DataVsphereVirtualMachine#nested_hv_enabled}
        :param num_cores_per_socket: The number of cores to distribute amongst the CPUs in this virtual machine. If specified, the value supplied to num_cpus must be evenly divisible by this value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#num_cores_per_socket DataVsphereVirtualMachine#num_cores_per_socket}
        :param num_cpus: The number of virtual processors to assign to this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#num_cpus DataVsphereVirtualMachine#num_cpus}
        :param replace_trigger: Triggers replacement of resource whenever it changes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#replace_trigger DataVsphereVirtualMachine#replace_trigger}
        :param run_tools_scripts_after_power_on: Enable the run of scripts after virtual machine power-on when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_after_power_on DataVsphereVirtualMachine#run_tools_scripts_after_power_on}
        :param run_tools_scripts_after_resume: Enable the run of scripts after virtual machine resume when when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_after_resume DataVsphereVirtualMachine#run_tools_scripts_after_resume}
        :param run_tools_scripts_before_guest_reboot: Enable the run of scripts before guest operating system reboot when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_reboot DataVsphereVirtualMachine#run_tools_scripts_before_guest_reboot}
        :param run_tools_scripts_before_guest_shutdown: Enable the run of scripts before guest operating system shutdown when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_shutdown DataVsphereVirtualMachine#run_tools_scripts_before_guest_shutdown}
        :param run_tools_scripts_before_guest_standby: Enable the run of scripts before guest operating system standby when VMware Tools is installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_standby DataVsphereVirtualMachine#run_tools_scripts_before_guest_standby}
        :param sata_controller_scan_count: The number of SATA controllers to scan for disk sizes and controller types on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sata_controller_scan_count DataVsphereVirtualMachine#sata_controller_scan_count}
        :param scsi_controller_scan_count: The number of SCSI controllers to scan for disk sizes and controller types on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#scsi_controller_scan_count DataVsphereVirtualMachine#scsi_controller_scan_count}
        :param storage_policy_id: The ID of the storage policy to assign to the virtual machine home directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#storage_policy_id DataVsphereVirtualMachine#storage_policy_id}
        :param swap_placement_policy: The swap file placement policy for this virtual machine. Can be one of inherit, hostLocal, or vmDirectory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#swap_placement_policy DataVsphereVirtualMachine#swap_placement_policy}
        :param sync_time_with_host: Enable guest clock synchronization with the host. On vSphere 7.0 U1 and above, with only this setting the clock is synchronized on startup and resume. Requires VMware Tools to be installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sync_time_with_host DataVsphereVirtualMachine#sync_time_with_host}
        :param sync_time_with_host_periodically: Enable periodic clock synchronization with the host. Supported only on vSphere 7.0 U1 and above. On prior versions setting ``sync_time_with_host`` is enough for periodic synchronization. Requires VMware Tools to be installed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sync_time_with_host_periodically DataVsphereVirtualMachine#sync_time_with_host_periodically}
        :param tools_upgrade_policy: Set the upgrade policy for VMware Tools. Can be one of ``manual`` or ``upgradeAtPowerCycle``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#tools_upgrade_policy DataVsphereVirtualMachine#tools_upgrade_policy}
        :param uuid: The UUID of the virtual machine. Also exposed as the ID of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#uuid DataVsphereVirtualMachine#uuid}
        :param vapp: vapp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vapp DataVsphereVirtualMachine#vapp}
        :param vbs_enabled: Flag to specify if Virtualization-based security is enabled for this virtual machine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vbs_enabled DataVsphereVirtualMachine#vbs_enabled}
        :param vvtd_enabled: Flag to specify if I/O MMU virtualization, also called Intel Virtualization Technology for Directed I/O (VT-d) and AMD I/O Virtualization (AMD-Vi or IOMMU), is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vvtd_enabled DataVsphereVirtualMachine#vvtd_enabled}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(vapp, dict):
            vapp = DataVsphereVirtualMachineVapp(**vapp)
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument alternate_guest_name", value=alternate_guest_name, expected_type=type_hints["alternate_guest_name"])
            check_type(argname="argument annotation", value=annotation, expected_type=type_hints["annotation"])
            check_type(argname="argument boot_delay", value=boot_delay, expected_type=type_hints["boot_delay"])
            check_type(argname="argument boot_retry_delay", value=boot_retry_delay, expected_type=type_hints["boot_retry_delay"])
            check_type(argname="argument boot_retry_enabled", value=boot_retry_enabled, expected_type=type_hints["boot_retry_enabled"])
            check_type(argname="argument cpu_hot_add_enabled", value=cpu_hot_add_enabled, expected_type=type_hints["cpu_hot_add_enabled"])
            check_type(argname="argument cpu_hot_remove_enabled", value=cpu_hot_remove_enabled, expected_type=type_hints["cpu_hot_remove_enabled"])
            check_type(argname="argument cpu_limit", value=cpu_limit, expected_type=type_hints["cpu_limit"])
            check_type(argname="argument cpu_performance_counters_enabled", value=cpu_performance_counters_enabled, expected_type=type_hints["cpu_performance_counters_enabled"])
            check_type(argname="argument cpu_reservation", value=cpu_reservation, expected_type=type_hints["cpu_reservation"])
            check_type(argname="argument cpu_share_count", value=cpu_share_count, expected_type=type_hints["cpu_share_count"])
            check_type(argname="argument cpu_share_level", value=cpu_share_level, expected_type=type_hints["cpu_share_level"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument efi_secure_boot_enabled", value=efi_secure_boot_enabled, expected_type=type_hints["efi_secure_boot_enabled"])
            check_type(argname="argument enable_disk_uuid", value=enable_disk_uuid, expected_type=type_hints["enable_disk_uuid"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument ept_rvi_mode", value=ept_rvi_mode, expected_type=type_hints["ept_rvi_mode"])
            check_type(argname="argument extra_config", value=extra_config, expected_type=type_hints["extra_config"])
            check_type(argname="argument firmware", value=firmware, expected_type=type_hints["firmware"])
            check_type(argname="argument guest_id", value=guest_id, expected_type=type_hints["guest_id"])
            check_type(argname="argument hardware_version", value=hardware_version, expected_type=type_hints["hardware_version"])
            check_type(argname="argument hv_mode", value=hv_mode, expected_type=type_hints["hv_mode"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ide_controller_scan_count", value=ide_controller_scan_count, expected_type=type_hints["ide_controller_scan_count"])
            check_type(argname="argument latency_sensitivity", value=latency_sensitivity, expected_type=type_hints["latency_sensitivity"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument memory_hot_add_enabled", value=memory_hot_add_enabled, expected_type=type_hints["memory_hot_add_enabled"])
            check_type(argname="argument memory_limit", value=memory_limit, expected_type=type_hints["memory_limit"])
            check_type(argname="argument memory_reservation", value=memory_reservation, expected_type=type_hints["memory_reservation"])
            check_type(argname="argument memory_share_count", value=memory_share_count, expected_type=type_hints["memory_share_count"])
            check_type(argname="argument memory_share_level", value=memory_share_level, expected_type=type_hints["memory_share_level"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nested_hv_enabled", value=nested_hv_enabled, expected_type=type_hints["nested_hv_enabled"])
            check_type(argname="argument num_cores_per_socket", value=num_cores_per_socket, expected_type=type_hints["num_cores_per_socket"])
            check_type(argname="argument num_cpus", value=num_cpus, expected_type=type_hints["num_cpus"])
            check_type(argname="argument replace_trigger", value=replace_trigger, expected_type=type_hints["replace_trigger"])
            check_type(argname="argument run_tools_scripts_after_power_on", value=run_tools_scripts_after_power_on, expected_type=type_hints["run_tools_scripts_after_power_on"])
            check_type(argname="argument run_tools_scripts_after_resume", value=run_tools_scripts_after_resume, expected_type=type_hints["run_tools_scripts_after_resume"])
            check_type(argname="argument run_tools_scripts_before_guest_reboot", value=run_tools_scripts_before_guest_reboot, expected_type=type_hints["run_tools_scripts_before_guest_reboot"])
            check_type(argname="argument run_tools_scripts_before_guest_shutdown", value=run_tools_scripts_before_guest_shutdown, expected_type=type_hints["run_tools_scripts_before_guest_shutdown"])
            check_type(argname="argument run_tools_scripts_before_guest_standby", value=run_tools_scripts_before_guest_standby, expected_type=type_hints["run_tools_scripts_before_guest_standby"])
            check_type(argname="argument sata_controller_scan_count", value=sata_controller_scan_count, expected_type=type_hints["sata_controller_scan_count"])
            check_type(argname="argument scsi_controller_scan_count", value=scsi_controller_scan_count, expected_type=type_hints["scsi_controller_scan_count"])
            check_type(argname="argument storage_policy_id", value=storage_policy_id, expected_type=type_hints["storage_policy_id"])
            check_type(argname="argument swap_placement_policy", value=swap_placement_policy, expected_type=type_hints["swap_placement_policy"])
            check_type(argname="argument sync_time_with_host", value=sync_time_with_host, expected_type=type_hints["sync_time_with_host"])
            check_type(argname="argument sync_time_with_host_periodically", value=sync_time_with_host_periodically, expected_type=type_hints["sync_time_with_host_periodically"])
            check_type(argname="argument tools_upgrade_policy", value=tools_upgrade_policy, expected_type=type_hints["tools_upgrade_policy"])
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
            check_type(argname="argument vapp", value=vapp, expected_type=type_hints["vapp"])
            check_type(argname="argument vbs_enabled", value=vbs_enabled, expected_type=type_hints["vbs_enabled"])
            check_type(argname="argument vvtd_enabled", value=vvtd_enabled, expected_type=type_hints["vvtd_enabled"])
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
        if alternate_guest_name is not None:
            self._values["alternate_guest_name"] = alternate_guest_name
        if annotation is not None:
            self._values["annotation"] = annotation
        if boot_delay is not None:
            self._values["boot_delay"] = boot_delay
        if boot_retry_delay is not None:
            self._values["boot_retry_delay"] = boot_retry_delay
        if boot_retry_enabled is not None:
            self._values["boot_retry_enabled"] = boot_retry_enabled
        if cpu_hot_add_enabled is not None:
            self._values["cpu_hot_add_enabled"] = cpu_hot_add_enabled
        if cpu_hot_remove_enabled is not None:
            self._values["cpu_hot_remove_enabled"] = cpu_hot_remove_enabled
        if cpu_limit is not None:
            self._values["cpu_limit"] = cpu_limit
        if cpu_performance_counters_enabled is not None:
            self._values["cpu_performance_counters_enabled"] = cpu_performance_counters_enabled
        if cpu_reservation is not None:
            self._values["cpu_reservation"] = cpu_reservation
        if cpu_share_count is not None:
            self._values["cpu_share_count"] = cpu_share_count
        if cpu_share_level is not None:
            self._values["cpu_share_level"] = cpu_share_level
        if datacenter_id is not None:
            self._values["datacenter_id"] = datacenter_id
        if efi_secure_boot_enabled is not None:
            self._values["efi_secure_boot_enabled"] = efi_secure_boot_enabled
        if enable_disk_uuid is not None:
            self._values["enable_disk_uuid"] = enable_disk_uuid
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if ept_rvi_mode is not None:
            self._values["ept_rvi_mode"] = ept_rvi_mode
        if extra_config is not None:
            self._values["extra_config"] = extra_config
        if firmware is not None:
            self._values["firmware"] = firmware
        if guest_id is not None:
            self._values["guest_id"] = guest_id
        if hardware_version is not None:
            self._values["hardware_version"] = hardware_version
        if hv_mode is not None:
            self._values["hv_mode"] = hv_mode
        if id is not None:
            self._values["id"] = id
        if ide_controller_scan_count is not None:
            self._values["ide_controller_scan_count"] = ide_controller_scan_count
        if latency_sensitivity is not None:
            self._values["latency_sensitivity"] = latency_sensitivity
        if memory is not None:
            self._values["memory"] = memory
        if memory_hot_add_enabled is not None:
            self._values["memory_hot_add_enabled"] = memory_hot_add_enabled
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if memory_reservation is not None:
            self._values["memory_reservation"] = memory_reservation
        if memory_share_count is not None:
            self._values["memory_share_count"] = memory_share_count
        if memory_share_level is not None:
            self._values["memory_share_level"] = memory_share_level
        if name is not None:
            self._values["name"] = name
        if nested_hv_enabled is not None:
            self._values["nested_hv_enabled"] = nested_hv_enabled
        if num_cores_per_socket is not None:
            self._values["num_cores_per_socket"] = num_cores_per_socket
        if num_cpus is not None:
            self._values["num_cpus"] = num_cpus
        if replace_trigger is not None:
            self._values["replace_trigger"] = replace_trigger
        if run_tools_scripts_after_power_on is not None:
            self._values["run_tools_scripts_after_power_on"] = run_tools_scripts_after_power_on
        if run_tools_scripts_after_resume is not None:
            self._values["run_tools_scripts_after_resume"] = run_tools_scripts_after_resume
        if run_tools_scripts_before_guest_reboot is not None:
            self._values["run_tools_scripts_before_guest_reboot"] = run_tools_scripts_before_guest_reboot
        if run_tools_scripts_before_guest_shutdown is not None:
            self._values["run_tools_scripts_before_guest_shutdown"] = run_tools_scripts_before_guest_shutdown
        if run_tools_scripts_before_guest_standby is not None:
            self._values["run_tools_scripts_before_guest_standby"] = run_tools_scripts_before_guest_standby
        if sata_controller_scan_count is not None:
            self._values["sata_controller_scan_count"] = sata_controller_scan_count
        if scsi_controller_scan_count is not None:
            self._values["scsi_controller_scan_count"] = scsi_controller_scan_count
        if storage_policy_id is not None:
            self._values["storage_policy_id"] = storage_policy_id
        if swap_placement_policy is not None:
            self._values["swap_placement_policy"] = swap_placement_policy
        if sync_time_with_host is not None:
            self._values["sync_time_with_host"] = sync_time_with_host
        if sync_time_with_host_periodically is not None:
            self._values["sync_time_with_host_periodically"] = sync_time_with_host_periodically
        if tools_upgrade_policy is not None:
            self._values["tools_upgrade_policy"] = tools_upgrade_policy
        if uuid is not None:
            self._values["uuid"] = uuid
        if vapp is not None:
            self._values["vapp"] = vapp
        if vbs_enabled is not None:
            self._values["vbs_enabled"] = vbs_enabled
        if vvtd_enabled is not None:
            self._values["vvtd_enabled"] = vvtd_enabled

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
    def alternate_guest_name(self) -> typing.Optional[builtins.str]:
        '''The guest name for the operating system when guest_id is otherGuest or otherGuest64.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#alternate_guest_name DataVsphereVirtualMachine#alternate_guest_name}
        '''
        result = self._values.get("alternate_guest_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def annotation(self) -> typing.Optional[builtins.str]:
        '''User-provided description of the virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#annotation DataVsphereVirtualMachine#annotation}
        '''
        result = self._values.get("annotation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_delay(self) -> typing.Optional[jsii.Number]:
        '''The number of milliseconds to wait before starting the boot sequence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_delay DataVsphereVirtualMachine#boot_delay}
        '''
        result = self._values.get("boot_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_retry_delay(self) -> typing.Optional[jsii.Number]:
        '''The number of milliseconds to wait before retrying the boot sequence. This only valid if boot_retry_enabled is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_retry_delay DataVsphereVirtualMachine#boot_retry_delay}
        '''
        result = self._values.get("boot_retry_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def boot_retry_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, a virtual machine that fails to boot will try again after the delay defined in boot_retry_delay.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#boot_retry_enabled DataVsphereVirtualMachine#boot_retry_enabled}
        '''
        result = self._values.get("boot_retry_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cpu_hot_add_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow CPUs to be added to this virtual machine while it is running.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_hot_add_enabled DataVsphereVirtualMachine#cpu_hot_add_enabled}
        '''
        result = self._values.get("cpu_hot_add_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cpu_hot_remove_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow CPUs to be added to this virtual machine while it is running.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_hot_remove_enabled DataVsphereVirtualMachine#cpu_hot_remove_enabled}
        '''
        result = self._values.get("cpu_hot_remove_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cpu_limit(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of memory (in MB) or CPU (in MHz) that this virtual machine can consume, regardless of available resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_limit DataVsphereVirtualMachine#cpu_limit}
        '''
        result = self._values.get("cpu_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_performance_counters_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable CPU performance counters on this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_performance_counters_enabled DataVsphereVirtualMachine#cpu_performance_counters_enabled}
        '''
        result = self._values.get("cpu_performance_counters_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cpu_reservation(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory (in MB) or CPU (in MHz) that this virtual machine is guaranteed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_reservation DataVsphereVirtualMachine#cpu_reservation}
        '''
        result = self._values.get("cpu_reservation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to cpu for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_share_count DataVsphereVirtualMachine#cpu_share_count}
        '''
        result = self._values.get("cpu_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for cpu resources. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#cpu_share_level DataVsphereVirtualMachine#cpu_share_level}
        '''
        result = self._values.get("cpu_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datacenter_id(self) -> typing.Optional[builtins.str]:
        '''The managed object ID of the datacenter the virtual machine is in.

        This is not required when using ESXi directly, or if there is only one datacenter in your infrastructure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#datacenter_id DataVsphereVirtualMachine#datacenter_id}
        '''
        result = self._values.get("datacenter_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def efi_secure_boot_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When the boot type set in firmware is efi, this enables EFI secure boot.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#efi_secure_boot_enabled DataVsphereVirtualMachine#efi_secure_boot_enabled}
        '''
        result = self._values.get("efi_secure_boot_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_disk_uuid(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Expose the UUIDs of attached virtual disks to the virtual machine, allowing access to them in the guest.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#enable_disk_uuid DataVsphereVirtualMachine#enable_disk_uuid}
        '''
        result = self._values.get("enable_disk_uuid")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable logging on this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#enable_logging DataVsphereVirtualMachine#enable_logging}
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ept_rvi_mode(self) -> typing.Optional[builtins.str]:
        '''The EPT/RVI (hardware memory virtualization) setting for this virtual machine. Can be one of automatic, on, or off.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#ept_rvi_mode DataVsphereVirtualMachine#ept_rvi_mode}
        '''
        result = self._values.get("ept_rvi_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Extra configuration data for this virtual machine.

        Can be used to supply advanced parameters not normally in configuration, such as instance metadata, or configuration data for OVF images.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#extra_config DataVsphereVirtualMachine#extra_config}
        '''
        result = self._values.get("extra_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def firmware(self) -> typing.Optional[builtins.str]:
        '''The firmware interface to use on the virtual machine. Can be one of bios or efi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#firmware DataVsphereVirtualMachine#firmware}
        '''
        result = self._values.get("firmware")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def guest_id(self) -> typing.Optional[builtins.str]:
        '''The guest ID for the operating system.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#guest_id DataVsphereVirtualMachine#guest_id}
        '''
        result = self._values.get("guest_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hardware_version(self) -> typing.Optional[jsii.Number]:
        '''The hardware version for the virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#hardware_version DataVsphereVirtualMachine#hardware_version}
        '''
        result = self._values.get("hardware_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def hv_mode(self) -> typing.Optional[builtins.str]:
        '''The (non-nested) hardware virtualization setting for this virtual machine. Can be one of hvAuto, hvOn, or hvOff.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#hv_mode DataVsphereVirtualMachine#hv_mode}
        '''
        result = self._values.get("hv_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#id DataVsphereVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ide_controller_scan_count(self) -> typing.Optional[jsii.Number]:
        '''The number of IDE controllers to scan for disk sizes and controller types on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#ide_controller_scan_count DataVsphereVirtualMachine#ide_controller_scan_count}
        '''
        result = self._values.get("ide_controller_scan_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def latency_sensitivity(self) -> typing.Optional[builtins.str]:
        '''Controls the scheduling delay of the virtual machine.

        Use a higher sensitivity for applications that require lower latency, such as VOIP, media player applications, or applications that require frequent access to mouse or keyboard devices. Can be one of low, normal, medium, or high.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#latency_sensitivity DataVsphereVirtualMachine#latency_sensitivity}
        '''
        result = self._values.get("latency_sensitivity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[jsii.Number]:
        '''The size of the virtual machine's memory, in MB.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory DataVsphereVirtualMachine#memory}
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_hot_add_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow memory to be added to this virtual machine while it is running.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_hot_add_enabled DataVsphereVirtualMachine#memory_hot_add_enabled}
        '''
        result = self._values.get("memory_hot_add_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of memory (in MB) or CPU (in MHz) that this virtual machine can consume, regardless of available resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_limit DataVsphereVirtualMachine#memory_limit}
        '''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_reservation(self) -> typing.Optional[jsii.Number]:
        '''The amount of memory (in MB) or CPU (in MHz) that this virtual machine is guaranteed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_reservation DataVsphereVirtualMachine#memory_reservation}
        '''
        result = self._values.get("memory_reservation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_share_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of shares to allocate to memory for a custom share level.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_share_count DataVsphereVirtualMachine#memory_share_count}
        '''
        result = self._values.get("memory_share_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_share_level(self) -> typing.Optional[builtins.str]:
        '''The allocation level for memory resources. Can be one of high, low, normal, or custom.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#memory_share_level DataVsphereVirtualMachine#memory_share_level}
        '''
        result = self._values.get("memory_share_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#name DataVsphereVirtualMachine#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nested_hv_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable nested hardware virtualization on this virtual machine, facilitating nested virtualization in the guest.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#nested_hv_enabled DataVsphereVirtualMachine#nested_hv_enabled}
        '''
        result = self._values.get("nested_hv_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def num_cores_per_socket(self) -> typing.Optional[jsii.Number]:
        '''The number of cores to distribute amongst the CPUs in this virtual machine.

        If specified, the value supplied to num_cpus must be evenly divisible by this value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#num_cores_per_socket DataVsphereVirtualMachine#num_cores_per_socket}
        '''
        result = self._values.get("num_cores_per_socket")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_cpus(self) -> typing.Optional[jsii.Number]:
        '''The number of virtual processors to assign to this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#num_cpus DataVsphereVirtualMachine#num_cpus}
        '''
        result = self._values.get("num_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replace_trigger(self) -> typing.Optional[builtins.str]:
        '''Triggers replacement of resource whenever it changes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#replace_trigger DataVsphereVirtualMachine#replace_trigger}
        '''
        result = self._values.get("replace_trigger")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_tools_scripts_after_power_on(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the run of scripts after virtual machine power-on when VMware Tools is installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_after_power_on DataVsphereVirtualMachine#run_tools_scripts_after_power_on}
        '''
        result = self._values.get("run_tools_scripts_after_power_on")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_tools_scripts_after_resume(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the run of scripts after virtual machine resume when when VMware Tools is installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_after_resume DataVsphereVirtualMachine#run_tools_scripts_after_resume}
        '''
        result = self._values.get("run_tools_scripts_after_resume")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_tools_scripts_before_guest_reboot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the run of scripts before guest operating system reboot when VMware Tools is installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_reboot DataVsphereVirtualMachine#run_tools_scripts_before_guest_reboot}
        '''
        result = self._values.get("run_tools_scripts_before_guest_reboot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_tools_scripts_before_guest_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the run of scripts before guest operating system shutdown when VMware Tools is installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_shutdown DataVsphereVirtualMachine#run_tools_scripts_before_guest_shutdown}
        '''
        result = self._values.get("run_tools_scripts_before_guest_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def run_tools_scripts_before_guest_standby(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable the run of scripts before guest operating system standby when VMware Tools is installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#run_tools_scripts_before_guest_standby DataVsphereVirtualMachine#run_tools_scripts_before_guest_standby}
        '''
        result = self._values.get("run_tools_scripts_before_guest_standby")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sata_controller_scan_count(self) -> typing.Optional[jsii.Number]:
        '''The number of SATA controllers to scan for disk sizes and controller types on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sata_controller_scan_count DataVsphereVirtualMachine#sata_controller_scan_count}
        '''
        result = self._values.get("sata_controller_scan_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scsi_controller_scan_count(self) -> typing.Optional[jsii.Number]:
        '''The number of SCSI controllers to scan for disk sizes and controller types on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#scsi_controller_scan_count DataVsphereVirtualMachine#scsi_controller_scan_count}
        '''
        result = self._values.get("scsi_controller_scan_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_policy_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the storage policy to assign to the virtual machine home directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#storage_policy_id DataVsphereVirtualMachine#storage_policy_id}
        '''
        result = self._values.get("storage_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def swap_placement_policy(self) -> typing.Optional[builtins.str]:
        '''The swap file placement policy for this virtual machine. Can be one of inherit, hostLocal, or vmDirectory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#swap_placement_policy DataVsphereVirtualMachine#swap_placement_policy}
        '''
        result = self._values.get("swap_placement_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_time_with_host(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable guest clock synchronization with the host.

        On vSphere 7.0 U1 and above, with only this setting the clock is synchronized on startup and resume. Requires VMware Tools to be installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sync_time_with_host DataVsphereVirtualMachine#sync_time_with_host}
        '''
        result = self._values.get("sync_time_with_host")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sync_time_with_host_periodically(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable periodic clock synchronization with the host.

        Supported only on vSphere 7.0 U1 and above. On prior versions setting ``sync_time_with_host`` is enough for periodic synchronization. Requires VMware Tools to be installed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#sync_time_with_host_periodically DataVsphereVirtualMachine#sync_time_with_host_periodically}
        '''
        result = self._values.get("sync_time_with_host_periodically")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tools_upgrade_policy(self) -> typing.Optional[builtins.str]:
        '''Set the upgrade policy for VMware Tools. Can be one of ``manual`` or ``upgradeAtPowerCycle``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#tools_upgrade_policy DataVsphereVirtualMachine#tools_upgrade_policy}
        '''
        result = self._values.get("tools_upgrade_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uuid(self) -> typing.Optional[builtins.str]:
        '''The UUID of the virtual machine. Also exposed as the ID of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#uuid DataVsphereVirtualMachine#uuid}
        '''
        result = self._values.get("uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vapp(self) -> typing.Optional["DataVsphereVirtualMachineVapp"]:
        '''vapp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vapp DataVsphereVirtualMachine#vapp}
        '''
        result = self._values.get("vapp")
        return typing.cast(typing.Optional["DataVsphereVirtualMachineVapp"], result)

    @builtins.property
    def vbs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to specify if Virtualization-based security is enabled for this virtual machine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vbs_enabled DataVsphereVirtualMachine#vbs_enabled}
        '''
        result = self._values.get("vbs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vvtd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Flag to specify if I/O MMU virtualization, also called Intel Virtualization Technology for Directed I/O (VT-d) and AMD I/O Virtualization (AMD-Vi or IOMMU), is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#vvtd_enabled DataVsphereVirtualMachine#vvtd_enabled}
        '''
        result = self._values.get("vvtd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVsphereVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineDisks",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataVsphereVirtualMachineDisks:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVsphereVirtualMachineDisks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataVsphereVirtualMachineDisksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineDisksList",
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
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineDisksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataVsphereVirtualMachineDisksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineDisksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataVsphereVirtualMachineDisksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineDisksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineDisksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineDisksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataVsphereVirtualMachineDisksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineDisksOutputReference",
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
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineDisksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="eagerlyScrub")
    def eagerly_scrub(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "eagerlyScrub"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @builtins.property
    @jsii.member(jsii_name="thinProvisioned")
    def thin_provisioned(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "thinProvisioned"))

    @builtins.property
    @jsii.member(jsii_name="unitNumber")
    def unit_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unitNumber"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataVsphereVirtualMachineDisks]:
        return typing.cast(typing.Optional[DataVsphereVirtualMachineDisks], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataVsphereVirtualMachineDisks],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineDisksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineNetworkInterfaces",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataVsphereVirtualMachineNetworkInterfaces:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVsphereVirtualMachineNetworkInterfaces(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataVsphereVirtualMachineNetworkInterfacesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineNetworkInterfacesList",
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
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineNetworkInterfacesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataVsphereVirtualMachineNetworkInterfacesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineNetworkInterfacesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataVsphereVirtualMachineNetworkInterfacesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineNetworkInterfacesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineNetworkInterfacesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineNetworkInterfacesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataVsphereVirtualMachineNetworkInterfacesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineNetworkInterfacesOutputReference",
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
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineNetworkInterfacesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="adapterType")
    def adapter_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adapterType"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthLimit")
    def bandwidth_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bandwidthLimit"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthReservation")
    def bandwidth_reservation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bandwidthReservation"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthShareCount")
    def bandwidth_share_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bandwidthShareCount"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthShareLevel")
    def bandwidth_share_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bandwidthShareLevel"))

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataVsphereVirtualMachineNetworkInterfaces]:
        return typing.cast(typing.Optional[DataVsphereVirtualMachineNetworkInterfaces], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataVsphereVirtualMachineNetworkInterfaces],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineNetworkInterfacesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineVapp",
    jsii_struct_bases=[],
    name_mapping={"properties": "properties"},
)
class DataVsphereVirtualMachineVapp:
    def __init__(
        self,
        *,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param properties: A map of customizable vApp properties and their values. Allows customization of VMs cloned from OVF templates which have customizable vApp properties. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#properties DataVsphereVirtualMachine#properties}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineVapp.__init__)
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of customizable vApp properties and their values.

        Allows customization of VMs cloned from OVF templates which have customizable vApp properties.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/d/virtual_machine#properties DataVsphereVirtualMachine#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVsphereVirtualMachineVapp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataVsphereVirtualMachineVappOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.dataVsphereVirtualMachine.DataVsphereVirtualMachineVappOutputReference",
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
            type_hints = typing.get_type_hints(DataVsphereVirtualMachineVappOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineVappOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataVsphereVirtualMachineVapp]:
        return typing.cast(typing.Optional[DataVsphereVirtualMachineVapp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataVsphereVirtualMachineVapp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVsphereVirtualMachineVappOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataVsphereVirtualMachine",
    "DataVsphereVirtualMachineConfig",
    "DataVsphereVirtualMachineDisks",
    "DataVsphereVirtualMachineDisksList",
    "DataVsphereVirtualMachineDisksOutputReference",
    "DataVsphereVirtualMachineNetworkInterfaces",
    "DataVsphereVirtualMachineNetworkInterfacesList",
    "DataVsphereVirtualMachineNetworkInterfacesOutputReference",
    "DataVsphereVirtualMachineVapp",
    "DataVsphereVirtualMachineVappOutputReference",
]

publication.publish()
