'''
# `cloudflare_logpush_job`

Refer to the Terraform Registory for docs: [`cloudflare_logpush_job`](https://www.terraform.io/docs/providers/cloudflare/r/logpush_job).
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


class LogpushJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.logpushJob.LogpushJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job cloudflare_logpush_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dataset: builtins.str,
        destination_conf: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filter: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        logpull_options: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        ownership_challenge: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job cloudflare_logpush_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See `Logpush destination documentation <https://developers.cloudflare.com/logs/reference/logpush-api-configuration#destination>`_. Available values: ``firewall_events``, ``http_requests``, ``spectrum_events``, ``nel_reports``, ``audit_logs``, ``gateway_dns``, ``gateway_http``, ``gateway_network``, ``dns_logs``, ``network_analytics_logs``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#dataset LogpushJob#dataset}
        :param destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See `Logpush destination documentation <https://developers.cloudflare.com/logs/reference/logpush-api-configuration#destination>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#destination_conf LogpushJob#destination_conf}
        :param account_id: The account identifier to target for the resource. Must provide only one of ``account_id``, ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#account_id LogpushJob#account_id}
        :param enabled: Whether to enable the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#enabled LogpushJob#enabled}
        :param filter: Use filters to select the events to include and/or remove from your logs. For more information, refer to `Filters <https://developers.cloudflare.com/logs/reference/logpush-api-configuration/filters/>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#filter LogpushJob#filter}
        :param frequency: A higher frequency will result in logs being pushed on faster with smaller files. ``low`` frequency will push logs less often with larger files. Available values: ``high``, ``low``. Defaults to ``high``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#frequency LogpushJob#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#id LogpushJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: The kind of logpush job to create. Available values: ``edge``, ``instant-logs``, ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#kind LogpushJob#kind}
        :param logpull_options: Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See `Logpull options documentation <https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#logpull_options LogpushJob#logpull_options}
        :param name: The name of the logpush job to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#name LogpushJob#name}
        :param ownership_challenge: Ownership challenge token to prove destination ownership, required when destination is Amazon S3, Google Cloud Storage, Microsoft Azure or Sumo Logic. See `Developer documentation <https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#ownership_challenge LogpushJob#ownership_challenge}
        :param zone_id: The zone identifier to target for the resource. Must provide only one of ``account_id``, ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#zone_id LogpushJob#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogpushJob.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogpushJobConfig(
            dataset=dataset,
            destination_conf=destination_conf,
            account_id=account_id,
            enabled=enabled,
            filter=filter,
            frequency=frequency,
            id=id,
            kind=kind,
            logpull_options=logpull_options,
            name=name,
            ownership_challenge=ownership_challenge,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetLogpullOptions")
    def reset_logpull_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogpullOptions", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOwnershipChallenge")
    def reset_ownership_challenge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwnershipChallenge", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfInput")
    def destination_conf_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationConfInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="logpullOptionsInput")
    def logpull_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logpullOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownershipChallengeInput")
    def ownership_challenge_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownershipChallengeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataset"))

    @dataset.setter
    def dataset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "dataset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataset", value)

    @builtins.property
    @jsii.member(jsii_name="destinationConf")
    def destination_conf(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationConf"))

    @destination_conf.setter
    def destination_conf(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "destination_conf").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConf", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="logpullOptions")
    def logpull_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logpullOptions"))

    @logpull_options.setter
    def logpull_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "logpull_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logpullOptions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ownershipChallenge")
    def ownership_challenge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownershipChallenge"))

    @ownership_challenge.setter
    def ownership_challenge(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "ownership_challenge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownershipChallenge", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogpushJob, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.logpushJob.LogpushJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset": "dataset",
        "destination_conf": "destinationConf",
        "account_id": "accountId",
        "enabled": "enabled",
        "filter": "filter",
        "frequency": "frequency",
        "id": "id",
        "kind": "kind",
        "logpull_options": "logpullOptions",
        "name": "name",
        "ownership_challenge": "ownershipChallenge",
        "zone_id": "zoneId",
    },
)
class LogpushJobConfig(cdktf.TerraformMetaArguments):
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
        dataset: builtins.str,
        destination_conf: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filter: typing.Optional[builtins.str] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        logpull_options: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        ownership_challenge: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See `Logpush destination documentation <https://developers.cloudflare.com/logs/reference/logpush-api-configuration#destination>`_. Available values: ``firewall_events``, ``http_requests``, ``spectrum_events``, ``nel_reports``, ``audit_logs``, ``gateway_dns``, ``gateway_http``, ``gateway_network``, ``dns_logs``, ``network_analytics_logs``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#dataset LogpushJob#dataset}
        :param destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See `Logpush destination documentation <https://developers.cloudflare.com/logs/reference/logpush-api-configuration#destination>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#destination_conf LogpushJob#destination_conf}
        :param account_id: The account identifier to target for the resource. Must provide only one of ``account_id``, ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#account_id LogpushJob#account_id}
        :param enabled: Whether to enable the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#enabled LogpushJob#enabled}
        :param filter: Use filters to select the events to include and/or remove from your logs. For more information, refer to `Filters <https://developers.cloudflare.com/logs/reference/logpush-api-configuration/filters/>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#filter LogpushJob#filter}
        :param frequency: A higher frequency will result in logs being pushed on faster with smaller files. ``low`` frequency will push logs less often with larger files. Available values: ``high``, ``low``. Defaults to ``high``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#frequency LogpushJob#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#id LogpushJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kind: The kind of logpush job to create. Available values: ``edge``, ``instant-logs``, ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#kind LogpushJob#kind}
        :param logpull_options: Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See `Logpull options documentation <https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#logpull_options LogpushJob#logpull_options}
        :param name: The name of the logpush job to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#name LogpushJob#name}
        :param ownership_challenge: Ownership challenge token to prove destination ownership, required when destination is Amazon S3, Google Cloud Storage, Microsoft Azure or Sumo Logic. See `Developer documentation <https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#ownership_challenge LogpushJob#ownership_challenge}
        :param zone_id: The zone identifier to target for the resource. Must provide only one of ``account_id``, ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#zone_id LogpushJob#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LogpushJobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument destination_conf", value=destination_conf, expected_type=type_hints["destination_conf"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument logpull_options", value=logpull_options, expected_type=type_hints["logpull_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ownership_challenge", value=ownership_challenge, expected_type=type_hints["ownership_challenge"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset": dataset,
            "destination_conf": destination_conf,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if enabled is not None:
            self._values["enabled"] = enabled
        if filter is not None:
            self._values["filter"] = filter
        if frequency is not None:
            self._values["frequency"] = frequency
        if id is not None:
            self._values["id"] = id
        if kind is not None:
            self._values["kind"] = kind
        if logpull_options is not None:
            self._values["logpull_options"] = logpull_options
        if name is not None:
            self._values["name"] = name
        if ownership_challenge is not None:
            self._values["ownership_challenge"] = ownership_challenge
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
    def dataset(self) -> builtins.str:
        '''Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

        Additional configuration parameters supported by the destination may be included. See `Logpush destination documentation <https://developers.cloudflare.com/logs/reference/logpush-api-configuration#destination>`_. Available values: ``firewall_events``, ``http_requests``, ``spectrum_events``, ``nel_reports``, ``audit_logs``, ``gateway_dns``, ``gateway_http``, ``gateway_network``, ``dns_logs``, ``network_analytics_logs``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#dataset LogpushJob#dataset}
        '''
        result = self._values.get("dataset")
        assert result is not None, "Required property 'dataset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_conf(self) -> builtins.str:
        '''Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

        Additional configuration parameters supported by the destination may be included. See `Logpush destination documentation <https://developers.cloudflare.com/logs/reference/logpush-api-configuration#destination>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#destination_conf LogpushJob#destination_conf}
        '''
        result = self._values.get("destination_conf")
        assert result is not None, "Required property 'destination_conf' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. Must provide only one of ``account_id``, ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#account_id LogpushJob#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#enabled LogpushJob#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''Use filters to select the events to include and/or remove from your logs. For more information, refer to `Filters <https://developers.cloudflare.com/logs/reference/logpush-api-configuration/filters/>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#filter LogpushJob#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''A higher frequency will result in logs being pushed on faster with smaller files.

        ``low`` frequency will push logs less often with larger files. Available values: ``high``, ``low``. Defaults to ``high``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#frequency LogpushJob#frequency}
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#id LogpushJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The kind of logpush job to create. Available values: ``edge``, ``instant-logs``, ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#kind LogpushJob#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logpull_options(self) -> typing.Optional[builtins.str]:
        '''Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See `Logpull options documentation <https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#logpull_options LogpushJob#logpull_options}
        '''
        result = self._values.get("logpull_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the logpush job to create.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#name LogpushJob#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ownership_challenge(self) -> typing.Optional[builtins.str]:
        '''Ownership challenge token to prove destination ownership, required when destination is Amazon S3, Google Cloud Storage, Microsoft Azure or Sumo Logic.

        See `Developer documentation <https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#ownership_challenge LogpushJob#ownership_challenge}
        '''
        result = self._values.get("ownership_challenge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource. Must provide only one of ``account_id``, ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/logpush_job#zone_id LogpushJob#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogpushJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LogpushJob",
    "LogpushJobConfig",
]

publication.publish()
