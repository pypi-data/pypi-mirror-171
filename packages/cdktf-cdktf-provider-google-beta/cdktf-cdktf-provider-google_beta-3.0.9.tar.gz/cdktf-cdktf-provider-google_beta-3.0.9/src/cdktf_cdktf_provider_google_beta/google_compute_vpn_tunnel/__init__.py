'''
# `google_compute_vpn_tunnel`

Refer to the Terraform Registory for docs: [`google_compute_vpn_tunnel`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel).
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


class GoogleComputeVpnTunnel(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeVpnTunnel.GoogleComputeVpnTunnel",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel google_compute_vpn_tunnel}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        shared_secret: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ike_version: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local_traffic_selector: typing.Optional[typing.Sequence[builtins.str]] = None,
        peer_external_gateway: typing.Optional[builtins.str] = None,
        peer_external_gateway_interface: typing.Optional[jsii.Number] = None,
        peer_gcp_gateway: typing.Optional[builtins.str] = None,
        peer_ip: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        remote_traffic_selector: typing.Optional[typing.Sequence[builtins.str]] = None,
        router: typing.Optional[builtins.str] = None,
        target_vpn_gateway: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeVpnTunnelTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_gateway: typing.Optional[builtins.str] = None,
        vpn_gateway_interface: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel google_compute_vpn_tunnel} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#name GoogleComputeVpnTunnel#name}
        :param shared_secret: Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#shared_secret GoogleComputeVpnTunnel#shared_secret}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#description GoogleComputeVpnTunnel#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#id GoogleComputeVpnTunnel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ike_version: IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway. Acceptable IKE versions are 1 or 2. Default version is 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#ike_version GoogleComputeVpnTunnel#ike_version}
        :param labels: Labels to apply to this VpnTunnel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#labels GoogleComputeVpnTunnel#labels}
        :param local_traffic_selector: Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example '192.168.0.0/16'. The ranges should be disjoint. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#local_traffic_selector GoogleComputeVpnTunnel#local_traffic_selector}
        :param peer_external_gateway: URL of the peer side external VPN gateway to which this VPN tunnel is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_external_gateway GoogleComputeVpnTunnel#peer_external_gateway}
        :param peer_external_gateway_interface: The interface ID of the external VPN gateway to which this VPN tunnel is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_external_gateway_interface GoogleComputeVpnTunnel#peer_external_gateway_interface}
        :param peer_gcp_gateway: URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected. If provided, the VPN tunnel will automatically use the same vpn_gateway_interface ID in the peer GCP VPN gateway. This field must reference a 'google_compute_ha_vpn_gateway' resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_gcp_gateway GoogleComputeVpnTunnel#peer_gcp_gateway}
        :param peer_ip: IP address of the peer VPN gateway. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_ip GoogleComputeVpnTunnel#peer_ip}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#project GoogleComputeVpnTunnel#project}.
        :param region: The region where the tunnel is located. If unset, is set to the region of 'target_vpn_gateway'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#region GoogleComputeVpnTunnel#region}
        :param remote_traffic_selector: Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example '192.168.0.0/16'. The ranges should be disjoint. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#remote_traffic_selector GoogleComputeVpnTunnel#remote_traffic_selector}
        :param router: URL of router resource to be used for dynamic routing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#router GoogleComputeVpnTunnel#router}
        :param target_vpn_gateway: URL of the Target VPN gateway with which this VPN tunnel is associated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#target_vpn_gateway GoogleComputeVpnTunnel#target_vpn_gateway}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#timeouts GoogleComputeVpnTunnel#timeouts}
        :param vpn_gateway: URL of the VPN gateway with which this VPN tunnel is associated. This must be used if a High Availability VPN gateway resource is created. This field must reference a 'google_compute_ha_vpn_gateway' resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#vpn_gateway GoogleComputeVpnTunnel#vpn_gateway}
        :param vpn_gateway_interface: The interface ID of the VPN gateway with which this VPN tunnel is associated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#vpn_gateway_interface GoogleComputeVpnTunnel#vpn_gateway_interface}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeVpnTunnel.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeVpnTunnelConfig(
            name=name,
            shared_secret=shared_secret,
            description=description,
            id=id,
            ike_version=ike_version,
            labels=labels,
            local_traffic_selector=local_traffic_selector,
            peer_external_gateway=peer_external_gateway,
            peer_external_gateway_interface=peer_external_gateway_interface,
            peer_gcp_gateway=peer_gcp_gateway,
            peer_ip=peer_ip,
            project=project,
            region=region,
            remote_traffic_selector=remote_traffic_selector,
            router=router,
            target_vpn_gateway=target_vpn_gateway,
            timeouts=timeouts,
            vpn_gateway=vpn_gateway,
            vpn_gateway_interface=vpn_gateway_interface,
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
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#create GoogleComputeVpnTunnel#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#delete GoogleComputeVpnTunnel#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#update GoogleComputeVpnTunnel#update}.
        '''
        value = GoogleComputeVpnTunnelTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIkeVersion")
    def reset_ike_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIkeVersion", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLocalTrafficSelector")
    def reset_local_traffic_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalTrafficSelector", []))

    @jsii.member(jsii_name="resetPeerExternalGateway")
    def reset_peer_external_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerExternalGateway", []))

    @jsii.member(jsii_name="resetPeerExternalGatewayInterface")
    def reset_peer_external_gateway_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerExternalGatewayInterface", []))

    @jsii.member(jsii_name="resetPeerGcpGateway")
    def reset_peer_gcp_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerGcpGateway", []))

    @jsii.member(jsii_name="resetPeerIp")
    def reset_peer_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerIp", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRemoteTrafficSelector")
    def reset_remote_traffic_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteTrafficSelector", []))

    @jsii.member(jsii_name="resetRouter")
    def reset_router(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouter", []))

    @jsii.member(jsii_name="resetTargetVpnGateway")
    def reset_target_vpn_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetVpnGateway", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpnGateway")
    def reset_vpn_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnGateway", []))

    @jsii.member(jsii_name="resetVpnGatewayInterface")
    def reset_vpn_gateway_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnGatewayInterface", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="detailedStatus")
    def detailed_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detailedStatus"))

    @builtins.property
    @jsii.member(jsii_name="labelFingerprint")
    def label_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="sharedSecretHash")
    def shared_secret_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedSecretHash"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeVpnTunnelTimeoutsOutputReference":
        return typing.cast("GoogleComputeVpnTunnelTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tunnelId")
    def tunnel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tunnelId"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeVersionInput")
    def ike_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ikeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="localTrafficSelectorInput")
    def local_traffic_selector_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localTrafficSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peerExternalGatewayInput")
    def peer_external_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerExternalGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="peerExternalGatewayInterfaceInput")
    def peer_external_gateway_interface_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "peerExternalGatewayInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="peerGcpGatewayInput")
    def peer_gcp_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerGcpGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="peerIpInput")
    def peer_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerIpInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteTrafficSelectorInput")
    def remote_traffic_selector_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "remoteTrafficSelectorInput"))

    @builtins.property
    @jsii.member(jsii_name="routerInput")
    def router_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routerInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedSecretInput")
    def shared_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="targetVpnGatewayInput")
    def target_vpn_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetVpnGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeVpnTunnelTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeVpnTunnelTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayInput")
    def vpn_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayInterfaceInput")
    def vpn_gateway_interface_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vpnGatewayInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ikeVersion")
    def ike_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ikeVersion"))

    @ike_version.setter
    def ike_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "ike_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="localTrafficSelector")
    def local_traffic_selector(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localTrafficSelector"))

    @local_traffic_selector.setter
    def local_traffic_selector(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "local_traffic_selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localTrafficSelector", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="peerExternalGateway")
    def peer_external_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerExternalGateway"))

    @peer_external_gateway.setter
    def peer_external_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "peer_external_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerExternalGateway", value)

    @builtins.property
    @jsii.member(jsii_name="peerExternalGatewayInterface")
    def peer_external_gateway_interface(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "peerExternalGatewayInterface"))

    @peer_external_gateway_interface.setter
    def peer_external_gateway_interface(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "peer_external_gateway_interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerExternalGatewayInterface", value)

    @builtins.property
    @jsii.member(jsii_name="peerGcpGateway")
    def peer_gcp_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerGcpGateway"))

    @peer_gcp_gateway.setter
    def peer_gcp_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "peer_gcp_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerGcpGateway", value)

    @builtins.property
    @jsii.member(jsii_name="peerIp")
    def peer_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerIp"))

    @peer_ip.setter
    def peer_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "peer_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerIp", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="remoteTrafficSelector")
    def remote_traffic_selector(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "remoteTrafficSelector"))

    @remote_traffic_selector.setter
    def remote_traffic_selector(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "remote_traffic_selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteTrafficSelector", value)

    @builtins.property
    @jsii.member(jsii_name="router")
    def router(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "router"))

    @router.setter
    def router(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "router").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "router", value)

    @builtins.property
    @jsii.member(jsii_name="sharedSecret")
    def shared_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedSecret"))

    @shared_secret.setter
    def shared_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "shared_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedSecret", value)

    @builtins.property
    @jsii.member(jsii_name="targetVpnGateway")
    def target_vpn_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetVpnGateway"))

    @target_vpn_gateway.setter
    def target_vpn_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "target_vpn_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetVpnGateway", value)

    @builtins.property
    @jsii.member(jsii_name="vpnGateway")
    def vpn_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnGateway"))

    @vpn_gateway.setter
    def vpn_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "vpn_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGateway", value)

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayInterface")
    def vpn_gateway_interface(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vpnGatewayInterface"))

    @vpn_gateway_interface.setter
    def vpn_gateway_interface(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnel, "vpn_gateway_interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayInterface", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeVpnTunnel.GoogleComputeVpnTunnelConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "shared_secret": "sharedSecret",
        "description": "description",
        "id": "id",
        "ike_version": "ikeVersion",
        "labels": "labels",
        "local_traffic_selector": "localTrafficSelector",
        "peer_external_gateway": "peerExternalGateway",
        "peer_external_gateway_interface": "peerExternalGatewayInterface",
        "peer_gcp_gateway": "peerGcpGateway",
        "peer_ip": "peerIp",
        "project": "project",
        "region": "region",
        "remote_traffic_selector": "remoteTrafficSelector",
        "router": "router",
        "target_vpn_gateway": "targetVpnGateway",
        "timeouts": "timeouts",
        "vpn_gateway": "vpnGateway",
        "vpn_gateway_interface": "vpnGatewayInterface",
    },
)
class GoogleComputeVpnTunnelConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        shared_secret: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ike_version: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local_traffic_selector: typing.Optional[typing.Sequence[builtins.str]] = None,
        peer_external_gateway: typing.Optional[builtins.str] = None,
        peer_external_gateway_interface: typing.Optional[jsii.Number] = None,
        peer_gcp_gateway: typing.Optional[builtins.str] = None,
        peer_ip: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        remote_traffic_selector: typing.Optional[typing.Sequence[builtins.str]] = None,
        router: typing.Optional[builtins.str] = None,
        target_vpn_gateway: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeVpnTunnelTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_gateway: typing.Optional[builtins.str] = None,
        vpn_gateway_interface: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#name GoogleComputeVpnTunnel#name}
        :param shared_secret: Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#shared_secret GoogleComputeVpnTunnel#shared_secret}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#description GoogleComputeVpnTunnel#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#id GoogleComputeVpnTunnel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ike_version: IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway. Acceptable IKE versions are 1 or 2. Default version is 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#ike_version GoogleComputeVpnTunnel#ike_version}
        :param labels: Labels to apply to this VpnTunnel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#labels GoogleComputeVpnTunnel#labels}
        :param local_traffic_selector: Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example '192.168.0.0/16'. The ranges should be disjoint. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#local_traffic_selector GoogleComputeVpnTunnel#local_traffic_selector}
        :param peer_external_gateway: URL of the peer side external VPN gateway to which this VPN tunnel is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_external_gateway GoogleComputeVpnTunnel#peer_external_gateway}
        :param peer_external_gateway_interface: The interface ID of the external VPN gateway to which this VPN tunnel is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_external_gateway_interface GoogleComputeVpnTunnel#peer_external_gateway_interface}
        :param peer_gcp_gateway: URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected. If provided, the VPN tunnel will automatically use the same vpn_gateway_interface ID in the peer GCP VPN gateway. This field must reference a 'google_compute_ha_vpn_gateway' resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_gcp_gateway GoogleComputeVpnTunnel#peer_gcp_gateway}
        :param peer_ip: IP address of the peer VPN gateway. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_ip GoogleComputeVpnTunnel#peer_ip}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#project GoogleComputeVpnTunnel#project}.
        :param region: The region where the tunnel is located. If unset, is set to the region of 'target_vpn_gateway'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#region GoogleComputeVpnTunnel#region}
        :param remote_traffic_selector: Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway. The value should be a CIDR formatted string, for example '192.168.0.0/16'. The ranges should be disjoint. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#remote_traffic_selector GoogleComputeVpnTunnel#remote_traffic_selector}
        :param router: URL of router resource to be used for dynamic routing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#router GoogleComputeVpnTunnel#router}
        :param target_vpn_gateway: URL of the Target VPN gateway with which this VPN tunnel is associated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#target_vpn_gateway GoogleComputeVpnTunnel#target_vpn_gateway}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#timeouts GoogleComputeVpnTunnel#timeouts}
        :param vpn_gateway: URL of the VPN gateway with which this VPN tunnel is associated. This must be used if a High Availability VPN gateway resource is created. This field must reference a 'google_compute_ha_vpn_gateway' resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#vpn_gateway GoogleComputeVpnTunnel#vpn_gateway}
        :param vpn_gateway_interface: The interface ID of the VPN gateway with which this VPN tunnel is associated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#vpn_gateway_interface GoogleComputeVpnTunnel#vpn_gateway_interface}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeVpnTunnelTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeVpnTunnelConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shared_secret", value=shared_secret, expected_type=type_hints["shared_secret"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ike_version", value=ike_version, expected_type=type_hints["ike_version"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument local_traffic_selector", value=local_traffic_selector, expected_type=type_hints["local_traffic_selector"])
            check_type(argname="argument peer_external_gateway", value=peer_external_gateway, expected_type=type_hints["peer_external_gateway"])
            check_type(argname="argument peer_external_gateway_interface", value=peer_external_gateway_interface, expected_type=type_hints["peer_external_gateway_interface"])
            check_type(argname="argument peer_gcp_gateway", value=peer_gcp_gateway, expected_type=type_hints["peer_gcp_gateway"])
            check_type(argname="argument peer_ip", value=peer_ip, expected_type=type_hints["peer_ip"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument remote_traffic_selector", value=remote_traffic_selector, expected_type=type_hints["remote_traffic_selector"])
            check_type(argname="argument router", value=router, expected_type=type_hints["router"])
            check_type(argname="argument target_vpn_gateway", value=target_vpn_gateway, expected_type=type_hints["target_vpn_gateway"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpn_gateway", value=vpn_gateway, expected_type=type_hints["vpn_gateway"])
            check_type(argname="argument vpn_gateway_interface", value=vpn_gateway_interface, expected_type=type_hints["vpn_gateway_interface"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "shared_secret": shared_secret,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if ike_version is not None:
            self._values["ike_version"] = ike_version
        if labels is not None:
            self._values["labels"] = labels
        if local_traffic_selector is not None:
            self._values["local_traffic_selector"] = local_traffic_selector
        if peer_external_gateway is not None:
            self._values["peer_external_gateway"] = peer_external_gateway
        if peer_external_gateway_interface is not None:
            self._values["peer_external_gateway_interface"] = peer_external_gateway_interface
        if peer_gcp_gateway is not None:
            self._values["peer_gcp_gateway"] = peer_gcp_gateway
        if peer_ip is not None:
            self._values["peer_ip"] = peer_ip
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if remote_traffic_selector is not None:
            self._values["remote_traffic_selector"] = remote_traffic_selector
        if router is not None:
            self._values["router"] = router
        if target_vpn_gateway is not None:
            self._values["target_vpn_gateway"] = target_vpn_gateway
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpn_gateway is not None:
            self._values["vpn_gateway"] = vpn_gateway
        if vpn_gateway_interface is not None:
            self._values["vpn_gateway_interface"] = vpn_gateway_interface

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
    def name(self) -> builtins.str:
        '''Name of the resource.

        The name must be 1-63 characters long, and
        comply with RFC1035. Specifically, the name must be 1-63
        characters long and match the regular expression
        '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character
        must be a lowercase letter, and all following characters must
        be a dash, lowercase letter, or digit,
        except the last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#name GoogleComputeVpnTunnel#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shared_secret(self) -> builtins.str:
        '''Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#shared_secret GoogleComputeVpnTunnel#shared_secret}
        '''
        result = self._values.get("shared_secret")
        assert result is not None, "Required property 'shared_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#description GoogleComputeVpnTunnel#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#id GoogleComputeVpnTunnel#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ike_version(self) -> typing.Optional[jsii.Number]:
        '''IKE protocol version to use when establishing the VPN tunnel with peer VPN gateway.

        Acceptable IKE versions are 1 or 2. Default version is 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#ike_version GoogleComputeVpnTunnel#ike_version}
        '''
        result = self._values.get("ike_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to this VpnTunnel.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#labels GoogleComputeVpnTunnel#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def local_traffic_selector(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Local traffic selector to use when establishing the VPN tunnel with peer VPN gateway.

        The value should be a CIDR formatted string,
        for example '192.168.0.0/16'. The ranges should be disjoint.
        Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#local_traffic_selector GoogleComputeVpnTunnel#local_traffic_selector}
        '''
        result = self._values.get("local_traffic_selector")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def peer_external_gateway(self) -> typing.Optional[builtins.str]:
        '''URL of the peer side external VPN gateway to which this VPN tunnel is connected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_external_gateway GoogleComputeVpnTunnel#peer_external_gateway}
        '''
        result = self._values.get("peer_external_gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_external_gateway_interface(self) -> typing.Optional[jsii.Number]:
        '''The interface ID of the external VPN gateway to which this VPN tunnel is connected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_external_gateway_interface GoogleComputeVpnTunnel#peer_external_gateway_interface}
        '''
        result = self._values.get("peer_external_gateway_interface")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def peer_gcp_gateway(self) -> typing.Optional[builtins.str]:
        '''URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected.

        If provided, the VPN tunnel will automatically use the same vpn_gateway_interface
        ID in the peer GCP VPN gateway.
        This field must reference a 'google_compute_ha_vpn_gateway' resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_gcp_gateway GoogleComputeVpnTunnel#peer_gcp_gateway}
        '''
        result = self._values.get("peer_gcp_gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_ip(self) -> typing.Optional[builtins.str]:
        '''IP address of the peer VPN gateway. Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#peer_ip GoogleComputeVpnTunnel#peer_ip}
        '''
        result = self._values.get("peer_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#project GoogleComputeVpnTunnel#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the tunnel is located. If unset, is set to the region of 'target_vpn_gateway'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#region GoogleComputeVpnTunnel#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_traffic_selector(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Remote traffic selector to use when establishing the VPN tunnel with peer VPN gateway.

        The value should be a CIDR formatted string,
        for example '192.168.0.0/16'. The ranges should be disjoint.
        Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#remote_traffic_selector GoogleComputeVpnTunnel#remote_traffic_selector}
        '''
        result = self._values.get("remote_traffic_selector")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def router(self) -> typing.Optional[builtins.str]:
        '''URL of router resource to be used for dynamic routing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#router GoogleComputeVpnTunnel#router}
        '''
        result = self._values.get("router")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_vpn_gateway(self) -> typing.Optional[builtins.str]:
        '''URL of the Target VPN gateway with which this VPN tunnel is associated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#target_vpn_gateway GoogleComputeVpnTunnel#target_vpn_gateway}
        '''
        result = self._values.get("target_vpn_gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeVpnTunnelTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#timeouts GoogleComputeVpnTunnel#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeVpnTunnelTimeouts"], result)

    @builtins.property
    def vpn_gateway(self) -> typing.Optional[builtins.str]:
        '''URL of the VPN gateway with which this VPN tunnel is associated.

        This must be used if a High Availability VPN gateway resource is created.
        This field must reference a 'google_compute_ha_vpn_gateway' resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#vpn_gateway GoogleComputeVpnTunnel#vpn_gateway}
        '''
        result = self._values.get("vpn_gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_gateway_interface(self) -> typing.Optional[jsii.Number]:
        '''The interface ID of the VPN gateway with which this VPN tunnel is associated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#vpn_gateway_interface GoogleComputeVpnTunnel#vpn_gateway_interface}
        '''
        result = self._values.get("vpn_gateway_interface")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeVpnTunnelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeVpnTunnel.GoogleComputeVpnTunnelTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeVpnTunnelTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#create GoogleComputeVpnTunnel#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#delete GoogleComputeVpnTunnel#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#update GoogleComputeVpnTunnel#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeVpnTunnelTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#create GoogleComputeVpnTunnel#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#delete GoogleComputeVpnTunnel#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_vpn_tunnel#update GoogleComputeVpnTunnel#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeVpnTunnelTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeVpnTunnelTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeVpnTunnel.GoogleComputeVpnTunnelTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeVpnTunnelTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnelTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnelTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnelTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeVpnTunnelTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeVpnTunnelTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeVpnTunnelTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeVpnTunnelTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeVpnTunnel",
    "GoogleComputeVpnTunnelConfig",
    "GoogleComputeVpnTunnelTimeouts",
    "GoogleComputeVpnTunnelTimeoutsOutputReference",
]

publication.publish()
