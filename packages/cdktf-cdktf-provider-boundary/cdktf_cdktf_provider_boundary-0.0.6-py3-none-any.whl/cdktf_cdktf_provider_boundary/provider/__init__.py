'''
# `provider`

Refer to the Terraform Registory for docs: [`boundary`](https://www.terraform.io/docs/providers/boundary).
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


class BoundaryProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-boundary.provider.BoundaryProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/boundary boundary}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        addr: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        auth_method_id: typing.Optional[builtins.str] = None,
        password_auth_method_login_name: typing.Optional[builtins.str] = None,
        password_auth_method_password: typing.Optional[builtins.str] = None,
        plugin_execution_dir: typing.Optional[builtins.str] = None,
        recovery_kms_hcl: typing.Optional[builtins.str] = None,
        tls_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/boundary boundary} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param addr: The base url of the Boundary API, e.g. "http://127.0.0.1:9200". If not set, it will be read from the "BOUNDARY_ADDR" env var. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#addr BoundaryProvider#addr}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#alias BoundaryProvider#alias}
        :param auth_method_id: The auth method ID e.g. ampw_1234567890. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#auth_method_id BoundaryProvider#auth_method_id}
        :param password_auth_method_login_name: The auth method login name for password-style auth methods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#password_auth_method_login_name BoundaryProvider#password_auth_method_login_name}
        :param password_auth_method_password: The auth method password for password-style auth methods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#password_auth_method_password BoundaryProvider#password_auth_method_password}
        :param plugin_execution_dir: Specifies a directory that the Boundary provider can use to write and execute its built-in plugins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#plugin_execution_dir BoundaryProvider#plugin_execution_dir}
        :param recovery_kms_hcl: Can be a heredoc string or a path on disk. If set, the string/file will be parsed as HCL and used with the recovery KMS mechanism. While this is set, it will override any other authentication information; the KMS mechanism will always be used. See Boundary's KMS docs for examples: https://boundaryproject.io/docs/configuration/kms Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#recovery_kms_hcl BoundaryProvider#recovery_kms_hcl}
        :param tls_insecure: When set to true, does not validate the Boundary API endpoint certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#tls_insecure BoundaryProvider#tls_insecure}
        :param token: The Boundary token to use, as a string or path on disk containing just the string. If set, the token read here will be used in place of authenticating with the auth method specified in "auth_method_id", although the recovery KMS mechanism will still override this. Can also be set with the BOUNDARY_TOKEN environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#token BoundaryProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BoundaryProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = BoundaryProviderConfig(
            addr=addr,
            alias=alias,
            auth_method_id=auth_method_id,
            password_auth_method_login_name=password_auth_method_login_name,
            password_auth_method_password=password_auth_method_password,
            plugin_execution_dir=plugin_execution_dir,
            recovery_kms_hcl=recovery_kms_hcl,
            tls_insecure=tls_insecure,
            token=token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuthMethodId")
    def reset_auth_method_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethodId", []))

    @jsii.member(jsii_name="resetPasswordAuthMethodLoginName")
    def reset_password_auth_method_login_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordAuthMethodLoginName", []))

    @jsii.member(jsii_name="resetPasswordAuthMethodPassword")
    def reset_password_auth_method_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordAuthMethodPassword", []))

    @jsii.member(jsii_name="resetPluginExecutionDir")
    def reset_plugin_execution_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPluginExecutionDir", []))

    @jsii.member(jsii_name="resetRecoveryKmsHcl")
    def reset_recovery_kms_hcl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryKmsHcl", []))

    @jsii.member(jsii_name="resetTlsInsecure")
    def reset_tls_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsInsecure", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="addrInput")
    def addr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addrInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodIdInput")
    def auth_method_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodIdInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordAuthMethodLoginNameInput")
    def password_auth_method_login_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordAuthMethodLoginNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordAuthMethodPasswordInput")
    def password_auth_method_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordAuthMethodPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="pluginExecutionDirInput")
    def plugin_execution_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginExecutionDirInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryKmsHclInput")
    def recovery_kms_hcl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryKmsHclInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInsecureInput")
    def tls_insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsInsecureInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="addr")
    def addr(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addr"))

    @addr.setter
    def addr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "addr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addr", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authMethodId")
    def auth_method_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authMethodId"))

    @auth_method_id.setter
    def auth_method_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "auth_method_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethodId", value)

    @builtins.property
    @jsii.member(jsii_name="passwordAuthMethodLoginName")
    def password_auth_method_login_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordAuthMethodLoginName"))

    @password_auth_method_login_name.setter
    def password_auth_method_login_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "password_auth_method_login_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordAuthMethodLoginName", value)

    @builtins.property
    @jsii.member(jsii_name="passwordAuthMethodPassword")
    def password_auth_method_password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordAuthMethodPassword"))

    @password_auth_method_password.setter
    def password_auth_method_password(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "password_auth_method_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordAuthMethodPassword", value)

    @builtins.property
    @jsii.member(jsii_name="pluginExecutionDir")
    def plugin_execution_dir(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginExecutionDir"))

    @plugin_execution_dir.setter
    def plugin_execution_dir(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "plugin_execution_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginExecutionDir", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryKmsHcl")
    def recovery_kms_hcl(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryKmsHcl"))

    @recovery_kms_hcl.setter
    def recovery_kms_hcl(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "recovery_kms_hcl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryKmsHcl", value)

    @builtins.property
    @jsii.member(jsii_name="tlsInsecure")
    def tls_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsInsecure"))

    @tls_insecure.setter
    def tls_insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "tls_insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsInsecure", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BoundaryProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-boundary.provider.BoundaryProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "addr": "addr",
        "alias": "alias",
        "auth_method_id": "authMethodId",
        "password_auth_method_login_name": "passwordAuthMethodLoginName",
        "password_auth_method_password": "passwordAuthMethodPassword",
        "plugin_execution_dir": "pluginExecutionDir",
        "recovery_kms_hcl": "recoveryKmsHcl",
        "tls_insecure": "tlsInsecure",
        "token": "token",
    },
)
class BoundaryProviderConfig:
    def __init__(
        self,
        *,
        addr: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        auth_method_id: typing.Optional[builtins.str] = None,
        password_auth_method_login_name: typing.Optional[builtins.str] = None,
        password_auth_method_password: typing.Optional[builtins.str] = None,
        plugin_execution_dir: typing.Optional[builtins.str] = None,
        recovery_kms_hcl: typing.Optional[builtins.str] = None,
        tls_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param addr: The base url of the Boundary API, e.g. "http://127.0.0.1:9200". If not set, it will be read from the "BOUNDARY_ADDR" env var. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#addr BoundaryProvider#addr}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#alias BoundaryProvider#alias}
        :param auth_method_id: The auth method ID e.g. ampw_1234567890. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#auth_method_id BoundaryProvider#auth_method_id}
        :param password_auth_method_login_name: The auth method login name for password-style auth methods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#password_auth_method_login_name BoundaryProvider#password_auth_method_login_name}
        :param password_auth_method_password: The auth method password for password-style auth methods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#password_auth_method_password BoundaryProvider#password_auth_method_password}
        :param plugin_execution_dir: Specifies a directory that the Boundary provider can use to write and execute its built-in plugins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#plugin_execution_dir BoundaryProvider#plugin_execution_dir}
        :param recovery_kms_hcl: Can be a heredoc string or a path on disk. If set, the string/file will be parsed as HCL and used with the recovery KMS mechanism. While this is set, it will override any other authentication information; the KMS mechanism will always be used. See Boundary's KMS docs for examples: https://boundaryproject.io/docs/configuration/kms Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#recovery_kms_hcl BoundaryProvider#recovery_kms_hcl}
        :param tls_insecure: When set to true, does not validate the Boundary API endpoint certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#tls_insecure BoundaryProvider#tls_insecure}
        :param token: The Boundary token to use, as a string or path on disk containing just the string. If set, the token read here will be used in place of authenticating with the auth method specified in "auth_method_id", although the recovery KMS mechanism will still override this. Can also be set with the BOUNDARY_TOKEN environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#token BoundaryProvider#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BoundaryProviderConfig.__init__)
            check_type(argname="argument addr", value=addr, expected_type=type_hints["addr"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument auth_method_id", value=auth_method_id, expected_type=type_hints["auth_method_id"])
            check_type(argname="argument password_auth_method_login_name", value=password_auth_method_login_name, expected_type=type_hints["password_auth_method_login_name"])
            check_type(argname="argument password_auth_method_password", value=password_auth_method_password, expected_type=type_hints["password_auth_method_password"])
            check_type(argname="argument plugin_execution_dir", value=plugin_execution_dir, expected_type=type_hints["plugin_execution_dir"])
            check_type(argname="argument recovery_kms_hcl", value=recovery_kms_hcl, expected_type=type_hints["recovery_kms_hcl"])
            check_type(argname="argument tls_insecure", value=tls_insecure, expected_type=type_hints["tls_insecure"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {
            "addr": addr,
        }
        if alias is not None:
            self._values["alias"] = alias
        if auth_method_id is not None:
            self._values["auth_method_id"] = auth_method_id
        if password_auth_method_login_name is not None:
            self._values["password_auth_method_login_name"] = password_auth_method_login_name
        if password_auth_method_password is not None:
            self._values["password_auth_method_password"] = password_auth_method_password
        if plugin_execution_dir is not None:
            self._values["plugin_execution_dir"] = plugin_execution_dir
        if recovery_kms_hcl is not None:
            self._values["recovery_kms_hcl"] = recovery_kms_hcl
        if tls_insecure is not None:
            self._values["tls_insecure"] = tls_insecure
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def addr(self) -> builtins.str:
        '''The base url of the Boundary API, e.g. "http://127.0.0.1:9200". If not set, it will be read from the "BOUNDARY_ADDR" env var.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#addr BoundaryProvider#addr}
        '''
        result = self._values.get("addr")
        assert result is not None, "Required property 'addr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#alias BoundaryProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_method_id(self) -> typing.Optional[builtins.str]:
        '''The auth method ID e.g. ampw_1234567890.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#auth_method_id BoundaryProvider#auth_method_id}
        '''
        result = self._values.get("auth_method_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_auth_method_login_name(self) -> typing.Optional[builtins.str]:
        '''The auth method login name for password-style auth methods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#password_auth_method_login_name BoundaryProvider#password_auth_method_login_name}
        '''
        result = self._values.get("password_auth_method_login_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_auth_method_password(self) -> typing.Optional[builtins.str]:
        '''The auth method password for password-style auth methods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#password_auth_method_password BoundaryProvider#password_auth_method_password}
        '''
        result = self._values.get("password_auth_method_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugin_execution_dir(self) -> typing.Optional[builtins.str]:
        '''Specifies a directory that the Boundary provider can use to write and execute its built-in plugins.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#plugin_execution_dir BoundaryProvider#plugin_execution_dir}
        '''
        result = self._values.get("plugin_execution_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_kms_hcl(self) -> typing.Optional[builtins.str]:
        '''Can be a heredoc string or a path on disk.

        If set, the string/file will be parsed as HCL and used with the recovery KMS mechanism. While this is set, it will override any other authentication information; the KMS mechanism will always be used. See Boundary's KMS docs for examples: https://boundaryproject.io/docs/configuration/kms

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#recovery_kms_hcl BoundaryProvider#recovery_kms_hcl}
        '''
        result = self._values.get("recovery_kms_hcl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When set to true, does not validate the Boundary API endpoint certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#tls_insecure BoundaryProvider#tls_insecure}
        '''
        result = self._values.get("tls_insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''The Boundary token to use, as a string or path on disk containing just the string.

        If set, the token read here will be used in place of authenticating with the auth method specified in "auth_method_id", although the recovery KMS mechanism will still override this. Can also be set with the BOUNDARY_TOKEN environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary#token BoundaryProvider#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BoundaryProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BoundaryProvider",
    "BoundaryProviderConfig",
]

publication.publish()
