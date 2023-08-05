'''
# `provider`

Refer to the Terraform Registory for docs: [`opc`](https://www.terraform.io/docs/providers/opc).
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


class OpcProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.provider.OpcProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc opc}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        identity_domain: builtins.str,
        password: builtins.str,
        user: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lbaas_endpoint: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
        storage_service_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc opc} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_domain: The OPC identity domain for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#identity_domain OpcProvider#identity_domain}
        :param password: The user password for OPC API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#password OpcProvider#password}
        :param user: The user name for OPC API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#user OpcProvider#user}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#alias OpcProvider#alias}
        :param endpoint: The HTTP endpoint for OPC API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#endpoint OpcProvider#endpoint}
        :param insecure: Skip TLS Verification for self-signed certificates. Should only be used if absolutely required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#insecure OpcProvider#insecure}
        :param lbaas_endpoint: The HTTP endpoint for the Load Balancer Classic service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#lbaas_endpoint OpcProvider#lbaas_endpoint}
        :param max_retries: Maximum number retries to wait for a successful response when operating on resources within OPC (defaults to 1). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#max_retries OpcProvider#max_retries}
        :param storage_endpoint: The HTTP endpoint for Oracle Storage operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#storage_endpoint OpcProvider#storage_endpoint}
        :param storage_service_id: The Storage Service ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#storage_service_id OpcProvider#storage_service_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OpcProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = OpcProviderConfig(
            identity_domain=identity_domain,
            password=password,
            user=user,
            alias=alias,
            endpoint=endpoint,
            insecure=insecure,
            lbaas_endpoint=lbaas_endpoint,
            max_retries=max_retries,
            storage_endpoint=storage_endpoint,
            storage_service_id=storage_service_id,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetInsecure")
    def reset_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecure", []))

    @jsii.member(jsii_name="resetLbaasEndpoint")
    def reset_lbaas_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLbaasEndpoint", []))

    @jsii.member(jsii_name="resetMaxRetries")
    def reset_max_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetries", []))

    @jsii.member(jsii_name="resetStorageEndpoint")
    def reset_storage_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageEndpoint", []))

    @jsii.member(jsii_name="resetStorageServiceId")
    def reset_storage_service_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageServiceId", []))

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
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="identityDomainInput")
    def identity_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureInput")
    def insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureInput"))

    @builtins.property
    @jsii.member(jsii_name="lbaasEndpointInput")
    def lbaas_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lbaasEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="storageEndpointInput")
    def storage_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="storageServiceIdInput")
    def storage_service_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageServiceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="identityDomain")
    def identity_domain(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityDomain"))

    @identity_domain.setter
    def identity_domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "identity_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="insecure")
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecure"))

    @insecure.setter
    def insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecure", value)

    @builtins.property
    @jsii.member(jsii_name="lbaasEndpoint")
    def lbaas_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lbaasEndpoint"))

    @lbaas_endpoint.setter
    def lbaas_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "lbaas_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lbaasEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "max_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="storageEndpoint")
    def storage_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageEndpoint"))

    @storage_endpoint.setter
    def storage_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "storage_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="storageServiceId")
    def storage_service_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageServiceId"))

    @storage_service_id.setter
    def storage_service_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "storage_service_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageServiceId", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "user"))

    @user.setter
    def user(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OpcProvider, "user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.provider.OpcProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "identity_domain": "identityDomain",
        "password": "password",
        "user": "user",
        "alias": "alias",
        "endpoint": "endpoint",
        "insecure": "insecure",
        "lbaas_endpoint": "lbaasEndpoint",
        "max_retries": "maxRetries",
        "storage_endpoint": "storageEndpoint",
        "storage_service_id": "storageServiceId",
    },
)
class OpcProviderConfig:
    def __init__(
        self,
        *,
        identity_domain: builtins.str,
        password: builtins.str,
        user: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lbaas_endpoint: typing.Optional[builtins.str] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        storage_endpoint: typing.Optional[builtins.str] = None,
        storage_service_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identity_domain: The OPC identity domain for API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#identity_domain OpcProvider#identity_domain}
        :param password: The user password for OPC API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#password OpcProvider#password}
        :param user: The user name for OPC API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#user OpcProvider#user}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#alias OpcProvider#alias}
        :param endpoint: The HTTP endpoint for OPC API operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#endpoint OpcProvider#endpoint}
        :param insecure: Skip TLS Verification for self-signed certificates. Should only be used if absolutely required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#insecure OpcProvider#insecure}
        :param lbaas_endpoint: The HTTP endpoint for the Load Balancer Classic service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#lbaas_endpoint OpcProvider#lbaas_endpoint}
        :param max_retries: Maximum number retries to wait for a successful response when operating on resources within OPC (defaults to 1). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#max_retries OpcProvider#max_retries}
        :param storage_endpoint: The HTTP endpoint for Oracle Storage operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#storage_endpoint OpcProvider#storage_endpoint}
        :param storage_service_id: The Storage Service ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#storage_service_id OpcProvider#storage_service_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OpcProviderConfig.__init__)
            check_type(argname="argument identity_domain", value=identity_domain, expected_type=type_hints["identity_domain"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument insecure", value=insecure, expected_type=type_hints["insecure"])
            check_type(argname="argument lbaas_endpoint", value=lbaas_endpoint, expected_type=type_hints["lbaas_endpoint"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument storage_endpoint", value=storage_endpoint, expected_type=type_hints["storage_endpoint"])
            check_type(argname="argument storage_service_id", value=storage_service_id, expected_type=type_hints["storage_service_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_domain": identity_domain,
            "password": password,
            "user": user,
        }
        if alias is not None:
            self._values["alias"] = alias
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if insecure is not None:
            self._values["insecure"] = insecure
        if lbaas_endpoint is not None:
            self._values["lbaas_endpoint"] = lbaas_endpoint
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if storage_endpoint is not None:
            self._values["storage_endpoint"] = storage_endpoint
        if storage_service_id is not None:
            self._values["storage_service_id"] = storage_service_id

    @builtins.property
    def identity_domain(self) -> builtins.str:
        '''The OPC identity domain for API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#identity_domain OpcProvider#identity_domain}
        '''
        result = self._values.get("identity_domain")
        assert result is not None, "Required property 'identity_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The user password for OPC API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#password OpcProvider#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> builtins.str:
        '''The user name for OPC API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#user OpcProvider#user}
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#alias OpcProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for OPC API operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#endpoint OpcProvider#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Skip TLS Verification for self-signed certificates. Should only be used if absolutely required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#insecure OpcProvider#insecure}
        '''
        result = self._values.get("insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lbaas_endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for the Load Balancer Classic service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#lbaas_endpoint OpcProvider#lbaas_endpoint}
        '''
        result = self._values.get("lbaas_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''Maximum number retries to wait for a successful response when operating on resources within OPC (defaults to 1).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#max_retries OpcProvider#max_retries}
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_endpoint(self) -> typing.Optional[builtins.str]:
        '''The HTTP endpoint for Oracle Storage operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#storage_endpoint OpcProvider#storage_endpoint}
        '''
        result = self._values.get("storage_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_service_id(self) -> typing.Optional[builtins.str]:
        '''The Storage Service ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc#storage_service_id OpcProvider#storage_service_id}
        '''
        result = self._values.get("storage_service_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpcProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OpcProvider",
    "OpcProviderConfig",
]

publication.publish()
