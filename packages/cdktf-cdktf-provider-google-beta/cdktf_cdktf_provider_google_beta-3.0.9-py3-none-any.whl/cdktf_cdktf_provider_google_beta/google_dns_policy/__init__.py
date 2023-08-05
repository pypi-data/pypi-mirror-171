'''
# `google_dns_policy`

Refer to the Terraform Registory for docs: [`google_dns_policy`](https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy).
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


class GoogleDnsPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy google_dns_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        alternative_name_server_config: typing.Optional[typing.Union["GoogleDnsPolicyAlternativeNameServerConfig", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_inbound_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        networks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsPolicyNetworks", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDnsPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy google_dns_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: User assigned name for this policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#name GoogleDnsPolicy#name}
        :param alternative_name_server_config: alternative_name_server_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#alternative_name_server_config GoogleDnsPolicy#alternative_name_server_config}
        :param description: A textual description field. Defaults to 'Managed by Terraform'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#description GoogleDnsPolicy#description}
        :param enable_inbound_forwarding: Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#enable_inbound_forwarding GoogleDnsPolicy#enable_inbound_forwarding}
        :param enable_logging: Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#enable_logging GoogleDnsPolicy#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#id GoogleDnsPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param networks: networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#networks GoogleDnsPolicy#networks}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#project GoogleDnsPolicy#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#timeouts GoogleDnsPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDnsPolicyConfig(
            name=name,
            alternative_name_server_config=alternative_name_server_config,
            description=description,
            enable_inbound_forwarding=enable_inbound_forwarding,
            enable_logging=enable_logging,
            id=id,
            networks=networks,
            project=project,
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

    @jsii.member(jsii_name="putAlternativeNameServerConfig")
    def put_alternative_name_server_config(
        self,
        *,
        target_name_servers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param target_name_servers: target_name_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#target_name_servers GoogleDnsPolicy#target_name_servers}
        '''
        value = GoogleDnsPolicyAlternativeNameServerConfig(
            target_name_servers=target_name_servers
        )

        return typing.cast(None, jsii.invoke(self, "putAlternativeNameServerConfig", [value]))

    @jsii.member(jsii_name="putNetworks")
    def put_networks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsPolicyNetworks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicy.put_networks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworks", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#create GoogleDnsPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#delete GoogleDnsPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#update GoogleDnsPolicy#update}.
        '''
        value = GoogleDnsPolicyTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlternativeNameServerConfig")
    def reset_alternative_name_server_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlternativeNameServerConfig", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnableInboundForwarding")
    def reset_enable_inbound_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableInboundForwarding", []))

    @jsii.member(jsii_name="resetEnableLogging")
    def reset_enable_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogging", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNetworks")
    def reset_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworks", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="alternativeNameServerConfig")
    def alternative_name_server_config(
        self,
    ) -> "GoogleDnsPolicyAlternativeNameServerConfigOutputReference":
        return typing.cast("GoogleDnsPolicyAlternativeNameServerConfigOutputReference", jsii.get(self, "alternativeNameServerConfig"))

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(self) -> "GoogleDnsPolicyNetworksList":
        return typing.cast("GoogleDnsPolicyNetworksList", jsii.get(self, "networks"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDnsPolicyTimeoutsOutputReference":
        return typing.cast("GoogleDnsPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alternativeNameServerConfigInput")
    def alternative_name_server_config_input(
        self,
    ) -> typing.Optional["GoogleDnsPolicyAlternativeNameServerConfig"]:
        return typing.cast(typing.Optional["GoogleDnsPolicyAlternativeNameServerConfig"], jsii.get(self, "alternativeNameServerConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInboundForwardingInput")
    def enable_inbound_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInboundForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networksInput")
    def networks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyNetworks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyNetworks"]]], jsii.get(self, "networksInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDnsPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDnsPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicy, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableInboundForwarding")
    def enable_inbound_forwarding(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableInboundForwarding"))

    @enable_inbound_forwarding.setter
    def enable_inbound_forwarding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicy, "enable_inbound_forwarding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableInboundForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="enableLogging")
    def enable_logging(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogging"))

    @enable_logging.setter
    def enable_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicy, "enable_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicy, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyAlternativeNameServerConfig",
    jsii_struct_bases=[],
    name_mapping={"target_name_servers": "targetNameServers"},
)
class GoogleDnsPolicyAlternativeNameServerConfig:
    def __init__(
        self,
        *,
        target_name_servers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param target_name_servers: target_name_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#target_name_servers GoogleDnsPolicy#target_name_servers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfig.__init__)
            check_type(argname="argument target_name_servers", value=target_name_servers, expected_type=type_hints["target_name_servers"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_name_servers": target_name_servers,
        }

    @builtins.property
    def target_name_servers(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers"]]:
        '''target_name_servers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#target_name_servers GoogleDnsPolicy#target_name_servers}
        '''
        result = self._values.get("target_name_servers")
        assert result is not None, "Required property 'target_name_servers' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsPolicyAlternativeNameServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsPolicyAlternativeNameServerConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyAlternativeNameServerConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetNameServers")
    def put_target_name_servers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfigOutputReference.put_target_name_servers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetNameServers", [value]))

    @builtins.property
    @jsii.member(jsii_name="targetNameServers")
    def target_name_servers(
        self,
    ) -> "GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList":
        return typing.cast("GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList", jsii.get(self, "targetNameServers"))

    @builtins.property
    @jsii.member(jsii_name="targetNameServersInput")
    def target_name_servers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers"]]], jsii.get(self, "targetNameServersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDnsPolicyAlternativeNameServerConfig]:
        return typing.cast(typing.Optional[GoogleDnsPolicyAlternativeNameServerConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsPolicyAlternativeNameServerConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers",
    jsii_struct_bases=[],
    name_mapping={"ipv4_address": "ipv4Address", "forwarding_path": "forwardingPath"},
)
class GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers:
    def __init__(
        self,
        *,
        ipv4_address: builtins.str,
        forwarding_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ipv4_address: IPv4 address to forward to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#ipv4_address GoogleDnsPolicy#ipv4_address}
        :param forwarding_path: Forwarding path for this TargetNameServer. If unset or 'default' Cloud DNS will make forwarding decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go to the Internet. When set to 'private', Cloud DNS will always send queries through VPC for this target Possible values: ["default", "private"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#forwarding_path GoogleDnsPolicy#forwarding_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers.__init__)
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument forwarding_path", value=forwarding_path, expected_type=type_hints["forwarding_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "ipv4_address": ipv4_address,
        }
        if forwarding_path is not None:
            self._values["forwarding_path"] = forwarding_path

    @builtins.property
    def ipv4_address(self) -> builtins.str:
        '''IPv4 address to forward to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#ipv4_address GoogleDnsPolicy#ipv4_address}
        '''
        result = self._values.get("ipv4_address")
        assert result is not None, "Required property 'ipv4_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def forwarding_path(self) -> typing.Optional[builtins.str]:
        '''Forwarding path for this TargetNameServer.

        If unset or 'default' Cloud DNS will make forwarding
        decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
        to the Internet. When set to 'private', Cloud DNS will always send queries through VPC for this target Possible values: ["default", "private"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#forwarding_path GoogleDnsPolicy#forwarding_path}
        '''
        result = self._values.get("forwarding_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList",
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
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetForwardingPath")
    def reset_forwarding_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingPath", []))

    @builtins.property
    @jsii.member(jsii_name="forwardingPathInput")
    def forwarding_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardingPathInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressInput")
    def ipv4_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingPath")
    def forwarding_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardingPath"))

    @forwarding_path.setter
    def forwarding_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference, "forwarding_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardingPath", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference, "ipv4_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyConfig",
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
        "alternative_name_server_config": "alternativeNameServerConfig",
        "description": "description",
        "enable_inbound_forwarding": "enableInboundForwarding",
        "enable_logging": "enableLogging",
        "id": "id",
        "networks": "networks",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleDnsPolicyConfig(cdktf.TerraformMetaArguments):
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
        alternative_name_server_config: typing.Optional[typing.Union[GoogleDnsPolicyAlternativeNameServerConfig, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_inbound_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        networks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsPolicyNetworks", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDnsPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: User assigned name for this policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#name GoogleDnsPolicy#name}
        :param alternative_name_server_config: alternative_name_server_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#alternative_name_server_config GoogleDnsPolicy#alternative_name_server_config}
        :param description: A textual description field. Defaults to 'Managed by Terraform'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#description GoogleDnsPolicy#description}
        :param enable_inbound_forwarding: Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address will be allocated from each of the sub-networks that are bound to this policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#enable_inbound_forwarding GoogleDnsPolicy#enable_inbound_forwarding}
        :param enable_logging: Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#enable_logging GoogleDnsPolicy#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#id GoogleDnsPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param networks: networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#networks GoogleDnsPolicy#networks}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#project GoogleDnsPolicy#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#timeouts GoogleDnsPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alternative_name_server_config, dict):
            alternative_name_server_config = GoogleDnsPolicyAlternativeNameServerConfig(**alternative_name_server_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleDnsPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alternative_name_server_config", value=alternative_name_server_config, expected_type=type_hints["alternative_name_server_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_inbound_forwarding", value=enable_inbound_forwarding, expected_type=type_hints["enable_inbound_forwarding"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if alternative_name_server_config is not None:
            self._values["alternative_name_server_config"] = alternative_name_server_config
        if description is not None:
            self._values["description"] = description
        if enable_inbound_forwarding is not None:
            self._values["enable_inbound_forwarding"] = enable_inbound_forwarding
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if id is not None:
            self._values["id"] = id
        if networks is not None:
            self._values["networks"] = networks
        if project is not None:
            self._values["project"] = project
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
    def name(self) -> builtins.str:
        '''User assigned name for this policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#name GoogleDnsPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alternative_name_server_config(
        self,
    ) -> typing.Optional[GoogleDnsPolicyAlternativeNameServerConfig]:
        '''alternative_name_server_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#alternative_name_server_config GoogleDnsPolicy#alternative_name_server_config}
        '''
        result = self._values.get("alternative_name_server_config")
        return typing.cast(typing.Optional[GoogleDnsPolicyAlternativeNameServerConfig], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A textual description field. Defaults to 'Managed by Terraform'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#description GoogleDnsPolicy#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_inbound_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections.

        When enabled, a
        virtual IP address will be allocated from each of the sub-networks
        that are bound to this policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#enable_inbound_forwarding GoogleDnsPolicy#enable_inbound_forwarding}
        '''
        result = self._values.get("enable_inbound_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#enable_logging GoogleDnsPolicy#enable_logging}
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#id GoogleDnsPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyNetworks"]]]:
        '''networks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#networks GoogleDnsPolicy#networks}
        '''
        result = self._values.get("networks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsPolicyNetworks"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#project GoogleDnsPolicy#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDnsPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#timeouts GoogleDnsPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDnsPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyNetworks",
    jsii_struct_bases=[],
    name_mapping={"network_url": "networkUrl"},
)
class GoogleDnsPolicyNetworks:
    def __init__(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to forward queries to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#network_url GoogleDnsPolicy#network_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyNetworks.__init__)
            check_type(argname="argument network_url", value=network_url, expected_type=type_hints["network_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_url": network_url,
        }

    @builtins.property
    def network_url(self) -> builtins.str:
        '''The id or fully qualified URL of the VPC network to forward queries to.

        This should be formatted like 'projects/{project}/global/networks/{network}' or
        'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#network_url GoogleDnsPolicy#network_url}
        '''
        result = self._values.get("network_url")
        assert result is not None, "Required property 'network_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsPolicyNetworks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsPolicyNetworksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyNetworksList",
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
            type_hints = typing.get_type_hints(GoogleDnsPolicyNetworksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleDnsPolicyNetworksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyNetworksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDnsPolicyNetworksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyNetworksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyNetworksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyNetworksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsPolicyNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsPolicyNetworks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsPolicyNetworks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyNetworksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsPolicyNetworksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyNetworksOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsPolicyNetworksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="networkUrlInput")
    def network_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="networkUrl")
    def network_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkUrl"))

    @network_url.setter
    def network_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyNetworksOutputReference, "network_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsPolicyNetworks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsPolicyNetworks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsPolicyNetworks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyNetworksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDnsPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#create GoogleDnsPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#delete GoogleDnsPolicy#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#update GoogleDnsPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#create GoogleDnsPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#delete GoogleDnsPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_policy#update GoogleDnsPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsPolicy.GoogleDnsPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDnsPolicy",
    "GoogleDnsPolicyAlternativeNameServerConfig",
    "GoogleDnsPolicyAlternativeNameServerConfigOutputReference",
    "GoogleDnsPolicyAlternativeNameServerConfigTargetNameServers",
    "GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersList",
    "GoogleDnsPolicyAlternativeNameServerConfigTargetNameServersOutputReference",
    "GoogleDnsPolicyConfig",
    "GoogleDnsPolicyNetworks",
    "GoogleDnsPolicyNetworksList",
    "GoogleDnsPolicyNetworksOutputReference",
    "GoogleDnsPolicyTimeouts",
    "GoogleDnsPolicyTimeoutsOutputReference",
]

publication.publish()
