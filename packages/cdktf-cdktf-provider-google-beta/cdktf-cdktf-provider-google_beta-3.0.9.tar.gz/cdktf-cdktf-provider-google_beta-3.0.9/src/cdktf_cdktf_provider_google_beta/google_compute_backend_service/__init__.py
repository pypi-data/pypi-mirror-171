'''
# `google_compute_backend_service`

Refer to the Terraform Registory for docs: [`google_compute_backend_service`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service).
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


class GoogleComputeBackendService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service google_compute_backend_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        affinity_cookie_ttl_sec: typing.Optional[jsii.Number] = None,
        backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendServiceBackend", typing.Dict[str, typing.Any]]]]] = None,
        cdn_policy: typing.Optional[typing.Union["GoogleComputeBackendServiceCdnPolicy", typing.Dict[str, typing.Any]]] = None,
        circuit_breakers: typing.Optional[typing.Union["GoogleComputeBackendServiceCircuitBreakers", typing.Dict[str, typing.Any]]] = None,
        connection_draining_timeout_sec: typing.Optional[jsii.Number] = None,
        consistent_hash: typing.Optional[typing.Union["GoogleComputeBackendServiceConsistentHash", typing.Dict[str, typing.Any]]] = None,
        custom_request_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_cdn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_checks: typing.Optional[typing.Sequence[builtins.str]] = None,
        iap: typing.Optional[typing.Union["GoogleComputeBackendServiceIap", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancing_scheme: typing.Optional[builtins.str] = None,
        locality_lb_policy: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeBackendServiceLogConfig", typing.Dict[str, typing.Any]]] = None,
        outlier_detection: typing.Optional[typing.Union["GoogleComputeBackendServiceOutlierDetection", typing.Dict[str, typing.Any]]] = None,
        port_name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
        security_settings: typing.Optional[typing.Union["GoogleComputeBackendServiceSecuritySettings", typing.Dict[str, typing.Any]]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeBackendServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        timeout_sec: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service google_compute_backend_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#name GoogleComputeBackendService#name}
        :param affinity_cookie_ttl_sec: Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the load balancing scheme is INTERNAL, this field is not used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#affinity_cookie_ttl_sec GoogleComputeBackendService#affinity_cookie_ttl_sec}
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#backend GoogleComputeBackendService#backend}
        :param cdn_policy: cdn_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cdn_policy GoogleComputeBackendService#cdn_policy}
        :param circuit_breakers: circuit_breakers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#circuit_breakers GoogleComputeBackendService#circuit_breakers}
        :param connection_draining_timeout_sec: Time for which instance will be drained (not accept new connections, but still work to finish started). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#connection_draining_timeout_sec GoogleComputeBackendService#connection_draining_timeout_sec}
        :param consistent_hash: consistent_hash block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consistent_hash GoogleComputeBackendService#consistent_hash}
        :param custom_request_headers: Headers that the HTTP/S load balancer should add to proxied requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#custom_request_headers GoogleComputeBackendService#custom_request_headers}
        :param custom_response_headers: Headers that the HTTP/S load balancer should add to proxied responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#custom_response_headers GoogleComputeBackendService#custom_response_headers}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#description GoogleComputeBackendService#description}
        :param enable_cdn: If true, enable Cloud CDN for this BackendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enable_cdn GoogleComputeBackendService#enable_cdn}
        :param health_checks: The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently at most one health check can be specified. A health check must be specified unless the backend service uses an internet or serverless NEG as a backend. For internal load balancing, a URL to a HealthCheck resource must be specified instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#health_checks GoogleComputeBackendService#health_checks}
        :param iap: iap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#iap GoogleComputeBackendService#iap}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#id GoogleComputeBackendService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancing_scheme: Indicates whether the backend service will be used with internal or external load balancing. A backend service created for one type of load balancing cannot be used with the other. For more information, refer to `Choosing a load balancer <https://cloud.google.com/load-balancing/docs/backend-service>`_. Default value: "EXTERNAL" Possible values: ["EXTERNAL", "INTERNAL_SELF_MANAGED", "EXTERNAL_MANAGED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#load_balancing_scheme GoogleComputeBackendService#load_balancing_scheme}
        :param locality_lb_policy: The load balancing algorithm used within the scope of the locality. The possible values are:. 'ROUND_ROBIN': This is a simple policy in which each healthy backend is selected in round robin order. 'LEAST_REQUEST': An O(1) algorithm which selects two random healthy hosts and picks the host which has fewer active requests. 'RING_HASH': The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests. 'RANDOM': The load balancer selects a random healthy host. 'ORIGINAL_DESTINATION': Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer. 'MAGLEV': used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, refer to https://ai.google/research/pubs/pub44824 This field is applicable to either: A regional backend service with the service_protocol set to HTTP, HTTPS, or HTTP2, and loadBalancingScheme set to INTERNAL_MANAGED. A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED. If session_affinity is not NONE, and this field is not set to MAGLEV or RING_HASH, session affinity settings will not take effect. Only ROUND_ROBIN and RING_HASH are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validate_for_proxyless field set to true. Possible values: ["ROUND_ROBIN", "LEAST_REQUEST", "RING_HASH", "RANDOM", "ORIGINAL_DESTINATION", "MAGLEV"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#locality_lb_policy GoogleComputeBackendService#locality_lb_policy}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#log_config GoogleComputeBackendService#log_config}
        :param outlier_detection: outlier_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#outlier_detection GoogleComputeBackendService#outlier_detection}
        :param port_name: Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the load balancing scheme is EXTERNAL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#port_name GoogleComputeBackendService#port_name}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#project GoogleComputeBackendService#project}.
        :param protocol: The protocol this BackendService uses to communicate with backends. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if used with the GA API. Possible values: ["HTTP", "HTTPS", "HTTP2", "TCP", "SSL", "GRPC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#protocol GoogleComputeBackendService#protocol}
        :param security_policy: The security policy associated with this backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#security_policy GoogleComputeBackendService#security_policy}
        :param security_settings: security_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#security_settings GoogleComputeBackendService#security_settings}
        :param session_affinity: Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP. Possible values: ["NONE", "CLIENT_IP", "CLIENT_IP_PORT_PROTO", "CLIENT_IP_PROTO", "GENERATED_COOKIE", "HEADER_FIELD", "HTTP_COOKIE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#session_affinity GoogleComputeBackendService#session_affinity}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#timeouts GoogleComputeBackendService#timeouts}
        :param timeout_sec: How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is [1, 86400]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#timeout_sec GoogleComputeBackendService#timeout_sec}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeBackendServiceConfig(
            name=name,
            affinity_cookie_ttl_sec=affinity_cookie_ttl_sec,
            backend=backend,
            cdn_policy=cdn_policy,
            circuit_breakers=circuit_breakers,
            connection_draining_timeout_sec=connection_draining_timeout_sec,
            consistent_hash=consistent_hash,
            custom_request_headers=custom_request_headers,
            custom_response_headers=custom_response_headers,
            description=description,
            enable_cdn=enable_cdn,
            health_checks=health_checks,
            iap=iap,
            id=id,
            load_balancing_scheme=load_balancing_scheme,
            locality_lb_policy=locality_lb_policy,
            log_config=log_config,
            outlier_detection=outlier_detection,
            port_name=port_name,
            project=project,
            protocol=protocol,
            security_policy=security_policy,
            security_settings=security_settings,
            session_affinity=session_affinity,
            timeouts=timeouts,
            timeout_sec=timeout_sec,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendServiceBackend", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendService.put_backend)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="putCdnPolicy")
    def put_cdn_policy(
        self,
        *,
        cache_key_policy: typing.Optional[typing.Union["GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy", typing.Dict[str, typing.Any]]] = None,
        cache_mode: typing.Optional[builtins.str] = None,
        client_ttl: typing.Optional[jsii.Number] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        negative_caching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        negative_caching_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy", typing.Dict[str, typing.Any]]]]] = None,
        serve_while_stale: typing.Optional[jsii.Number] = None,
        signed_url_cache_max_age_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_key_policy: cache_key_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cache_key_policy GoogleComputeBackendService#cache_key_policy}
        :param cache_mode: Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC Possible values: ["USE_ORIGIN_HEADERS", "FORCE_CACHE_ALL", "CACHE_ALL_STATIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cache_mode GoogleComputeBackendService#cache_mode}
        :param client_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#client_ttl GoogleComputeBackendService#client_ttl}
        :param default_ttl: Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#default_ttl GoogleComputeBackendService#default_ttl}
        :param max_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_ttl GoogleComputeBackendService#max_ttl}
        :param negative_caching: Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#negative_caching GoogleComputeBackendService#negative_caching}
        :param negative_caching_policy: negative_caching_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#negative_caching_policy GoogleComputeBackendService#negative_caching_policy}
        :param serve_while_stale: Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#serve_while_stale GoogleComputeBackendService#serve_while_stale}
        :param signed_url_cache_max_age_sec: Maximum number of seconds the response to a signed URL request will be considered fresh, defaults to 1hr (3600s). After this time period, the response will be revalidated before being served. When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#signed_url_cache_max_age_sec GoogleComputeBackendService#signed_url_cache_max_age_sec}
        '''
        value = GoogleComputeBackendServiceCdnPolicy(
            cache_key_policy=cache_key_policy,
            cache_mode=cache_mode,
            client_ttl=client_ttl,
            default_ttl=default_ttl,
            max_ttl=max_ttl,
            negative_caching=negative_caching,
            negative_caching_policy=negative_caching_policy,
            serve_while_stale=serve_while_stale,
            signed_url_cache_max_age_sec=signed_url_cache_max_age_sec,
        )

        return typing.cast(None, jsii.invoke(self, "putCdnPolicy", [value]))

    @jsii.member(jsii_name="putCircuitBreakers")
    def put_circuit_breakers(
        self,
        *,
        connect_timeout: typing.Optional[typing.Union["GoogleComputeBackendServiceCircuitBreakersConnectTimeout", typing.Dict[str, typing.Any]]] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        max_pending_requests: typing.Optional[jsii.Number] = None,
        max_requests: typing.Optional[jsii.Number] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connect_timeout: connect_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#connect_timeout GoogleComputeBackendService#connect_timeout}
        :param max_connections: The maximum number of connections to the backend cluster. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections GoogleComputeBackendService#max_connections}
        :param max_pending_requests: The maximum number of pending requests to the backend cluster. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_pending_requests GoogleComputeBackendService#max_pending_requests}
        :param max_requests: The maximum number of parallel requests to the backend cluster. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_requests GoogleComputeBackendService#max_requests}
        :param max_requests_per_connection: Maximum requests for a single backend connection. This parameter is respected by both the HTTP/1.1 and HTTP/2 implementations. If not specified, there is no limit. Setting this parameter to 1 will effectively disable keep alive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_requests_per_connection GoogleComputeBackendService#max_requests_per_connection}
        :param max_retries: The maximum number of parallel retries to the backend cluster. Defaults to 3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_retries GoogleComputeBackendService#max_retries}
        '''
        value = GoogleComputeBackendServiceCircuitBreakers(
            connect_timeout=connect_timeout,
            max_connections=max_connections,
            max_pending_requests=max_pending_requests,
            max_requests=max_requests,
            max_requests_per_connection=max_requests_per_connection,
            max_retries=max_retries,
        )

        return typing.cast(None, jsii.invoke(self, "putCircuitBreakers", [value]))

    @jsii.member(jsii_name="putConsistentHash")
    def put_consistent_hash(
        self,
        *,
        http_cookie: typing.Optional[typing.Union["GoogleComputeBackendServiceConsistentHashHttpCookie", typing.Dict[str, typing.Any]]] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_cookie: http_cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#http_cookie GoogleComputeBackendService#http_cookie}
        :param http_header_name: The hash based on the value of the specified header field. This field is applicable if the sessionAffinity is set to HEADER_FIELD. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#http_header_name GoogleComputeBackendService#http_header_name}
        :param minimum_ring_size: The minimum number of virtual nodes to use for the hash ring. Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#minimum_ring_size GoogleComputeBackendService#minimum_ring_size}
        '''
        value = GoogleComputeBackendServiceConsistentHash(
            http_cookie=http_cookie,
            http_header_name=http_header_name,
            minimum_ring_size=minimum_ring_size,
        )

        return typing.cast(None, jsii.invoke(self, "putConsistentHash", [value]))

    @jsii.member(jsii_name="putIap")
    def put_iap(
        self,
        *,
        oauth2_client_id: builtins.str,
        oauth2_client_secret: builtins.str,
    ) -> None:
        '''
        :param oauth2_client_id: OAuth2 Client ID for IAP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#oauth2_client_id GoogleComputeBackendService#oauth2_client_id}
        :param oauth2_client_secret: OAuth2 Client Secret for IAP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#oauth2_client_secret GoogleComputeBackendService#oauth2_client_secret}
        '''
        value = GoogleComputeBackendServiceIap(
            oauth2_client_id=oauth2_client_id,
            oauth2_client_secret=oauth2_client_secret,
        )

        return typing.cast(None, jsii.invoke(self, "putIap", [value]))

    @jsii.member(jsii_name="putLogConfig")
    def put_log_config(
        self,
        *,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sample_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable: Whether to enable logging for the load balancer traffic served by this backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enable GoogleComputeBackendService#enable}
        :param sample_rate: This field can only be specified if logging is enabled for this backend service. The value of the field must be in [0, 1]. This configures the sampling rate of requests to the load balancer where 1.0 means all logged requests are reported and 0.0 means no logged requests are reported. The default value is 1.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#sample_rate GoogleComputeBackendService#sample_rate}
        '''
        value = GoogleComputeBackendServiceLogConfig(
            enable=enable, sample_rate=sample_rate
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfig", [value]))

    @jsii.member(jsii_name="putOutlierDetection")
    def put_outlier_detection(
        self,
        *,
        base_ejection_time: typing.Optional[typing.Union["GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime", typing.Dict[str, typing.Any]]] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_failure: typing.Optional[jsii.Number] = None,
        enforcing_consecutive_errors: typing.Optional[jsii.Number] = None,
        enforcing_consecutive_gateway_failure: typing.Optional[jsii.Number] = None,
        enforcing_success_rate: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[typing.Union["GoogleComputeBackendServiceOutlierDetectionInterval", typing.Dict[str, typing.Any]]] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        success_rate_minimum_hosts: typing.Optional[jsii.Number] = None,
        success_rate_request_volume: typing.Optional[jsii.Number] = None,
        success_rate_stdev_factor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param base_ejection_time: base_ejection_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#base_ejection_time GoogleComputeBackendService#base_ejection_time}
        :param consecutive_errors: Number of errors before a host is ejected from the connection pool. When the backend host is accessed over HTTP, a 5xx return code qualifies as an error. Defaults to 5. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consecutive_errors GoogleComputeBackendService#consecutive_errors}
        :param consecutive_gateway_failure: The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs. Defaults to 5. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consecutive_gateway_failure GoogleComputeBackendService#consecutive_gateway_failure}
        :param enforcing_consecutive_errors: The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive 5xx. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_consecutive_errors GoogleComputeBackendService#enforcing_consecutive_errors}
        :param enforcing_consecutive_gateway_failure: The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive gateway failures. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_consecutive_gateway_failure GoogleComputeBackendService#enforcing_consecutive_gateway_failure}
        :param enforcing_success_rate: The percentage chance that a host will be actually ejected when an outlier status is detected through success rate statistics. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_success_rate GoogleComputeBackendService#enforcing_success_rate}
        :param interval: interval block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#interval GoogleComputeBackendService#interval}
        :param max_ejection_percent: Maximum percentage of hosts in the load balancing pool for the backend service that can be ejected. Defaults to 10%. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_ejection_percent GoogleComputeBackendService#max_ejection_percent}
        :param success_rate_minimum_hosts: The number of hosts in a cluster that must have enough request volume to detect success rate outliers. If the number of hosts is less than this setting, outlier detection via success rate statistics is not performed for any host in the cluster. Defaults to 5. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_minimum_hosts GoogleComputeBackendService#success_rate_minimum_hosts}
        :param success_rate_request_volume: The minimum number of total requests that must be collected in one interval (as defined by the interval duration above) to include this host in success rate based outlier detection. If the volume is lower than this setting, outlier detection via success rate statistics is not performed for that host. Defaults to 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_request_volume GoogleComputeBackendService#success_rate_request_volume}
        :param success_rate_stdev_factor: This factor is used to determine the ejection threshold for success rate outlier ejection. The ejection threshold is the difference between the mean success rate, and the product of this factor and the standard deviation of the mean success rate: mean - (stdev * success_rate_stdev_factor). This factor is divided by a thousand to get a double. That is, if the desired factor is 1.9, the runtime value should be 1900. Defaults to 1900. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_stdev_factor GoogleComputeBackendService#success_rate_stdev_factor}
        '''
        value = GoogleComputeBackendServiceOutlierDetection(
            base_ejection_time=base_ejection_time,
            consecutive_errors=consecutive_errors,
            consecutive_gateway_failure=consecutive_gateway_failure,
            enforcing_consecutive_errors=enforcing_consecutive_errors,
            enforcing_consecutive_gateway_failure=enforcing_consecutive_gateway_failure,
            enforcing_success_rate=enforcing_success_rate,
            interval=interval,
            max_ejection_percent=max_ejection_percent,
            success_rate_minimum_hosts=success_rate_minimum_hosts,
            success_rate_request_volume=success_rate_request_volume,
            success_rate_stdev_factor=success_rate_stdev_factor,
        )

        return typing.cast(None, jsii.invoke(self, "putOutlierDetection", [value]))

    @jsii.member(jsii_name="putSecuritySettings")
    def put_security_settings(
        self,
        *,
        client_tls_policy: builtins.str,
        subject_alt_names: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param client_tls_policy: ClientTlsPolicy is a resource that specifies how a client should authenticate connections to backends of a service. This resource itself does not affect configuration unless it is attached to a backend service resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#client_tls_policy GoogleComputeBackendService#client_tls_policy}
        :param subject_alt_names: A list of alternate names to verify the subject identity in the certificate. If specified, the client will verify that the server certificate's subject alt name matches one of the specified values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#subject_alt_names GoogleComputeBackendService#subject_alt_names}
        '''
        value = GoogleComputeBackendServiceSecuritySettings(
            client_tls_policy=client_tls_policy, subject_alt_names=subject_alt_names
        )

        return typing.cast(None, jsii.invoke(self, "putSecuritySettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#create GoogleComputeBackendService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#delete GoogleComputeBackendService#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#update GoogleComputeBackendService#update}.
        '''
        value = GoogleComputeBackendServiceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAffinityCookieTtlSec")
    def reset_affinity_cookie_ttl_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAffinityCookieTtlSec", []))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetCdnPolicy")
    def reset_cdn_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnPolicy", []))

    @jsii.member(jsii_name="resetCircuitBreakers")
    def reset_circuit_breakers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCircuitBreakers", []))

    @jsii.member(jsii_name="resetConnectionDrainingTimeoutSec")
    def reset_connection_draining_timeout_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionDrainingTimeoutSec", []))

    @jsii.member(jsii_name="resetConsistentHash")
    def reset_consistent_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsistentHash", []))

    @jsii.member(jsii_name="resetCustomRequestHeaders")
    def reset_custom_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRequestHeaders", []))

    @jsii.member(jsii_name="resetCustomResponseHeaders")
    def reset_custom_response_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomResponseHeaders", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnableCdn")
    def reset_enable_cdn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableCdn", []))

    @jsii.member(jsii_name="resetHealthChecks")
    def reset_health_checks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthChecks", []))

    @jsii.member(jsii_name="resetIap")
    def reset_iap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIap", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadBalancingScheme")
    def reset_load_balancing_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingScheme", []))

    @jsii.member(jsii_name="resetLocalityLbPolicy")
    def reset_locality_lb_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalityLbPolicy", []))

    @jsii.member(jsii_name="resetLogConfig")
    def reset_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfig", []))

    @jsii.member(jsii_name="resetOutlierDetection")
    def reset_outlier_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutlierDetection", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetSecurityPolicy")
    def reset_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityPolicy", []))

    @jsii.member(jsii_name="resetSecuritySettings")
    def reset_security_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecuritySettings", []))

    @jsii.member(jsii_name="resetSessionAffinity")
    def reset_session_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinity", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimeoutSec")
    def reset_timeout_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSec", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> "GoogleComputeBackendServiceBackendList":
        return typing.cast("GoogleComputeBackendServiceBackendList", jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="cdnPolicy")
    def cdn_policy(self) -> "GoogleComputeBackendServiceCdnPolicyOutputReference":
        return typing.cast("GoogleComputeBackendServiceCdnPolicyOutputReference", jsii.get(self, "cdnPolicy"))

    @builtins.property
    @jsii.member(jsii_name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> "GoogleComputeBackendServiceCircuitBreakersOutputReference":
        return typing.cast("GoogleComputeBackendServiceCircuitBreakersOutputReference", jsii.get(self, "circuitBreakers"))

    @builtins.property
    @jsii.member(jsii_name="consistentHash")
    def consistent_hash(
        self,
    ) -> "GoogleComputeBackendServiceConsistentHashOutputReference":
        return typing.cast("GoogleComputeBackendServiceConsistentHashOutputReference", jsii.get(self, "consistentHash"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="iap")
    def iap(self) -> "GoogleComputeBackendServiceIapOutputReference":
        return typing.cast("GoogleComputeBackendServiceIapOutputReference", jsii.get(self, "iap"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "GoogleComputeBackendServiceLogConfigOutputReference":
        return typing.cast("GoogleComputeBackendServiceLogConfigOutputReference", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetection")
    def outlier_detection(
        self,
    ) -> "GoogleComputeBackendServiceOutlierDetectionOutputReference":
        return typing.cast("GoogleComputeBackendServiceOutlierDetectionOutputReference", jsii.get(self, "outlierDetection"))

    @builtins.property
    @jsii.member(jsii_name="securitySettings")
    def security_settings(
        self,
    ) -> "GoogleComputeBackendServiceSecuritySettingsOutputReference":
        return typing.cast("GoogleComputeBackendServiceSecuritySettingsOutputReference", jsii.get(self, "securitySettings"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeBackendServiceTimeoutsOutputReference":
        return typing.cast("GoogleComputeBackendServiceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="affinityCookieTtlSecInput")
    def affinity_cookie_ttl_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "affinityCookieTtlSecInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendServiceBackend"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendServiceBackend"]]], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnPolicyInput")
    def cdn_policy_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceCdnPolicy"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceCdnPolicy"], jsii.get(self, "cdnPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="circuitBreakersInput")
    def circuit_breakers_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceCircuitBreakers"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceCircuitBreakers"], jsii.get(self, "circuitBreakersInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingTimeoutSecInput")
    def connection_draining_timeout_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectionDrainingTimeoutSecInput"))

    @builtins.property
    @jsii.member(jsii_name="consistentHashInput")
    def consistent_hash_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceConsistentHash"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceConsistentHash"], jsii.get(self, "consistentHashInput"))

    @builtins.property
    @jsii.member(jsii_name="customRequestHeadersInput")
    def custom_request_headers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customRequestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="customResponseHeadersInput")
    def custom_response_headers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customResponseHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enableCdnInput")
    def enable_cdn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableCdnInput"))

    @builtins.property
    @jsii.member(jsii_name="healthChecksInput")
    def health_checks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "healthChecksInput"))

    @builtins.property
    @jsii.member(jsii_name="iapInput")
    def iap_input(self) -> typing.Optional["GoogleComputeBackendServiceIap"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceIap"], jsii.get(self, "iapInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingSchemeInput")
    def load_balancing_scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingSchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="localityLbPolicyInput")
    def locality_lb_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localityLbPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigInput")
    def log_config_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceLogConfig"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceLogConfig"], jsii.get(self, "logConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetectionInput")
    def outlier_detection_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceOutlierDetection"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceOutlierDetection"], jsii.get(self, "outlierDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicyInput")
    def security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="securitySettingsInput")
    def security_settings_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceSecuritySettings"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceSecuritySettings"], jsii.get(self, "securitySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityInput")
    def session_affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecInput")
    def timeout_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeBackendServiceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeBackendServiceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "affinityCookieTtlSec"))

    @affinity_cookie_ttl_sec.setter
    def affinity_cookie_ttl_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "affinity_cookie_ttl_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "affinityCookieTtlSec", value)

    @builtins.property
    @jsii.member(jsii_name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectionDrainingTimeoutSec"))

    @connection_draining_timeout_sec.setter
    def connection_draining_timeout_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "connection_draining_timeout_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionDrainingTimeoutSec", value)

    @builtins.property
    @jsii.member(jsii_name="customRequestHeaders")
    def custom_request_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customRequestHeaders"))

    @custom_request_headers.setter
    def custom_request_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "custom_request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customRequestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="customResponseHeaders")
    def custom_response_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customResponseHeaders"))

    @custom_response_headers.setter
    def custom_response_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "custom_response_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customResponseHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableCdn")
    def enable_cdn(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableCdn"))

    @enable_cdn.setter
    def enable_cdn(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "enable_cdn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCdn", value)

    @builtins.property
    @jsii.member(jsii_name="healthChecks")
    def health_checks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "healthChecks"))

    @health_checks.setter
    def health_checks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "health_checks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthChecks", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingScheme")
    def load_balancing_scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingScheme"))

    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "load_balancing_scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingScheme", value)

    @builtins.property
    @jsii.member(jsii_name="localityLbPolicy")
    def locality_lb_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localityLbPolicy"))

    @locality_lb_policy.setter
    def locality_lb_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "locality_lb_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localityLbPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicy")
    def security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityPolicy"))

    @security_policy.setter
    def security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "security_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinity")
    def session_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionAffinity"))

    @session_affinity.setter
    def session_affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "session_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSec")
    def timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSec"))

    @timeout_sec.setter
    def timeout_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendService, "timeout_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSec", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceBackend",
    jsii_struct_bases=[],
    name_mapping={
        "group": "group",
        "balancing_mode": "balancingMode",
        "capacity_scaler": "capacityScaler",
        "description": "description",
        "max_connections": "maxConnections",
        "max_connections_per_endpoint": "maxConnectionsPerEndpoint",
        "max_connections_per_instance": "maxConnectionsPerInstance",
        "max_rate": "maxRate",
        "max_rate_per_endpoint": "maxRatePerEndpoint",
        "max_rate_per_instance": "maxRatePerInstance",
        "max_utilization": "maxUtilization",
    },
)
class GoogleComputeBackendServiceBackend:
    def __init__(
        self,
        *,
        group: builtins.str,
        balancing_mode: typing.Optional[builtins.str] = None,
        capacity_scaler: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        max_connections_per_endpoint: typing.Optional[jsii.Number] = None,
        max_connections_per_instance: typing.Optional[jsii.Number] = None,
        max_rate: typing.Optional[jsii.Number] = None,
        max_rate_per_endpoint: typing.Optional[jsii.Number] = None,
        max_rate_per_instance: typing.Optional[jsii.Number] = None,
        max_utilization: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group: The fully-qualified URL of an Instance Group or Network Endpoint Group resource. In case of instance group this defines the list of instances that serve traffic. Member virtual machine instances from each instance group must live in the same zone as the instance group itself. No two backends in a backend service are allowed to use same Instance Group resource. For Network Endpoint Groups this defines list of endpoints. All endpoints of Network Endpoint Group must be hosted on instances located in the same zone as the Network Endpoint Group. Backend services cannot mix Instance Group and Network Endpoint Group backends. Note that you must specify an Instance Group or Network Endpoint Group resource using the fully-qualified URL, rather than a partial URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#group GoogleComputeBackendService#group}
        :param balancing_mode: Specifies the balancing mode for this backend. For global HTTP(S) or TCP/SSL load balancing, the default is UTILIZATION. Valid values are UTILIZATION, RATE (for HTTP(S)) and CONNECTION (for TCP/SSL). See the `Backend Services Overview <https://cloud.google.com/load-balancing/docs/backend-service#balancing-mode>`_ for an explanation of load balancing modes. Default value: "UTILIZATION" Possible values: ["UTILIZATION", "RATE", "CONNECTION"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#balancing_mode GoogleComputeBackendService#balancing_mode}
        :param capacity_scaler: A multiplier applied to the group's maximum servicing capacity (based on UTILIZATION, RATE or CONNECTION). Default value is 1, which means the group will serve up to 100% of its configured capacity (depending on balancingMode). A setting of 0 means the group is completely drained, offering 0% of its available Capacity. Valid range is [0.0,1.0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#capacity_scaler GoogleComputeBackendService#capacity_scaler}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#description GoogleComputeBackendService#description}
        :param max_connections: The max number of simultaneous connections for the group. Can be used with either CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections or one of maxConnectionsPerInstance or maxConnectionsPerEndpoint, as appropriate for group type, must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections GoogleComputeBackendService#max_connections}
        :param max_connections_per_endpoint: The max number of simultaneous connections that a single backend network endpoint can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections or maxConnectionsPerEndpoint must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections_per_endpoint GoogleComputeBackendService#max_connections_per_endpoint}
        :param max_connections_per_instance: The max number of simultaneous connections that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes. For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections_per_instance GoogleComputeBackendService#max_connections_per_instance}
        :param max_rate: The max requests per second (RPS) of the group. Can be used with either RATE or UTILIZATION balancing modes, but required if RATE mode. For RATE mode, either maxRate or one of maxRatePerInstance or maxRatePerEndpoint, as appropriate for group type, must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_rate GoogleComputeBackendService#max_rate}
        :param max_rate_per_endpoint: The max requests per second (RPS) that a single backend network endpoint can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerEndpoint must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_rate_per_endpoint GoogleComputeBackendService#max_rate_per_endpoint}
        :param max_rate_per_instance: The max requests per second (RPS) that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerInstance must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_rate_per_instance GoogleComputeBackendService#max_rate_per_instance}
        :param max_utilization: Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization target for the group. Valid range is [0.0, 1.0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_utilization GoogleComputeBackendService#max_utilization}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceBackend.__init__)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument balancing_mode", value=balancing_mode, expected_type=type_hints["balancing_mode"])
            check_type(argname="argument capacity_scaler", value=capacity_scaler, expected_type=type_hints["capacity_scaler"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument max_connections_per_endpoint", value=max_connections_per_endpoint, expected_type=type_hints["max_connections_per_endpoint"])
            check_type(argname="argument max_connections_per_instance", value=max_connections_per_instance, expected_type=type_hints["max_connections_per_instance"])
            check_type(argname="argument max_rate", value=max_rate, expected_type=type_hints["max_rate"])
            check_type(argname="argument max_rate_per_endpoint", value=max_rate_per_endpoint, expected_type=type_hints["max_rate_per_endpoint"])
            check_type(argname="argument max_rate_per_instance", value=max_rate_per_instance, expected_type=type_hints["max_rate_per_instance"])
            check_type(argname="argument max_utilization", value=max_utilization, expected_type=type_hints["max_utilization"])
        self._values: typing.Dict[str, typing.Any] = {
            "group": group,
        }
        if balancing_mode is not None:
            self._values["balancing_mode"] = balancing_mode
        if capacity_scaler is not None:
            self._values["capacity_scaler"] = capacity_scaler
        if description is not None:
            self._values["description"] = description
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if max_connections_per_endpoint is not None:
            self._values["max_connections_per_endpoint"] = max_connections_per_endpoint
        if max_connections_per_instance is not None:
            self._values["max_connections_per_instance"] = max_connections_per_instance
        if max_rate is not None:
            self._values["max_rate"] = max_rate
        if max_rate_per_endpoint is not None:
            self._values["max_rate_per_endpoint"] = max_rate_per_endpoint
        if max_rate_per_instance is not None:
            self._values["max_rate_per_instance"] = max_rate_per_instance
        if max_utilization is not None:
            self._values["max_utilization"] = max_utilization

    @builtins.property
    def group(self) -> builtins.str:
        '''The fully-qualified URL of an Instance Group or Network Endpoint Group resource.

        In case of instance group this defines the list
        of instances that serve traffic. Member virtual machine
        instances from each instance group must live in the same zone as
        the instance group itself. No two backends in a backend service
        are allowed to use same Instance Group resource.

        For Network Endpoint Groups this defines list of endpoints. All
        endpoints of Network Endpoint Group must be hosted on instances
        located in the same zone as the Network Endpoint Group.

        Backend services cannot mix Instance Group and
        Network Endpoint Group backends.

        Note that you must specify an Instance Group or Network Endpoint
        Group resource using the fully-qualified URL, rather than a
        partial URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#group GoogleComputeBackendService#group}
        '''
        result = self._values.get("group")
        assert result is not None, "Required property 'group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def balancing_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies the balancing mode for this backend.

        For global HTTP(S) or TCP/SSL load balancing, the default is
        UTILIZATION. Valid values are UTILIZATION, RATE (for HTTP(S))
        and CONNECTION (for TCP/SSL).

        See the `Backend Services Overview <https://cloud.google.com/load-balancing/docs/backend-service#balancing-mode>`_
        for an explanation of load balancing modes. Default value: "UTILIZATION" Possible values: ["UTILIZATION", "RATE", "CONNECTION"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#balancing_mode GoogleComputeBackendService#balancing_mode}
        '''
        result = self._values.get("balancing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_scaler(self) -> typing.Optional[jsii.Number]:
        '''A multiplier applied to the group's maximum servicing capacity (based on UTILIZATION, RATE or CONNECTION).

        Default value is 1, which means the group will serve up to 100%
        of its configured capacity (depending on balancingMode). A
        setting of 0 means the group is completely drained, offering
        0% of its available Capacity. Valid range is [0.0,1.0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#capacity_scaler GoogleComputeBackendService#capacity_scaler}
        '''
        result = self._values.get("capacity_scaler")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#description GoogleComputeBackendService#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''The max number of simultaneous connections for the group. Can be used with either CONNECTION or UTILIZATION balancing modes.

        For CONNECTION mode, either maxConnections or one
        of maxConnectionsPerInstance or maxConnectionsPerEndpoint,
        as appropriate for group type, must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections GoogleComputeBackendService#max_connections}
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_connections_per_endpoint(self) -> typing.Optional[jsii.Number]:
        '''The max number of simultaneous connections that a single backend network endpoint can handle.

        This is used to calculate the
        capacity of the group. Can be used in either CONNECTION or
        UTILIZATION balancing modes.

        For CONNECTION mode, either
        maxConnections or maxConnectionsPerEndpoint must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections_per_endpoint GoogleComputeBackendService#max_connections_per_endpoint}
        '''
        result = self._values.get("max_connections_per_endpoint")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_connections_per_instance(self) -> typing.Optional[jsii.Number]:
        '''The max number of simultaneous connections that a single backend instance can handle.

        This is used to calculate the
        capacity of the group. Can be used in either CONNECTION or
        UTILIZATION balancing modes.

        For CONNECTION mode, either maxConnections or
        maxConnectionsPerInstance must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections_per_instance GoogleComputeBackendService#max_connections_per_instance}
        '''
        result = self._values.get("max_connections_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_rate(self) -> typing.Optional[jsii.Number]:
        '''The max requests per second (RPS) of the group.

        Can be used with either RATE or UTILIZATION balancing modes,
        but required if RATE mode. For RATE mode, either maxRate or one
        of maxRatePerInstance or maxRatePerEndpoint, as appropriate for
        group type, must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_rate GoogleComputeBackendService#max_rate}
        '''
        result = self._values.get("max_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_rate_per_endpoint(self) -> typing.Optional[jsii.Number]:
        '''The max requests per second (RPS) that a single backend network endpoint can handle.

        This is used to calculate the capacity of
        the group. Can be used in either balancing mode. For RATE mode,
        either maxRate or maxRatePerEndpoint must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_rate_per_endpoint GoogleComputeBackendService#max_rate_per_endpoint}
        '''
        result = self._values.get("max_rate_per_endpoint")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_rate_per_instance(self) -> typing.Optional[jsii.Number]:
        '''The max requests per second (RPS) that a single backend instance can handle.

        This is used to calculate the capacity of
        the group. Can be used in either balancing mode. For RATE mode,
        either maxRate or maxRatePerInstance must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_rate_per_instance GoogleComputeBackendService#max_rate_per_instance}
        '''
        result = self._values.get("max_rate_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_utilization(self) -> typing.Optional[jsii.Number]:
        '''Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization target for the group. Valid range is [0.0, 1.0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_utilization GoogleComputeBackendService#max_utilization}
        '''
        result = self._values.get("max_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceBackendList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceBackendList",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceBackendList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeBackendServiceBackendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceBackendList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeBackendServiceBackendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceBackend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceBackend]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceBackend]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendServiceBackendOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceBackendOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceBackendOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBalancingMode")
    def reset_balancing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBalancingMode", []))

    @jsii.member(jsii_name="resetCapacityScaler")
    def reset_capacity_scaler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityScaler", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetMaxConnections")
    def reset_max_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnections", []))

    @jsii.member(jsii_name="resetMaxConnectionsPerEndpoint")
    def reset_max_connections_per_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionsPerEndpoint", []))

    @jsii.member(jsii_name="resetMaxConnectionsPerInstance")
    def reset_max_connections_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnectionsPerInstance", []))

    @jsii.member(jsii_name="resetMaxRate")
    def reset_max_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRate", []))

    @jsii.member(jsii_name="resetMaxRatePerEndpoint")
    def reset_max_rate_per_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRatePerEndpoint", []))

    @jsii.member(jsii_name="resetMaxRatePerInstance")
    def reset_max_rate_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRatePerInstance", []))

    @jsii.member(jsii_name="resetMaxUtilization")
    def reset_max_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUtilization", []))

    @builtins.property
    @jsii.member(jsii_name="balancingModeInput")
    def balancing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityScalerInput")
    def capacity_scaler_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityScalerInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPerEndpointInput")
    def max_connections_per_endpoint_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsPerEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPerInstanceInput")
    def max_connections_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRateInput")
    def max_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRatePerEndpointInput")
    def max_rate_per_endpoint_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRatePerEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRatePerInstanceInput")
    def max_rate_per_instance_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRatePerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUtilizationInput")
    def max_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="balancingMode")
    def balancing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancingMode"))

    @balancing_mode.setter
    def balancing_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "balancing_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancingMode", value)

    @builtins.property
    @jsii.member(jsii_name="capacityScaler")
    def capacity_scaler(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacityScaler"))

    @capacity_scaler.setter
    def capacity_scaler(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "capacity_scaler").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityScaler", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPerEndpoint")
    def max_connections_per_endpoint(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionsPerEndpoint"))

    @max_connections_per_endpoint.setter
    def max_connections_per_endpoint(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_connections_per_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionsPerEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsPerInstance")
    def max_connections_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnectionsPerInstance"))

    @max_connections_per_instance.setter
    def max_connections_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_connections_per_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnectionsPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="maxRate")
    def max_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRate"))

    @max_rate.setter
    def max_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRate", value)

    @builtins.property
    @jsii.member(jsii_name="maxRatePerEndpoint")
    def max_rate_per_endpoint(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRatePerEndpoint"))

    @max_rate_per_endpoint.setter
    def max_rate_per_endpoint(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_rate_per_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRatePerEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="maxRatePerInstance")
    def max_rate_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRatePerInstance"))

    @max_rate_per_instance.setter
    def max_rate_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_rate_per_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRatePerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="maxUtilization")
    def max_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUtilization"))

    @max_utilization.setter
    def max_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "max_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeBackendServiceBackend, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeBackendServiceBackend, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeBackendServiceBackend, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceBackendOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "cache_key_policy": "cacheKeyPolicy",
        "cache_mode": "cacheMode",
        "client_ttl": "clientTtl",
        "default_ttl": "defaultTtl",
        "max_ttl": "maxTtl",
        "negative_caching": "negativeCaching",
        "negative_caching_policy": "negativeCachingPolicy",
        "serve_while_stale": "serveWhileStale",
        "signed_url_cache_max_age_sec": "signedUrlCacheMaxAgeSec",
    },
)
class GoogleComputeBackendServiceCdnPolicy:
    def __init__(
        self,
        *,
        cache_key_policy: typing.Optional[typing.Union["GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy", typing.Dict[str, typing.Any]]] = None,
        cache_mode: typing.Optional[builtins.str] = None,
        client_ttl: typing.Optional[jsii.Number] = None,
        default_ttl: typing.Optional[jsii.Number] = None,
        max_ttl: typing.Optional[jsii.Number] = None,
        negative_caching: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        negative_caching_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy", typing.Dict[str, typing.Any]]]]] = None,
        serve_while_stale: typing.Optional[jsii.Number] = None,
        signed_url_cache_max_age_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cache_key_policy: cache_key_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cache_key_policy GoogleComputeBackendService#cache_key_policy}
        :param cache_mode: Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC Possible values: ["USE_ORIGIN_HEADERS", "FORCE_CACHE_ALL", "CACHE_ALL_STATIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cache_mode GoogleComputeBackendService#cache_mode}
        :param client_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#client_ttl GoogleComputeBackendService#client_ttl}
        :param default_ttl: Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#default_ttl GoogleComputeBackendService#default_ttl}
        :param max_ttl: Specifies the maximum allowed TTL for cached content served by this origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_ttl GoogleComputeBackendService#max_ttl}
        :param negative_caching: Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#negative_caching GoogleComputeBackendService#negative_caching}
        :param negative_caching_policy: negative_caching_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#negative_caching_policy GoogleComputeBackendService#negative_caching_policy}
        :param serve_while_stale: Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#serve_while_stale GoogleComputeBackendService#serve_while_stale}
        :param signed_url_cache_max_age_sec: Maximum number of seconds the response to a signed URL request will be considered fresh, defaults to 1hr (3600s). After this time period, the response will be revalidated before being served. When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#signed_url_cache_max_age_sec GoogleComputeBackendService#signed_url_cache_max_age_sec}
        '''
        if isinstance(cache_key_policy, dict):
            cache_key_policy = GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy(**cache_key_policy)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicy.__init__)
            check_type(argname="argument cache_key_policy", value=cache_key_policy, expected_type=type_hints["cache_key_policy"])
            check_type(argname="argument cache_mode", value=cache_mode, expected_type=type_hints["cache_mode"])
            check_type(argname="argument client_ttl", value=client_ttl, expected_type=type_hints["client_ttl"])
            check_type(argname="argument default_ttl", value=default_ttl, expected_type=type_hints["default_ttl"])
            check_type(argname="argument max_ttl", value=max_ttl, expected_type=type_hints["max_ttl"])
            check_type(argname="argument negative_caching", value=negative_caching, expected_type=type_hints["negative_caching"])
            check_type(argname="argument negative_caching_policy", value=negative_caching_policy, expected_type=type_hints["negative_caching_policy"])
            check_type(argname="argument serve_while_stale", value=serve_while_stale, expected_type=type_hints["serve_while_stale"])
            check_type(argname="argument signed_url_cache_max_age_sec", value=signed_url_cache_max_age_sec, expected_type=type_hints["signed_url_cache_max_age_sec"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cache_key_policy is not None:
            self._values["cache_key_policy"] = cache_key_policy
        if cache_mode is not None:
            self._values["cache_mode"] = cache_mode
        if client_ttl is not None:
            self._values["client_ttl"] = client_ttl
        if default_ttl is not None:
            self._values["default_ttl"] = default_ttl
        if max_ttl is not None:
            self._values["max_ttl"] = max_ttl
        if negative_caching is not None:
            self._values["negative_caching"] = negative_caching
        if negative_caching_policy is not None:
            self._values["negative_caching_policy"] = negative_caching_policy
        if serve_while_stale is not None:
            self._values["serve_while_stale"] = serve_while_stale
        if signed_url_cache_max_age_sec is not None:
            self._values["signed_url_cache_max_age_sec"] = signed_url_cache_max_age_sec

    @builtins.property
    def cache_key_policy(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy"]:
        '''cache_key_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cache_key_policy GoogleComputeBackendService#cache_key_policy}
        '''
        result = self._values.get("cache_key_policy")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy"], result)

    @builtins.property
    def cache_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies the cache setting for all responses from this backend.

        The possible values are: USE_ORIGIN_HEADERS, FORCE_CACHE_ALL and CACHE_ALL_STATIC Possible values: ["USE_ORIGIN_HEADERS", "FORCE_CACHE_ALL", "CACHE_ALL_STATIC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cache_mode GoogleComputeBackendService#cache_mode}
        '''
        result = self._values.get("cache_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum allowed TTL for cached content served by this origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#client_ttl GoogleComputeBackendService#client_ttl}
        '''
        result = self._values.get("client_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-max-age).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#default_ttl GoogleComputeBackendService#default_ttl}
        '''
        result = self._values.get("default_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum allowed TTL for cached content served by this origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_ttl GoogleComputeBackendService#max_ttl}
        '''
        result = self._values.get("max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def negative_caching(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#negative_caching GoogleComputeBackendService#negative_caching}
        '''
        result = self._values.get("negative_caching")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def negative_caching_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy"]]]:
        '''negative_caching_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#negative_caching_policy GoogleComputeBackendService#negative_caching_policy}
        '''
        result = self._values.get("negative_caching_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy"]]], result)

    @builtins.property
    def serve_while_stale(self) -> typing.Optional[jsii.Number]:
        '''Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#serve_while_stale GoogleComputeBackendService#serve_while_stale}
        '''
        result = self._values.get("serve_while_stale")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def signed_url_cache_max_age_sec(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of seconds the response to a signed URL request will be considered fresh, defaults to 1hr (3600s).

        After this
        time period, the response will be revalidated before
        being served.

        When serving responses to signed URL requests, Cloud CDN will
        internally behave as though all responses from this backend had a
        "Cache-Control: public, max-age=[TTL]" header, regardless of any
        existing Cache-Control header. The actual headers served in
        responses will not be altered.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#signed_url_cache_max_age_sec GoogleComputeBackendService#signed_url_cache_max_age_sec}
        '''
        result = self._values.get("signed_url_cache_max_age_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceCdnPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "include_host": "includeHost",
        "include_named_cookies": "includeNamedCookies",
        "include_protocol": "includeProtocol",
        "include_query_string": "includeQueryString",
        "query_string_blacklist": "queryStringBlacklist",
        "query_string_whitelist": "queryStringWhitelist",
    },
)
class GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy:
    def __init__(
        self,
        *,
        include_host: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_named_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_protocol: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_query_string: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        query_string_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param include_host: If true requests to different hosts will be cached separately. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_host GoogleComputeBackendService#include_host}
        :param include_named_cookies: Names of cookies to include in cache keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_named_cookies GoogleComputeBackendService#include_named_cookies}
        :param include_protocol: If true, http and https requests will be cached separately. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_protocol GoogleComputeBackendService#include_protocol}
        :param include_query_string: If true, include query string parameters in the cache key according to query_string_whitelist and query_string_blacklist. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_query_string GoogleComputeBackendService#include_query_string}
        :param query_string_blacklist: Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify query_string_whitelist or query_string_blacklist, not both. '&' and '=' will be percent encoded and not treated as delimiters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#query_string_blacklist GoogleComputeBackendService#query_string_blacklist}
        :param query_string_whitelist: Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify query_string_whitelist or query_string_blacklist, not both. '&' and '=' will be percent encoded and not treated as delimiters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#query_string_whitelist GoogleComputeBackendService#query_string_whitelist}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy.__init__)
            check_type(argname="argument include_host", value=include_host, expected_type=type_hints["include_host"])
            check_type(argname="argument include_named_cookies", value=include_named_cookies, expected_type=type_hints["include_named_cookies"])
            check_type(argname="argument include_protocol", value=include_protocol, expected_type=type_hints["include_protocol"])
            check_type(argname="argument include_query_string", value=include_query_string, expected_type=type_hints["include_query_string"])
            check_type(argname="argument query_string_blacklist", value=query_string_blacklist, expected_type=type_hints["query_string_blacklist"])
            check_type(argname="argument query_string_whitelist", value=query_string_whitelist, expected_type=type_hints["query_string_whitelist"])
        self._values: typing.Dict[str, typing.Any] = {}
        if include_host is not None:
            self._values["include_host"] = include_host
        if include_named_cookies is not None:
            self._values["include_named_cookies"] = include_named_cookies
        if include_protocol is not None:
            self._values["include_protocol"] = include_protocol
        if include_query_string is not None:
            self._values["include_query_string"] = include_query_string
        if query_string_blacklist is not None:
            self._values["query_string_blacklist"] = query_string_blacklist
        if query_string_whitelist is not None:
            self._values["query_string_whitelist"] = query_string_whitelist

    @builtins.property
    def include_host(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true requests to different hosts will be cached separately.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_host GoogleComputeBackendService#include_host}
        '''
        result = self._values.get("include_host")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_named_cookies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of cookies to include in cache keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_named_cookies GoogleComputeBackendService#include_named_cookies}
        '''
        result = self._values.get("include_named_cookies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_protocol(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, http and https requests will be cached separately.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_protocol GoogleComputeBackendService#include_protocol}
        '''
        result = self._values.get("include_protocol")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include_query_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, include query string parameters in the cache key according to query_string_whitelist and query_string_blacklist.

        If neither is set, the entire query
        string will be included.

        If false, the query string will be excluded from the cache
        key entirely.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_query_string GoogleComputeBackendService#include_query_string}
        '''
        result = self._values.get("include_query_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def query_string_blacklist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of query string parameters to exclude in cache keys.

        All other parameters will be included. Either specify
        query_string_whitelist or query_string_blacklist, not both.
        '&' and '=' will be percent encoded and not treated as
        delimiters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#query_string_blacklist GoogleComputeBackendService#query_string_blacklist}
        '''
        result = self._values.get("query_string_blacklist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of query string parameters to include in cache keys.

        All other parameters will be excluded. Either specify
        query_string_whitelist or query_string_blacklist, not both.
        '&' and '=' will be percent encoded and not treated as
        delimiters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#query_string_whitelist GoogleComputeBackendService#query_string_whitelist}
        '''
        result = self._values.get("query_string_whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIncludeHost")
    def reset_include_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeHost", []))

    @jsii.member(jsii_name="resetIncludeNamedCookies")
    def reset_include_named_cookies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeNamedCookies", []))

    @jsii.member(jsii_name="resetIncludeProtocol")
    def reset_include_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeProtocol", []))

    @jsii.member(jsii_name="resetIncludeQueryString")
    def reset_include_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeQueryString", []))

    @jsii.member(jsii_name="resetQueryStringBlacklist")
    def reset_query_string_blacklist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringBlacklist", []))

    @jsii.member(jsii_name="resetQueryStringWhitelist")
    def reset_query_string_whitelist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringWhitelist", []))

    @builtins.property
    @jsii.member(jsii_name="includeHostInput")
    def include_host_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeHostInput"))

    @builtins.property
    @jsii.member(jsii_name="includeNamedCookiesInput")
    def include_named_cookies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeNamedCookiesInput"))

    @builtins.property
    @jsii.member(jsii_name="includeProtocolInput")
    def include_protocol_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="includeQueryStringInput")
    def include_query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "includeQueryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringBlacklistInput")
    def query_string_blacklist_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringBlacklistInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringWhitelistInput")
    def query_string_whitelist_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringWhitelistInput"))

    @builtins.property
    @jsii.member(jsii_name="includeHost")
    def include_host(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeHost"))

    @include_host.setter
    def include_host(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "include_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeHost", value)

    @builtins.property
    @jsii.member(jsii_name="includeNamedCookies")
    def include_named_cookies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includeNamedCookies"))

    @include_named_cookies.setter
    def include_named_cookies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "include_named_cookies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeNamedCookies", value)

    @builtins.property
    @jsii.member(jsii_name="includeProtocol")
    def include_protocol(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeProtocol"))

    @include_protocol.setter
    def include_protocol(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "include_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="includeQueryString")
    def include_query_string(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "includeQueryString"))

    @include_query_string.setter
    def include_query_string(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "include_query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeQueryString", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringBlacklist")
    def query_string_blacklist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringBlacklist"))

    @query_string_blacklist.setter
    def query_string_blacklist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "query_string_blacklist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringBlacklist", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringWhitelist")
    def query_string_whitelist(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringWhitelist"))

    @query_string_whitelist.setter
    def query_string_whitelist(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "query_string_whitelist").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringWhitelist", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "ttl": "ttl"},
)
class GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy:
    def __init__(
        self,
        *,
        code: typing.Optional[jsii.Number] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param code: The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#code GoogleComputeBackendService#code}
        :param ttl: The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#ttl GoogleComputeBackendService#ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy.__init__)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if code is not None:
            self._values["code"] = code
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def code(self) -> typing.Optional[jsii.Number]:
        '''The HTTP status code to define a TTL against.

        Only HTTP status codes 300, 301, 308, 404, 405, 410, 421, 451 and 501
        can be specified as values, and you cannot specify a status code more than once.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#code GoogleComputeBackendService#code}
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''The TTL (in seconds) for which to cache responses with the corresponding status code.

        The maximum allowed value is 1800s
        (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#ttl GoogleComputeBackendService#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCode")
    def reset_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCode", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="codeInput")
    def code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "codeInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "code"))

    @code.setter
    def code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference, "code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "code", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendServiceCdnPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCdnPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCacheKeyPolicy")
    def put_cache_key_policy(
        self,
        *,
        include_host: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_named_cookies: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_protocol: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include_query_string: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        query_string_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param include_host: If true requests to different hosts will be cached separately. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_host GoogleComputeBackendService#include_host}
        :param include_named_cookies: Names of cookies to include in cache keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_named_cookies GoogleComputeBackendService#include_named_cookies}
        :param include_protocol: If true, http and https requests will be cached separately. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_protocol GoogleComputeBackendService#include_protocol}
        :param include_query_string: If true, include query string parameters in the cache key according to query_string_whitelist and query_string_blacklist. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#include_query_string GoogleComputeBackendService#include_query_string}
        :param query_string_blacklist: Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify query_string_whitelist or query_string_blacklist, not both. '&' and '=' will be percent encoded and not treated as delimiters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#query_string_blacklist GoogleComputeBackendService#query_string_blacklist}
        :param query_string_whitelist: Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify query_string_whitelist or query_string_blacklist, not both. '&' and '=' will be percent encoded and not treated as delimiters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#query_string_whitelist GoogleComputeBackendService#query_string_whitelist}
        '''
        value = GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy(
            include_host=include_host,
            include_named_cookies=include_named_cookies,
            include_protocol=include_protocol,
            include_query_string=include_query_string,
            query_string_blacklist=query_string_blacklist,
            query_string_whitelist=query_string_whitelist,
        )

        return typing.cast(None, jsii.invoke(self, "putCacheKeyPolicy", [value]))

    @jsii.member(jsii_name="putNegativeCachingPolicy")
    def put_negative_caching_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCdnPolicyOutputReference.put_negative_caching_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNegativeCachingPolicy", [value]))

    @jsii.member(jsii_name="resetCacheKeyPolicy")
    def reset_cache_key_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKeyPolicy", []))

    @jsii.member(jsii_name="resetCacheMode")
    def reset_cache_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheMode", []))

    @jsii.member(jsii_name="resetClientTtl")
    def reset_client_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTtl", []))

    @jsii.member(jsii_name="resetDefaultTtl")
    def reset_default_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultTtl", []))

    @jsii.member(jsii_name="resetMaxTtl")
    def reset_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTtl", []))

    @jsii.member(jsii_name="resetNegativeCaching")
    def reset_negative_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegativeCaching", []))

    @jsii.member(jsii_name="resetNegativeCachingPolicy")
    def reset_negative_caching_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegativeCachingPolicy", []))

    @jsii.member(jsii_name="resetServeWhileStale")
    def reset_serve_while_stale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServeWhileStale", []))

    @jsii.member(jsii_name="resetSignedUrlCacheMaxAgeSec")
    def reset_signed_url_cache_max_age_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignedUrlCacheMaxAgeSec", []))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyPolicy")
    def cache_key_policy(
        self,
    ) -> GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference:
        return typing.cast(GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference, jsii.get(self, "cacheKeyPolicy"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingPolicy")
    def negative_caching_policy(
        self,
    ) -> GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList:
        return typing.cast(GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList, jsii.get(self, "negativeCachingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyPolicyInput")
    def cache_key_policy_input(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy], jsii.get(self, "cacheKeyPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheModeInput")
    def cache_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheModeInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTtlInput")
    def client_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTtlInput")
    def default_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTtlInput")
    def max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingInput")
    def negative_caching_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negativeCachingInput"))

    @builtins.property
    @jsii.member(jsii_name="negativeCachingPolicyInput")
    def negative_caching_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy]]], jsii.get(self, "negativeCachingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="serveWhileStaleInput")
    def serve_while_stale_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "serveWhileStaleInput"))

    @builtins.property
    @jsii.member(jsii_name="signedUrlCacheMaxAgeSecInput")
    def signed_url_cache_max_age_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "signedUrlCacheMaxAgeSecInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheMode")
    def cache_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheMode"))

    @cache_mode.setter
    def cache_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "cache_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheMode", value)

    @builtins.property
    @jsii.member(jsii_name="clientTtl")
    def client_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientTtl"))

    @client_ttl.setter
    def client_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "client_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTtl", value)

    @builtins.property
    @jsii.member(jsii_name="defaultTtl")
    def default_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultTtl"))

    @default_ttl.setter
    def default_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "default_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTtl", value)

    @builtins.property
    @jsii.member(jsii_name="maxTtl")
    def max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTtl"))

    @max_ttl.setter
    def max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="negativeCaching")
    def negative_caching(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negativeCaching"))

    @negative_caching.setter
    def negative_caching(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "negative_caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negativeCaching", value)

    @builtins.property
    @jsii.member(jsii_name="serveWhileStale")
    def serve_while_stale(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "serveWhileStale"))

    @serve_while_stale.setter
    def serve_while_stale(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "serve_while_stale").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serveWhileStale", value)

    @builtins.property
    @jsii.member(jsii_name="signedUrlCacheMaxAgeSec")
    def signed_url_cache_max_age_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "signedUrlCacheMaxAgeSec"))

    @signed_url_cache_max_age_sec.setter
    def signed_url_cache_max_age_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "signed_url_cache_max_age_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signedUrlCacheMaxAgeSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeBackendServiceCdnPolicy]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCdnPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceCdnPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCdnPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCircuitBreakers",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "max_pending_requests": "maxPendingRequests",
        "max_requests": "maxRequests",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
    },
)
class GoogleComputeBackendServiceCircuitBreakers:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[typing.Union["GoogleComputeBackendServiceCircuitBreakersConnectTimeout", typing.Dict[str, typing.Any]]] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        max_pending_requests: typing.Optional[jsii.Number] = None,
        max_requests: typing.Optional[jsii.Number] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connect_timeout: connect_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#connect_timeout GoogleComputeBackendService#connect_timeout}
        :param max_connections: The maximum number of connections to the backend cluster. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections GoogleComputeBackendService#max_connections}
        :param max_pending_requests: The maximum number of pending requests to the backend cluster. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_pending_requests GoogleComputeBackendService#max_pending_requests}
        :param max_requests: The maximum number of parallel requests to the backend cluster. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_requests GoogleComputeBackendService#max_requests}
        :param max_requests_per_connection: Maximum requests for a single backend connection. This parameter is respected by both the HTTP/1.1 and HTTP/2 implementations. If not specified, there is no limit. Setting this parameter to 1 will effectively disable keep alive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_requests_per_connection GoogleComputeBackendService#max_requests_per_connection}
        :param max_retries: The maximum number of parallel retries to the backend cluster. Defaults to 3. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_retries GoogleComputeBackendService#max_retries}
        '''
        if isinstance(connect_timeout, dict):
            connect_timeout = GoogleComputeBackendServiceCircuitBreakersConnectTimeout(**connect_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCircuitBreakers.__init__)
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument max_pending_requests", value=max_pending_requests, expected_type=type_hints["max_pending_requests"])
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
            check_type(argname="argument max_requests_per_connection", value=max_requests_per_connection, expected_type=type_hints["max_requests_per_connection"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if max_pending_requests is not None:
            self._values["max_pending_requests"] = max_pending_requests
        if max_requests is not None:
            self._values["max_requests"] = max_requests
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries

    @builtins.property
    def connect_timeout(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceCircuitBreakersConnectTimeout"]:
        '''connect_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#connect_timeout GoogleComputeBackendService#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceCircuitBreakersConnectTimeout"], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of connections to the backend cluster. Defaults to 1024.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_connections GoogleComputeBackendService#max_connections}
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of pending requests to the backend cluster. Defaults to 1024.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_pending_requests GoogleComputeBackendService#max_pending_requests}
        '''
        result = self._values.get("max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_requests(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of parallel requests to the backend cluster. Defaults to 1024.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_requests GoogleComputeBackendService#max_requests}
        '''
        result = self._values.get("max_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        '''Maximum requests for a single backend connection.

        This parameter
        is respected by both the HTTP/1.1 and HTTP/2 implementations. If
        not specified, there is no limit. Setting this parameter to 1
        will effectively disable keep alive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_requests_per_connection GoogleComputeBackendService#max_requests_per_connection}
        '''
        result = self._values.get("max_requests_per_connection")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of parallel retries to the backend cluster. Defaults to 3.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_retries GoogleComputeBackendService#max_retries}
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceCircuitBreakers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCircuitBreakersConnectTimeout",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeBackendServiceCircuitBreakersConnectTimeout:
    def __init__(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCircuitBreakersConnectTimeout.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> jsii.Number:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations less than one second are represented
        with a 0 seconds field and a positive nanos field. Must
        be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceCircuitBreakersConnectTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceCircuitBreakersConnectTimeout]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCircuitBreakersConnectTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceCircuitBreakersConnectTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendServiceCircuitBreakersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceCircuitBreakersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceCircuitBreakersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConnectTimeout")
    def put_connect_timeout(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        value = GoogleComputeBackendServiceCircuitBreakersConnectTimeout(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putConnectTimeout", [value]))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetMaxConnections")
    def reset_max_connections(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConnections", []))

    @jsii.member(jsii_name="resetMaxPendingRequests")
    def reset_max_pending_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPendingRequests", []))

    @jsii.member(jsii_name="resetMaxRequests")
    def reset_max_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRequests", []))

    @jsii.member(jsii_name="resetMaxRequestsPerConnection")
    def reset_max_requests_per_connection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRequestsPerConnection", []))

    @jsii.member(jsii_name="resetMaxRetries")
    def reset_max_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetries", []))

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(
        self,
    ) -> GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference:
        return typing.cast(GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference, jsii.get(self, "connectTimeout"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceCircuitBreakersConnectTimeout]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCircuitBreakersConnectTimeout], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequestsInput")
    def max_pending_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPendingRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequestsInput")
    def max_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequestsPerConnectionInput")
    def max_requests_per_connection_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestsPerConnectionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersOutputReference, "max_connections").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequests")
    def max_pending_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPendingRequests"))

    @max_pending_requests.setter
    def max_pending_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersOutputReference, "max_pending_requests").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPendingRequests", value)

    @builtins.property
    @jsii.member(jsii_name="maxRequests")
    def max_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequests"))

    @max_requests.setter
    def max_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersOutputReference, "max_requests").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="maxRequestsPerConnection")
    def max_requests_per_connection(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequestsPerConnection"))

    @max_requests_per_connection.setter
    def max_requests_per_connection(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersOutputReference, "max_requests_per_connection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequestsPerConnection", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersOutputReference, "max_retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceCircuitBreakers]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCircuitBreakers], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceCircuitBreakers],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceCircuitBreakersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConfig",
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
        "affinity_cookie_ttl_sec": "affinityCookieTtlSec",
        "backend": "backend",
        "cdn_policy": "cdnPolicy",
        "circuit_breakers": "circuitBreakers",
        "connection_draining_timeout_sec": "connectionDrainingTimeoutSec",
        "consistent_hash": "consistentHash",
        "custom_request_headers": "customRequestHeaders",
        "custom_response_headers": "customResponseHeaders",
        "description": "description",
        "enable_cdn": "enableCdn",
        "health_checks": "healthChecks",
        "iap": "iap",
        "id": "id",
        "load_balancing_scheme": "loadBalancingScheme",
        "locality_lb_policy": "localityLbPolicy",
        "log_config": "logConfig",
        "outlier_detection": "outlierDetection",
        "port_name": "portName",
        "project": "project",
        "protocol": "protocol",
        "security_policy": "securityPolicy",
        "security_settings": "securitySettings",
        "session_affinity": "sessionAffinity",
        "timeouts": "timeouts",
        "timeout_sec": "timeoutSec",
    },
)
class GoogleComputeBackendServiceConfig(cdktf.TerraformMetaArguments):
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
        affinity_cookie_ttl_sec: typing.Optional[jsii.Number] = None,
        backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeBackendServiceBackend, typing.Dict[str, typing.Any]]]]] = None,
        cdn_policy: typing.Optional[typing.Union[GoogleComputeBackendServiceCdnPolicy, typing.Dict[str, typing.Any]]] = None,
        circuit_breakers: typing.Optional[typing.Union[GoogleComputeBackendServiceCircuitBreakers, typing.Dict[str, typing.Any]]] = None,
        connection_draining_timeout_sec: typing.Optional[jsii.Number] = None,
        consistent_hash: typing.Optional[typing.Union["GoogleComputeBackendServiceConsistentHash", typing.Dict[str, typing.Any]]] = None,
        custom_request_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_cdn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        health_checks: typing.Optional[typing.Sequence[builtins.str]] = None,
        iap: typing.Optional[typing.Union["GoogleComputeBackendServiceIap", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancing_scheme: typing.Optional[builtins.str] = None,
        locality_lb_policy: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeBackendServiceLogConfig", typing.Dict[str, typing.Any]]] = None,
        outlier_detection: typing.Optional[typing.Union["GoogleComputeBackendServiceOutlierDetection", typing.Dict[str, typing.Any]]] = None,
        port_name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        security_policy: typing.Optional[builtins.str] = None,
        security_settings: typing.Optional[typing.Union["GoogleComputeBackendServiceSecuritySettings", typing.Dict[str, typing.Any]]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeBackendServiceTimeouts", typing.Dict[str, typing.Any]]] = None,
        timeout_sec: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#name GoogleComputeBackendService#name}
        :param affinity_cookie_ttl_sec: Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day. When the load balancing scheme is INTERNAL, this field is not used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#affinity_cookie_ttl_sec GoogleComputeBackendService#affinity_cookie_ttl_sec}
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#backend GoogleComputeBackendService#backend}
        :param cdn_policy: cdn_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cdn_policy GoogleComputeBackendService#cdn_policy}
        :param circuit_breakers: circuit_breakers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#circuit_breakers GoogleComputeBackendService#circuit_breakers}
        :param connection_draining_timeout_sec: Time for which instance will be drained (not accept new connections, but still work to finish started). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#connection_draining_timeout_sec GoogleComputeBackendService#connection_draining_timeout_sec}
        :param consistent_hash: consistent_hash block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consistent_hash GoogleComputeBackendService#consistent_hash}
        :param custom_request_headers: Headers that the HTTP/S load balancer should add to proxied requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#custom_request_headers GoogleComputeBackendService#custom_request_headers}
        :param custom_response_headers: Headers that the HTTP/S load balancer should add to proxied responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#custom_response_headers GoogleComputeBackendService#custom_response_headers}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#description GoogleComputeBackendService#description}
        :param enable_cdn: If true, enable Cloud CDN for this BackendService. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enable_cdn GoogleComputeBackendService#enable_cdn}
        :param health_checks: The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently at most one health check can be specified. A health check must be specified unless the backend service uses an internet or serverless NEG as a backend. For internal load balancing, a URL to a HealthCheck resource must be specified instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#health_checks GoogleComputeBackendService#health_checks}
        :param iap: iap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#iap GoogleComputeBackendService#iap}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#id GoogleComputeBackendService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancing_scheme: Indicates whether the backend service will be used with internal or external load balancing. A backend service created for one type of load balancing cannot be used with the other. For more information, refer to `Choosing a load balancer <https://cloud.google.com/load-balancing/docs/backend-service>`_. Default value: "EXTERNAL" Possible values: ["EXTERNAL", "INTERNAL_SELF_MANAGED", "EXTERNAL_MANAGED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#load_balancing_scheme GoogleComputeBackendService#load_balancing_scheme}
        :param locality_lb_policy: The load balancing algorithm used within the scope of the locality. The possible values are:. 'ROUND_ROBIN': This is a simple policy in which each healthy backend is selected in round robin order. 'LEAST_REQUEST': An O(1) algorithm which selects two random healthy hosts and picks the host which has fewer active requests. 'RING_HASH': The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests. 'RANDOM': The load balancer selects a random healthy host. 'ORIGINAL_DESTINATION': Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer. 'MAGLEV': used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, refer to https://ai.google/research/pubs/pub44824 This field is applicable to either: A regional backend service with the service_protocol set to HTTP, HTTPS, or HTTP2, and loadBalancingScheme set to INTERNAL_MANAGED. A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED. If session_affinity is not NONE, and this field is not set to MAGLEV or RING_HASH, session affinity settings will not take effect. Only ROUND_ROBIN and RING_HASH are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validate_for_proxyless field set to true. Possible values: ["ROUND_ROBIN", "LEAST_REQUEST", "RING_HASH", "RANDOM", "ORIGINAL_DESTINATION", "MAGLEV"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#locality_lb_policy GoogleComputeBackendService#locality_lb_policy}
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#log_config GoogleComputeBackendService#log_config}
        :param outlier_detection: outlier_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#outlier_detection GoogleComputeBackendService#outlier_detection}
        :param port_name: Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the load balancing scheme is EXTERNAL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#port_name GoogleComputeBackendService#port_name}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#project GoogleComputeBackendService#project}.
        :param protocol: The protocol this BackendService uses to communicate with backends. The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer types and may result in errors if used with the GA API. Possible values: ["HTTP", "HTTPS", "HTTP2", "TCP", "SSL", "GRPC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#protocol GoogleComputeBackendService#protocol}
        :param security_policy: The security policy associated with this backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#security_policy GoogleComputeBackendService#security_policy}
        :param security_settings: security_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#security_settings GoogleComputeBackendService#security_settings}
        :param session_affinity: Type of session affinity to use. The default is NONE. Session affinity is not applicable if the protocol is UDP. Possible values: ["NONE", "CLIENT_IP", "CLIENT_IP_PORT_PROTO", "CLIENT_IP_PROTO", "GENERATED_COOKIE", "HEADER_FIELD", "HTTP_COOKIE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#session_affinity GoogleComputeBackendService#session_affinity}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#timeouts GoogleComputeBackendService#timeouts}
        :param timeout_sec: How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is [1, 86400]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#timeout_sec GoogleComputeBackendService#timeout_sec}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cdn_policy, dict):
            cdn_policy = GoogleComputeBackendServiceCdnPolicy(**cdn_policy)
        if isinstance(circuit_breakers, dict):
            circuit_breakers = GoogleComputeBackendServiceCircuitBreakers(**circuit_breakers)
        if isinstance(consistent_hash, dict):
            consistent_hash = GoogleComputeBackendServiceConsistentHash(**consistent_hash)
        if isinstance(iap, dict):
            iap = GoogleComputeBackendServiceIap(**iap)
        if isinstance(log_config, dict):
            log_config = GoogleComputeBackendServiceLogConfig(**log_config)
        if isinstance(outlier_detection, dict):
            outlier_detection = GoogleComputeBackendServiceOutlierDetection(**outlier_detection)
        if isinstance(security_settings, dict):
            security_settings = GoogleComputeBackendServiceSecuritySettings(**security_settings)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeBackendServiceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument affinity_cookie_ttl_sec", value=affinity_cookie_ttl_sec, expected_type=type_hints["affinity_cookie_ttl_sec"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument cdn_policy", value=cdn_policy, expected_type=type_hints["cdn_policy"])
            check_type(argname="argument circuit_breakers", value=circuit_breakers, expected_type=type_hints["circuit_breakers"])
            check_type(argname="argument connection_draining_timeout_sec", value=connection_draining_timeout_sec, expected_type=type_hints["connection_draining_timeout_sec"])
            check_type(argname="argument consistent_hash", value=consistent_hash, expected_type=type_hints["consistent_hash"])
            check_type(argname="argument custom_request_headers", value=custom_request_headers, expected_type=type_hints["custom_request_headers"])
            check_type(argname="argument custom_response_headers", value=custom_response_headers, expected_type=type_hints["custom_response_headers"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_cdn", value=enable_cdn, expected_type=type_hints["enable_cdn"])
            check_type(argname="argument health_checks", value=health_checks, expected_type=type_hints["health_checks"])
            check_type(argname="argument iap", value=iap, expected_type=type_hints["iap"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_balancing_scheme", value=load_balancing_scheme, expected_type=type_hints["load_balancing_scheme"])
            check_type(argname="argument locality_lb_policy", value=locality_lb_policy, expected_type=type_hints["locality_lb_policy"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument outlier_detection", value=outlier_detection, expected_type=type_hints["outlier_detection"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            check_type(argname="argument security_settings", value=security_settings, expected_type=type_hints["security_settings"])
            check_type(argname="argument session_affinity", value=session_affinity, expected_type=type_hints["session_affinity"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timeout_sec", value=timeout_sec, expected_type=type_hints["timeout_sec"])
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
        if affinity_cookie_ttl_sec is not None:
            self._values["affinity_cookie_ttl_sec"] = affinity_cookie_ttl_sec
        if backend is not None:
            self._values["backend"] = backend
        if cdn_policy is not None:
            self._values["cdn_policy"] = cdn_policy
        if circuit_breakers is not None:
            self._values["circuit_breakers"] = circuit_breakers
        if connection_draining_timeout_sec is not None:
            self._values["connection_draining_timeout_sec"] = connection_draining_timeout_sec
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if custom_request_headers is not None:
            self._values["custom_request_headers"] = custom_request_headers
        if custom_response_headers is not None:
            self._values["custom_response_headers"] = custom_response_headers
        if description is not None:
            self._values["description"] = description
        if enable_cdn is not None:
            self._values["enable_cdn"] = enable_cdn
        if health_checks is not None:
            self._values["health_checks"] = health_checks
        if iap is not None:
            self._values["iap"] = iap
        if id is not None:
            self._values["id"] = id
        if load_balancing_scheme is not None:
            self._values["load_balancing_scheme"] = load_balancing_scheme
        if locality_lb_policy is not None:
            self._values["locality_lb_policy"] = locality_lb_policy
        if log_config is not None:
            self._values["log_config"] = log_config
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port_name is not None:
            self._values["port_name"] = port_name
        if project is not None:
            self._values["project"] = project
        if protocol is not None:
            self._values["protocol"] = protocol
        if security_policy is not None:
            self._values["security_policy"] = security_policy
        if security_settings is not None:
            self._values["security_settings"] = security_settings
        if session_affinity is not None:
            self._values["session_affinity"] = session_affinity
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timeout_sec is not None:
            self._values["timeout_sec"] = timeout_sec

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

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#name GoogleComputeBackendService#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def affinity_cookie_ttl_sec(self) -> typing.Optional[jsii.Number]:
        '''Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE.

        If set to 0, the cookie is non-persistent and lasts
        only until the end of the browser session (or equivalent). The
        maximum allowed value for TTL is one day.

        When the load balancing scheme is INTERNAL, this field is not used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#affinity_cookie_ttl_sec GoogleComputeBackendService#affinity_cookie_ttl_sec}
        '''
        result = self._values.get("affinity_cookie_ttl_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backend(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceBackend]]]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#backend GoogleComputeBackendService#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeBackendServiceBackend]]], result)

    @builtins.property
    def cdn_policy(self) -> typing.Optional[GoogleComputeBackendServiceCdnPolicy]:
        '''cdn_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#cdn_policy GoogleComputeBackendService#cdn_policy}
        '''
        result = self._values.get("cdn_policy")
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCdnPolicy], result)

    @builtins.property
    def circuit_breakers(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceCircuitBreakers]:
        '''circuit_breakers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#circuit_breakers GoogleComputeBackendService#circuit_breakers}
        '''
        result = self._values.get("circuit_breakers")
        return typing.cast(typing.Optional[GoogleComputeBackendServiceCircuitBreakers], result)

    @builtins.property
    def connection_draining_timeout_sec(self) -> typing.Optional[jsii.Number]:
        '''Time for which instance will be drained (not accept new connections, but still work to finish started).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#connection_draining_timeout_sec GoogleComputeBackendService#connection_draining_timeout_sec}
        '''
        result = self._values.get("connection_draining_timeout_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceConsistentHash"]:
        '''consistent_hash block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consistent_hash GoogleComputeBackendService#consistent_hash}
        '''
        result = self._values.get("consistent_hash")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceConsistentHash"], result)

    @builtins.property
    def custom_request_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Headers that the HTTP/S load balancer should add to proxied requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#custom_request_headers GoogleComputeBackendService#custom_request_headers}
        '''
        result = self._values.get("custom_request_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_response_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Headers that the HTTP/S load balancer should add to proxied responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#custom_response_headers GoogleComputeBackendService#custom_response_headers}
        '''
        result = self._values.get("custom_response_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#description GoogleComputeBackendService#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_cdn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, enable Cloud CDN for this BackendService.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enable_cdn GoogleComputeBackendService#enable_cdn}
        '''
        result = self._values.get("enable_cdn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def health_checks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService.

        Currently at most one health
        check can be specified.

        A health check must be specified unless the backend service uses an internet
        or serverless NEG as a backend.

        For internal load balancing, a URL to a HealthCheck resource must be specified instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#health_checks GoogleComputeBackendService#health_checks}
        '''
        result = self._values.get("health_checks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def iap(self) -> typing.Optional["GoogleComputeBackendServiceIap"]:
        '''iap block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#iap GoogleComputeBackendService#iap}
        '''
        result = self._values.get("iap")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceIap"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#id GoogleComputeBackendService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancing_scheme(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the backend service will be used with internal or external load balancing.

        A backend service created for one type of
        load balancing cannot be used with the other. For more information, refer to
        `Choosing a load balancer <https://cloud.google.com/load-balancing/docs/backend-service>`_. Default value: "EXTERNAL" Possible values: ["EXTERNAL", "INTERNAL_SELF_MANAGED", "EXTERNAL_MANAGED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#load_balancing_scheme GoogleComputeBackendService#load_balancing_scheme}
        '''
        result = self._values.get("load_balancing_scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locality_lb_policy(self) -> typing.Optional[builtins.str]:
        '''The load balancing algorithm used within the scope of the locality. The possible values are:.

        'ROUND_ROBIN': This is a simple policy in which each healthy backend
        is selected in round robin order.

        'LEAST_REQUEST': An O(1) algorithm which selects two random healthy
        hosts and picks the host which has fewer active requests.

        'RING_HASH': The ring/modulo hash load balancer implements consistent
        hashing to backends. The algorithm has the property that the
        addition/removal of a host from a set of N hosts only affects
        1/N of the requests.

        'RANDOM': The load balancer selects a random healthy host.

        'ORIGINAL_DESTINATION': Backend host is selected based on the client
        connection metadata, i.e., connections are opened
        to the same address as the destination address of
        the incoming connection before the connection
        was redirected to the load balancer.

        'MAGLEV': used as a drop in replacement for the ring hash load balancer.
        Maglev is not as stable as ring hash but has faster table lookup
        build times and host selection times. For more information about
        Maglev, refer to https://ai.google/research/pubs/pub44824

        This field is applicable to either:

        A regional backend service with the service_protocol set to HTTP, HTTPS, or HTTP2,
        and loadBalancingScheme set to INTERNAL_MANAGED.
        A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED.

        If session_affinity is not NONE, and this field is not set to MAGLEV or RING_HASH,
        session affinity settings will not take effect.

        Only ROUND_ROBIN and RING_HASH are supported when the backend service is referenced
        by a URL map that is bound to target gRPC proxy that has validate_for_proxyless
        field set to true. Possible values: ["ROUND_ROBIN", "LEAST_REQUEST", "RING_HASH", "RANDOM", "ORIGINAL_DESTINATION", "MAGLEV"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#locality_lb_policy GoogleComputeBackendService#locality_lb_policy}
        '''
        result = self._values.get("locality_lb_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_config(self) -> typing.Optional["GoogleComputeBackendServiceLogConfig"]:
        '''log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#log_config GoogleComputeBackendService#log_config}
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceLogConfig"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceOutlierDetection"]:
        '''outlier_detection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#outlier_detection GoogleComputeBackendService#outlier_detection}
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceOutlierDetection"], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Name of backend port.

        The same name should appear in the instance
        groups referenced by this service. Required when the load balancing
        scheme is EXTERNAL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#port_name GoogleComputeBackendService#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#project GoogleComputeBackendService#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol this BackendService uses to communicate with backends.

        The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
        types and may result in errors if used with the GA API. Possible values: ["HTTP", "HTTPS", "HTTP2", "TCP", "SSL", "GRPC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#protocol GoogleComputeBackendService#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_policy(self) -> typing.Optional[builtins.str]:
        '''The security policy associated with this backend service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#security_policy GoogleComputeBackendService#security_policy}
        '''
        result = self._values.get("security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_settings(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceSecuritySettings"]:
        '''security_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#security_settings GoogleComputeBackendService#security_settings}
        '''
        result = self._values.get("security_settings")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceSecuritySettings"], result)

    @builtins.property
    def session_affinity(self) -> typing.Optional[builtins.str]:
        '''Type of session affinity to use.

        The default is NONE. Session affinity is
        not applicable if the protocol is UDP. Possible values: ["NONE", "CLIENT_IP", "CLIENT_IP_PORT_PROTO", "CLIENT_IP_PROTO", "GENERATED_COOKIE", "HEADER_FIELD", "HTTP_COOKIE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#session_affinity GoogleComputeBackendService#session_affinity}
        '''
        result = self._values.get("session_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeBackendServiceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#timeouts GoogleComputeBackendService#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceTimeouts"], result)

    @builtins.property
    def timeout_sec(self) -> typing.Optional[jsii.Number]:
        '''How many seconds to wait for the backend before considering it a failed request.

        Default is 30 seconds. Valid range is [1, 86400].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#timeout_sec GoogleComputeBackendService#timeout_sec}
        '''
        result = self._values.get("timeout_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "minimum_ring_size": "minimumRingSize",
    },
)
class GoogleComputeBackendServiceConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional[typing.Union["GoogleComputeBackendServiceConsistentHashHttpCookie", typing.Dict[str, typing.Any]]] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param http_cookie: http_cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#http_cookie GoogleComputeBackendService#http_cookie}
        :param http_header_name: The hash based on the value of the specified header field. This field is applicable if the sessionAffinity is set to HEADER_FIELD. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#http_header_name GoogleComputeBackendService#http_header_name}
        :param minimum_ring_size: The minimum number of virtual nodes to use for the hash ring. Larger ring sizes result in more granular load distributions. If the number of hosts in the load balancing pool is larger than the ring size, each host will be assigned a single virtual node. Defaults to 1024. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#minimum_ring_size GoogleComputeBackendService#minimum_ring_size}
        '''
        if isinstance(http_cookie, dict):
            http_cookie = GoogleComputeBackendServiceConsistentHashHttpCookie(**http_cookie)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConsistentHash.__init__)
            check_type(argname="argument http_cookie", value=http_cookie, expected_type=type_hints["http_cookie"])
            check_type(argname="argument http_header_name", value=http_header_name, expected_type=type_hints["http_header_name"])
            check_type(argname="argument minimum_ring_size", value=minimum_ring_size, expected_type=type_hints["minimum_ring_size"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceConsistentHashHttpCookie"]:
        '''http_cookie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#http_cookie GoogleComputeBackendService#http_cookie}
        '''
        result = self._values.get("http_cookie")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceConsistentHashHttpCookie"], result)

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        '''The hash based on the value of the specified header field.

        This field is applicable if the sessionAffinity is set to HEADER_FIELD.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#http_header_name GoogleComputeBackendService#http_header_name}
        '''
        result = self._values.get("http_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of virtual nodes to use for the hash ring.

        Larger ring sizes result in more granular load
        distributions. If the number of hosts in the load balancing pool
        is larger than the ring size, each host will be assigned a single
        virtual node.
        Defaults to 1024.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#minimum_ring_size GoogleComputeBackendService#minimum_ring_size}
        '''
        result = self._values.get("minimum_ring_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class GoogleComputeBackendServiceConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[typing.Union["GoogleComputeBackendServiceConsistentHashHttpCookieTtl", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the cookie. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#name GoogleComputeBackendService#name}
        :param path: Path to set for the cookie. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#path GoogleComputeBackendService#path}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#ttl GoogleComputeBackendService#ttl}
        '''
        if isinstance(ttl, dict):
            ttl = GoogleComputeBackendServiceConsistentHashHttpCookieTtl(**ttl)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConsistentHashHttpCookie.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the cookie.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#name GoogleComputeBackendService#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to set for the cookie.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#path GoogleComputeBackendService#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceConsistentHashHttpCookieTtl"]:
        '''ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#ttl GoogleComputeBackendService#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceConsistentHashHttpCookieTtl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTtl")
    def put_ttl(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        value = GoogleComputeBackendServiceConsistentHashHttpCookieTtl(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putTtl", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(
        self,
    ) -> "GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference":
        return typing.cast("GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference", jsii.get(self, "ttl"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceConsistentHashHttpCookieTtl"]:
        return typing.cast(typing.Optional["GoogleComputeBackendServiceConsistentHashHttpCookieTtl"], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookie]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookie], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookie],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConsistentHashHttpCookieTtl",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeBackendServiceConsistentHashHttpCookieTtl:
    def __init__(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 seconds field and a positive nanos field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConsistentHashHttpCookieTtl.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> jsii.Number:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations less than one second are represented
        with a 0 seconds field and a positive nanos field. Must
        be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceConsistentHashHttpCookieTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookieTtl]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookieTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookieTtl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendServiceConsistentHashOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceConsistentHashOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceConsistentHashOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpCookie")
    def put_http_cookie(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[typing.Union[GoogleComputeBackendServiceConsistentHashHttpCookieTtl, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the cookie. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#name GoogleComputeBackendService#name}
        :param path: Path to set for the cookie. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#path GoogleComputeBackendService#path}
        :param ttl: ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#ttl GoogleComputeBackendService#ttl}
        '''
        value = GoogleComputeBackendServiceConsistentHashHttpCookie(
            name=name, path=path, ttl=ttl
        )

        return typing.cast(None, jsii.invoke(self, "putHttpCookie", [value]))

    @jsii.member(jsii_name="resetHttpCookie")
    def reset_http_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpCookie", []))

    @jsii.member(jsii_name="resetHttpHeaderName")
    def reset_http_header_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaderName", []))

    @jsii.member(jsii_name="resetMinimumRingSize")
    def reset_minimum_ring_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumRingSize", []))

    @builtins.property
    @jsii.member(jsii_name="httpCookie")
    def http_cookie(
        self,
    ) -> GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference:
        return typing.cast(GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference, jsii.get(self, "httpCookie"))

    @builtins.property
    @jsii.member(jsii_name="httpCookieInput")
    def http_cookie_input(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookie]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceConsistentHashHttpCookie], jsii.get(self, "httpCookieInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderNameInput")
    def http_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumRingSizeInput")
    def minimum_ring_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumRingSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderName")
    def http_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpHeaderName"))

    @http_header_name.setter
    def http_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashOutputReference, "http_header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="minimumRingSize")
    def minimum_ring_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumRingSize"))

    @minimum_ring_size.setter
    def minimum_ring_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashOutputReference, "minimum_ring_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumRingSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceConsistentHash]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceConsistentHash], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceConsistentHash],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceConsistentHashOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceIap",
    jsii_struct_bases=[],
    name_mapping={
        "oauth2_client_id": "oauth2ClientId",
        "oauth2_client_secret": "oauth2ClientSecret",
    },
)
class GoogleComputeBackendServiceIap:
    def __init__(
        self,
        *,
        oauth2_client_id: builtins.str,
        oauth2_client_secret: builtins.str,
    ) -> None:
        '''
        :param oauth2_client_id: OAuth2 Client ID for IAP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#oauth2_client_id GoogleComputeBackendService#oauth2_client_id}
        :param oauth2_client_secret: OAuth2 Client Secret for IAP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#oauth2_client_secret GoogleComputeBackendService#oauth2_client_secret}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceIap.__init__)
            check_type(argname="argument oauth2_client_id", value=oauth2_client_id, expected_type=type_hints["oauth2_client_id"])
            check_type(argname="argument oauth2_client_secret", value=oauth2_client_secret, expected_type=type_hints["oauth2_client_secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "oauth2_client_id": oauth2_client_id,
            "oauth2_client_secret": oauth2_client_secret,
        }

    @builtins.property
    def oauth2_client_id(self) -> builtins.str:
        '''OAuth2 Client ID for IAP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#oauth2_client_id GoogleComputeBackendService#oauth2_client_id}
        '''
        result = self._values.get("oauth2_client_id")
        assert result is not None, "Required property 'oauth2_client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth2_client_secret(self) -> builtins.str:
        '''OAuth2 Client Secret for IAP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#oauth2_client_secret GoogleComputeBackendService#oauth2_client_secret}
        '''
        result = self._values.get("oauth2_client_secret")
        assert result is not None, "Required property 'oauth2_client_secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceIap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceIapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceIapOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceIapOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecretSha256")
    def oauth2_client_secret_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientSecretSha256"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientIdInput")
    def oauth2_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauth2ClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecretInput")
    def oauth2_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauth2ClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientId")
    def oauth2_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientId"))

    @oauth2_client_id.setter
    def oauth2_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceIapOutputReference, "oauth2_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2ClientId", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientSecret"))

    @oauth2_client_secret.setter
    def oauth2_client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceIapOutputReference, "oauth2_client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2ClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeBackendServiceIap]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceIap], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceIap],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceIapOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceLogConfig",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable", "sample_rate": "sampleRate"},
)
class GoogleComputeBackendServiceLogConfig:
    def __init__(
        self,
        *,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sample_rate: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enable: Whether to enable logging for the load balancer traffic served by this backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enable GoogleComputeBackendService#enable}
        :param sample_rate: This field can only be specified if logging is enabled for this backend service. The value of the field must be in [0, 1]. This configures the sampling rate of requests to the load balancer where 1.0 means all logged requests are reported and 0.0 means no logged requests are reported. The default value is 1.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#sample_rate GoogleComputeBackendService#sample_rate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceLogConfig.__init__)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument sample_rate", value=sample_rate, expected_type=type_hints["sample_rate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable is not None:
            self._values["enable"] = enable
        if sample_rate is not None:
            self._values["sample_rate"] = sample_rate

    @builtins.property
    def enable(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to enable logging for the load balancer traffic served by this backend service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enable GoogleComputeBackendService#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sample_rate(self) -> typing.Optional[jsii.Number]:
        '''This field can only be specified if logging is enabled for this backend service.

        The value of
        the field must be in [0, 1]. This configures the sampling rate of requests to the load balancer
        where 1.0 means all logged requests are reported and 0.0 means no logged requests are reported.
        The default value is 1.0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#sample_rate GoogleComputeBackendService#sample_rate}
        '''
        result = self._values.get("sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceLogConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceLogConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetSampleRate")
    def reset_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleRate", []))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleRateInput")
    def sample_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceLogConfigOutputReference, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="sampleRate")
    def sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sampleRate"))

    @sample_rate.setter
    def sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceLogConfigOutputReference, "sample_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeBackendServiceLogConfig]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceLogConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_failure": "consecutiveGatewayFailure",
        "enforcing_consecutive_errors": "enforcingConsecutiveErrors",
        "enforcing_consecutive_gateway_failure": "enforcingConsecutiveGatewayFailure",
        "enforcing_success_rate": "enforcingSuccessRate",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "success_rate_minimum_hosts": "successRateMinimumHosts",
        "success_rate_request_volume": "successRateRequestVolume",
        "success_rate_stdev_factor": "successRateStdevFactor",
    },
)
class GoogleComputeBackendServiceOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[typing.Union["GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime", typing.Dict[str, typing.Any]]] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_failure: typing.Optional[jsii.Number] = None,
        enforcing_consecutive_errors: typing.Optional[jsii.Number] = None,
        enforcing_consecutive_gateway_failure: typing.Optional[jsii.Number] = None,
        enforcing_success_rate: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[typing.Union["GoogleComputeBackendServiceOutlierDetectionInterval", typing.Dict[str, typing.Any]]] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        success_rate_minimum_hosts: typing.Optional[jsii.Number] = None,
        success_rate_request_volume: typing.Optional[jsii.Number] = None,
        success_rate_stdev_factor: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param base_ejection_time: base_ejection_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#base_ejection_time GoogleComputeBackendService#base_ejection_time}
        :param consecutive_errors: Number of errors before a host is ejected from the connection pool. When the backend host is accessed over HTTP, a 5xx return code qualifies as an error. Defaults to 5. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consecutive_errors GoogleComputeBackendService#consecutive_errors}
        :param consecutive_gateway_failure: The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs. Defaults to 5. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consecutive_gateway_failure GoogleComputeBackendService#consecutive_gateway_failure}
        :param enforcing_consecutive_errors: The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive 5xx. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_consecutive_errors GoogleComputeBackendService#enforcing_consecutive_errors}
        :param enforcing_consecutive_gateway_failure: The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive gateway failures. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_consecutive_gateway_failure GoogleComputeBackendService#enforcing_consecutive_gateway_failure}
        :param enforcing_success_rate: The percentage chance that a host will be actually ejected when an outlier status is detected through success rate statistics. This setting can be used to disable ejection or to ramp it up slowly. Defaults to 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_success_rate GoogleComputeBackendService#enforcing_success_rate}
        :param interval: interval block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#interval GoogleComputeBackendService#interval}
        :param max_ejection_percent: Maximum percentage of hosts in the load balancing pool for the backend service that can be ejected. Defaults to 10%. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_ejection_percent GoogleComputeBackendService#max_ejection_percent}
        :param success_rate_minimum_hosts: The number of hosts in a cluster that must have enough request volume to detect success rate outliers. If the number of hosts is less than this setting, outlier detection via success rate statistics is not performed for any host in the cluster. Defaults to 5. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_minimum_hosts GoogleComputeBackendService#success_rate_minimum_hosts}
        :param success_rate_request_volume: The minimum number of total requests that must be collected in one interval (as defined by the interval duration above) to include this host in success rate based outlier detection. If the volume is lower than this setting, outlier detection via success rate statistics is not performed for that host. Defaults to 100. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_request_volume GoogleComputeBackendService#success_rate_request_volume}
        :param success_rate_stdev_factor: This factor is used to determine the ejection threshold for success rate outlier ejection. The ejection threshold is the difference between the mean success rate, and the product of this factor and the standard deviation of the mean success rate: mean - (stdev * success_rate_stdev_factor). This factor is divided by a thousand to get a double. That is, if the desired factor is 1.9, the runtime value should be 1900. Defaults to 1900. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_stdev_factor GoogleComputeBackendService#success_rate_stdev_factor}
        '''
        if isinstance(base_ejection_time, dict):
            base_ejection_time = GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime(**base_ejection_time)
        if isinstance(interval, dict):
            interval = GoogleComputeBackendServiceOutlierDetectionInterval(**interval)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceOutlierDetection.__init__)
            check_type(argname="argument base_ejection_time", value=base_ejection_time, expected_type=type_hints["base_ejection_time"])
            check_type(argname="argument consecutive_errors", value=consecutive_errors, expected_type=type_hints["consecutive_errors"])
            check_type(argname="argument consecutive_gateway_failure", value=consecutive_gateway_failure, expected_type=type_hints["consecutive_gateway_failure"])
            check_type(argname="argument enforcing_consecutive_errors", value=enforcing_consecutive_errors, expected_type=type_hints["enforcing_consecutive_errors"])
            check_type(argname="argument enforcing_consecutive_gateway_failure", value=enforcing_consecutive_gateway_failure, expected_type=type_hints["enforcing_consecutive_gateway_failure"])
            check_type(argname="argument enforcing_success_rate", value=enforcing_success_rate, expected_type=type_hints["enforcing_success_rate"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument max_ejection_percent", value=max_ejection_percent, expected_type=type_hints["max_ejection_percent"])
            check_type(argname="argument success_rate_minimum_hosts", value=success_rate_minimum_hosts, expected_type=type_hints["success_rate_minimum_hosts"])
            check_type(argname="argument success_rate_request_volume", value=success_rate_request_volume, expected_type=type_hints["success_rate_request_volume"])
            check_type(argname="argument success_rate_stdev_factor", value=success_rate_stdev_factor, expected_type=type_hints["success_rate_stdev_factor"])
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_failure is not None:
            self._values["consecutive_gateway_failure"] = consecutive_gateway_failure
        if enforcing_consecutive_errors is not None:
            self._values["enforcing_consecutive_errors"] = enforcing_consecutive_errors
        if enforcing_consecutive_gateway_failure is not None:
            self._values["enforcing_consecutive_gateway_failure"] = enforcing_consecutive_gateway_failure
        if enforcing_success_rate is not None:
            self._values["enforcing_success_rate"] = enforcing_success_rate
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if success_rate_minimum_hosts is not None:
            self._values["success_rate_minimum_hosts"] = success_rate_minimum_hosts
        if success_rate_request_volume is not None:
            self._values["success_rate_request_volume"] = success_rate_request_volume
        if success_rate_stdev_factor is not None:
            self._values["success_rate_stdev_factor"] = success_rate_stdev_factor

    @builtins.property
    def base_ejection_time(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime"]:
        '''base_ejection_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#base_ejection_time GoogleComputeBackendService#base_ejection_time}
        '''
        result = self._values.get("base_ejection_time")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime"], result)

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of errors before a host is ejected from the connection pool.

        When the
        backend host is accessed over HTTP, a 5xx return code qualifies as an error.
        Defaults to 5.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consecutive_errors GoogleComputeBackendService#consecutive_errors}
        '''
        result = self._values.get("consecutive_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_gateway_failure(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive gateway failures (502, 503, 504 status or connection errors that are mapped to one of those status codes) before a consecutive gateway failure ejection occurs.

        Defaults to 5.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#consecutive_gateway_failure GoogleComputeBackendService#consecutive_gateway_failure}
        '''
        result = self._values.get("consecutive_gateway_failure")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enforcing_consecutive_errors(self) -> typing.Optional[jsii.Number]:
        '''The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive 5xx.

        This setting can be used to disable
        ejection or to ramp it up slowly. Defaults to 100.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_consecutive_errors GoogleComputeBackendService#enforcing_consecutive_errors}
        '''
        result = self._values.get("enforcing_consecutive_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enforcing_consecutive_gateway_failure(self) -> typing.Optional[jsii.Number]:
        '''The percentage chance that a host will be actually ejected when an outlier status is detected through consecutive gateway failures.

        This setting can be
        used to disable ejection or to ramp it up slowly. Defaults to 0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_consecutive_gateway_failure GoogleComputeBackendService#enforcing_consecutive_gateway_failure}
        '''
        result = self._values.get("enforcing_consecutive_gateway_failure")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enforcing_success_rate(self) -> typing.Optional[jsii.Number]:
        '''The percentage chance that a host will be actually ejected when an outlier status is detected through success rate statistics.

        This setting can be used to
        disable ejection or to ramp it up slowly. Defaults to 100.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#enforcing_success_rate GoogleComputeBackendService#enforcing_success_rate}
        '''
        result = self._values.get("enforcing_success_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(
        self,
    ) -> typing.Optional["GoogleComputeBackendServiceOutlierDetectionInterval"]:
        '''interval block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#interval GoogleComputeBackendService#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional["GoogleComputeBackendServiceOutlierDetectionInterval"], result)

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        '''Maximum percentage of hosts in the load balancing pool for the backend service that can be ejected. Defaults to 10%.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#max_ejection_percent GoogleComputeBackendService#max_ejection_percent}
        '''
        result = self._values.get("max_ejection_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_rate_minimum_hosts(self) -> typing.Optional[jsii.Number]:
        '''The number of hosts in a cluster that must have enough request volume to detect success rate outliers.

        If the number of hosts is less than this setting, outlier
        detection via success rate statistics is not performed for any host in the
        cluster. Defaults to 5.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_minimum_hosts GoogleComputeBackendService#success_rate_minimum_hosts}
        '''
        result = self._values.get("success_rate_minimum_hosts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_rate_request_volume(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of total requests that must be collected in one interval (as defined by the interval duration above) to include this host in success rate based outlier detection.

        If the volume is lower than this setting, outlier
        detection via success rate statistics is not performed for that host. Defaults
        to 100.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_request_volume GoogleComputeBackendService#success_rate_request_volume}
        '''
        result = self._values.get("success_rate_request_volume")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_rate_stdev_factor(self) -> typing.Optional[jsii.Number]:
        '''This factor is used to determine the ejection threshold for success rate outlier ejection.

        The ejection threshold is the difference between the mean success
        rate, and the product of this factor and the standard deviation of the mean
        success rate: mean - (stdev * success_rate_stdev_factor). This factor is divided
        by a thousand to get a double. That is, if the desired factor is 1.9, the
        runtime value should be 1900. Defaults to 1900.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#success_rate_stdev_factor GoogleComputeBackendService#success_rate_stdev_factor}
        '''
        result = self._values.get("success_rate_stdev_factor")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime:
    def __init__(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> jsii.Number:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceOutlierDetectionInterval",
    jsii_struct_bases=[],
    name_mapping={"seconds": "seconds", "nanos": "nanos"},
)
class GoogleComputeBackendServiceOutlierDetectionInterval:
    def __init__(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceOutlierDetectionInterval.__init__)
            check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
        self._values: typing.Dict[str, typing.Any] = {
            "seconds": seconds,
        }
        if nanos is not None:
            self._values["nanos"] = nanos

    @builtins.property
    def seconds(self) -> jsii.Number:
        '''Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        '''
        result = self._values.get("seconds")
        assert result is not None, "Required property 'seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nanos(self) -> typing.Optional[jsii.Number]:
        '''Span of time that's a fraction of a second at nanosecond resolution.

        Durations
        less than one second are represented with a 0 'seconds' field and a positive
        'nanos' field. Must be from 0 to 999,999,999 inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        result = self._values.get("nanos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceOutlierDetectionInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNanos")
    def reset_nanos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanos", []))

    @builtins.property
    @jsii.member(jsii_name="nanosInput")
    def nanos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanosInput"))

    @builtins.property
    @jsii.member(jsii_name="secondsInput")
    def seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "secondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nanos")
    def nanos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanos"))

    @nanos.setter
    def nanos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference, "nanos").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanos", value)

    @builtins.property
    @jsii.member(jsii_name="seconds")
    def seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "seconds"))

    @seconds.setter
    def seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference, "seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "seconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceOutlierDetectionInterval]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceOutlierDetectionInterval], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceOutlierDetectionInterval],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeBackendServiceOutlierDetectionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceOutlierDetectionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceOutlierDetectionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBaseEjectionTime")
    def put_base_ejection_time(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        value = GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putBaseEjectionTime", [value]))

    @jsii.member(jsii_name="putInterval")
    def put_interval(
        self,
        *,
        seconds: jsii.Number,
        nanos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param seconds: Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#seconds GoogleComputeBackendService#seconds}
        :param nanos: Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 'seconds' field and a positive 'nanos' field. Must be from 0 to 999,999,999 inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#nanos GoogleComputeBackendService#nanos}
        '''
        value = GoogleComputeBackendServiceOutlierDetectionInterval(
            seconds=seconds, nanos=nanos
        )

        return typing.cast(None, jsii.invoke(self, "putInterval", [value]))

    @jsii.member(jsii_name="resetBaseEjectionTime")
    def reset_base_ejection_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseEjectionTime", []))

    @jsii.member(jsii_name="resetConsecutiveErrors")
    def reset_consecutive_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsecutiveErrors", []))

    @jsii.member(jsii_name="resetConsecutiveGatewayFailure")
    def reset_consecutive_gateway_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsecutiveGatewayFailure", []))

    @jsii.member(jsii_name="resetEnforcingConsecutiveErrors")
    def reset_enforcing_consecutive_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforcingConsecutiveErrors", []))

    @jsii.member(jsii_name="resetEnforcingConsecutiveGatewayFailure")
    def reset_enforcing_consecutive_gateway_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforcingConsecutiveGatewayFailure", []))

    @jsii.member(jsii_name="resetEnforcingSuccessRate")
    def reset_enforcing_success_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforcingSuccessRate", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetMaxEjectionPercent")
    def reset_max_ejection_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxEjectionPercent", []))

    @jsii.member(jsii_name="resetSuccessRateMinimumHosts")
    def reset_success_rate_minimum_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessRateMinimumHosts", []))

    @jsii.member(jsii_name="resetSuccessRateRequestVolume")
    def reset_success_rate_request_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessRateRequestVolume", []))

    @jsii.member(jsii_name="resetSuccessRateStdevFactor")
    def reset_success_rate_stdev_factor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessRateStdevFactor", []))

    @builtins.property
    @jsii.member(jsii_name="baseEjectionTime")
    def base_ejection_time(
        self,
    ) -> GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference:
        return typing.cast(GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference, jsii.get(self, "baseEjectionTime"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(
        self,
    ) -> GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference:
        return typing.cast(GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference, jsii.get(self, "interval"))

    @builtins.property
    @jsii.member(jsii_name="baseEjectionTimeInput")
    def base_ejection_time_input(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime], jsii.get(self, "baseEjectionTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="consecutiveErrorsInput")
    def consecutive_errors_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "consecutiveErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="consecutiveGatewayFailureInput")
    def consecutive_gateway_failure_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "consecutiveGatewayFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcingConsecutiveErrorsInput")
    def enforcing_consecutive_errors_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enforcingConsecutiveErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcingConsecutiveGatewayFailureInput")
    def enforcing_consecutive_gateway_failure_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enforcingConsecutiveGatewayFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcingSuccessRateInput")
    def enforcing_success_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enforcingSuccessRateInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceOutlierDetectionInterval]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceOutlierDetectionInterval], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercentInput")
    def max_ejection_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxEjectionPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="successRateMinimumHostsInput")
    def success_rate_minimum_hosts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successRateMinimumHostsInput"))

    @builtins.property
    @jsii.member(jsii_name="successRateRequestVolumeInput")
    def success_rate_request_volume_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successRateRequestVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="successRateStdevFactorInput")
    def success_rate_stdev_factor_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successRateStdevFactorInput"))

    @builtins.property
    @jsii.member(jsii_name="consecutiveErrors")
    def consecutive_errors(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "consecutiveErrors"))

    @consecutive_errors.setter
    def consecutive_errors(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "consecutive_errors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consecutiveErrors", value)

    @builtins.property
    @jsii.member(jsii_name="consecutiveGatewayFailure")
    def consecutive_gateway_failure(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "consecutiveGatewayFailure"))

    @consecutive_gateway_failure.setter
    def consecutive_gateway_failure(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "consecutive_gateway_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consecutiveGatewayFailure", value)

    @builtins.property
    @jsii.member(jsii_name="enforcingConsecutiveErrors")
    def enforcing_consecutive_errors(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enforcingConsecutiveErrors"))

    @enforcing_consecutive_errors.setter
    def enforcing_consecutive_errors(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "enforcing_consecutive_errors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcingConsecutiveErrors", value)

    @builtins.property
    @jsii.member(jsii_name="enforcingConsecutiveGatewayFailure")
    def enforcing_consecutive_gateway_failure(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enforcingConsecutiveGatewayFailure"))

    @enforcing_consecutive_gateway_failure.setter
    def enforcing_consecutive_gateway_failure(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "enforcing_consecutive_gateway_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcingConsecutiveGatewayFailure", value)

    @builtins.property
    @jsii.member(jsii_name="enforcingSuccessRate")
    def enforcing_success_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enforcingSuccessRate"))

    @enforcing_success_rate.setter
    def enforcing_success_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "enforcing_success_rate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcingSuccessRate", value)

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercent")
    def max_ejection_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEjectionPercent"))

    @max_ejection_percent.setter
    def max_ejection_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "max_ejection_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEjectionPercent", value)

    @builtins.property
    @jsii.member(jsii_name="successRateMinimumHosts")
    def success_rate_minimum_hosts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRateMinimumHosts"))

    @success_rate_minimum_hosts.setter
    def success_rate_minimum_hosts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "success_rate_minimum_hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successRateMinimumHosts", value)

    @builtins.property
    @jsii.member(jsii_name="successRateRequestVolume")
    def success_rate_request_volume(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRateRequestVolume"))

    @success_rate_request_volume.setter
    def success_rate_request_volume(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "success_rate_request_volume").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successRateRequestVolume", value)

    @builtins.property
    @jsii.member(jsii_name="successRateStdevFactor")
    def success_rate_stdev_factor(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successRateStdevFactor"))

    @success_rate_stdev_factor.setter
    def success_rate_stdev_factor(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "success_rate_stdev_factor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successRateStdevFactor", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceOutlierDetection]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceOutlierDetection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceOutlierDetection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceOutlierDetectionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceSecuritySettings",
    jsii_struct_bases=[],
    name_mapping={
        "client_tls_policy": "clientTlsPolicy",
        "subject_alt_names": "subjectAltNames",
    },
)
class GoogleComputeBackendServiceSecuritySettings:
    def __init__(
        self,
        *,
        client_tls_policy: builtins.str,
        subject_alt_names: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param client_tls_policy: ClientTlsPolicy is a resource that specifies how a client should authenticate connections to backends of a service. This resource itself does not affect configuration unless it is attached to a backend service resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#client_tls_policy GoogleComputeBackendService#client_tls_policy}
        :param subject_alt_names: A list of alternate names to verify the subject identity in the certificate. If specified, the client will verify that the server certificate's subject alt name matches one of the specified values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#subject_alt_names GoogleComputeBackendService#subject_alt_names}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceSecuritySettings.__init__)
            check_type(argname="argument client_tls_policy", value=client_tls_policy, expected_type=type_hints["client_tls_policy"])
            check_type(argname="argument subject_alt_names", value=subject_alt_names, expected_type=type_hints["subject_alt_names"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_tls_policy": client_tls_policy,
            "subject_alt_names": subject_alt_names,
        }

    @builtins.property
    def client_tls_policy(self) -> builtins.str:
        '''ClientTlsPolicy is a resource that specifies how a client should authenticate connections to backends of a service.

        This resource itself does not affect
        configuration unless it is attached to a backend service resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#client_tls_policy GoogleComputeBackendService#client_tls_policy}
        '''
        result = self._values.get("client_tls_policy")
        assert result is not None, "Required property 'client_tls_policy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject_alt_names(self) -> typing.List[builtins.str]:
        '''A list of alternate names to verify the subject identity in the certificate.

        If specified, the client will verify that the server certificate's subject
        alt name matches one of the specified values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#subject_alt_names GoogleComputeBackendService#subject_alt_names}
        '''
        result = self._values.get("subject_alt_names")
        assert result is not None, "Required property 'subject_alt_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceSecuritySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceSecuritySettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceSecuritySettingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceSecuritySettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clientTlsPolicyInput")
    def client_tls_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientTlsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltNamesInput")
    def subject_alt_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subjectAltNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTlsPolicy")
    def client_tls_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientTlsPolicy"))

    @client_tls_policy.setter
    def client_tls_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceSecuritySettingsOutputReference, "client_tls_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTlsPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="subjectAltNames")
    def subject_alt_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subjectAltNames"))

    @subject_alt_names.setter
    def subject_alt_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceSecuritySettingsOutputReference, "subject_alt_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectAltNames", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeBackendServiceSecuritySettings]:
        return typing.cast(typing.Optional[GoogleComputeBackendServiceSecuritySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeBackendServiceSecuritySettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceSecuritySettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeBackendServiceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#create GoogleComputeBackendService#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#delete GoogleComputeBackendService#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#update GoogleComputeBackendService#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#create GoogleComputeBackendService#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#delete GoogleComputeBackendService#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_backend_service#update GoogleComputeBackendService#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeBackendServiceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeBackendServiceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeBackendService.GoogleComputeBackendServiceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeBackendServiceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeBackendServiceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeBackendServiceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeBackendServiceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeBackendServiceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeBackendService",
    "GoogleComputeBackendServiceBackend",
    "GoogleComputeBackendServiceBackendList",
    "GoogleComputeBackendServiceBackendOutputReference",
    "GoogleComputeBackendServiceCdnPolicy",
    "GoogleComputeBackendServiceCdnPolicyCacheKeyPolicy",
    "GoogleComputeBackendServiceCdnPolicyCacheKeyPolicyOutputReference",
    "GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicy",
    "GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyList",
    "GoogleComputeBackendServiceCdnPolicyNegativeCachingPolicyOutputReference",
    "GoogleComputeBackendServiceCdnPolicyOutputReference",
    "GoogleComputeBackendServiceCircuitBreakers",
    "GoogleComputeBackendServiceCircuitBreakersConnectTimeout",
    "GoogleComputeBackendServiceCircuitBreakersConnectTimeoutOutputReference",
    "GoogleComputeBackendServiceCircuitBreakersOutputReference",
    "GoogleComputeBackendServiceConfig",
    "GoogleComputeBackendServiceConsistentHash",
    "GoogleComputeBackendServiceConsistentHashHttpCookie",
    "GoogleComputeBackendServiceConsistentHashHttpCookieOutputReference",
    "GoogleComputeBackendServiceConsistentHashHttpCookieTtl",
    "GoogleComputeBackendServiceConsistentHashHttpCookieTtlOutputReference",
    "GoogleComputeBackendServiceConsistentHashOutputReference",
    "GoogleComputeBackendServiceIap",
    "GoogleComputeBackendServiceIapOutputReference",
    "GoogleComputeBackendServiceLogConfig",
    "GoogleComputeBackendServiceLogConfigOutputReference",
    "GoogleComputeBackendServiceOutlierDetection",
    "GoogleComputeBackendServiceOutlierDetectionBaseEjectionTime",
    "GoogleComputeBackendServiceOutlierDetectionBaseEjectionTimeOutputReference",
    "GoogleComputeBackendServiceOutlierDetectionInterval",
    "GoogleComputeBackendServiceOutlierDetectionIntervalOutputReference",
    "GoogleComputeBackendServiceOutlierDetectionOutputReference",
    "GoogleComputeBackendServiceSecuritySettings",
    "GoogleComputeBackendServiceSecuritySettingsOutputReference",
    "GoogleComputeBackendServiceTimeouts",
    "GoogleComputeBackendServiceTimeoutsOutputReference",
]

publication.publish()
