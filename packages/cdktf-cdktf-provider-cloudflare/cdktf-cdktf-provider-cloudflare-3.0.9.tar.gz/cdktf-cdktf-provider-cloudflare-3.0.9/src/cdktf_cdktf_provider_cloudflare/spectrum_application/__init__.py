'''
# `cloudflare_spectrum_application`

Refer to the Terraform Registory for docs: [`cloudflare_spectrum_application`](https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application).
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


class SpectrumApplication(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application cloudflare_spectrum_application}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dns: typing.Union["SpectrumApplicationDns", typing.Dict[str, typing.Any]],
        protocol: builtins.str,
        zone_id: builtins.str,
        argo_smart_routing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_ip_connectivity: typing.Optional[builtins.str] = None,
        edge_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_firewall: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        origin_direct: typing.Optional[typing.Sequence[builtins.str]] = None,
        origin_dns: typing.Optional[typing.Union["SpectrumApplicationOriginDns", typing.Dict[str, typing.Any]]] = None,
        origin_port: typing.Optional[jsii.Number] = None,
        origin_port_range: typing.Optional[typing.Union["SpectrumApplicationOriginPortRange", typing.Dict[str, typing.Any]]] = None,
        proxy_protocol: typing.Optional[builtins.str] = None,
        tls: typing.Optional[builtins.str] = None,
        traffic_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application cloudflare_spectrum_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#dns SpectrumApplication#dns}
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#protocol SpectrumApplication#protocol}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#zone_id SpectrumApplication#zone_id}
        :param argo_smart_routing: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#argo_smart_routing SpectrumApplication#argo_smart_routing}
        :param edge_ip_connectivity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#edge_ip_connectivity SpectrumApplication#edge_ip_connectivity}.
        :param edge_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#edge_ips SpectrumApplication#edge_ips}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#id SpectrumApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_firewall: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#ip_firewall SpectrumApplication#ip_firewall}
        :param origin_direct: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_direct SpectrumApplication#origin_direct}.
        :param origin_dns: origin_dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_dns SpectrumApplication#origin_dns}
        :param origin_port: Conflicts with ``origin_port_range``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_port SpectrumApplication#origin_port}
        :param origin_port_range: origin_port_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_port_range SpectrumApplication#origin_port_range}
        :param proxy_protocol: Defaults to ``off``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#proxy_protocol SpectrumApplication#proxy_protocol}
        :param tls: Defaults to ``off``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#tls SpectrumApplication#tls}
        :param traffic_type: Defaults to ``direct``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#traffic_type SpectrumApplication#traffic_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpectrumApplication.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SpectrumApplicationConfig(
            dns=dns,
            protocol=protocol,
            zone_id=zone_id,
            argo_smart_routing=argo_smart_routing,
            edge_ip_connectivity=edge_ip_connectivity,
            edge_ips=edge_ips,
            id=id,
            ip_firewall=ip_firewall,
            origin_direct=origin_direct,
            origin_dns=origin_dns,
            origin_port=origin_port,
            origin_port_range=origin_port_range,
            proxy_protocol=proxy_protocol,
            tls=tls,
            traffic_type=traffic_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDns")
    def put_dns(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#name SpectrumApplication#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#type SpectrumApplication#type}.
        '''
        value = SpectrumApplicationDns(name=name, type=type)

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putOriginDns")
    def put_origin_dns(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#name SpectrumApplication#name}.
        '''
        value = SpectrumApplicationOriginDns(name=name)

        return typing.cast(None, jsii.invoke(self, "putOriginDns", [value]))

    @jsii.member(jsii_name="putOriginPortRange")
    def put_origin_port_range(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#end SpectrumApplication#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#start SpectrumApplication#start}.
        '''
        value = SpectrumApplicationOriginPortRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putOriginPortRange", [value]))

    @jsii.member(jsii_name="resetArgoSmartRouting")
    def reset_argo_smart_routing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgoSmartRouting", []))

    @jsii.member(jsii_name="resetEdgeIpConnectivity")
    def reset_edge_ip_connectivity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeIpConnectivity", []))

    @jsii.member(jsii_name="resetEdgeIps")
    def reset_edge_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeIps", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpFirewall")
    def reset_ip_firewall(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpFirewall", []))

    @jsii.member(jsii_name="resetOriginDirect")
    def reset_origin_direct(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginDirect", []))

    @jsii.member(jsii_name="resetOriginDns")
    def reset_origin_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginDns", []))

    @jsii.member(jsii_name="resetOriginPort")
    def reset_origin_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginPort", []))

    @jsii.member(jsii_name="resetOriginPortRange")
    def reset_origin_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginPortRange", []))

    @jsii.member(jsii_name="resetProxyProtocol")
    def reset_proxy_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyProtocol", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetTrafficType")
    def reset_traffic_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> "SpectrumApplicationDnsOutputReference":
        return typing.cast("SpectrumApplicationDnsOutputReference", jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="originDns")
    def origin_dns(self) -> "SpectrumApplicationOriginDnsOutputReference":
        return typing.cast("SpectrumApplicationOriginDnsOutputReference", jsii.get(self, "originDns"))

    @builtins.property
    @jsii.member(jsii_name="originPortRange")
    def origin_port_range(self) -> "SpectrumApplicationOriginPortRangeOutputReference":
        return typing.cast("SpectrumApplicationOriginPortRangeOutputReference", jsii.get(self, "originPortRange"))

    @builtins.property
    @jsii.member(jsii_name="argoSmartRoutingInput")
    def argo_smart_routing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "argoSmartRoutingInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional["SpectrumApplicationDns"]:
        return typing.cast(typing.Optional["SpectrumApplicationDns"], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeIpConnectivityInput")
    def edge_ip_connectivity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeIpConnectivityInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeIpsInput")
    def edge_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "edgeIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipFirewallInput")
    def ip_firewall_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipFirewallInput"))

    @builtins.property
    @jsii.member(jsii_name="originDirectInput")
    def origin_direct_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "originDirectInput"))

    @builtins.property
    @jsii.member(jsii_name="originDnsInput")
    def origin_dns_input(self) -> typing.Optional["SpectrumApplicationOriginDns"]:
        return typing.cast(typing.Optional["SpectrumApplicationOriginDns"], jsii.get(self, "originDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="originPortInput")
    def origin_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "originPortInput"))

    @builtins.property
    @jsii.member(jsii_name="originPortRangeInput")
    def origin_port_range_input(
        self,
    ) -> typing.Optional["SpectrumApplicationOriginPortRange"]:
        return typing.cast(typing.Optional["SpectrumApplicationOriginPortRange"], jsii.get(self, "originPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyProtocolInput")
    def proxy_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficTypeInput")
    def traffic_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trafficTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="argoSmartRouting")
    def argo_smart_routing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "argoSmartRouting"))

    @argo_smart_routing.setter
    def argo_smart_routing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "argo_smart_routing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "argoSmartRouting", value)

    @builtins.property
    @jsii.member(jsii_name="edgeIpConnectivity")
    def edge_ip_connectivity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeIpConnectivity"))

    @edge_ip_connectivity.setter
    def edge_ip_connectivity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "edge_ip_connectivity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeIpConnectivity", value)

    @builtins.property
    @jsii.member(jsii_name="edgeIps")
    def edge_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "edgeIps"))

    @edge_ips.setter
    def edge_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "edge_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeIps", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipFirewall")
    def ip_firewall(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipFirewall"))

    @ip_firewall.setter
    def ip_firewall(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "ip_firewall").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipFirewall", value)

    @builtins.property
    @jsii.member(jsii_name="originDirect")
    def origin_direct(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "originDirect"))

    @origin_direct.setter
    def origin_direct(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "origin_direct").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originDirect", value)

    @builtins.property
    @jsii.member(jsii_name="originPort")
    def origin_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "originPort"))

    @origin_port.setter
    def origin_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "origin_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originPort", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="proxyProtocol")
    def proxy_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyProtocol"))

    @proxy_protocol.setter
    def proxy_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "proxy_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="trafficType")
    def traffic_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trafficType"))

    @traffic_type.setter
    def traffic_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "traffic_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficType", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplication, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dns": "dns",
        "protocol": "protocol",
        "zone_id": "zoneId",
        "argo_smart_routing": "argoSmartRouting",
        "edge_ip_connectivity": "edgeIpConnectivity",
        "edge_ips": "edgeIps",
        "id": "id",
        "ip_firewall": "ipFirewall",
        "origin_direct": "originDirect",
        "origin_dns": "originDns",
        "origin_port": "originPort",
        "origin_port_range": "originPortRange",
        "proxy_protocol": "proxyProtocol",
        "tls": "tls",
        "traffic_type": "trafficType",
    },
)
class SpectrumApplicationConfig(cdktf.TerraformMetaArguments):
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
        dns: typing.Union["SpectrumApplicationDns", typing.Dict[str, typing.Any]],
        protocol: builtins.str,
        zone_id: builtins.str,
        argo_smart_routing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_ip_connectivity: typing.Optional[builtins.str] = None,
        edge_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_firewall: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        origin_direct: typing.Optional[typing.Sequence[builtins.str]] = None,
        origin_dns: typing.Optional[typing.Union["SpectrumApplicationOriginDns", typing.Dict[str, typing.Any]]] = None,
        origin_port: typing.Optional[jsii.Number] = None,
        origin_port_range: typing.Optional[typing.Union["SpectrumApplicationOriginPortRange", typing.Dict[str, typing.Any]]] = None,
        proxy_protocol: typing.Optional[builtins.str] = None,
        tls: typing.Optional[builtins.str] = None,
        traffic_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#dns SpectrumApplication#dns}
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#protocol SpectrumApplication#protocol}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#zone_id SpectrumApplication#zone_id}
        :param argo_smart_routing: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#argo_smart_routing SpectrumApplication#argo_smart_routing}
        :param edge_ip_connectivity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#edge_ip_connectivity SpectrumApplication#edge_ip_connectivity}.
        :param edge_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#edge_ips SpectrumApplication#edge_ips}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#id SpectrumApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_firewall: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#ip_firewall SpectrumApplication#ip_firewall}
        :param origin_direct: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_direct SpectrumApplication#origin_direct}.
        :param origin_dns: origin_dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_dns SpectrumApplication#origin_dns}
        :param origin_port: Conflicts with ``origin_port_range``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_port SpectrumApplication#origin_port}
        :param origin_port_range: origin_port_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_port_range SpectrumApplication#origin_port_range}
        :param proxy_protocol: Defaults to ``off``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#proxy_protocol SpectrumApplication#proxy_protocol}
        :param tls: Defaults to ``off``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#tls SpectrumApplication#tls}
        :param traffic_type: Defaults to ``direct``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#traffic_type SpectrumApplication#traffic_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dns, dict):
            dns = SpectrumApplicationDns(**dns)
        if isinstance(origin_dns, dict):
            origin_dns = SpectrumApplicationOriginDns(**origin_dns)
        if isinstance(origin_port_range, dict):
            origin_port_range = SpectrumApplicationOriginPortRange(**origin_port_range)
        if __debug__:
            type_hints = typing.get_type_hints(SpectrumApplicationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument argo_smart_routing", value=argo_smart_routing, expected_type=type_hints["argo_smart_routing"])
            check_type(argname="argument edge_ip_connectivity", value=edge_ip_connectivity, expected_type=type_hints["edge_ip_connectivity"])
            check_type(argname="argument edge_ips", value=edge_ips, expected_type=type_hints["edge_ips"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_firewall", value=ip_firewall, expected_type=type_hints["ip_firewall"])
            check_type(argname="argument origin_direct", value=origin_direct, expected_type=type_hints["origin_direct"])
            check_type(argname="argument origin_dns", value=origin_dns, expected_type=type_hints["origin_dns"])
            check_type(argname="argument origin_port", value=origin_port, expected_type=type_hints["origin_port"])
            check_type(argname="argument origin_port_range", value=origin_port_range, expected_type=type_hints["origin_port_range"])
            check_type(argname="argument proxy_protocol", value=proxy_protocol, expected_type=type_hints["proxy_protocol"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns": dns,
            "protocol": protocol,
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
        if argo_smart_routing is not None:
            self._values["argo_smart_routing"] = argo_smart_routing
        if edge_ip_connectivity is not None:
            self._values["edge_ip_connectivity"] = edge_ip_connectivity
        if edge_ips is not None:
            self._values["edge_ips"] = edge_ips
        if id is not None:
            self._values["id"] = id
        if ip_firewall is not None:
            self._values["ip_firewall"] = ip_firewall
        if origin_direct is not None:
            self._values["origin_direct"] = origin_direct
        if origin_dns is not None:
            self._values["origin_dns"] = origin_dns
        if origin_port is not None:
            self._values["origin_port"] = origin_port
        if origin_port_range is not None:
            self._values["origin_port_range"] = origin_port_range
        if proxy_protocol is not None:
            self._values["proxy_protocol"] = proxy_protocol
        if tls is not None:
            self._values["tls"] = tls
        if traffic_type is not None:
            self._values["traffic_type"] = traffic_type

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
    def dns(self) -> "SpectrumApplicationDns":
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#dns SpectrumApplication#dns}
        '''
        result = self._values.get("dns")
        assert result is not None, "Required property 'dns' is missing"
        return typing.cast("SpectrumApplicationDns", result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#protocol SpectrumApplication#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#zone_id SpectrumApplication#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def argo_smart_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#argo_smart_routing SpectrumApplication#argo_smart_routing}
        '''
        result = self._values.get("argo_smart_routing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def edge_ip_connectivity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#edge_ip_connectivity SpectrumApplication#edge_ip_connectivity}.'''
        result = self._values.get("edge_ip_connectivity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#edge_ips SpectrumApplication#edge_ips}.'''
        result = self._values.get("edge_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#id SpectrumApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_firewall(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#ip_firewall SpectrumApplication#ip_firewall}
        '''
        result = self._values.get("ip_firewall")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def origin_direct(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_direct SpectrumApplication#origin_direct}.'''
        result = self._values.get("origin_direct")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def origin_dns(self) -> typing.Optional["SpectrumApplicationOriginDns"]:
        '''origin_dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_dns SpectrumApplication#origin_dns}
        '''
        result = self._values.get("origin_dns")
        return typing.cast(typing.Optional["SpectrumApplicationOriginDns"], result)

    @builtins.property
    def origin_port(self) -> typing.Optional[jsii.Number]:
        '''Conflicts with ``origin_port_range``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_port SpectrumApplication#origin_port}
        '''
        result = self._values.get("origin_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def origin_port_range(
        self,
    ) -> typing.Optional["SpectrumApplicationOriginPortRange"]:
        '''origin_port_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#origin_port_range SpectrumApplication#origin_port_range}
        '''
        result = self._values.get("origin_port_range")
        return typing.cast(typing.Optional["SpectrumApplicationOriginPortRange"], result)

    @builtins.property
    def proxy_protocol(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``off``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#proxy_protocol SpectrumApplication#proxy_protocol}
        '''
        result = self._values.get("proxy_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``off``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#tls SpectrumApplication#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_type(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``direct``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#traffic_type SpectrumApplication#traffic_type}
        '''
        result = self._values.get("traffic_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpectrumApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationDns",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class SpectrumApplicationDns:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#name SpectrumApplication#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#type SpectrumApplication#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpectrumApplicationDns.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#name SpectrumApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#type SpectrumApplication#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpectrumApplicationDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpectrumApplicationDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationDnsOutputReference",
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
            type_hints = typing.get_type_hints(SpectrumApplicationDnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationDnsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationDnsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpectrumApplicationDns]:
        return typing.cast(typing.Optional[SpectrumApplicationDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SpectrumApplicationDns]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationDnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationOriginDns",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class SpectrumApplicationOriginDns:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#name SpectrumApplication#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpectrumApplicationOriginDns.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#name SpectrumApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpectrumApplicationOriginDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpectrumApplicationOriginDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationOriginDnsOutputReference",
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
            type_hints = typing.get_type_hints(SpectrumApplicationOriginDnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationOriginDnsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpectrumApplicationOriginDns]:
        return typing.cast(typing.Optional[SpectrumApplicationOriginDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpectrumApplicationOriginDns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationOriginDnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationOriginPortRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class SpectrumApplicationOriginPortRange:
    def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#end SpectrumApplication#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#start SpectrumApplication#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SpectrumApplicationOriginPortRange.__init__)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#end SpectrumApplication#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/spectrum_application#start SpectrumApplication#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpectrumApplicationOriginPortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SpectrumApplicationOriginPortRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.spectrumApplication.SpectrumApplicationOriginPortRangeOutputReference",
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
            type_hints = typing.get_type_hints(SpectrumApplicationOriginPortRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationOriginPortRangeOutputReference, "end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationOriginPortRangeOutputReference, "start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SpectrumApplicationOriginPortRange]:
        return typing.cast(typing.Optional[SpectrumApplicationOriginPortRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SpectrumApplicationOriginPortRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SpectrumApplicationOriginPortRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SpectrumApplication",
    "SpectrumApplicationConfig",
    "SpectrumApplicationDns",
    "SpectrumApplicationDnsOutputReference",
    "SpectrumApplicationOriginDns",
    "SpectrumApplicationOriginDnsOutputReference",
    "SpectrumApplicationOriginPortRange",
    "SpectrumApplicationOriginPortRangeOutputReference",
]

publication.publish()
