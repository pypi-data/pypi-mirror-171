'''
# `boundary_auth_method_oidc`

Refer to the Terraform Registory for docs: [`boundary_auth_method_oidc`](https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc).
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


class AuthMethodOidc(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-boundary.authMethodOidc.AuthMethodOidc",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc boundary_auth_method_oidc}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scope_id: builtins.str,
        account_claim_maps: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        api_url_prefix: typing.Optional[builtins.str] = None,
        callback_url: typing.Optional[builtins.str] = None,
        claims_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_hmac: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_discovered_config_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idp_ca_certs: typing.Optional[typing.Sequence[builtins.str]] = None,
        is_primary_for_scope: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        issuer: typing.Optional[builtins.str] = None,
        max_age: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        signing_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        state: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc boundary_auth_method_oidc} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param scope_id: The scope ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#scope_id AuthMethodOidc#scope_id}
        :param account_claim_maps: Account claim maps for the to_claim of sub. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#account_claim_maps AuthMethodOidc#account_claim_maps}
        :param allowed_audiences: Audiences for which the provider responses will be allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#allowed_audiences AuthMethodOidc#allowed_audiences}
        :param api_url_prefix: The API prefix to use when generating callback URLs for the provider. Should be set to an address at which the provider can reach back to the controller. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#api_url_prefix AuthMethodOidc#api_url_prefix}
        :param callback_url: The URL that should be provided to the IdP for callbacks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#callback_url AuthMethodOidc#callback_url}
        :param claims_scopes: Claims scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#claims_scopes AuthMethodOidc#claims_scopes}
        :param client_id: The client ID assigned to this auth method from the provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_id AuthMethodOidc#client_id}
        :param client_secret: The secret key assigned to this auth method from the provider. Once set, only the hash will be kept and the original value can be removed from configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_secret AuthMethodOidc#client_secret}
        :param client_secret_hmac: The HMAC of the client secret returned by the Boundary controller, which is used for comparison after initial setting of the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_secret_hmac AuthMethodOidc#client_secret_hmac}
        :param description: The auth method description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#description AuthMethodOidc#description}
        :param disable_discovered_config_validation: Disables validation logic ensuring that the OIDC provider's information from its discovery endpoint matches the information here. The validation is only performed at create or update time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#disable_discovered_config_validation AuthMethodOidc#disable_discovered_config_validation}
        :param idp_ca_certs: A list of CA certificates to trust when validating the IdP's token signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#idp_ca_certs AuthMethodOidc#idp_ca_certs}
        :param is_primary_for_scope: When true, makes this auth method the primary auth method for the scope in which it resides. The primary auth method for a scope means the the user will be automatically created when they login using an OIDC account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#is_primary_for_scope AuthMethodOidc#is_primary_for_scope}
        :param issuer: The issuer corresponding to the provider, which must match the issuer field in generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#issuer AuthMethodOidc#issuer}
        :param max_age: The max age to provide to the provider, indicating how much time is allowed to have passed since the last authentication before the user is challenged again. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#max_age AuthMethodOidc#max_age}
        :param name: The auth method name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#name AuthMethodOidc#name}
        :param signing_algorithms: Allowed signing algorithms for the provider's issued tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#signing_algorithms AuthMethodOidc#signing_algorithms}
        :param state: Can be one of 'inactive', 'active-private', or 'active-public'. Currently automatically set to active-public. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#state AuthMethodOidc#state}
        :param type: The type of auth method; hardcoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#type AuthMethodOidc#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AuthMethodOidc.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AuthMethodOidcConfig(
            scope_id=scope_id,
            account_claim_maps=account_claim_maps,
            allowed_audiences=allowed_audiences,
            api_url_prefix=api_url_prefix,
            callback_url=callback_url,
            claims_scopes=claims_scopes,
            client_id=client_id,
            client_secret=client_secret,
            client_secret_hmac=client_secret_hmac,
            description=description,
            disable_discovered_config_validation=disable_discovered_config_validation,
            idp_ca_certs=idp_ca_certs,
            is_primary_for_scope=is_primary_for_scope,
            issuer=issuer,
            max_age=max_age,
            name=name,
            signing_algorithms=signing_algorithms,
            state=state,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAccountClaimMaps")
    def reset_account_claim_maps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountClaimMaps", []))

    @jsii.member(jsii_name="resetAllowedAudiences")
    def reset_allowed_audiences(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedAudiences", []))

    @jsii.member(jsii_name="resetApiUrlPrefix")
    def reset_api_url_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiUrlPrefix", []))

    @jsii.member(jsii_name="resetCallbackUrl")
    def reset_callback_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCallbackUrl", []))

    @jsii.member(jsii_name="resetClaimsScopes")
    def reset_claims_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimsScopes", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSecretHmac")
    def reset_client_secret_hmac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecretHmac", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableDiscoveredConfigValidation")
    def reset_disable_discovered_config_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableDiscoveredConfigValidation", []))

    @jsii.member(jsii_name="resetIdpCaCerts")
    def reset_idp_ca_certs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpCaCerts", []))

    @jsii.member(jsii_name="resetIsPrimaryForScope")
    def reset_is_primary_for_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsPrimaryForScope", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSigningAlgorithms")
    def reset_signing_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningAlgorithms", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

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
    @jsii.member(jsii_name="accountClaimMapsInput")
    def account_claim_maps_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accountClaimMapsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedAudiencesInput")
    def allowed_audiences_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedAudiencesInput"))

    @builtins.property
    @jsii.member(jsii_name="apiUrlPrefixInput")
    def api_url_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrlPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="callbackUrlInput")
    def callback_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callbackUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="claimsScopesInput")
    def claims_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "claimsScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretHmacInput")
    def client_secret_hmac_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretHmacInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableDiscoveredConfigValidationInput")
    def disable_discovered_config_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableDiscoveredConfigValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="idpCaCertsInput")
    def idp_ca_certs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idpCaCertsInput"))

    @builtins.property
    @jsii.member(jsii_name="isPrimaryForScopeInput")
    def is_primary_for_scope_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isPrimaryForScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeIdInput")
    def scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithmsInput")
    def signing_algorithms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "signingAlgorithmsInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accountClaimMaps")
    def account_claim_maps(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accountClaimMaps"))

    @account_claim_maps.setter
    def account_claim_maps(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "account_claim_maps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountClaimMaps", value)

    @builtins.property
    @jsii.member(jsii_name="allowedAudiences")
    def allowed_audiences(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedAudiences"))

    @allowed_audiences.setter
    def allowed_audiences(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "allowed_audiences").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAudiences", value)

    @builtins.property
    @jsii.member(jsii_name="apiUrlPrefix")
    def api_url_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiUrlPrefix"))

    @api_url_prefix.setter
    def api_url_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "api_url_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUrlPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="callbackUrl")
    def callback_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callbackUrl"))

    @callback_url.setter
    def callback_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "callback_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callbackUrl", value)

    @builtins.property
    @jsii.member(jsii_name="claimsScopes")
    def claims_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "claimsScopes"))

    @claims_scopes.setter
    def claims_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "claims_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "claimsScopes", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretHmac")
    def client_secret_hmac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretHmac"))

    @client_secret_hmac.setter
    def client_secret_hmac(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "client_secret_hmac").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretHmac", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableDiscoveredConfigValidation")
    def disable_discovered_config_validation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableDiscoveredConfigValidation"))

    @disable_discovered_config_validation.setter
    def disable_discovered_config_validation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "disable_discovered_config_validation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableDiscoveredConfigValidation", value)

    @builtins.property
    @jsii.member(jsii_name="idpCaCerts")
    def idp_ca_certs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "idpCaCerts"))

    @idp_ca_certs.setter
    def idp_ca_certs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "idp_ca_certs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idpCaCerts", value)

    @builtins.property
    @jsii.member(jsii_name="isPrimaryForScope")
    def is_primary_for_scope(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isPrimaryForScope"))

    @is_primary_for_scope.setter
    def is_primary_for_scope(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "is_primary_for_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isPrimaryForScope", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scopeId")
    def scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scopeId"))

    @scope_id.setter
    def scope_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "scope_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeId", value)

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithms")
    def signing_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "signingAlgorithms"))

    @signing_algorithms.setter
    def signing_algorithms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "signing_algorithms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AuthMethodOidc, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-boundary.authMethodOidc.AuthMethodOidcConfig",
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
        "account_claim_maps": "accountClaimMaps",
        "allowed_audiences": "allowedAudiences",
        "api_url_prefix": "apiUrlPrefix",
        "callback_url": "callbackUrl",
        "claims_scopes": "claimsScopes",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "client_secret_hmac": "clientSecretHmac",
        "description": "description",
        "disable_discovered_config_validation": "disableDiscoveredConfigValidation",
        "idp_ca_certs": "idpCaCerts",
        "is_primary_for_scope": "isPrimaryForScope",
        "issuer": "issuer",
        "max_age": "maxAge",
        "name": "name",
        "signing_algorithms": "signingAlgorithms",
        "state": "state",
        "type": "type",
    },
)
class AuthMethodOidcConfig(cdktf.TerraformMetaArguments):
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
        account_claim_maps: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        api_url_prefix: typing.Optional[builtins.str] = None,
        callback_url: typing.Optional[builtins.str] = None,
        claims_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_secret_hmac: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_discovered_config_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        idp_ca_certs: typing.Optional[typing.Sequence[builtins.str]] = None,
        is_primary_for_scope: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        issuer: typing.Optional[builtins.str] = None,
        max_age: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        signing_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        state: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param scope_id: The scope ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#scope_id AuthMethodOidc#scope_id}
        :param account_claim_maps: Account claim maps for the to_claim of sub. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#account_claim_maps AuthMethodOidc#account_claim_maps}
        :param allowed_audiences: Audiences for which the provider responses will be allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#allowed_audiences AuthMethodOidc#allowed_audiences}
        :param api_url_prefix: The API prefix to use when generating callback URLs for the provider. Should be set to an address at which the provider can reach back to the controller. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#api_url_prefix AuthMethodOidc#api_url_prefix}
        :param callback_url: The URL that should be provided to the IdP for callbacks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#callback_url AuthMethodOidc#callback_url}
        :param claims_scopes: Claims scopes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#claims_scopes AuthMethodOidc#claims_scopes}
        :param client_id: The client ID assigned to this auth method from the provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_id AuthMethodOidc#client_id}
        :param client_secret: The secret key assigned to this auth method from the provider. Once set, only the hash will be kept and the original value can be removed from configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_secret AuthMethodOidc#client_secret}
        :param client_secret_hmac: The HMAC of the client secret returned by the Boundary controller, which is used for comparison after initial setting of the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_secret_hmac AuthMethodOidc#client_secret_hmac}
        :param description: The auth method description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#description AuthMethodOidc#description}
        :param disable_discovered_config_validation: Disables validation logic ensuring that the OIDC provider's information from its discovery endpoint matches the information here. The validation is only performed at create or update time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#disable_discovered_config_validation AuthMethodOidc#disable_discovered_config_validation}
        :param idp_ca_certs: A list of CA certificates to trust when validating the IdP's token signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#idp_ca_certs AuthMethodOidc#idp_ca_certs}
        :param is_primary_for_scope: When true, makes this auth method the primary auth method for the scope in which it resides. The primary auth method for a scope means the the user will be automatically created when they login using an OIDC account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#is_primary_for_scope AuthMethodOidc#is_primary_for_scope}
        :param issuer: The issuer corresponding to the provider, which must match the issuer field in generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#issuer AuthMethodOidc#issuer}
        :param max_age: The max age to provide to the provider, indicating how much time is allowed to have passed since the last authentication before the user is challenged again. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#max_age AuthMethodOidc#max_age}
        :param name: The auth method name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#name AuthMethodOidc#name}
        :param signing_algorithms: Allowed signing algorithms for the provider's issued tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#signing_algorithms AuthMethodOidc#signing_algorithms}
        :param state: Can be one of 'inactive', 'active-private', or 'active-public'. Currently automatically set to active-public. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#state AuthMethodOidc#state}
        :param type: The type of auth method; hardcoded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#type AuthMethodOidc#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AuthMethodOidcConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument scope_id", value=scope_id, expected_type=type_hints["scope_id"])
            check_type(argname="argument account_claim_maps", value=account_claim_maps, expected_type=type_hints["account_claim_maps"])
            check_type(argname="argument allowed_audiences", value=allowed_audiences, expected_type=type_hints["allowed_audiences"])
            check_type(argname="argument api_url_prefix", value=api_url_prefix, expected_type=type_hints["api_url_prefix"])
            check_type(argname="argument callback_url", value=callback_url, expected_type=type_hints["callback_url"])
            check_type(argname="argument claims_scopes", value=claims_scopes, expected_type=type_hints["claims_scopes"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument client_secret_hmac", value=client_secret_hmac, expected_type=type_hints["client_secret_hmac"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_discovered_config_validation", value=disable_discovered_config_validation, expected_type=type_hints["disable_discovered_config_validation"])
            check_type(argname="argument idp_ca_certs", value=idp_ca_certs, expected_type=type_hints["idp_ca_certs"])
            check_type(argname="argument is_primary_for_scope", value=is_primary_for_scope, expected_type=type_hints["is_primary_for_scope"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signing_algorithms", value=signing_algorithms, expected_type=type_hints["signing_algorithms"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
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
        if account_claim_maps is not None:
            self._values["account_claim_maps"] = account_claim_maps
        if allowed_audiences is not None:
            self._values["allowed_audiences"] = allowed_audiences
        if api_url_prefix is not None:
            self._values["api_url_prefix"] = api_url_prefix
        if callback_url is not None:
            self._values["callback_url"] = callback_url
        if claims_scopes is not None:
            self._values["claims_scopes"] = claims_scopes
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_secret_hmac is not None:
            self._values["client_secret_hmac"] = client_secret_hmac
        if description is not None:
            self._values["description"] = description
        if disable_discovered_config_validation is not None:
            self._values["disable_discovered_config_validation"] = disable_discovered_config_validation
        if idp_ca_certs is not None:
            self._values["idp_ca_certs"] = idp_ca_certs
        if is_primary_for_scope is not None:
            self._values["is_primary_for_scope"] = is_primary_for_scope
        if issuer is not None:
            self._values["issuer"] = issuer
        if max_age is not None:
            self._values["max_age"] = max_age
        if name is not None:
            self._values["name"] = name
        if signing_algorithms is not None:
            self._values["signing_algorithms"] = signing_algorithms
        if state is not None:
            self._values["state"] = state
        if type is not None:
            self._values["type"] = type

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
        '''The scope ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#scope_id AuthMethodOidc#scope_id}
        '''
        result = self._values.get("scope_id")
        assert result is not None, "Required property 'scope_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_claim_maps(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Account claim maps for the to_claim of sub.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#account_claim_maps AuthMethodOidc#account_claim_maps}
        '''
        result = self._values.get("account_claim_maps")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Audiences for which the provider responses will be allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#allowed_audiences AuthMethodOidc#allowed_audiences}
        '''
        result = self._values.get("allowed_audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def api_url_prefix(self) -> typing.Optional[builtins.str]:
        '''The API prefix to use when generating callback URLs for the provider.

        Should be set to an address at which the provider can reach back to the controller.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#api_url_prefix AuthMethodOidc#api_url_prefix}
        '''
        result = self._values.get("api_url_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def callback_url(self) -> typing.Optional[builtins.str]:
        '''The URL that should be provided to the IdP for callbacks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#callback_url AuthMethodOidc#callback_url}
        '''
        result = self._values.get("callback_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def claims_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Claims scopes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#claims_scopes AuthMethodOidc#claims_scopes}
        '''
        result = self._values.get("claims_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''The client ID assigned to this auth method from the provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_id AuthMethodOidc#client_id}
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The secret key assigned to this auth method from the provider.

        Once set, only the hash will be kept and the original value can be removed from configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_secret AuthMethodOidc#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret_hmac(self) -> typing.Optional[builtins.str]:
        '''The HMAC of the client secret returned by the Boundary controller, which is used for comparison after initial setting of the value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#client_secret_hmac AuthMethodOidc#client_secret_hmac}
        '''
        result = self._values.get("client_secret_hmac")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The auth method description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#description AuthMethodOidc#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_discovered_config_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disables validation logic ensuring that the OIDC provider's information from its discovery endpoint matches the information here.

        The validation is only performed at create or update time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#disable_discovered_config_validation AuthMethodOidc#disable_discovered_config_validation}
        '''
        result = self._values.get("disable_discovered_config_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def idp_ca_certs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of CA certificates to trust when validating the IdP's token signatures.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#idp_ca_certs AuthMethodOidc#idp_ca_certs}
        '''
        result = self._values.get("idp_ca_certs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def is_primary_for_scope(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, makes this auth method the primary auth method for the scope in which it resides.

        The primary auth method for a scope means the the user will be automatically created when they login using an OIDC account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#is_primary_for_scope AuthMethodOidc#is_primary_for_scope}
        '''
        result = self._values.get("is_primary_for_scope")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''The issuer corresponding to the provider, which must match the issuer field in generated tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#issuer AuthMethodOidc#issuer}
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_age(self) -> typing.Optional[jsii.Number]:
        '''The max age to provide to the provider, indicating how much time is allowed to have passed since the last authentication before the user is challenged again.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#max_age AuthMethodOidc#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The auth method name. Defaults to the resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#name AuthMethodOidc#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signing_algorithms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allowed signing algorithms for the provider's issued tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#signing_algorithms AuthMethodOidc#signing_algorithms}
        '''
        result = self._values.get("signing_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Can be one of 'inactive', 'active-private', or 'active-public'. Currently automatically set to active-public.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#state AuthMethodOidc#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of auth method; hardcoded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/auth_method_oidc#type AuthMethodOidc#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthMethodOidcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthMethodOidc",
    "AuthMethodOidcConfig",
]

publication.publish()
