'''
# `provider`

Refer to the Terraform Registory for docs: [`datadog`](https://www.terraform.io/docs/providers/datadog).
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


class DatadogProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.provider.DatadogProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog datadog}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_url: typing.Optional[builtins.str] = None,
        app_key: typing.Optional[builtins.str] = None,
        http_client_retry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_client_retry_timeout: typing.Optional[jsii.Number] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog datadog} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#alias DatadogProvider#alias}
        :param api_key: (Required unless validate is false) Datadog API key. This can also be set via the DD_API_KEY environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#api_key DatadogProvider#api_key}
        :param api_url: The API URL. This can also be set via the DD_HOST environment variable. Note that this URL must not end with the /api/ path. For example, https://api.datadoghq.com/ is a correct value, while https://api.datadoghq.com/api/ is not. And if you're working with "EU" version of Datadog, use https://api.datadoghq.eu/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#api_url DatadogProvider#api_url}
        :param app_key: (Required unless validate is false) Datadog APP key. This can also be set via the DD_APP_KEY environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#app_key DatadogProvider#app_key}
        :param http_client_retry_enabled: Enables request retries on HTTP status codes 429 and 5xx. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#http_client_retry_enabled DatadogProvider#http_client_retry_enabled}
        :param http_client_retry_timeout: The HTTP request retry timeout period. Defaults to 60 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#http_client_retry_timeout DatadogProvider#http_client_retry_timeout}
        :param validate: Enables validation of the provided API and APP keys during provider initialization. Default is true. When false, api_key and app_key won't be checked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#validate DatadogProvider#validate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DatadogProviderConfig(
            alias=alias,
            api_key=api_key,
            api_url=api_url,
            app_key=app_key,
            http_client_retry_enabled=http_client_retry_enabled,
            http_client_retry_timeout=http_client_retry_timeout,
            validate=validate,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetApiUrl")
    def reset_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiUrl", []))

    @jsii.member(jsii_name="resetAppKey")
    def reset_app_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppKey", []))

    @jsii.member(jsii_name="resetHttpClientRetryEnabled")
    def reset_http_client_retry_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpClientRetryEnabled", []))

    @jsii.member(jsii_name="resetHttpClientRetryTimeout")
    def reset_http_client_retry_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpClientRetryTimeout", []))

    @jsii.member(jsii_name="resetValidate")
    def reset_validate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidate", []))

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
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiUrlInput")
    def api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="appKeyInput")
    def app_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="httpClientRetryEnabledInput")
    def http_client_retry_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpClientRetryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="httpClientRetryTimeoutInput")
    def http_client_retry_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpClientRetryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="validateInput")
    def validate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiUrl")
    def api_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrl"))

    @api_url.setter
    def api_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "api_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="appKey")
    def app_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appKey"))

    @app_key.setter
    def app_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "app_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appKey", value)

    @builtins.property
    @jsii.member(jsii_name="httpClientRetryEnabled")
    def http_client_retry_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "httpClientRetryEnabled"))

    @http_client_retry_enabled.setter
    def http_client_retry_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "http_client_retry_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpClientRetryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="httpClientRetryTimeout")
    def http_client_retry_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpClientRetryTimeout"))

    @http_client_retry_timeout.setter
    def http_client_retry_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "http_client_retry_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpClientRetryTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="validate")
    def validate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validate"))

    @validate.setter
    def validate(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DatadogProvider, "validate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validate", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.provider.DatadogProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "api_key": "apiKey",
        "api_url": "apiUrl",
        "app_key": "appKey",
        "http_client_retry_enabled": "httpClientRetryEnabled",
        "http_client_retry_timeout": "httpClientRetryTimeout",
        "validate": "validate",
    },
)
class DatadogProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_url: typing.Optional[builtins.str] = None,
        app_key: typing.Optional[builtins.str] = None,
        http_client_retry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        http_client_retry_timeout: typing.Optional[jsii.Number] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#alias DatadogProvider#alias}
        :param api_key: (Required unless validate is false) Datadog API key. This can also be set via the DD_API_KEY environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#api_key DatadogProvider#api_key}
        :param api_url: The API URL. This can also be set via the DD_HOST environment variable. Note that this URL must not end with the /api/ path. For example, https://api.datadoghq.com/ is a correct value, while https://api.datadoghq.com/api/ is not. And if you're working with "EU" version of Datadog, use https://api.datadoghq.eu/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#api_url DatadogProvider#api_url}
        :param app_key: (Required unless validate is false) Datadog APP key. This can also be set via the DD_APP_KEY environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#app_key DatadogProvider#app_key}
        :param http_client_retry_enabled: Enables request retries on HTTP status codes 429 and 5xx. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#http_client_retry_enabled DatadogProvider#http_client_retry_enabled}
        :param http_client_retry_timeout: The HTTP request retry timeout period. Defaults to 60 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#http_client_retry_timeout DatadogProvider#http_client_retry_timeout}
        :param validate: Enables validation of the provided API and APP keys during provider initialization. Default is true. When false, api_key and app_key won't be checked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#validate DatadogProvider#validate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DatadogProviderConfig.__init__)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_url", value=api_url, expected_type=type_hints["api_url"])
            check_type(argname="argument app_key", value=app_key, expected_type=type_hints["app_key"])
            check_type(argname="argument http_client_retry_enabled", value=http_client_retry_enabled, expected_type=type_hints["http_client_retry_enabled"])
            check_type(argname="argument http_client_retry_timeout", value=http_client_retry_timeout, expected_type=type_hints["http_client_retry_timeout"])
            check_type(argname="argument validate", value=validate, expected_type=type_hints["validate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if api_key is not None:
            self._values["api_key"] = api_key
        if api_url is not None:
            self._values["api_url"] = api_url
        if app_key is not None:
            self._values["app_key"] = app_key
        if http_client_retry_enabled is not None:
            self._values["http_client_retry_enabled"] = http_client_retry_enabled
        if http_client_retry_timeout is not None:
            self._values["http_client_retry_timeout"] = http_client_retry_timeout
        if validate is not None:
            self._values["validate"] = validate

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#alias DatadogProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''(Required unless validate is false) Datadog API key. This can also be set via the DD_API_KEY environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#api_key DatadogProvider#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_url(self) -> typing.Optional[builtins.str]:
        '''The API URL.

        This can also be set via the DD_HOST environment variable. Note that this URL must not end with the /api/ path. For example, https://api.datadoghq.com/ is a correct value, while https://api.datadoghq.com/api/ is not. And if you're working with "EU" version of Datadog, use https://api.datadoghq.eu/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#api_url DatadogProvider#api_url}
        '''
        result = self._values.get("api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_key(self) -> typing.Optional[builtins.str]:
        '''(Required unless validate is false) Datadog APP key. This can also be set via the DD_APP_KEY environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#app_key DatadogProvider#app_key}
        '''
        result = self._values.get("app_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_client_retry_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables request retries on HTTP status codes 429 and 5xx. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#http_client_retry_enabled DatadogProvider#http_client_retry_enabled}
        '''
        result = self._values.get("http_client_retry_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def http_client_retry_timeout(self) -> typing.Optional[jsii.Number]:
        '''The HTTP request retry timeout period. Defaults to 60 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#http_client_retry_timeout DatadogProvider#http_client_retry_timeout}
        '''
        result = self._values.get("http_client_retry_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def validate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables validation of the provided API and APP keys during provider initialization.

        Default is true. When false, api_key and app_key won't be checked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog#validate DatadogProvider#validate}
        '''
        result = self._values.get("validate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatadogProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatadogProvider",
    "DatadogProviderConfig",
]

publication.publish()
