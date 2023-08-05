'''
# `boundary_host_catalog_plugin`

Refer to the Terraform Registory for docs: [`boundary_host_catalog_plugin`](https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin).
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


class HostCatalogPlugin(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-boundary.hostCatalogPlugin.HostCatalogPlugin",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin boundary_host_catalog_plugin}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scope_id: builtins.str,
        attributes_json: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        internal_force_update: typing.Optional[builtins.str] = None,
        internal_hmac_used_for_secrets_config_hmac: typing.Optional[builtins.str] = None,
        internal_secrets_config_hmac: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        plugin_id: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        secrets_hmac: typing.Optional[builtins.str] = None,
        secrets_json: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin boundary_host_catalog_plugin} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param scope_id: The scope ID in which the resource is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#scope_id HostCatalogPlugin#scope_id}
        :param attributes_json: The attributes for the host catalog. Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" or remove the block to clear all attributes in the host catalog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#attributes_json HostCatalogPlugin#attributes_json}
        :param description: The host catalog description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#description HostCatalogPlugin#description}
        :param internal_force_update: Internal only. Used to force update so that we can always check the value of secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_force_update HostCatalogPlugin#internal_force_update}
        :param internal_hmac_used_for_secrets_config_hmac: Internal only. The Boundary-provided HMAC used to calculate the current value of the HMAC'd config. Used for drift detection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_hmac_used_for_secrets_config_hmac HostCatalogPlugin#internal_hmac_used_for_secrets_config_hmac}
        :param internal_secrets_config_hmac: Internal only. HMAC of (serverSecretsHmac + config secrets). Used for proper secrets handling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_secrets_config_hmac HostCatalogPlugin#internal_secrets_config_hmac}
        :param name: The host catalog name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#name HostCatalogPlugin#name}
        :param plugin_id: The ID of the plugin that should back the resource. This or plugin_name must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#plugin_id HostCatalogPlugin#plugin_id}
        :param plugin_name: The name of the plugin that should back the resource. This or plugin_id must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#plugin_name HostCatalogPlugin#plugin_name}
        :param secrets_hmac: The HMAC'd secrets value returned from the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#secrets_hmac HostCatalogPlugin#secrets_hmac}
        :param secrets_json: The secrets for the host catalog. Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" to clear any existing values. NOTE: Unlike "attributes_json", removing this block will NOT clear secrets from the host catalog; this allows injecting secrets for one call, then removing them for storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#secrets_json HostCatalogPlugin#secrets_json}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HostCatalogPlugin.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = HostCatalogPluginConfig(
            scope_id=scope_id,
            attributes_json=attributes_json,
            description=description,
            internal_force_update=internal_force_update,
            internal_hmac_used_for_secrets_config_hmac=internal_hmac_used_for_secrets_config_hmac,
            internal_secrets_config_hmac=internal_secrets_config_hmac,
            name=name,
            plugin_id=plugin_id,
            plugin_name=plugin_name,
            secrets_hmac=secrets_hmac,
            secrets_json=secrets_json,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAttributesJson")
    def reset_attributes_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributesJson", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetInternalForceUpdate")
    def reset_internal_force_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalForceUpdate", []))

    @jsii.member(jsii_name="resetInternalHmacUsedForSecretsConfigHmac")
    def reset_internal_hmac_used_for_secrets_config_hmac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalHmacUsedForSecretsConfigHmac", []))

    @jsii.member(jsii_name="resetInternalSecretsConfigHmac")
    def reset_internal_secrets_config_hmac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalSecretsConfigHmac", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPluginId")
    def reset_plugin_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginId", []))

    @jsii.member(jsii_name="resetPluginName")
    def reset_plugin_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginName", []))

    @jsii.member(jsii_name="resetSecretsHmac")
    def reset_secrets_hmac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsHmac", []))

    @jsii.member(jsii_name="resetSecretsJson")
    def reset_secrets_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretsJson", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="attributesJsonInput")
    def attributes_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributesJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalForceUpdateInput")
    def internal_force_update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "internalForceUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="internalHmacUsedForSecretsConfigHmacInput")
    def internal_hmac_used_for_secrets_config_hmac_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "internalHmacUsedForSecretsConfigHmacInput"))

    @builtins.property
    @jsii.member(jsii_name="internalSecretsConfigHmacInput")
    def internal_secrets_config_hmac_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "internalSecretsConfigHmacInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginIdInput")
    def plugin_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginIdInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginNameInput")
    def plugin_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeIdInput")
    def scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsHmacInput")
    def secrets_hmac_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsHmacInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsJsonInput")
    def secrets_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretsJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="attributesJson")
    def attributes_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributesJson"))

    @attributes_json.setter
    def attributes_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "attributes_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributesJson", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="internalForceUpdate")
    def internal_force_update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalForceUpdate"))

    @internal_force_update.setter
    def internal_force_update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "internal_force_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalForceUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="internalHmacUsedForSecretsConfigHmac")
    def internal_hmac_used_for_secrets_config_hmac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalHmacUsedForSecretsConfigHmac"))

    @internal_hmac_used_for_secrets_config_hmac.setter
    def internal_hmac_used_for_secrets_config_hmac(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "internal_hmac_used_for_secrets_config_hmac").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalHmacUsedForSecretsConfigHmac", value)

    @builtins.property
    @jsii.member(jsii_name="internalSecretsConfigHmac")
    def internal_secrets_config_hmac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalSecretsConfigHmac"))

    @internal_secrets_config_hmac.setter
    def internal_secrets_config_hmac(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "internal_secrets_config_hmac").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalSecretsConfigHmac", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pluginId")
    def plugin_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginId"))

    @plugin_id.setter
    def plugin_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "plugin_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginId", value)

    @builtins.property
    @jsii.member(jsii_name="pluginName")
    def plugin_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pluginName"))

    @plugin_name.setter
    def plugin_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "plugin_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginName", value)

    @builtins.property
    @jsii.member(jsii_name="scopeId")
    def scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scopeId"))

    @scope_id.setter
    def scope_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "scope_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeId", value)

    @builtins.property
    @jsii.member(jsii_name="secretsHmac")
    def secrets_hmac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsHmac"))

    @secrets_hmac.setter
    def secrets_hmac(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "secrets_hmac").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsHmac", value)

    @builtins.property
    @jsii.member(jsii_name="secretsJson")
    def secrets_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsJson"))

    @secrets_json.setter
    def secrets_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HostCatalogPlugin, "secrets_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretsJson", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-boundary.hostCatalogPlugin.HostCatalogPluginConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "scope_id": "scopeId",
        "attributes_json": "attributesJson",
        "description": "description",
        "internal_force_update": "internalForceUpdate",
        "internal_hmac_used_for_secrets_config_hmac": "internalHmacUsedForSecretsConfigHmac",
        "internal_secrets_config_hmac": "internalSecretsConfigHmac",
        "name": "name",
        "plugin_id": "pluginId",
        "plugin_name": "pluginName",
        "secrets_hmac": "secretsHmac",
        "secrets_json": "secretsJson",
    },
)
class HostCatalogPluginConfig(cdktf.TerraformMetaArguments):
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
        scope_id: builtins.str,
        attributes_json: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        internal_force_update: typing.Optional[builtins.str] = None,
        internal_hmac_used_for_secrets_config_hmac: typing.Optional[builtins.str] = None,
        internal_secrets_config_hmac: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        plugin_id: typing.Optional[builtins.str] = None,
        plugin_name: typing.Optional[builtins.str] = None,
        secrets_hmac: typing.Optional[builtins.str] = None,
        secrets_json: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param scope_id: The scope ID in which the resource is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#scope_id HostCatalogPlugin#scope_id}
        :param attributes_json: The attributes for the host catalog. Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" or remove the block to clear all attributes in the host catalog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#attributes_json HostCatalogPlugin#attributes_json}
        :param description: The host catalog description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#description HostCatalogPlugin#description}
        :param internal_force_update: Internal only. Used to force update so that we can always check the value of secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_force_update HostCatalogPlugin#internal_force_update}
        :param internal_hmac_used_for_secrets_config_hmac: Internal only. The Boundary-provided HMAC used to calculate the current value of the HMAC'd config. Used for drift detection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_hmac_used_for_secrets_config_hmac HostCatalogPlugin#internal_hmac_used_for_secrets_config_hmac}
        :param internal_secrets_config_hmac: Internal only. HMAC of (serverSecretsHmac + config secrets). Used for proper secrets handling. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_secrets_config_hmac HostCatalogPlugin#internal_secrets_config_hmac}
        :param name: The host catalog name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#name HostCatalogPlugin#name}
        :param plugin_id: The ID of the plugin that should back the resource. This or plugin_name must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#plugin_id HostCatalogPlugin#plugin_id}
        :param plugin_name: The name of the plugin that should back the resource. This or plugin_id must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#plugin_name HostCatalogPlugin#plugin_name}
        :param secrets_hmac: The HMAC'd secrets value returned from the server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#secrets_hmac HostCatalogPlugin#secrets_hmac}
        :param secrets_json: The secrets for the host catalog. Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" to clear any existing values. NOTE: Unlike "attributes_json", removing this block will NOT clear secrets from the host catalog; this allows injecting secrets for one call, then removing them for storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#secrets_json HostCatalogPlugin#secrets_json}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(HostCatalogPluginConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument scope_id", value=scope_id, expected_type=type_hints["scope_id"])
            check_type(argname="argument attributes_json", value=attributes_json, expected_type=type_hints["attributes_json"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument internal_force_update", value=internal_force_update, expected_type=type_hints["internal_force_update"])
            check_type(argname="argument internal_hmac_used_for_secrets_config_hmac", value=internal_hmac_used_for_secrets_config_hmac, expected_type=type_hints["internal_hmac_used_for_secrets_config_hmac"])
            check_type(argname="argument internal_secrets_config_hmac", value=internal_secrets_config_hmac, expected_type=type_hints["internal_secrets_config_hmac"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument plugin_id", value=plugin_id, expected_type=type_hints["plugin_id"])
            check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
            check_type(argname="argument secrets_hmac", value=secrets_hmac, expected_type=type_hints["secrets_hmac"])
            check_type(argname="argument secrets_json", value=secrets_json, expected_type=type_hints["secrets_json"])
        self._values: typing.Dict[str, typing.Any] = {
            "scope_id": scope_id,
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
        if attributes_json is not None:
            self._values["attributes_json"] = attributes_json
        if description is not None:
            self._values["description"] = description
        if internal_force_update is not None:
            self._values["internal_force_update"] = internal_force_update
        if internal_hmac_used_for_secrets_config_hmac is not None:
            self._values["internal_hmac_used_for_secrets_config_hmac"] = internal_hmac_used_for_secrets_config_hmac
        if internal_secrets_config_hmac is not None:
            self._values["internal_secrets_config_hmac"] = internal_secrets_config_hmac
        if name is not None:
            self._values["name"] = name
        if plugin_id is not None:
            self._values["plugin_id"] = plugin_id
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if secrets_hmac is not None:
            self._values["secrets_hmac"] = secrets_hmac
        if secrets_json is not None:
            self._values["secrets_json"] = secrets_json

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
    def scope_id(self) -> builtins.str:
        '''The scope ID in which the resource is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#scope_id HostCatalogPlugin#scope_id}
        '''
        result = self._values.get("scope_id")
        assert result is not None, "Required property 'scope_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes_json(self) -> typing.Optional[builtins.str]:
        '''The attributes for the host catalog.

        Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" or remove the block to clear all attributes in the host catalog.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#attributes_json HostCatalogPlugin#attributes_json}
        '''
        result = self._values.get("attributes_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The host catalog description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#description HostCatalogPlugin#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_force_update(self) -> typing.Optional[builtins.str]:
        '''Internal only. Used to force update so that we can always check the value of secrets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_force_update HostCatalogPlugin#internal_force_update}
        '''
        result = self._values.get("internal_force_update")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_hmac_used_for_secrets_config_hmac(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Internal only. The Boundary-provided HMAC used to calculate the current value of the HMAC'd config. Used for drift detection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_hmac_used_for_secrets_config_hmac HostCatalogPlugin#internal_hmac_used_for_secrets_config_hmac}
        '''
        result = self._values.get("internal_hmac_used_for_secrets_config_hmac")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_secrets_config_hmac(self) -> typing.Optional[builtins.str]:
        '''Internal only. HMAC of (serverSecretsHmac + config secrets). Used for proper secrets handling.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#internal_secrets_config_hmac HostCatalogPlugin#internal_secrets_config_hmac}
        '''
        result = self._values.get("internal_secrets_config_hmac")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The host catalog name. Defaults to the resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#name HostCatalogPlugin#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the plugin that should back the resource. This or plugin_name must be defined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#plugin_id HostCatalogPlugin#plugin_id}
        '''
        result = self._values.get("plugin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''The name of the plugin that should back the resource. This or plugin_id must be defined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#plugin_name HostCatalogPlugin#plugin_name}
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_hmac(self) -> typing.Optional[builtins.str]:
        '''The HMAC'd secrets value returned from the server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#secrets_hmac HostCatalogPlugin#secrets_hmac}
        '''
        result = self._values.get("secrets_hmac")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secrets_json(self) -> typing.Optional[builtins.str]:
        '''The secrets for the host catalog.

        Either values encoded with the "jsonencode" function, pre-escaped JSON string, or a file:// or env:// path. Set to a string "null" to clear any existing values. NOTE: Unlike "attributes_json", removing this block will NOT clear secrets from the host catalog; this allows injecting secrets for one call, then removing them for storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/host_catalog_plugin#secrets_json HostCatalogPlugin#secrets_json}
        '''
        result = self._values.get("secrets_json")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostCatalogPluginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HostCatalogPlugin",
    "HostCatalogPluginConfig",
]

publication.publish()
