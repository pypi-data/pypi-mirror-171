'''
# `provider`

Refer to the Terraform Registory for docs: [`pagerduty`](https://www.terraform.io/docs/providers/pagerduty).
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


class PagerdutyProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.provider.PagerdutyProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/pagerduty pagerduty}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        token: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        api_url_override: typing.Optional[builtins.str] = None,
        service_region: typing.Optional[builtins.str] = None,
        skip_credentials_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/pagerduty pagerduty} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#token PagerdutyProvider#token}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#alias PagerdutyProvider#alias}
        :param api_url_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#api_url_override PagerdutyProvider#api_url_override}.
        :param service_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#service_region PagerdutyProvider#service_region}.
        :param skip_credentials_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#skip_credentials_validation PagerdutyProvider#skip_credentials_validation}.
        :param user_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#user_token PagerdutyProvider#user_token}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagerdutyProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = PagerdutyProviderConfig(
            token=token,
            alias=alias,
            api_url_override=api_url_override,
            service_region=service_region,
            skip_credentials_validation=skip_credentials_validation,
            user_token=user_token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiUrlOverride")
    def reset_api_url_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiUrlOverride", []))

    @jsii.member(jsii_name="resetServiceRegion")
    def reset_service_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegion", []))

    @jsii.member(jsii_name="resetSkipCredentialsValidation")
    def reset_skip_credentials_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipCredentialsValidation", []))

    @jsii.member(jsii_name="resetUserToken")
    def reset_user_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserToken", []))

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
    @jsii.member(jsii_name="apiUrlOverrideInput")
    def api_url_override_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrlOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegionInput")
    def service_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="skipCredentialsValidationInput")
    def skip_credentials_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipCredentialsValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="userTokenInput")
    def user_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagerdutyProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiUrlOverride")
    def api_url_override(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrlOverride"))

    @api_url_override.setter
    def api_url_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagerdutyProvider, "api_url_override").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUrlOverride", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRegion")
    def service_region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRegion"))

    @service_region.setter
    def service_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagerdutyProvider, "service_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRegion", value)

    @builtins.property
    @jsii.member(jsii_name="skipCredentialsValidation")
    def skip_credentials_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipCredentialsValidation"))

    @skip_credentials_validation.setter
    def skip_credentials_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagerdutyProvider, "skip_credentials_validation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipCredentialsValidation", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagerdutyProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="userToken")
    def user_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userToken"))

    @user_token.setter
    def user_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PagerdutyProvider, "user_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userToken", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.provider.PagerdutyProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "token": "token",
        "alias": "alias",
        "api_url_override": "apiUrlOverride",
        "service_region": "serviceRegion",
        "skip_credentials_validation": "skipCredentialsValidation",
        "user_token": "userToken",
    },
)
class PagerdutyProviderConfig:
    def __init__(
        self,
        *,
        token: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        api_url_override: typing.Optional[builtins.str] = None,
        service_region: typing.Optional[builtins.str] = None,
        skip_credentials_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#token PagerdutyProvider#token}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#alias PagerdutyProvider#alias}
        :param api_url_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#api_url_override PagerdutyProvider#api_url_override}.
        :param service_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#service_region PagerdutyProvider#service_region}.
        :param skip_credentials_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#skip_credentials_validation PagerdutyProvider#skip_credentials_validation}.
        :param user_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#user_token PagerdutyProvider#user_token}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PagerdutyProviderConfig.__init__)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_url_override", value=api_url_override, expected_type=type_hints["api_url_override"])
            check_type(argname="argument service_region", value=service_region, expected_type=type_hints["service_region"])
            check_type(argname="argument skip_credentials_validation", value=skip_credentials_validation, expected_type=type_hints["skip_credentials_validation"])
            check_type(argname="argument user_token", value=user_token, expected_type=type_hints["user_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "token": token,
        }
        if alias is not None:
            self._values["alias"] = alias
        if api_url_override is not None:
            self._values["api_url_override"] = api_url_override
        if service_region is not None:
            self._values["service_region"] = service_region
        if skip_credentials_validation is not None:
            self._values["skip_credentials_validation"] = skip_credentials_validation
        if user_token is not None:
            self._values["user_token"] = user_token

    @builtins.property
    def token(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#token PagerdutyProvider#token}.'''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#alias PagerdutyProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_url_override(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#api_url_override PagerdutyProvider#api_url_override}.'''
        result = self._values.get("api_url_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#service_region PagerdutyProvider#service_region}.'''
        result = self._values.get("service_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_credentials_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#skip_credentials_validation PagerdutyProvider#skip_credentials_validation}.'''
        result = self._values.get("skip_credentials_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty#user_token PagerdutyProvider#user_token}.'''
        result = self._values.get("user_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagerdutyProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "PagerdutyProvider",
    "PagerdutyProviderConfig",
]

publication.publish()
