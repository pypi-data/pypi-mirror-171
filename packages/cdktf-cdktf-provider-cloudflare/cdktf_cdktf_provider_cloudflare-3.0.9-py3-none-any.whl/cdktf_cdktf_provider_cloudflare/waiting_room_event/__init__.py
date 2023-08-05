'''
# `cloudflare_waiting_room_event`

Refer to the Terraform Registory for docs: [`cloudflare_waiting_room_event`](https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event).
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


class WaitingRoomEvent(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.waitingRoomEvent.WaitingRoomEvent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event cloudflare_waiting_room_event}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        event_end_time: builtins.str,
        event_start_time: builtins.str,
        name: builtins.str,
        waiting_room_id: builtins.str,
        zone_id: builtins.str,
        custom_page_html: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_session_renewal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        new_users_per_minute: typing.Optional[jsii.Number] = None,
        prequeue_start_time: typing.Optional[builtins.str] = None,
        queueing_method: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[jsii.Number] = None,
        shuffle_at_event_start: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suspended: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        total_active_users: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event cloudflare_waiting_room_event} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param event_end_time: ISO 8601 timestamp that marks the end of the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#event_end_time WaitingRoomEvent#event_end_time}
        :param event_start_time: ISO 8601 timestamp that marks the start of the event. Must occur at least 1 minute before ``event_end_time``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#event_start_time WaitingRoomEvent#event_start_time}
        :param name: A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#name WaitingRoomEvent#name}
        :param waiting_room_id: The Waiting Room ID the event should apply to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#waiting_room_id WaitingRoomEvent#waiting_room_id}
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#zone_id WaitingRoomEvent#zone_id}
        :param custom_page_html: This is a templated html file that will be rendered at the edge. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#custom_page_html WaitingRoomEvent#custom_page_html}
        :param description: A description to let users add more details about the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#description WaitingRoomEvent#description}
        :param disable_session_renewal: Disables automatic renewal of session cookies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#disable_session_renewal WaitingRoomEvent#disable_session_renewal}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#id WaitingRoomEvent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param new_users_per_minute: The number of new users that will be let into the route every minute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#new_users_per_minute WaitingRoomEvent#new_users_per_minute}
        :param prequeue_start_time: ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before ``event_start_time``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#prequeue_start_time WaitingRoomEvent#prequeue_start_time}
        :param queueing_method: The queueing method used by the waiting room. Available values: ``fifo``, ``random``, ``passthrough``, ``reject``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#queueing_method WaitingRoomEvent#queueing_method}
        :param session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#session_duration WaitingRoomEvent#session_duration}
        :param shuffle_at_event_start: Users in the prequeue will be shuffled randomly at the ``event_start_time``. Requires that ``prequeue_start_time`` is not null. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#shuffle_at_event_start WaitingRoomEvent#shuffle_at_event_start}
        :param suspended: If suspended, the event is ignored and traffic will be handled based on the waiting room configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#suspended WaitingRoomEvent#suspended}
        :param total_active_users: The total number of active user sessions on the route at a point in time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#total_active_users WaitingRoomEvent#total_active_users}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WaitingRoomEvent.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WaitingRoomEventConfig(
            event_end_time=event_end_time,
            event_start_time=event_start_time,
            name=name,
            waiting_room_id=waiting_room_id,
            zone_id=zone_id,
            custom_page_html=custom_page_html,
            description=description,
            disable_session_renewal=disable_session_renewal,
            id=id,
            new_users_per_minute=new_users_per_minute,
            prequeue_start_time=prequeue_start_time,
            queueing_method=queueing_method,
            session_duration=session_duration,
            shuffle_at_event_start=shuffle_at_event_start,
            suspended=suspended,
            total_active_users=total_active_users,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCustomPageHtml")
    def reset_custom_page_html(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPageHtml", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableSessionRenewal")
    def reset_disable_session_renewal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableSessionRenewal", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNewUsersPerMinute")
    def reset_new_users_per_minute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewUsersPerMinute", []))

    @jsii.member(jsii_name="resetPrequeueStartTime")
    def reset_prequeue_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrequeueStartTime", []))

    @jsii.member(jsii_name="resetQueueingMethod")
    def reset_queueing_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueingMethod", []))

    @jsii.member(jsii_name="resetSessionDuration")
    def reset_session_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionDuration", []))

    @jsii.member(jsii_name="resetShuffleAtEventStart")
    def reset_shuffle_at_event_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShuffleAtEventStart", []))

    @jsii.member(jsii_name="resetSuspended")
    def reset_suspended(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspended", []))

    @jsii.member(jsii_name="resetTotalActiveUsers")
    def reset_total_active_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTotalActiveUsers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="modifiedOn")
    def modified_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedOn"))

    @builtins.property
    @jsii.member(jsii_name="customPageHtmlInput")
    def custom_page_html_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customPageHtmlInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableSessionRenewalInput")
    def disable_session_renewal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableSessionRenewalInput"))

    @builtins.property
    @jsii.member(jsii_name="eventEndTimeInput")
    def event_end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventEndTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="eventStartTimeInput")
    def event_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="newUsersPerMinuteInput")
    def new_users_per_minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "newUsersPerMinuteInput"))

    @builtins.property
    @jsii.member(jsii_name="prequeueStartTimeInput")
    def prequeue_start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prequeueStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="queueingMethodInput")
    def queueing_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueingMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionDurationInput")
    def session_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="shuffleAtEventStartInput")
    def shuffle_at_event_start_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "shuffleAtEventStartInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendedInput")
    def suspended_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "suspendedInput"))

    @builtins.property
    @jsii.member(jsii_name="totalActiveUsersInput")
    def total_active_users_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "totalActiveUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="waitingRoomIdInput")
    def waiting_room_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitingRoomIdInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customPageHtml")
    def custom_page_html(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customPageHtml"))

    @custom_page_html.setter
    def custom_page_html(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "custom_page_html").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customPageHtml", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableSessionRenewal")
    def disable_session_renewal(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableSessionRenewal"))

    @disable_session_renewal.setter
    def disable_session_renewal(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "disable_session_renewal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableSessionRenewal", value)

    @builtins.property
    @jsii.member(jsii_name="eventEndTime")
    def event_end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventEndTime"))

    @event_end_time.setter
    def event_end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "event_end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventEndTime", value)

    @builtins.property
    @jsii.member(jsii_name="eventStartTime")
    def event_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventStartTime"))

    @event_start_time.setter
    def event_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "event_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="newUsersPerMinute")
    def new_users_per_minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "newUsersPerMinute"))

    @new_users_per_minute.setter
    def new_users_per_minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "new_users_per_minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newUsersPerMinute", value)

    @builtins.property
    @jsii.member(jsii_name="prequeueStartTime")
    def prequeue_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prequeueStartTime"))

    @prequeue_start_time.setter
    def prequeue_start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "prequeue_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prequeueStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="queueingMethod")
    def queueing_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueingMethod"))

    @queueing_method.setter
    def queueing_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "queueing_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueingMethod", value)

    @builtins.property
    @jsii.member(jsii_name="sessionDuration")
    def session_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionDuration"))

    @session_duration.setter
    def session_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "session_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="shuffleAtEventStart")
    def shuffle_at_event_start(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "shuffleAtEventStart"))

    @shuffle_at_event_start.setter
    def shuffle_at_event_start(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "shuffle_at_event_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shuffleAtEventStart", value)

    @builtins.property
    @jsii.member(jsii_name="suspended")
    def suspended(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "suspended"))

    @suspended.setter
    def suspended(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "suspended").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspended", value)

    @builtins.property
    @jsii.member(jsii_name="totalActiveUsers")
    def total_active_users(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalActiveUsers"))

    @total_active_users.setter
    def total_active_users(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "total_active_users").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalActiveUsers", value)

    @builtins.property
    @jsii.member(jsii_name="waitingRoomId")
    def waiting_room_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitingRoomId"))

    @waiting_room_id.setter
    def waiting_room_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "waiting_room_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitingRoomId", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WaitingRoomEvent, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.waitingRoomEvent.WaitingRoomEventConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "event_end_time": "eventEndTime",
        "event_start_time": "eventStartTime",
        "name": "name",
        "waiting_room_id": "waitingRoomId",
        "zone_id": "zoneId",
        "custom_page_html": "customPageHtml",
        "description": "description",
        "disable_session_renewal": "disableSessionRenewal",
        "id": "id",
        "new_users_per_minute": "newUsersPerMinute",
        "prequeue_start_time": "prequeueStartTime",
        "queueing_method": "queueingMethod",
        "session_duration": "sessionDuration",
        "shuffle_at_event_start": "shuffleAtEventStart",
        "suspended": "suspended",
        "total_active_users": "totalActiveUsers",
    },
)
class WaitingRoomEventConfig(cdktf.TerraformMetaArguments):
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
        event_end_time: builtins.str,
        event_start_time: builtins.str,
        name: builtins.str,
        waiting_room_id: builtins.str,
        zone_id: builtins.str,
        custom_page_html: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_session_renewal: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        new_users_per_minute: typing.Optional[jsii.Number] = None,
        prequeue_start_time: typing.Optional[builtins.str] = None,
        queueing_method: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[jsii.Number] = None,
        shuffle_at_event_start: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suspended: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        total_active_users: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param event_end_time: ISO 8601 timestamp that marks the end of the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#event_end_time WaitingRoomEvent#event_end_time}
        :param event_start_time: ISO 8601 timestamp that marks the start of the event. Must occur at least 1 minute before ``event_end_time``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#event_start_time WaitingRoomEvent#event_start_time}
        :param name: A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#name WaitingRoomEvent#name}
        :param waiting_room_id: The Waiting Room ID the event should apply to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#waiting_room_id WaitingRoomEvent#waiting_room_id}
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#zone_id WaitingRoomEvent#zone_id}
        :param custom_page_html: This is a templated html file that will be rendered at the edge. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#custom_page_html WaitingRoomEvent#custom_page_html}
        :param description: A description to let users add more details about the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#description WaitingRoomEvent#description}
        :param disable_session_renewal: Disables automatic renewal of session cookies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#disable_session_renewal WaitingRoomEvent#disable_session_renewal}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#id WaitingRoomEvent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param new_users_per_minute: The number of new users that will be let into the route every minute. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#new_users_per_minute WaitingRoomEvent#new_users_per_minute}
        :param prequeue_start_time: ISO 8601 timestamp that marks when to begin queueing all users before the event starts. Must occur at least 5 minutes before ``event_start_time``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#prequeue_start_time WaitingRoomEvent#prequeue_start_time}
        :param queueing_method: The queueing method used by the waiting room. Available values: ``fifo``, ``random``, ``passthrough``, ``reject``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#queueing_method WaitingRoomEvent#queueing_method}
        :param session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#session_duration WaitingRoomEvent#session_duration}
        :param shuffle_at_event_start: Users in the prequeue will be shuffled randomly at the ``event_start_time``. Requires that ``prequeue_start_time`` is not null. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#shuffle_at_event_start WaitingRoomEvent#shuffle_at_event_start}
        :param suspended: If suspended, the event is ignored and traffic will be handled based on the waiting room configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#suspended WaitingRoomEvent#suspended}
        :param total_active_users: The total number of active user sessions on the route at a point in time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#total_active_users WaitingRoomEvent#total_active_users}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(WaitingRoomEventConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument event_end_time", value=event_end_time, expected_type=type_hints["event_end_time"])
            check_type(argname="argument event_start_time", value=event_start_time, expected_type=type_hints["event_start_time"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument waiting_room_id", value=waiting_room_id, expected_type=type_hints["waiting_room_id"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument custom_page_html", value=custom_page_html, expected_type=type_hints["custom_page_html"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_session_renewal", value=disable_session_renewal, expected_type=type_hints["disable_session_renewal"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument new_users_per_minute", value=new_users_per_minute, expected_type=type_hints["new_users_per_minute"])
            check_type(argname="argument prequeue_start_time", value=prequeue_start_time, expected_type=type_hints["prequeue_start_time"])
            check_type(argname="argument queueing_method", value=queueing_method, expected_type=type_hints["queueing_method"])
            check_type(argname="argument session_duration", value=session_duration, expected_type=type_hints["session_duration"])
            check_type(argname="argument shuffle_at_event_start", value=shuffle_at_event_start, expected_type=type_hints["shuffle_at_event_start"])
            check_type(argname="argument suspended", value=suspended, expected_type=type_hints["suspended"])
            check_type(argname="argument total_active_users", value=total_active_users, expected_type=type_hints["total_active_users"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_end_time": event_end_time,
            "event_start_time": event_start_time,
            "name": name,
            "waiting_room_id": waiting_room_id,
            "zone_id": zone_id,
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
        if custom_page_html is not None:
            self._values["custom_page_html"] = custom_page_html
        if description is not None:
            self._values["description"] = description
        if disable_session_renewal is not None:
            self._values["disable_session_renewal"] = disable_session_renewal
        if id is not None:
            self._values["id"] = id
        if new_users_per_minute is not None:
            self._values["new_users_per_minute"] = new_users_per_minute
        if prequeue_start_time is not None:
            self._values["prequeue_start_time"] = prequeue_start_time
        if queueing_method is not None:
            self._values["queueing_method"] = queueing_method
        if session_duration is not None:
            self._values["session_duration"] = session_duration
        if shuffle_at_event_start is not None:
            self._values["shuffle_at_event_start"] = shuffle_at_event_start
        if suspended is not None:
            self._values["suspended"] = suspended
        if total_active_users is not None:
            self._values["total_active_users"] = total_active_users

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
    def event_end_time(self) -> builtins.str:
        '''ISO 8601 timestamp that marks the end of the event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#event_end_time WaitingRoomEvent#event_end_time}
        '''
        result = self._values.get("event_end_time")
        assert result is not None, "Required property 'event_end_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_start_time(self) -> builtins.str:
        '''ISO 8601 timestamp that marks the start of the event. Must occur at least 1 minute before ``event_end_time``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#event_start_time WaitingRoomEvent#event_start_time}
        '''
        result = self._values.get("event_start_time")
        assert result is not None, "Required property 'event_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique name to identify the event. Only alphanumeric characters, hyphens, and underscores are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#name WaitingRoomEvent#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def waiting_room_id(self) -> builtins.str:
        '''The Waiting Room ID the event should apply to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#waiting_room_id WaitingRoomEvent#waiting_room_id}
        '''
        result = self._values.get("waiting_room_id")
        assert result is not None, "Required property 'waiting_room_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#zone_id WaitingRoomEvent#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_page_html(self) -> typing.Optional[builtins.str]:
        '''This is a templated html file that will be rendered at the edge.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#custom_page_html WaitingRoomEvent#custom_page_html}
        '''
        result = self._values.get("custom_page_html")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description to let users add more details about the event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#description WaitingRoomEvent#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_session_renewal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disables automatic renewal of session cookies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#disable_session_renewal WaitingRoomEvent#disable_session_renewal}
        '''
        result = self._values.get("disable_session_renewal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#id WaitingRoomEvent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def new_users_per_minute(self) -> typing.Optional[jsii.Number]:
        '''The number of new users that will be let into the route every minute.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#new_users_per_minute WaitingRoomEvent#new_users_per_minute}
        '''
        result = self._values.get("new_users_per_minute")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def prequeue_start_time(self) -> typing.Optional[builtins.str]:
        '''ISO 8601 timestamp that marks when to begin queueing all users before the event starts.

        Must occur at least 5 minutes before ``event_start_time``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#prequeue_start_time WaitingRoomEvent#prequeue_start_time}
        '''
        result = self._values.get("prequeue_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queueing_method(self) -> typing.Optional[builtins.str]:
        '''The queueing method used by the waiting room. Available values: ``fifo``, ``random``, ``passthrough``, ``reject``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#queueing_method WaitingRoomEvent#queueing_method}
        '''
        result = self._values.get("queueing_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_duration(self) -> typing.Optional[jsii.Number]:
        '''Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to the origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#session_duration WaitingRoomEvent#session_duration}
        '''
        result = self._values.get("session_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shuffle_at_event_start(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Users in the prequeue will be shuffled randomly at the ``event_start_time``.

        Requires that ``prequeue_start_time`` is not null. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#shuffle_at_event_start WaitingRoomEvent#shuffle_at_event_start}
        '''
        result = self._values.get("shuffle_at_event_start")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def suspended(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If suspended, the event is ignored and traffic will be handled based on the waiting room configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#suspended WaitingRoomEvent#suspended}
        '''
        result = self._values.get("suspended")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def total_active_users(self) -> typing.Optional[jsii.Number]:
        '''The total number of active user sessions on the route at a point in time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/waiting_room_event#total_active_users WaitingRoomEvent#total_active_users}
        '''
        result = self._values.get("total_active_users")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaitingRoomEventConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "WaitingRoomEvent",
    "WaitingRoomEventConfig",
]

publication.publish()
