'''
# `provider`

Refer to the Terraform Registory for docs: [`azuread`](https://www.terraform.io/docs/providers/azuread).
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


class AzureadProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.provider.AzureadProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread azuread}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_certificate_password: typing.Optional[builtins.str] = None,
        client_certificate_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        disable_terraform_partner_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        oidc_request_token: typing.Optional[builtins.str] = None,
        oidc_request_url: typing.Optional[builtins.str] = None,
        oidc_token: typing.Optional[builtins.str] = None,
        oidc_token_file_path: typing.Optional[builtins.str] = None,
        partner_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_cli: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_msi: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_oidc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread azuread} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#alias AzureadProvider#alias}
        :param client_certificate: Base64 encoded PKCS#12 certificate bundle to use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate AzureadProvider#client_certificate}
        :param client_certificate_password: The password to decrypt the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate_password AzureadProvider#client_certificate_password}
        :param client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate_path AzureadProvider#client_certificate_path}
        :param client_id: The Client ID which should be used for service principal authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_id AzureadProvider#client_id}
        :param client_secret: The application password to use when authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_secret AzureadProvider#client_secret}
        :param disable_terraform_partner_id: Disable the Terraform Partner ID, which is used if a custom ``partner_id`` isn't specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#disable_terraform_partner_id AzureadProvider#disable_terraform_partner_id}
        :param environment: The cloud environment which should be used. Possible values are: ``global`` (also ``public``), ``usgovernmentl4`` (also ``usgovernment``), ``usgovernmentl5`` (also ``dod``), and ``china``. Defaults to ``global`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#environment AzureadProvider#environment}
        :param msi_endpoint: The path to a custom endpoint for Managed Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#msi_endpoint AzureadProvider#msi_endpoint}
        :param oidc_request_token: The bearer token for the request to the OIDC provider. For use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_request_token AzureadProvider#oidc_request_token}
        :param oidc_request_url: The URL for the OIDC provider from which to request an ID token. For use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_request_url AzureadProvider#oidc_request_url}
        :param oidc_token: The ID token for use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_token AzureadProvider#oidc_token}
        :param oidc_token_file_path: The path to a file containing an ID token for use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_token_file_path AzureadProvider#oidc_token_file_path}
        :param partner_id: A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#partner_id AzureadProvider#partner_id}
        :param tenant_id: The Tenant ID which should be used. Works with all authentication methods except Managed Identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#tenant_id AzureadProvider#tenant_id}
        :param use_cli: Allow Azure CLI to be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_cli AzureadProvider#use_cli}
        :param use_msi: Allow Managed Identity to be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_msi AzureadProvider#use_msi}
        :param use_oidc: Allow OpenID Connect to be used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_oidc AzureadProvider#use_oidc}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzureadProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AzureadProviderConfig(
            alias=alias,
            client_certificate=client_certificate,
            client_certificate_password=client_certificate_password,
            client_certificate_path=client_certificate_path,
            client_id=client_id,
            client_secret=client_secret,
            disable_terraform_partner_id=disable_terraform_partner_id,
            environment=environment,
            msi_endpoint=msi_endpoint,
            oidc_request_token=oidc_request_token,
            oidc_request_url=oidc_request_url,
            oidc_token=oidc_token,
            oidc_token_file_path=oidc_token_file_path,
            partner_id=partner_id,
            tenant_id=tenant_id,
            use_cli=use_cli,
            use_msi=use_msi,
            use_oidc=use_oidc,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetClientCertificate")
    def reset_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificate", []))

    @jsii.member(jsii_name="resetClientCertificatePassword")
    def reset_client_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePassword", []))

    @jsii.member(jsii_name="resetClientCertificatePath")
    def reset_client_certificate_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePath", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetDisableTerraformPartnerId")
    def reset_disable_terraform_partner_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableTerraformPartnerId", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetMsiEndpoint")
    def reset_msi_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsiEndpoint", []))

    @jsii.member(jsii_name="resetOidcRequestToken")
    def reset_oidc_request_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcRequestToken", []))

    @jsii.member(jsii_name="resetOidcRequestUrl")
    def reset_oidc_request_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcRequestUrl", []))

    @jsii.member(jsii_name="resetOidcToken")
    def reset_oidc_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcToken", []))

    @jsii.member(jsii_name="resetOidcTokenFilePath")
    def reset_oidc_token_file_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcTokenFilePath", []))

    @jsii.member(jsii_name="resetPartnerId")
    def reset_partner_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartnerId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @jsii.member(jsii_name="resetUseCli")
    def reset_use_cli(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCli", []))

    @jsii.member(jsii_name="resetUseMsi")
    def reset_use_msi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseMsi", []))

    @jsii.member(jsii_name="resetUseOidc")
    def reset_use_oidc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseOidc", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateInput")
    def client_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePasswordInput")
    def client_certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePathInput")
    def client_certificate_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="disableTerraformPartnerIdInput")
    def disable_terraform_partner_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableTerraformPartnerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="msiEndpointInput")
    def msi_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcRequestTokenInput")
    def oidc_request_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcRequestTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcRequestUrlInput")
    def oidc_request_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcRequestUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcTokenFilePathInput")
    def oidc_token_file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcTokenFilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcTokenInput")
    def oidc_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="partnerIdInput")
    def partner_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useCliInput")
    def use_cli_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCliInput"))

    @builtins.property
    @jsii.member(jsii_name="useMsiInput")
    def use_msi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useMsiInput"))

    @builtins.property
    @jsii.member(jsii_name="useOidcInput")
    def use_oidc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useOidcInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificate")
    def client_certificate(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificate"))

    @client_certificate.setter
    def client_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePassword")
    def client_certificate_password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePassword"))

    @client_certificate_password.setter
    def client_certificate_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "client_certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePath")
    def client_certificate_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePath"))

    @client_certificate_path.setter
    def client_certificate_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "client_certificate_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePath", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="disableTerraformPartnerId")
    def disable_terraform_partner_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableTerraformPartnerId"))

    @disable_terraform_partner_id.setter
    def disable_terraform_partner_id(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "disable_terraform_partner_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableTerraformPartnerId", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="msiEndpoint")
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiEndpoint"))

    @msi_endpoint.setter
    def msi_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "msi_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "msiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="oidcRequestToken")
    def oidc_request_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcRequestToken"))

    @oidc_request_token.setter
    def oidc_request_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "oidc_request_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcRequestToken", value)

    @builtins.property
    @jsii.member(jsii_name="oidcRequestUrl")
    def oidc_request_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcRequestUrl"))

    @oidc_request_url.setter
    def oidc_request_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "oidc_request_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcRequestUrl", value)

    @builtins.property
    @jsii.member(jsii_name="oidcToken")
    def oidc_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcToken"))

    @oidc_token.setter
    def oidc_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "oidc_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcToken", value)

    @builtins.property
    @jsii.member(jsii_name="oidcTokenFilePath")
    def oidc_token_file_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oidcTokenFilePath"))

    @oidc_token_file_path.setter
    def oidc_token_file_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "oidc_token_file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oidcTokenFilePath", value)

    @builtins.property
    @jsii.member(jsii_name="partnerId")
    def partner_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerId"))

    @partner_id.setter
    def partner_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "partner_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="useCli")
    def use_cli(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCli"))

    @use_cli.setter
    def use_cli(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "use_cli").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCli", value)

    @builtins.property
    @jsii.member(jsii_name="useMsi")
    def use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useMsi"))

    @use_msi.setter
    def use_msi(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "use_msi").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useMsi", value)

    @builtins.property
    @jsii.member(jsii_name="useOidc")
    def use_oidc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useOidc"))

    @use_oidc.setter
    def use_oidc(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzureadProvider, "use_oidc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useOidc", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.provider.AzureadProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "client_certificate": "clientCertificate",
        "client_certificate_password": "clientCertificatePassword",
        "client_certificate_path": "clientCertificatePath",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "disable_terraform_partner_id": "disableTerraformPartnerId",
        "environment": "environment",
        "msi_endpoint": "msiEndpoint",
        "oidc_request_token": "oidcRequestToken",
        "oidc_request_url": "oidcRequestUrl",
        "oidc_token": "oidcToken",
        "oidc_token_file_path": "oidcTokenFilePath",
        "partner_id": "partnerId",
        "tenant_id": "tenantId",
        "use_cli": "useCli",
        "use_msi": "useMsi",
        "use_oidc": "useOidc",
    },
)
class AzureadProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        client_certificate_password: typing.Optional[builtins.str] = None,
        client_certificate_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        disable_terraform_partner_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        oidc_request_token: typing.Optional[builtins.str] = None,
        oidc_request_url: typing.Optional[builtins.str] = None,
        oidc_token: typing.Optional[builtins.str] = None,
        oidc_token_file_path: typing.Optional[builtins.str] = None,
        partner_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_cli: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_msi: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_oidc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#alias AzureadProvider#alias}
        :param client_certificate: Base64 encoded PKCS#12 certificate bundle to use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate AzureadProvider#client_certificate}
        :param client_certificate_password: The password to decrypt the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate_password AzureadProvider#client_certificate_password}
        :param client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate_path AzureadProvider#client_certificate_path}
        :param client_id: The Client ID which should be used for service principal authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_id AzureadProvider#client_id}
        :param client_secret: The application password to use when authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_secret AzureadProvider#client_secret}
        :param disable_terraform_partner_id: Disable the Terraform Partner ID, which is used if a custom ``partner_id`` isn't specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#disable_terraform_partner_id AzureadProvider#disable_terraform_partner_id}
        :param environment: The cloud environment which should be used. Possible values are: ``global`` (also ``public``), ``usgovernmentl4`` (also ``usgovernment``), ``usgovernmentl5`` (also ``dod``), and ``china``. Defaults to ``global`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#environment AzureadProvider#environment}
        :param msi_endpoint: The path to a custom endpoint for Managed Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#msi_endpoint AzureadProvider#msi_endpoint}
        :param oidc_request_token: The bearer token for the request to the OIDC provider. For use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_request_token AzureadProvider#oidc_request_token}
        :param oidc_request_url: The URL for the OIDC provider from which to request an ID token. For use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_request_url AzureadProvider#oidc_request_url}
        :param oidc_token: The ID token for use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_token AzureadProvider#oidc_token}
        :param oidc_token_file_path: The path to a file containing an ID token for use when authenticating as a Service Principal using OpenID Connect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_token_file_path AzureadProvider#oidc_token_file_path}
        :param partner_id: A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#partner_id AzureadProvider#partner_id}
        :param tenant_id: The Tenant ID which should be used. Works with all authentication methods except Managed Identity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#tenant_id AzureadProvider#tenant_id}
        :param use_cli: Allow Azure CLI to be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_cli AzureadProvider#use_cli}
        :param use_msi: Allow Managed Identity to be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_msi AzureadProvider#use_msi}
        :param use_oidc: Allow OpenID Connect to be used for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_oidc AzureadProvider#use_oidc}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzureadProviderConfig.__init__)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument client_certificate", value=client_certificate, expected_type=type_hints["client_certificate"])
            check_type(argname="argument client_certificate_password", value=client_certificate_password, expected_type=type_hints["client_certificate_password"])
            check_type(argname="argument client_certificate_path", value=client_certificate_path, expected_type=type_hints["client_certificate_path"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument disable_terraform_partner_id", value=disable_terraform_partner_id, expected_type=type_hints["disable_terraform_partner_id"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument msi_endpoint", value=msi_endpoint, expected_type=type_hints["msi_endpoint"])
            check_type(argname="argument oidc_request_token", value=oidc_request_token, expected_type=type_hints["oidc_request_token"])
            check_type(argname="argument oidc_request_url", value=oidc_request_url, expected_type=type_hints["oidc_request_url"])
            check_type(argname="argument oidc_token", value=oidc_token, expected_type=type_hints["oidc_token"])
            check_type(argname="argument oidc_token_file_path", value=oidc_token_file_path, expected_type=type_hints["oidc_token_file_path"])
            check_type(argname="argument partner_id", value=partner_id, expected_type=type_hints["partner_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument use_cli", value=use_cli, expected_type=type_hints["use_cli"])
            check_type(argname="argument use_msi", value=use_msi, expected_type=type_hints["use_msi"])
            check_type(argname="argument use_oidc", value=use_oidc, expected_type=type_hints["use_oidc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if client_certificate_password is not None:
            self._values["client_certificate_password"] = client_certificate_password
        if client_certificate_path is not None:
            self._values["client_certificate_path"] = client_certificate_path
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if disable_terraform_partner_id is not None:
            self._values["disable_terraform_partner_id"] = disable_terraform_partner_id
        if environment is not None:
            self._values["environment"] = environment
        if msi_endpoint is not None:
            self._values["msi_endpoint"] = msi_endpoint
        if oidc_request_token is not None:
            self._values["oidc_request_token"] = oidc_request_token
        if oidc_request_url is not None:
            self._values["oidc_request_url"] = oidc_request_url
        if oidc_token is not None:
            self._values["oidc_token"] = oidc_token
        if oidc_token_file_path is not None:
            self._values["oidc_token_file_path"] = oidc_token_file_path
        if partner_id is not None:
            self._values["partner_id"] = partner_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if use_cli is not None:
            self._values["use_cli"] = use_cli
        if use_msi is not None:
            self._values["use_msi"] = use_msi
        if use_oidc is not None:
            self._values["use_oidc"] = use_oidc

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#alias AzureadProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''Base64 encoded PKCS#12 certificate bundle to use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate AzureadProvider#client_certificate}
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_password(self) -> typing.Optional[builtins.str]:
        '''The password to decrypt the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate_password AzureadProvider#client_certificate_password}
        '''
        result = self._values.get("client_certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_path(self) -> typing.Optional[builtins.str]:
        '''The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_certificate_path AzureadProvider#client_certificate_path}
        '''
        result = self._values.get("client_certificate_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''The Client ID which should be used for service principal authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_id AzureadProvider#client_id}
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The application password to use when authenticating as a Service Principal using a Client Secret.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#client_secret AzureadProvider#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_terraform_partner_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable the Terraform Partner ID, which is used if a custom ``partner_id`` isn't specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#disable_terraform_partner_id AzureadProvider#disable_terraform_partner_id}
        '''
        result = self._values.get("disable_terraform_partner_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The cloud environment which should be used.

        Possible values are: ``global`` (also ``public``), ``usgovernmentl4`` (also ``usgovernment``), ``usgovernmentl5`` (also ``dod``), and ``china``. Defaults to ``global``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#environment AzureadProvider#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        '''The path to a custom endpoint for Managed Identity - in most circumstances this should be detected automatically.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#msi_endpoint AzureadProvider#msi_endpoint}
        '''
        result = self._values.get("msi_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oidc_request_token(self) -> typing.Optional[builtins.str]:
        '''The bearer token for the request to the OIDC provider.

        For use when authenticating as a Service Principal using OpenID Connect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_request_token AzureadProvider#oidc_request_token}
        '''
        result = self._values.get("oidc_request_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oidc_request_url(self) -> typing.Optional[builtins.str]:
        '''The URL for the OIDC provider from which to request an ID token.

        For use when authenticating as a Service Principal using OpenID Connect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_request_url AzureadProvider#oidc_request_url}
        '''
        result = self._values.get("oidc_request_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oidc_token(self) -> typing.Optional[builtins.str]:
        '''The ID token for use when authenticating as a Service Principal using OpenID Connect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_token AzureadProvider#oidc_token}
        '''
        result = self._values.get("oidc_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oidc_token_file_path(self) -> typing.Optional[builtins.str]:
        '''The path to a file containing an ID token for use when authenticating as a Service Principal using OpenID Connect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#oidc_token_file_path AzureadProvider#oidc_token_file_path}
        '''
        result = self._values.get("oidc_token_file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partner_id(self) -> typing.Optional[builtins.str]:
        '''A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#partner_id AzureadProvider#partner_id}
        '''
        result = self._values.get("partner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''The Tenant ID which should be used. Works with all authentication methods except Managed Identity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#tenant_id AzureadProvider#tenant_id}
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_cli(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow Azure CLI to be used for Authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_cli AzureadProvider#use_cli}
        '''
        result = self._values.get("use_cli")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow Managed Identity to be used for Authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_msi AzureadProvider#use_msi}
        '''
        result = self._values.get("use_msi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_oidc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow OpenID Connect to be used for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread#use_oidc AzureadProvider#use_oidc}
        '''
        result = self._values.get("use_oidc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzureadProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzureadProvider",
    "AzureadProviderConfig",
]

publication.publish()
