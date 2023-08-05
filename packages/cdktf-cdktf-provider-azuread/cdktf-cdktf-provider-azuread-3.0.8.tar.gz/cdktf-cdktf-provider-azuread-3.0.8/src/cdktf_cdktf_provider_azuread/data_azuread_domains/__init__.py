'''
# `data_azuread_domains`

Refer to the Terraform Registory for docs: [`data_azuread_domains`](https://www.terraform.io/docs/providers/azuread/d/domains).
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


class DataAzureadDomains(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomains",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azuread/d/domains azuread_domains}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        admin_managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        include_unverified: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_default: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_initial: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_root: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        supports_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DataAzureadDomainsTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azuread/d/domains azuread_domains} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_managed: Set to ``true`` to only return domains whose DNS is managed by Microsoft 365. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#admin_managed DataAzureadDomains#admin_managed}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#id DataAzureadDomains#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_unverified: Set to ``true`` if unverified Azure AD domains should be included. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#include_unverified DataAzureadDomains#include_unverified}
        :param only_default: Set to ``true`` to only return the default domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_default DataAzureadDomains#only_default}
        :param only_initial: Set to ``true`` to only return the initial domain, which is your primary Azure Active Directory tenant domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_initial DataAzureadDomains#only_initial}
        :param only_root: Set to ``true`` to only return verified root domains. Excludes subdomains and unverified domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_root DataAzureadDomains#only_root}
        :param supports_services: A list of supported services that must be supported by a domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#supports_services DataAzureadDomains#supports_services}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#timeouts DataAzureadDomains#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzureadDomains.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAzureadDomainsConfig(
            admin_managed=admin_managed,
            id=id,
            include_unverified=include_unverified,
            only_default=only_default,
            only_initial=only_initial,
            only_root=only_root,
            supports_services=supports_services,
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
    def put_timeouts(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#read DataAzureadDomains#read}.
        '''
        value = DataAzureadDomainsTimeouts(read=read)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdminManaged")
    def reset_admin_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminManaged", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncludeUnverified")
    def reset_include_unverified(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeUnverified", []))

    @jsii.member(jsii_name="resetOnlyDefault")
    def reset_only_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyDefault", []))

    @jsii.member(jsii_name="resetOnlyInitial")
    def reset_only_initial(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyInitial", []))

    @jsii.member(jsii_name="resetOnlyRoot")
    def reset_only_root(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyRoot", []))

    @jsii.member(jsii_name="resetSupportsServices")
    def reset_supports_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportsServices", []))

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
    @jsii.member(jsii_name="domains")
    def domains(self) -> "DataAzureadDomainsDomainsList":
        return typing.cast("DataAzureadDomainsDomainsList", jsii.get(self, "domains"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataAzureadDomainsTimeoutsOutputReference":
        return typing.cast("DataAzureadDomainsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="adminManagedInput")
    def admin_managed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adminManagedInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="includeUnverifiedInput")
    def include_unverified_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeUnverifiedInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyDefaultInput")
    def only_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyInitialInput")
    def only_initial_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyInitialInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyRootInput")
    def only_root_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyRootInput"))

    @builtins.property
    @jsii.member(jsii_name="supportsServicesInput")
    def supports_services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "supportsServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataAzureadDomainsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataAzureadDomainsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="adminManaged")
    def admin_managed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "adminManaged"))

    @admin_managed.setter
    def admin_managed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "admin_managed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminManaged", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="includeUnverified")
    def include_unverified(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeUnverified"))

    @include_unverified.setter
    def include_unverified(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "include_unverified").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeUnverified", value)

    @builtins.property
    @jsii.member(jsii_name="onlyDefault")
    def only_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyDefault"))

    @only_default.setter
    def only_default(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "only_default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyDefault", value)

    @builtins.property
    @jsii.member(jsii_name="onlyInitial")
    def only_initial(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyInitial"))

    @only_initial.setter
    def only_initial(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "only_initial").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyInitial", value)

    @builtins.property
    @jsii.member(jsii_name="onlyRoot")
    def only_root(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyRoot"))

    @only_root.setter
    def only_root(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "only_root").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyRoot", value)

    @builtins.property
    @jsii.member(jsii_name="supportsServices")
    def supports_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportsServices"))

    @supports_services.setter
    def supports_services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomains, "supports_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportsServices", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomainsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "admin_managed": "adminManaged",
        "id": "id",
        "include_unverified": "includeUnverified",
        "only_default": "onlyDefault",
        "only_initial": "onlyInitial",
        "only_root": "onlyRoot",
        "supports_services": "supportsServices",
        "timeouts": "timeouts",
    },
)
class DataAzureadDomainsConfig(cdktf.TerraformMetaArguments):
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
        admin_managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        include_unverified: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_default: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_initial: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_root: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        supports_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DataAzureadDomainsTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_managed: Set to ``true`` to only return domains whose DNS is managed by Microsoft 365. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#admin_managed DataAzureadDomains#admin_managed}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#id DataAzureadDomains#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param include_unverified: Set to ``true`` if unverified Azure AD domains should be included. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#include_unverified DataAzureadDomains#include_unverified}
        :param only_default: Set to ``true`` to only return the default domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_default DataAzureadDomains#only_default}
        :param only_initial: Set to ``true`` to only return the initial domain, which is your primary Azure Active Directory tenant domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_initial DataAzureadDomains#only_initial}
        :param only_root: Set to ``true`` to only return verified root domains. Excludes subdomains and unverified domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_root DataAzureadDomains#only_root}
        :param supports_services: A list of supported services that must be supported by a domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#supports_services DataAzureadDomains#supports_services}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#timeouts DataAzureadDomains#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataAzureadDomainsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataAzureadDomainsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_managed", value=admin_managed, expected_type=type_hints["admin_managed"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument include_unverified", value=include_unverified, expected_type=type_hints["include_unverified"])
            check_type(argname="argument only_default", value=only_default, expected_type=type_hints["only_default"])
            check_type(argname="argument only_initial", value=only_initial, expected_type=type_hints["only_initial"])
            check_type(argname="argument only_root", value=only_root, expected_type=type_hints["only_root"])
            check_type(argname="argument supports_services", value=supports_services, expected_type=type_hints["supports_services"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if admin_managed is not None:
            self._values["admin_managed"] = admin_managed
        if id is not None:
            self._values["id"] = id
        if include_unverified is not None:
            self._values["include_unverified"] = include_unverified
        if only_default is not None:
            self._values["only_default"] = only_default
        if only_initial is not None:
            self._values["only_initial"] = only_initial
        if only_root is not None:
            self._values["only_root"] = only_root
        if supports_services is not None:
            self._values["supports_services"] = supports_services
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
    def admin_managed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to ``true`` to only return domains whose DNS is managed by Microsoft 365.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#admin_managed DataAzureadDomains#admin_managed}
        '''
        result = self._values.get("admin_managed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#id DataAzureadDomains#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_unverified(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to ``true`` if unverified Azure AD domains should be included.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#include_unverified DataAzureadDomains#include_unverified}
        '''
        result = self._values.get("include_unverified")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def only_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to ``true`` to only return the default domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_default DataAzureadDomains#only_default}
        '''
        result = self._values.get("only_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def only_initial(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to ``true`` to only return the initial domain, which is your primary Azure Active Directory tenant domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_initial DataAzureadDomains#only_initial}
        '''
        result = self._values.get("only_initial")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def only_root(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to ``true`` to only return verified root domains. Excludes subdomains and unverified domains.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#only_root DataAzureadDomains#only_root}
        '''
        result = self._values.get("only_root")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def supports_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of supported services that must be supported by a domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#supports_services DataAzureadDomains#supports_services}
        '''
        result = self._values.get("supports_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataAzureadDomainsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#timeouts DataAzureadDomains#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataAzureadDomainsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzureadDomainsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomainsDomains",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAzureadDomainsDomains:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzureadDomainsDomains(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzureadDomainsDomainsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomainsDomainsList",
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
            type_hints = typing.get_type_hints(DataAzureadDomainsDomainsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAzureadDomainsDomainsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzureadDomainsDomainsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAzureadDomainsDomainsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomainsDomainsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAzureadDomainsDomainsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataAzureadDomainsDomainsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataAzureadDomainsDomainsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomainsDomainsOutputReference",
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
            type_hints = typing.get_type_hints(DataAzureadDomainsDomainsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="adminManaged")
    def admin_managed(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "adminManaged"))

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "default"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @builtins.property
    @jsii.member(jsii_name="initial")
    def initial(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "initial"))

    @builtins.property
    @jsii.member(jsii_name="root")
    def root(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "root"))

    @builtins.property
    @jsii.member(jsii_name="supportedServices")
    def supported_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedServices"))

    @builtins.property
    @jsii.member(jsii_name="verified")
    def verified(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "verified"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAzureadDomainsDomains]:
        return typing.cast(typing.Optional[DataAzureadDomainsDomains], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DataAzureadDomainsDomains]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomainsDomainsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomainsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"read": "read"},
)
class DataAzureadDomainsTimeouts:
    def __init__(self, *, read: typing.Optional[builtins.str] = None) -> None:
        '''
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#read DataAzureadDomains#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataAzureadDomainsTimeouts.__init__)
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azuread/d/domains#read DataAzureadDomains#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAzureadDomainsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAzureadDomainsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azuread.dataAzureadDomains.DataAzureadDomainsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataAzureadDomainsTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomainsTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataAzureadDomainsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataAzureadDomainsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataAzureadDomainsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataAzureadDomainsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataAzureadDomains",
    "DataAzureadDomainsConfig",
    "DataAzureadDomainsDomains",
    "DataAzureadDomainsDomainsList",
    "DataAzureadDomainsDomainsOutputReference",
    "DataAzureadDomainsTimeouts",
    "DataAzureadDomainsTimeoutsOutputReference",
]

publication.publish()
