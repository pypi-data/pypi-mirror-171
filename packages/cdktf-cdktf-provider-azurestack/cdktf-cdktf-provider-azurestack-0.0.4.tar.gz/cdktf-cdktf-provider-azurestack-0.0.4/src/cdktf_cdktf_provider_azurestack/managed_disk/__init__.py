'''
# `azurestack_managed_disk`

Refer to the Terraform Registory for docs: [`azurestack_managed_disk`](https://www.terraform.io/docs/providers/azurestack/r/managed_disk).
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


class ManagedDisk(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDisk",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk azurestack_managed_disk}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        create_option: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        storage_account_type: builtins.str,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union["ManagedDiskEncryption", typing.Dict[str, typing.Any]]] = None,
        hyper_v_generation: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_reference_id: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        source_resource_id: typing.Optional[builtins.str] = None,
        source_uri: typing.Optional[builtins.str] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ManagedDiskTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk azurestack_managed_disk} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#create_option ManagedDisk#create_option}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#location ManagedDisk#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#name ManagedDisk#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#resource_group_name ManagedDisk#resource_group_name}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#storage_account_type ManagedDisk#storage_account_type}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#disk_size_gb ManagedDisk#disk_size_gb}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#encryption ManagedDisk#encryption}
        :param hyper_v_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#hyper_v_generation ManagedDisk#hyper_v_generation}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#id ManagedDisk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_reference_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#image_reference_id ManagedDisk#image_reference_id}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#os_type ManagedDisk#os_type}.
        :param source_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_resource_id ManagedDisk#source_resource_id}.
        :param source_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_uri ManagedDisk#source_uri}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#storage_account_id ManagedDisk#storage_account_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#tags ManagedDisk#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#timeouts ManagedDisk#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDisk.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedDiskConfig(
            create_option=create_option,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            storage_account_type=storage_account_type,
            disk_size_gb=disk_size_gb,
            encryption=encryption,
            hyper_v_generation=hyper_v_generation,
            id=id,
            image_reference_id=image_reference_id,
            os_type=os_type,
            source_resource_id=source_resource_id,
            source_uri=source_uri,
            storage_account_id=storage_account_id,
            tags=tags,
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

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        disk_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        key_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionKeyEncryptionKey", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#enabled ManagedDisk#enabled}.
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#disk_encryption_key ManagedDisk#disk_encryption_key}
        :param key_encryption_key: key_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#key_encryption_key ManagedDisk#key_encryption_key}
        '''
        value = ManagedDiskEncryption(
            enabled=enabled,
            disk_encryption_key=disk_encryption_key,
            key_encryption_key=key_encryption_key,
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#create ManagedDisk#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#delete ManagedDisk#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#read ManagedDisk#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#update ManagedDisk#update}.
        '''
        value = ManagedDiskTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetHyperVGeneration")
    def reset_hyper_v_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHyperVGeneration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageReferenceId")
    def reset_image_reference_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageReferenceId", []))

    @jsii.member(jsii_name="resetOsType")
    def reset_os_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsType", []))

    @jsii.member(jsii_name="resetSourceResourceId")
    def reset_source_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceResourceId", []))

    @jsii.member(jsii_name="resetSourceUri")
    def reset_source_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceUri", []))

    @jsii.member(jsii_name="resetStorageAccountId")
    def reset_storage_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> "ManagedDiskEncryptionOutputReference":
        return typing.cast("ManagedDiskEncryptionOutputReference", jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ManagedDiskTimeoutsOutputReference":
        return typing.cast("ManagedDiskTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional["ManagedDiskEncryption"]:
        return typing.cast(typing.Optional["ManagedDiskEncryption"], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hyperVGenerationInput")
    def hyper_v_generation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hyperVGenerationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageReferenceIdInput")
    def image_reference_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageReferenceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceResourceIdInput")
    def source_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUriInput")
    def source_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ManagedDiskTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ManagedDiskTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "create_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="hyperVGeneration")
    def hyper_v_generation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hyperVGeneration"))

    @hyper_v_generation.setter
    def hyper_v_generation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "hyper_v_generation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hyperVGeneration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageReferenceId")
    def image_reference_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageReferenceId"))

    @image_reference_id.setter
    def image_reference_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "image_reference_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageReferenceId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "os_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceResourceId")
    def source_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceResourceId"))

    @source_resource_id.setter
    def source_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "source_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUri")
    def source_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUri"))

    @source_uri.setter
    def source_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "source_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUri", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "create_option": "createOption",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "storage_account_type": "storageAccountType",
        "disk_size_gb": "diskSizeGb",
        "encryption": "encryption",
        "hyper_v_generation": "hyperVGeneration",
        "id": "id",
        "image_reference_id": "imageReferenceId",
        "os_type": "osType",
        "source_resource_id": "sourceResourceId",
        "source_uri": "sourceUri",
        "storage_account_id": "storageAccountId",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ManagedDiskConfig(cdktf.TerraformMetaArguments):
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
        create_option: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        storage_account_type: builtins.str,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union["ManagedDiskEncryption", typing.Dict[str, typing.Any]]] = None,
        hyper_v_generation: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_reference_id: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        source_resource_id: typing.Optional[builtins.str] = None,
        source_uri: typing.Optional[builtins.str] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ManagedDiskTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#create_option ManagedDisk#create_option}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#location ManagedDisk#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#name ManagedDisk#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#resource_group_name ManagedDisk#resource_group_name}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#storage_account_type ManagedDisk#storage_account_type}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#disk_size_gb ManagedDisk#disk_size_gb}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#encryption ManagedDisk#encryption}
        :param hyper_v_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#hyper_v_generation ManagedDisk#hyper_v_generation}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#id ManagedDisk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_reference_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#image_reference_id ManagedDisk#image_reference_id}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#os_type ManagedDisk#os_type}.
        :param source_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_resource_id ManagedDisk#source_resource_id}.
        :param source_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_uri ManagedDisk#source_uri}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#storage_account_id ManagedDisk#storage_account_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#tags ManagedDisk#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#timeouts ManagedDisk#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(encryption, dict):
            encryption = ManagedDiskEncryption(**encryption)
        if isinstance(timeouts, dict):
            timeouts = ManagedDiskTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument hyper_v_generation", value=hyper_v_generation, expected_type=type_hints["hyper_v_generation"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_reference_id", value=image_reference_id, expected_type=type_hints["image_reference_id"])
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument source_resource_id", value=source_resource_id, expected_type=type_hints["source_resource_id"])
            check_type(argname="argument source_uri", value=source_uri, expected_type=type_hints["source_uri"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "create_option": create_option,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "storage_account_type": storage_account_type,
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
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if encryption is not None:
            self._values["encryption"] = encryption
        if hyper_v_generation is not None:
            self._values["hyper_v_generation"] = hyper_v_generation
        if id is not None:
            self._values["id"] = id
        if image_reference_id is not None:
            self._values["image_reference_id"] = image_reference_id
        if os_type is not None:
            self._values["os_type"] = os_type
        if source_resource_id is not None:
            self._values["source_resource_id"] = source_resource_id
        if source_uri is not None:
            self._values["source_uri"] = source_uri
        if storage_account_id is not None:
            self._values["storage_account_id"] = storage_account_id
        if tags is not None:
            self._values["tags"] = tags
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
    def create_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#create_option ManagedDisk#create_option}.'''
        result = self._values.get("create_option")
        assert result is not None, "Required property 'create_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#location ManagedDisk#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#name ManagedDisk#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#resource_group_name ManagedDisk#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#storage_account_type ManagedDisk#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#disk_size_gb ManagedDisk#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption(self) -> typing.Optional["ManagedDiskEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#encryption ManagedDisk#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["ManagedDiskEncryption"], result)

    @builtins.property
    def hyper_v_generation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#hyper_v_generation ManagedDisk#hyper_v_generation}.'''
        result = self._values.get("hyper_v_generation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#id ManagedDisk#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_reference_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#image_reference_id ManagedDisk#image_reference_id}.'''
        result = self._values.get("image_reference_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#os_type ManagedDisk#os_type}.'''
        result = self._values.get("os_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_resource_id ManagedDisk#source_resource_id}.'''
        result = self._values.get("source_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_uri ManagedDisk#source_uri}.'''
        result = self._values.get("source_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#storage_account_id ManagedDisk#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#tags ManagedDisk#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ManagedDiskTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#timeouts ManagedDisk#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ManagedDiskTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "disk_encryption_key": "diskEncryptionKey",
        "key_encryption_key": "keyEncryptionKey",
    },
)
class ManagedDiskEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        disk_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        key_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionKeyEncryptionKey", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#enabled ManagedDisk#enabled}.
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#disk_encryption_key ManagedDisk#disk_encryption_key}
        :param key_encryption_key: key_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#key_encryption_key ManagedDisk#key_encryption_key}
        '''
        if isinstance(disk_encryption_key, dict):
            disk_encryption_key = ManagedDiskEncryptionDiskEncryptionKey(**disk_encryption_key)
        if isinstance(key_encryption_key, dict):
            key_encryption_key = ManagedDiskEncryptionKeyEncryptionKey(**key_encryption_key)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskEncryption.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument disk_encryption_key", value=disk_encryption_key, expected_type=type_hints["disk_encryption_key"])
            check_type(argname="argument key_encryption_key", value=key_encryption_key, expected_type=type_hints["key_encryption_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if disk_encryption_key is not None:
            self._values["disk_encryption_key"] = disk_encryption_key
        if key_encryption_key is not None:
            self._values["key_encryption_key"] = key_encryption_key

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#enabled ManagedDisk#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def disk_encryption_key(
        self,
    ) -> typing.Optional["ManagedDiskEncryptionDiskEncryptionKey"]:
        '''disk_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#disk_encryption_key ManagedDisk#disk_encryption_key}
        '''
        result = self._values.get("disk_encryption_key")
        return typing.cast(typing.Optional["ManagedDiskEncryptionDiskEncryptionKey"], result)

    @builtins.property
    def key_encryption_key(
        self,
    ) -> typing.Optional["ManagedDiskEncryptionKeyEncryptionKey"]:
        '''key_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#key_encryption_key ManagedDisk#key_encryption_key}
        '''
        result = self._values.get("key_encryption_key")
        return typing.cast(typing.Optional["ManagedDiskEncryptionKeyEncryptionKey"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskEncryptionDiskEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"secret_url": "secretUrl", "source_vault_id": "sourceVaultId"},
)
class ManagedDiskEncryptionDiskEncryptionKey:
    def __init__(
        self,
        *,
        secret_url: builtins.str,
        source_vault_id: builtins.str,
    ) -> None:
        '''
        :param secret_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#secret_url ManagedDisk#secret_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskEncryptionDiskEncryptionKey.__init__)
            check_type(argname="argument secret_url", value=secret_url, expected_type=type_hints["secret_url"])
            check_type(argname="argument source_vault_id", value=source_vault_id, expected_type=type_hints["source_vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_url": secret_url,
            "source_vault_id": source_vault_id,
        }

    @builtins.property
    def secret_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#secret_url ManagedDisk#secret_url}.'''
        result = self._values.get("secret_url")
        assert result is not None, "Required property 'secret_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.'''
        result = self._values.get("source_vault_id")
        assert result is not None, "Required property 'source_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskEncryptionDiskEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDiskEncryptionDiskEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskEncryptionDiskEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskEncryptionDiskEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretUrlInput")
    def secret_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultIdInput")
    def source_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretUrl")
    def secret_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretUrl"))

    @secret_url.setter
    def secret_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionDiskEncryptionKeyOutputReference, "secret_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretUrl", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVaultId")
    def source_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVaultId"))

    @source_vault_id.setter
    def source_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionDiskEncryptionKeyOutputReference, "source_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDiskEncryptionDiskEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionDiskEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDiskEncryptionDiskEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionDiskEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskEncryptionKeyEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"key_url": "keyUrl", "source_vault_id": "sourceVaultId"},
)
class ManagedDiskEncryptionKeyEncryptionKey:
    def __init__(self, *, key_url: builtins.str, source_vault_id: builtins.str) -> None:
        '''
        :param key_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#key_url ManagedDisk#key_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskEncryptionKeyEncryptionKey.__init__)
            check_type(argname="argument key_url", value=key_url, expected_type=type_hints["key_url"])
            check_type(argname="argument source_vault_id", value=source_vault_id, expected_type=type_hints["source_vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_url": key_url,
            "source_vault_id": source_vault_id,
        }

    @builtins.property
    def key_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#key_url ManagedDisk#key_url}.'''
        result = self._values.get("key_url")
        assert result is not None, "Required property 'key_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.'''
        result = self._values.get("source_vault_id")
        assert result is not None, "Required property 'source_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskEncryptionKeyEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDiskEncryptionKeyEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskEncryptionKeyEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskEncryptionKeyEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyUrlInput")
    def key_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultIdInput")
    def source_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUrl")
    def key_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyUrl"))

    @key_url.setter
    def key_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionKeyEncryptionKeyOutputReference, "key_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVaultId")
    def source_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVaultId"))

    @source_vault_id.setter
    def source_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionKeyEncryptionKeyOutputReference, "source_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDiskEncryptionKeyEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionKeyEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDiskEncryptionKeyEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionKeyEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedDiskEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiskEncryptionKey")
    def put_disk_encryption_key(
        self,
        *,
        secret_url: builtins.str,
        source_vault_id: builtins.str,
    ) -> None:
        '''
        :param secret_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#secret_url ManagedDisk#secret_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        value = ManagedDiskEncryptionDiskEncryptionKey(
            secret_url=secret_url, source_vault_id=source_vault_id
        )

        return typing.cast(None, jsii.invoke(self, "putDiskEncryptionKey", [value]))

    @jsii.member(jsii_name="putKeyEncryptionKey")
    def put_key_encryption_key(
        self,
        *,
        key_url: builtins.str,
        source_vault_id: builtins.str,
    ) -> None:
        '''
        :param key_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#key_url ManagedDisk#key_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        value = ManagedDiskEncryptionKeyEncryptionKey(
            key_url=key_url, source_vault_id=source_vault_id
        )

        return typing.cast(None, jsii.invoke(self, "putKeyEncryptionKey", [value]))

    @jsii.member(jsii_name="resetDiskEncryptionKey")
    def reset_disk_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKey", []))

    @jsii.member(jsii_name="resetKeyEncryptionKey")
    def reset_key_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyEncryptionKey", []))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> ManagedDiskEncryptionDiskEncryptionKeyOutputReference:
        return typing.cast(ManagedDiskEncryptionDiskEncryptionKeyOutputReference, jsii.get(self, "diskEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="keyEncryptionKey")
    def key_encryption_key(
        self,
    ) -> ManagedDiskEncryptionKeyEncryptionKeyOutputReference:
        return typing.cast(ManagedDiskEncryptionKeyEncryptionKeyOutputReference, jsii.get(self, "keyEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyInput")
    def disk_encryption_key_input(
        self,
    ) -> typing.Optional[ManagedDiskEncryptionDiskEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionDiskEncryptionKey], jsii.get(self, "diskEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keyEncryptionKeyInput")
    def key_encryption_key_input(
        self,
    ) -> typing.Optional[ManagedDiskEncryptionKeyEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionKeyEncryptionKey], jsii.get(self, "keyEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDiskEncryption]:
        return typing.cast(typing.Optional[ManagedDiskEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ManagedDiskEncryption]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ManagedDiskTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#create ManagedDisk#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#delete ManagedDisk#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#read ManagedDisk#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#update ManagedDisk#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#create ManagedDisk#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#delete ManagedDisk#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#read ManagedDisk#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/managed_disk#update ManagedDisk#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDiskTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.managedDisk.ManagedDiskTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedDiskTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedDiskTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedDiskTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedDisk",
    "ManagedDiskConfig",
    "ManagedDiskEncryption",
    "ManagedDiskEncryptionDiskEncryptionKey",
    "ManagedDiskEncryptionDiskEncryptionKeyOutputReference",
    "ManagedDiskEncryptionKeyEncryptionKey",
    "ManagedDiskEncryptionKeyEncryptionKeyOutputReference",
    "ManagedDiskEncryptionOutputReference",
    "ManagedDiskTimeouts",
    "ManagedDiskTimeoutsOutputReference",
]

publication.publish()
