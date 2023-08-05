'''
# `data_consul_agent_self`

Refer to the Terraform Registory for docs: [`data_consul_agent_self`](https://www.terraform.io/docs/providers/consul/d/agent_self).
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


class DataConsulAgentSelf(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.dataConsulAgentSelf.DataConsulAgentSelf",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/d/agent_self consul_agent_self}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/d/agent_self consul_agent_self} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulAgentSelf.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataConsulAgentSelfConfig(
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aclDatacenter")
    def acl_datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aclDatacenter"))

    @builtins.property
    @jsii.member(jsii_name="aclDefaultPolicy")
    def acl_default_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aclDefaultPolicy"))

    @builtins.property
    @jsii.member(jsii_name="aclDisabledTtl")
    def acl_disabled_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aclDisabledTtl"))

    @builtins.property
    @jsii.member(jsii_name="aclDownPolicy")
    def acl_down_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aclDownPolicy"))

    @builtins.property
    @jsii.member(jsii_name="aclEnforce08Semantics")
    def acl_enforce08_semantics(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "aclEnforce08Semantics"))

    @builtins.property
    @jsii.member(jsii_name="aclTtl")
    def acl_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aclTtl"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "addresses"))

    @builtins.property
    @jsii.member(jsii_name="advertiseAddr")
    def advertise_addr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "advertiseAddr"))

    @builtins.property
    @jsii.member(jsii_name="advertiseAddrs")
    def advertise_addrs(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "advertiseAddrs"))

    @builtins.property
    @jsii.member(jsii_name="advertiseAddrWan")
    def advertise_addr_wan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "advertiseAddrWan"))

    @builtins.property
    @jsii.member(jsii_name="atlasJoin")
    def atlas_join(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "atlasJoin"))

    @builtins.property
    @jsii.member(jsii_name="bindAddr")
    def bind_addr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bindAddr"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapExpect")
    def bootstrap_expect(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bootstrapExpect"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapMode")
    def bootstrap_mode(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "bootstrapMode"))

    @builtins.property
    @jsii.member(jsii_name="checkDeregisterIntervalMin")
    def check_deregister_interval_min(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkDeregisterIntervalMin"))

    @builtins.property
    @jsii.member(jsii_name="checkReapInterval")
    def check_reap_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkReapInterval"))

    @builtins.property
    @jsii.member(jsii_name="checkUpdateInterval")
    def check_update_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkUpdateInterval"))

    @builtins.property
    @jsii.member(jsii_name="clientAddr")
    def client_addr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAddr"))

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @builtins.property
    @jsii.member(jsii_name="dataDir")
    def data_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataDir"))

    @builtins.property
    @jsii.member(jsii_name="devMode")
    def dev_mode(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "devMode"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="dnsRecursors")
    def dns_recursors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsRecursors"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="enableAnonymousSignature")
    def enable_anonymous_signature(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableAnonymousSignature"))

    @builtins.property
    @jsii.member(jsii_name="enableCoordinates")
    def enable_coordinates(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableCoordinates"))

    @builtins.property
    @jsii.member(jsii_name="enableDebug")
    def enable_debug(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableDebug"))

    @builtins.property
    @jsii.member(jsii_name="enableRemoteExec")
    def enable_remote_exec(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableRemoteExec"))

    @builtins.property
    @jsii.member(jsii_name="enableSyslog")
    def enable_syslog(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableSyslog"))

    @builtins.property
    @jsii.member(jsii_name="enableUi")
    def enable_ui(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableUi"))

    @builtins.property
    @jsii.member(jsii_name="enableUpdateCheck")
    def enable_update_check(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enableUpdateCheck"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="leaveOnInt")
    def leave_on_int(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "leaveOnInt"))

    @builtins.property
    @jsii.member(jsii_name="leaveOnTerm")
    def leave_on_term(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "leaveOnTerm"))

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="performance")
    def performance(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "performance"))

    @builtins.property
    @jsii.member(jsii_name="pidFile")
    def pid_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pidFile"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> cdktf.NumberMap:
        return typing.cast(cdktf.NumberMap, jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="protocolVersion")
    def protocol_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "protocolVersion"))

    @builtins.property
    @jsii.member(jsii_name="reconnectTimeoutLan")
    def reconnect_timeout_lan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reconnectTimeoutLan"))

    @builtins.property
    @jsii.member(jsii_name="reconnectTimeoutWan")
    def reconnect_timeout_wan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reconnectTimeoutWan"))

    @builtins.property
    @jsii.member(jsii_name="rejoinAfterLeave")
    def rejoin_after_leave(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "rejoinAfterLeave"))

    @builtins.property
    @jsii.member(jsii_name="retryJoin")
    def retry_join(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryJoin"))

    @builtins.property
    @jsii.member(jsii_name="retryJoinEc2")
    def retry_join_ec2(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "retryJoinEc2"))

    @builtins.property
    @jsii.member(jsii_name="retryJoinGce")
    def retry_join_gce(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "retryJoinGce"))

    @builtins.property
    @jsii.member(jsii_name="retryJoinWan")
    def retry_join_wan(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "retryJoinWan"))

    @builtins.property
    @jsii.member(jsii_name="retryMaxAttempts")
    def retry_max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryMaxAttempts"))

    @builtins.property
    @jsii.member(jsii_name="retryMaxAttemptsWan")
    def retry_max_attempts_wan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retryMaxAttemptsWan"))

    @builtins.property
    @jsii.member(jsii_name="serfLanBindAddr")
    def serf_lan_bind_addr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serfLanBindAddr"))

    @builtins.property
    @jsii.member(jsii_name="serfWanBindAddr")
    def serf_wan_bind_addr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serfWanBindAddr"))

    @builtins.property
    @jsii.member(jsii_name="serverMode")
    def server_mode(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "serverMode"))

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @builtins.property
    @jsii.member(jsii_name="sessionTtlMin")
    def session_ttl_min(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionTtlMin"))

    @builtins.property
    @jsii.member(jsii_name="startJoin")
    def start_join(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "startJoin"))

    @builtins.property
    @jsii.member(jsii_name="startJoinWan")
    def start_join_wan(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "startJoinWan"))

    @builtins.property
    @jsii.member(jsii_name="syslogFacility")
    def syslog_facility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syslogFacility"))

    @builtins.property
    @jsii.member(jsii_name="taggedAddresses")
    def tagged_addresses(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "taggedAddresses"))

    @builtins.property
    @jsii.member(jsii_name="telemetry")
    def telemetry(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "telemetry"))

    @builtins.property
    @jsii.member(jsii_name="tlsCaFile")
    def tls_ca_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCaFile"))

    @builtins.property
    @jsii.member(jsii_name="tlsCertFile")
    def tls_cert_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCertFile"))

    @builtins.property
    @jsii.member(jsii_name="tlsKeyFile")
    def tls_key_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsKeyFile"))

    @builtins.property
    @jsii.member(jsii_name="tlsMinVersion")
    def tls_min_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsMinVersion"))

    @builtins.property
    @jsii.member(jsii_name="tlsVerifyIncoming")
    def tls_verify_incoming(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "tlsVerifyIncoming"))

    @builtins.property
    @jsii.member(jsii_name="tlsVerifyOutgoing")
    def tls_verify_outgoing(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "tlsVerifyOutgoing"))

    @builtins.property
    @jsii.member(jsii_name="tlsVerifyServerHostname")
    def tls_verify_server_hostname(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "tlsVerifyServerHostname"))

    @builtins.property
    @jsii.member(jsii_name="translateWanAddrs")
    def translate_wan_addrs(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "translateWanAddrs"))

    @builtins.property
    @jsii.member(jsii_name="uiDir")
    def ui_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uiDir"))

    @builtins.property
    @jsii.member(jsii_name="unixSockets")
    def unix_sockets(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "unixSockets"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="versionPrerelease")
    def version_prerelease(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionPrerelease"))

    @builtins.property
    @jsii.member(jsii_name="versionRevision")
    def version_revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionRevision"))


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.dataConsulAgentSelf.DataConsulAgentSelfConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
    },
)
class DataConsulAgentSelfConfig(cdktf.TerraformMetaArguments):
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
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataConsulAgentSelfConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
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

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConsulAgentSelfConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataConsulAgentSelf",
    "DataConsulAgentSelfConfig",
]

publication.publish()
