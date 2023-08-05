'''
# `datadog_integration_slack_channel`

Refer to the Terraform Registory for docs: [`datadog_integration_slack_channel`](https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel).
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


class IntegrationSlackChannel(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.integrationSlackChannel.IntegrationSlackChannel",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel datadog_integration_slack_channel}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_name: builtins.str,
        channel_name: builtins.str,
        display: typing.Union["IntegrationSlackChannelDisplay", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel datadog_integration_slack_channel} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_name: Slack account name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#account_name IntegrationSlackChannel#account_name}
        :param channel_name: Slack channel name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#channel_name IntegrationSlackChannel#channel_name}
        :param display: display block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#display IntegrationSlackChannel#display}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#id IntegrationSlackChannel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IntegrationSlackChannel.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IntegrationSlackChannelConfig(
            account_name=account_name,
            channel_name=channel_name,
            display=display,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDisplay")
    def put_display(
        self,
        *,
        message: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notified: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param message: Show the main body of the alert event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#message IntegrationSlackChannel#message}
        :param notified: Show the list of @-handles in the alert event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#notified IntegrationSlackChannel#notified}
        :param snapshot: Show the alert event's snapshot image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#snapshot IntegrationSlackChannel#snapshot}
        :param tags: Show the scopes on which the monitor alerted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#tags IntegrationSlackChannel#tags}
        '''
        value = IntegrationSlackChannelDisplay(
            message=message, notified=notified, snapshot=snapshot, tags=tags
        )

        return typing.cast(None, jsii.invoke(self, "putDisplay", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="display")
    def display(self) -> "IntegrationSlackChannelDisplayOutputReference":
        return typing.cast("IntegrationSlackChannelDisplayOutputReference", jsii.get(self, "display"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="channelNameInput")
    def channel_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="displayInput")
    def display_input(self) -> typing.Optional["IntegrationSlackChannelDisplay"]:
        return typing.cast(typing.Optional["IntegrationSlackChannelDisplay"], jsii.get(self, "displayInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannel, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannel, "channel_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannel, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.integrationSlackChannel.IntegrationSlackChannelConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_name": "accountName",
        "channel_name": "channelName",
        "display": "display",
        "id": "id",
    },
)
class IntegrationSlackChannelConfig(cdktf.TerraformMetaArguments):
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
        account_name: builtins.str,
        channel_name: builtins.str,
        display: typing.Union["IntegrationSlackChannelDisplay", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_name: Slack account name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#account_name IntegrationSlackChannel#account_name}
        :param channel_name: Slack channel name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#channel_name IntegrationSlackChannel#channel_name}
        :param display: display block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#display IntegrationSlackChannel#display}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#id IntegrationSlackChannel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(display, dict):
            display = IntegrationSlackChannelDisplay(**display)
        if __debug__:
            type_hints = typing.get_type_hints(IntegrationSlackChannelConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument display", value=display, expected_type=type_hints["display"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "channel_name": channel_name,
            "display": display,
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
        if id is not None:
            self._values["id"] = id

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
    def account_name(self) -> builtins.str:
        '''Slack account name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#account_name IntegrationSlackChannel#account_name}
        '''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''Slack channel name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#channel_name IntegrationSlackChannel#channel_name}
        '''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display(self) -> "IntegrationSlackChannelDisplay":
        '''display block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#display IntegrationSlackChannel#display}
        '''
        result = self._values.get("display")
        assert result is not None, "Required property 'display' is missing"
        return typing.cast("IntegrationSlackChannelDisplay", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#id IntegrationSlackChannel#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationSlackChannelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.integrationSlackChannel.IntegrationSlackChannelDisplay",
    jsii_struct_bases=[],
    name_mapping={
        "message": "message",
        "notified": "notified",
        "snapshot": "snapshot",
        "tags": "tags",
    },
)
class IntegrationSlackChannelDisplay:
    def __init__(
        self,
        *,
        message: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        notified: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param message: Show the main body of the alert event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#message IntegrationSlackChannel#message}
        :param notified: Show the list of @-handles in the alert event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#notified IntegrationSlackChannel#notified}
        :param snapshot: Show the alert event's snapshot image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#snapshot IntegrationSlackChannel#snapshot}
        :param tags: Show the scopes on which the monitor alerted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#tags IntegrationSlackChannel#tags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IntegrationSlackChannelDisplay.__init__)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument notified", value=notified, expected_type=type_hints["notified"])
            check_type(argname="argument snapshot", value=snapshot, expected_type=type_hints["snapshot"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if notified is not None:
            self._values["notified"] = notified
        if snapshot is not None:
            self._values["snapshot"] = snapshot
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Show the main body of the alert event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#message IntegrationSlackChannel#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def notified(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Show the list of @-handles in the alert event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#notified IntegrationSlackChannel#notified}
        '''
        result = self._values.get("notified")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def snapshot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Show the alert event's snapshot image.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#snapshot IntegrationSlackChannel#snapshot}
        '''
        result = self._values.get("snapshot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Show the scopes on which the monitor alerted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/integration_slack_channel#tags IntegrationSlackChannel#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationSlackChannelDisplay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IntegrationSlackChannelDisplayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.integrationSlackChannel.IntegrationSlackChannelDisplayOutputReference",
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
            type_hints = typing.get_type_hints(IntegrationSlackChannelDisplayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetNotified")
    def reset_notified(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotified", []))

    @jsii.member(jsii_name="resetSnapshot")
    def reset_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshot", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="notifiedInput")
    def notified_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "notifiedInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotInput")
    def snapshot_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "snapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannelDisplayOutputReference, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="notified")
    def notified(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "notified"))

    @notified.setter
    def notified(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannelDisplayOutputReference, "notified").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notified", value)

    @builtins.property
    @jsii.member(jsii_name="snapshot")
    def snapshot(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "snapshot"))

    @snapshot.setter
    def snapshot(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannelDisplayOutputReference, "snapshot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshot", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannelDisplayOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IntegrationSlackChannelDisplay]:
        return typing.cast(typing.Optional[IntegrationSlackChannelDisplay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IntegrationSlackChannelDisplay],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IntegrationSlackChannelDisplayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IntegrationSlackChannel",
    "IntegrationSlackChannelConfig",
    "IntegrationSlackChannelDisplay",
    "IntegrationSlackChannelDisplayOutputReference",
]

publication.publish()
