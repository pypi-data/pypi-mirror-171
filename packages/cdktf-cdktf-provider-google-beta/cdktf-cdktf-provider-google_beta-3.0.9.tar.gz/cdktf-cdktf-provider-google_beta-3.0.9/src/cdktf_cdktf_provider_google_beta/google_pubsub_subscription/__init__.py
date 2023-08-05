'''
# `google_pubsub_subscription`

Refer to the Terraform Registory for docs: [`google_pubsub_subscription`](https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription).
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


class GooglePubsubSubscription(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription google_pubsub_subscription}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        topic: builtins.str,
        ack_deadline_seconds: typing.Optional[jsii.Number] = None,
        bigquery_config: typing.Optional[typing.Union["GooglePubsubSubscriptionBigqueryConfig", typing.Dict[str, typing.Any]]] = None,
        dead_letter_policy: typing.Optional[typing.Union["GooglePubsubSubscriptionDeadLetterPolicy", typing.Dict[str, typing.Any]]] = None,
        enable_exactly_once_delivery: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_message_ordering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expiration_policy: typing.Optional[typing.Union["GooglePubsubSubscriptionExpirationPolicy", typing.Dict[str, typing.Any]]] = None,
        filter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        message_retention_duration: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        push_config: typing.Optional[typing.Union["GooglePubsubSubscriptionPushConfig", typing.Dict[str, typing.Any]]] = None,
        retain_acked_messages: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retry_policy: typing.Optional[typing.Union["GooglePubsubSubscriptionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePubsubSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription google_pubsub_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the subscription. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#name GooglePubsubSubscription#name}
        :param topic: A reference to a Topic resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#topic GooglePubsubSubscription#topic}
        :param ack_deadline_seconds: This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#ack_deadline_seconds GooglePubsubSubscription#ack_deadline_seconds}
        :param bigquery_config: bigquery_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#bigquery_config GooglePubsubSubscription#bigquery_config}
        :param dead_letter_policy: dead_letter_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#dead_letter_policy GooglePubsubSubscription#dead_letter_policy}
        :param enable_exactly_once_delivery: If 'true', Pub/Sub provides the following guarantees for the delivery of a message with a given value of messageId on this Subscriptions': - The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires. - An acknowledged message will not be resent to a subscriber. Note that subscribers may still receive multiple copies of a message when 'enable_exactly_once_delivery' is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct messageId values Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#enable_exactly_once_delivery GooglePubsubSubscription#enable_exactly_once_delivery}
        :param enable_message_ordering: If 'true', messages published with the same orderingKey in PubsubMessage will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#enable_message_ordering GooglePubsubSubscription#enable_message_ordering}
        :param expiration_policy: expiration_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#expiration_policy GooglePubsubSubscription#expiration_policy}
        :param filter: The subscription only delivers the messages that match the filter. Pub/Sub automatically acknowledges the messages that don't match the filter. You can filter messages by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription, you can't modify the filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#filter GooglePubsubSubscription#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#id GooglePubsubSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this Subscription. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#labels GooglePubsubSubscription#labels}
        :param message_retention_duration: How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If retain_acked_messages is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: '"600.5s"'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#message_retention_duration GooglePubsubSubscription#message_retention_duration}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#project GooglePubsubSubscription#project}.
        :param push_config: push_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#push_config GooglePubsubSubscription#push_config}
        :param retain_acked_messages: Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#retain_acked_messages GooglePubsubSubscription#retain_acked_messages}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#retry_policy GooglePubsubSubscription#retry_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#timeouts GooglePubsubSubscription#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscription.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GooglePubsubSubscriptionConfig(
            name=name,
            topic=topic,
            ack_deadline_seconds=ack_deadline_seconds,
            bigquery_config=bigquery_config,
            dead_letter_policy=dead_letter_policy,
            enable_exactly_once_delivery=enable_exactly_once_delivery,
            enable_message_ordering=enable_message_ordering,
            expiration_policy=expiration_policy,
            filter=filter,
            id=id,
            labels=labels,
            message_retention_duration=message_retention_duration,
            project=project,
            push_config=push_config,
            retain_acked_messages=retain_acked_messages,
            retry_policy=retry_policy,
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

    @jsii.member(jsii_name="putBigqueryConfig")
    def put_bigquery_config(
        self,
        *,
        table: builtins.str,
        drop_unknown_fields: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_topic_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        write_metadata: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param table: The name of the table to which to write data, of the form {projectId}:{datasetId}.{tableId}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#table GooglePubsubSubscription#table}
        :param drop_unknown_fields: When true and useTopicSchema is true, any fields that are a part of the topic schema that are not part of the BigQuery table schema are dropped when writing to BigQuery. Otherwise, the schemas must be kept in sync and any messages with extra fields are not written and remain in the subscription's backlog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#drop_unknown_fields GooglePubsubSubscription#drop_unknown_fields}
        :param use_topic_schema: When true, use the topic's schema as the columns to write to in BigQuery, if it exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#use_topic_schema GooglePubsubSubscription#use_topic_schema}
        :param write_metadata: When true, write the subscription name, messageId, publishTime, attributes, and orderingKey to additional columns in the table. The subscription name, messageId, and publishTime fields are put in their own columns while all other message properties (other than data) are written to a JSON object in the attributes column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#write_metadata GooglePubsubSubscription#write_metadata}
        '''
        value = GooglePubsubSubscriptionBigqueryConfig(
            table=table,
            drop_unknown_fields=drop_unknown_fields,
            use_topic_schema=use_topic_schema,
            write_metadata=write_metadata,
        )

        return typing.cast(None, jsii.invoke(self, "putBigqueryConfig", [value]))

    @jsii.member(jsii_name="putDeadLetterPolicy")
    def put_dead_letter_policy(
        self,
        *,
        dead_letter_topic: typing.Optional[builtins.str] = None,
        max_delivery_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dead_letter_topic: The name of the topic to which dead letter messages should be published. Format is 'projects/{project}/topics/{topic}'. The Cloud Pub/Sub service account associated with the enclosing subscription's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Publish() to this topic. The operation will fail if the topic does not exist. Users should ensure that there is a subscription attached to this topic since messages published to a topic with no subscriptions are lost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#dead_letter_topic GooglePubsubSubscription#dead_letter_topic}
        :param max_delivery_attempts: The maximum number of delivery attempts for any message. The value must be between 5 and 100. The number of delivery attempts is defined as 1 + (the sum of number of NACKs and number of times the acknowledgement deadline has been exceeded for the message). A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that client libraries may automatically extend ack_deadlines. This field will be honored on a best effort basis. If this parameter is 0, a default value of 5 is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#max_delivery_attempts GooglePubsubSubscription#max_delivery_attempts}
        '''
        value = GooglePubsubSubscriptionDeadLetterPolicy(
            dead_letter_topic=dead_letter_topic,
            max_delivery_attempts=max_delivery_attempts,
        )

        return typing.cast(None, jsii.invoke(self, "putDeadLetterPolicy", [value]))

    @jsii.member(jsii_name="putExpirationPolicy")
    def put_expiration_policy(self, *, ttl: builtins.str) -> None:
        '''
        :param ttl: Specifies the "time-to-live" duration for an associated resource. The resource expires if it is not active for a period of ttl. If ttl is not set, the associated resource never expires. A duration in seconds with up to nine fractional digits, terminated by 's'. Example - "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#ttl GooglePubsubSubscription#ttl}
        '''
        value = GooglePubsubSubscriptionExpirationPolicy(ttl=ttl)

        return typing.cast(None, jsii.invoke(self, "putExpirationPolicy", [value]))

    @jsii.member(jsii_name="putPushConfig")
    def put_push_config(
        self,
        *,
        push_endpoint: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        oidc_token: typing.Optional[typing.Union["GooglePubsubSubscriptionPushConfigOidcToken", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param push_endpoint: A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use "https://example.com/push". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#push_endpoint GooglePubsubSubscription#push_endpoint}
        :param attributes: Endpoint configuration attributes. Every endpoint has a set of API supported attributes that can be used to control different aspects of the message delivery. The currently supported attribute is x-goog-version, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata). The endpoint version is based on the version of the Pub/Sub API. If not present during the subscriptions.create call, it will default to the version of the API used to make such call. If not present during a subscriptions.modifyPushConfig call, its value will not be changed. subscriptions.get calls will always return a valid version, even if the subscription was created without this attribute. The possible values for this attribute are: - v1beta1: uses the push format defined in the v1beta1 Pub/Sub API. - v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#attributes GooglePubsubSubscription#attributes}
        :param oidc_token: oidc_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#oidc_token GooglePubsubSubscription#oidc_token}
        '''
        value = GooglePubsubSubscriptionPushConfig(
            push_endpoint=push_endpoint, attributes=attributes, oidc_token=oidc_token
        )

        return typing.cast(None, jsii.invoke(self, "putPushConfig", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        maximum_backoff: typing.Optional[builtins.str] = None,
        minimum_backoff: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param maximum_backoff: The maximum delay between consecutive deliveries of a given message. Value should be between 0 and 600 seconds. Defaults to 600 seconds. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#maximum_backoff GooglePubsubSubscription#maximum_backoff}
        :param minimum_backoff: The minimum delay between consecutive deliveries of a given message. Value should be between 0 and 600 seconds. Defaults to 10 seconds. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#minimum_backoff GooglePubsubSubscription#minimum_backoff}
        '''
        value = GooglePubsubSubscriptionRetryPolicy(
            maximum_backoff=maximum_backoff, minimum_backoff=minimum_backoff
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#create GooglePubsubSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#delete GooglePubsubSubscription#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#update GooglePubsubSubscription#update}.
        '''
        value = GooglePubsubSubscriptionTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAckDeadlineSeconds")
    def reset_ack_deadline_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAckDeadlineSeconds", []))

    @jsii.member(jsii_name="resetBigqueryConfig")
    def reset_bigquery_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigqueryConfig", []))

    @jsii.member(jsii_name="resetDeadLetterPolicy")
    def reset_dead_letter_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetterPolicy", []))

    @jsii.member(jsii_name="resetEnableExactlyOnceDelivery")
    def reset_enable_exactly_once_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExactlyOnceDelivery", []))

    @jsii.member(jsii_name="resetEnableMessageOrdering")
    def reset_enable_message_ordering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMessageOrdering", []))

    @jsii.member(jsii_name="resetExpirationPolicy")
    def reset_expiration_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationPolicy", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMessageRetentionDuration")
    def reset_message_retention_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageRetentionDuration", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPushConfig")
    def reset_push_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushConfig", []))

    @jsii.member(jsii_name="resetRetainAckedMessages")
    def reset_retain_acked_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetainAckedMessages", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

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
    @jsii.member(jsii_name="bigqueryConfig")
    def bigquery_config(
        self,
    ) -> "GooglePubsubSubscriptionBigqueryConfigOutputReference":
        return typing.cast("GooglePubsubSubscriptionBigqueryConfigOutputReference", jsii.get(self, "bigqueryConfig"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterPolicy")
    def dead_letter_policy(
        self,
    ) -> "GooglePubsubSubscriptionDeadLetterPolicyOutputReference":
        return typing.cast("GooglePubsubSubscriptionDeadLetterPolicyOutputReference", jsii.get(self, "deadLetterPolicy"))

    @builtins.property
    @jsii.member(jsii_name="expirationPolicy")
    def expiration_policy(
        self,
    ) -> "GooglePubsubSubscriptionExpirationPolicyOutputReference":
        return typing.cast("GooglePubsubSubscriptionExpirationPolicyOutputReference", jsii.get(self, "expirationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="pushConfig")
    def push_config(self) -> "GooglePubsubSubscriptionPushConfigOutputReference":
        return typing.cast("GooglePubsubSubscriptionPushConfigOutputReference", jsii.get(self, "pushConfig"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "GooglePubsubSubscriptionRetryPolicyOutputReference":
        return typing.cast("GooglePubsubSubscriptionRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePubsubSubscriptionTimeoutsOutputReference":
        return typing.cast("GooglePubsubSubscriptionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="ackDeadlineSecondsInput")
    def ack_deadline_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ackDeadlineSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="bigqueryConfigInput")
    def bigquery_config_input(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionBigqueryConfig"]:
        return typing.cast(typing.Optional["GooglePubsubSubscriptionBigqueryConfig"], jsii.get(self, "bigqueryConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterPolicyInput")
    def dead_letter_policy_input(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionDeadLetterPolicy"]:
        return typing.cast(typing.Optional["GooglePubsubSubscriptionDeadLetterPolicy"], jsii.get(self, "deadLetterPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="enableExactlyOnceDeliveryInput")
    def enable_exactly_once_delivery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableExactlyOnceDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMessageOrderingInput")
    def enable_message_ordering_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableMessageOrderingInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationPolicyInput")
    def expiration_policy_input(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionExpirationPolicy"]:
        return typing.cast(typing.Optional["GooglePubsubSubscriptionExpirationPolicy"], jsii.get(self, "expirationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageRetentionDurationInput")
    def message_retention_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageRetentionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pushConfigInput")
    def push_config_input(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionPushConfig"]:
        return typing.cast(typing.Optional["GooglePubsubSubscriptionPushConfig"], jsii.get(self, "pushConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="retainAckedMessagesInput")
    def retain_acked_messages_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "retainAckedMessagesInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionRetryPolicy"]:
        return typing.cast(typing.Optional["GooglePubsubSubscriptionRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePubsubSubscriptionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePubsubSubscriptionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="ackDeadlineSeconds")
    def ack_deadline_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ackDeadlineSeconds"))

    @ack_deadline_seconds.setter
    def ack_deadline_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "ack_deadline_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ackDeadlineSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="enableExactlyOnceDelivery")
    def enable_exactly_once_delivery(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableExactlyOnceDelivery"))

    @enable_exactly_once_delivery.setter
    def enable_exactly_once_delivery(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "enable_exactly_once_delivery").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExactlyOnceDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="enableMessageOrdering")
    def enable_message_ordering(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableMessageOrdering"))

    @enable_message_ordering.setter
    def enable_message_ordering(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "enable_message_ordering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMessageOrdering", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="messageRetentionDuration")
    def message_retention_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageRetentionDuration"))

    @message_retention_duration.setter
    def message_retention_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "message_retention_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageRetentionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="retainAckedMessages")
    def retain_acked_messages(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "retainAckedMessages"))

    @retain_acked_messages.setter
    def retain_acked_messages(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "retain_acked_messages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainAckedMessages", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscription, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionBigqueryConfig",
    jsii_struct_bases=[],
    name_mapping={
        "table": "table",
        "drop_unknown_fields": "dropUnknownFields",
        "use_topic_schema": "useTopicSchema",
        "write_metadata": "writeMetadata",
    },
)
class GooglePubsubSubscriptionBigqueryConfig:
    def __init__(
        self,
        *,
        table: builtins.str,
        drop_unknown_fields: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_topic_schema: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        write_metadata: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param table: The name of the table to which to write data, of the form {projectId}:{datasetId}.{tableId}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#table GooglePubsubSubscription#table}
        :param drop_unknown_fields: When true and useTopicSchema is true, any fields that are a part of the topic schema that are not part of the BigQuery table schema are dropped when writing to BigQuery. Otherwise, the schemas must be kept in sync and any messages with extra fields are not written and remain in the subscription's backlog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#drop_unknown_fields GooglePubsubSubscription#drop_unknown_fields}
        :param use_topic_schema: When true, use the topic's schema as the columns to write to in BigQuery, if it exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#use_topic_schema GooglePubsubSubscription#use_topic_schema}
        :param write_metadata: When true, write the subscription name, messageId, publishTime, attributes, and orderingKey to additional columns in the table. The subscription name, messageId, and publishTime fields are put in their own columns while all other message properties (other than data) are written to a JSON object in the attributes column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#write_metadata GooglePubsubSubscription#write_metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionBigqueryConfig.__init__)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument drop_unknown_fields", value=drop_unknown_fields, expected_type=type_hints["drop_unknown_fields"])
            check_type(argname="argument use_topic_schema", value=use_topic_schema, expected_type=type_hints["use_topic_schema"])
            check_type(argname="argument write_metadata", value=write_metadata, expected_type=type_hints["write_metadata"])
        self._values: typing.Dict[str, typing.Any] = {
            "table": table,
        }
        if drop_unknown_fields is not None:
            self._values["drop_unknown_fields"] = drop_unknown_fields
        if use_topic_schema is not None:
            self._values["use_topic_schema"] = use_topic_schema
        if write_metadata is not None:
            self._values["write_metadata"] = write_metadata

    @builtins.property
    def table(self) -> builtins.str:
        '''The name of the table to which to write data, of the form {projectId}:{datasetId}.{tableId}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#table GooglePubsubSubscription#table}
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def drop_unknown_fields(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true and useTopicSchema is true, any fields that are a part of the topic schema that are not part of the BigQuery table schema are dropped when writing to BigQuery.

        Otherwise, the schemas must be kept in sync and any messages with extra fields are not written and remain in the subscription's backlog.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#drop_unknown_fields GooglePubsubSubscription#drop_unknown_fields}
        '''
        result = self._values.get("drop_unknown_fields")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_topic_schema(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, use the topic's schema as the columns to write to in BigQuery, if it exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#use_topic_schema GooglePubsubSubscription#use_topic_schema}
        '''
        result = self._values.get("use_topic_schema")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def write_metadata(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, write the subscription name, messageId, publishTime, attributes, and orderingKey to additional columns in the table.

        The subscription name, messageId, and publishTime fields are put in their own columns while all other message properties (other than data) are written to a JSON object in the attributes column.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#write_metadata GooglePubsubSubscription#write_metadata}
        '''
        result = self._values.get("write_metadata")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionBigqueryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubSubscriptionBigqueryConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionBigqueryConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionBigqueryConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDropUnknownFields")
    def reset_drop_unknown_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropUnknownFields", []))

    @jsii.member(jsii_name="resetUseTopicSchema")
    def reset_use_topic_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseTopicSchema", []))

    @jsii.member(jsii_name="resetWriteMetadata")
    def reset_write_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteMetadata", []))

    @builtins.property
    @jsii.member(jsii_name="dropUnknownFieldsInput")
    def drop_unknown_fields_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dropUnknownFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableInput")
    def table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableInput"))

    @builtins.property
    @jsii.member(jsii_name="useTopicSchemaInput")
    def use_topic_schema_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useTopicSchemaInput"))

    @builtins.property
    @jsii.member(jsii_name="writeMetadataInput")
    def write_metadata_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "writeMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="dropUnknownFields")
    def drop_unknown_fields(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dropUnknownFields"))

    @drop_unknown_fields.setter
    def drop_unknown_fields(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionBigqueryConfigOutputReference, "drop_unknown_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dropUnknownFields", value)

    @builtins.property
    @jsii.member(jsii_name="table")
    def table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "table"))

    @table.setter
    def table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionBigqueryConfigOutputReference, "table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "table", value)

    @builtins.property
    @jsii.member(jsii_name="useTopicSchema")
    def use_topic_schema(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useTopicSchema"))

    @use_topic_schema.setter
    def use_topic_schema(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionBigqueryConfigOutputReference, "use_topic_schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useTopicSchema", value)

    @builtins.property
    @jsii.member(jsii_name="writeMetadata")
    def write_metadata(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "writeMetadata"))

    @write_metadata.setter
    def write_metadata(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionBigqueryConfigOutputReference, "write_metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePubsubSubscriptionBigqueryConfig]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionBigqueryConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubSubscriptionBigqueryConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionBigqueryConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionConfig",
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
        "topic": "topic",
        "ack_deadline_seconds": "ackDeadlineSeconds",
        "bigquery_config": "bigqueryConfig",
        "dead_letter_policy": "deadLetterPolicy",
        "enable_exactly_once_delivery": "enableExactlyOnceDelivery",
        "enable_message_ordering": "enableMessageOrdering",
        "expiration_policy": "expirationPolicy",
        "filter": "filter",
        "id": "id",
        "labels": "labels",
        "message_retention_duration": "messageRetentionDuration",
        "project": "project",
        "push_config": "pushConfig",
        "retain_acked_messages": "retainAckedMessages",
        "retry_policy": "retryPolicy",
        "timeouts": "timeouts",
    },
)
class GooglePubsubSubscriptionConfig(cdktf.TerraformMetaArguments):
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
        topic: builtins.str,
        ack_deadline_seconds: typing.Optional[jsii.Number] = None,
        bigquery_config: typing.Optional[typing.Union[GooglePubsubSubscriptionBigqueryConfig, typing.Dict[str, typing.Any]]] = None,
        dead_letter_policy: typing.Optional[typing.Union["GooglePubsubSubscriptionDeadLetterPolicy", typing.Dict[str, typing.Any]]] = None,
        enable_exactly_once_delivery: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_message_ordering: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        expiration_policy: typing.Optional[typing.Union["GooglePubsubSubscriptionExpirationPolicy", typing.Dict[str, typing.Any]]] = None,
        filter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        message_retention_duration: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        push_config: typing.Optional[typing.Union["GooglePubsubSubscriptionPushConfig", typing.Dict[str, typing.Any]]] = None,
        retain_acked_messages: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retry_policy: typing.Optional[typing.Union["GooglePubsubSubscriptionRetryPolicy", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePubsubSubscriptionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the subscription. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#name GooglePubsubSubscription#name}
        :param topic: A reference to a Topic resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#topic GooglePubsubSubscription#topic}
        :param ack_deadline_seconds: This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions, this value is used as the initial value for the ack deadline. To override this value for a given message, call subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#ack_deadline_seconds GooglePubsubSubscription#ack_deadline_seconds}
        :param bigquery_config: bigquery_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#bigquery_config GooglePubsubSubscription#bigquery_config}
        :param dead_letter_policy: dead_letter_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#dead_letter_policy GooglePubsubSubscription#dead_letter_policy}
        :param enable_exactly_once_delivery: If 'true', Pub/Sub provides the following guarantees for the delivery of a message with a given value of messageId on this Subscriptions': - The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires. - An acknowledged message will not be resent to a subscriber. Note that subscribers may still receive multiple copies of a message when 'enable_exactly_once_delivery' is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct messageId values Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#enable_exactly_once_delivery GooglePubsubSubscription#enable_exactly_once_delivery}
        :param enable_message_ordering: If 'true', messages published with the same orderingKey in PubsubMessage will be delivered to the subscribers in the order in which they are received by the Pub/Sub system. Otherwise, they may be delivered in any order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#enable_message_ordering GooglePubsubSubscription#enable_message_ordering}
        :param expiration_policy: expiration_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#expiration_policy GooglePubsubSubscription#expiration_policy}
        :param filter: The subscription only delivers the messages that match the filter. Pub/Sub automatically acknowledges the messages that don't match the filter. You can filter messages by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription, you can't modify the filter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#filter GooglePubsubSubscription#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#id GooglePubsubSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this Subscription. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#labels GooglePubsubSubscription#labels}
        :param message_retention_duration: How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If retain_acked_messages is true, then this also configures the retention of acknowledged messages, and thus configures how far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: '"600.5s"'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#message_retention_duration GooglePubsubSubscription#message_retention_duration}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#project GooglePubsubSubscription#project}.
        :param push_config: push_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#push_config GooglePubsubSubscription#push_config}
        :param retain_acked_messages: Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#retain_acked_messages GooglePubsubSubscription#retain_acked_messages}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#retry_policy GooglePubsubSubscription#retry_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#timeouts GooglePubsubSubscription#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(bigquery_config, dict):
            bigquery_config = GooglePubsubSubscriptionBigqueryConfig(**bigquery_config)
        if isinstance(dead_letter_policy, dict):
            dead_letter_policy = GooglePubsubSubscriptionDeadLetterPolicy(**dead_letter_policy)
        if isinstance(expiration_policy, dict):
            expiration_policy = GooglePubsubSubscriptionExpirationPolicy(**expiration_policy)
        if isinstance(push_config, dict):
            push_config = GooglePubsubSubscriptionPushConfig(**push_config)
        if isinstance(retry_policy, dict):
            retry_policy = GooglePubsubSubscriptionRetryPolicy(**retry_policy)
        if isinstance(timeouts, dict):
            timeouts = GooglePubsubSubscriptionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument ack_deadline_seconds", value=ack_deadline_seconds, expected_type=type_hints["ack_deadline_seconds"])
            check_type(argname="argument bigquery_config", value=bigquery_config, expected_type=type_hints["bigquery_config"])
            check_type(argname="argument dead_letter_policy", value=dead_letter_policy, expected_type=type_hints["dead_letter_policy"])
            check_type(argname="argument enable_exactly_once_delivery", value=enable_exactly_once_delivery, expected_type=type_hints["enable_exactly_once_delivery"])
            check_type(argname="argument enable_message_ordering", value=enable_message_ordering, expected_type=type_hints["enable_message_ordering"])
            check_type(argname="argument expiration_policy", value=expiration_policy, expected_type=type_hints["expiration_policy"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument message_retention_duration", value=message_retention_duration, expected_type=type_hints["message_retention_duration"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument push_config", value=push_config, expected_type=type_hints["push_config"])
            check_type(argname="argument retain_acked_messages", value=retain_acked_messages, expected_type=type_hints["retain_acked_messages"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "topic": topic,
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
        if ack_deadline_seconds is not None:
            self._values["ack_deadline_seconds"] = ack_deadline_seconds
        if bigquery_config is not None:
            self._values["bigquery_config"] = bigquery_config
        if dead_letter_policy is not None:
            self._values["dead_letter_policy"] = dead_letter_policy
        if enable_exactly_once_delivery is not None:
            self._values["enable_exactly_once_delivery"] = enable_exactly_once_delivery
        if enable_message_ordering is not None:
            self._values["enable_message_ordering"] = enable_message_ordering
        if expiration_policy is not None:
            self._values["expiration_policy"] = expiration_policy
        if filter is not None:
            self._values["filter"] = filter
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if message_retention_duration is not None:
            self._values["message_retention_duration"] = message_retention_duration
        if project is not None:
            self._values["project"] = project
        if push_config is not None:
            self._values["push_config"] = push_config
        if retain_acked_messages is not None:
            self._values["retain_acked_messages"] = retain_acked_messages
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
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
        '''Name of the subscription.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#name GooglePubsubSubscription#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''A reference to a Topic resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#topic GooglePubsubSubscription#topic}
        '''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ack_deadline_seconds(self) -> typing.Optional[jsii.Number]:
        '''This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the message.

        After message
        delivery but before the ack deadline expires and before the message is
        acknowledged, it is an outstanding message and will not be delivered
        again during that time (on a best-effort basis).

        For pull subscriptions, this value is used as the initial value for
        the ack deadline. To override this value for a given message, call
        subscriptions.modifyAckDeadline with the corresponding ackId if using
        pull. The minimum custom deadline you can specify is 10 seconds. The
        maximum custom deadline you can specify is 600 seconds (10 minutes).
        If this parameter is 0, a default value of 10 seconds is used.

        For push delivery, this value is also used to set the request timeout
        for the call to the push endpoint.

        If the subscriber never acknowledges the message, the Pub/Sub system
        will eventually redeliver the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#ack_deadline_seconds GooglePubsubSubscription#ack_deadline_seconds}
        '''
        result = self._values.get("ack_deadline_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bigquery_config(
        self,
    ) -> typing.Optional[GooglePubsubSubscriptionBigqueryConfig]:
        '''bigquery_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#bigquery_config GooglePubsubSubscription#bigquery_config}
        '''
        result = self._values.get("bigquery_config")
        return typing.cast(typing.Optional[GooglePubsubSubscriptionBigqueryConfig], result)

    @builtins.property
    def dead_letter_policy(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionDeadLetterPolicy"]:
        '''dead_letter_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#dead_letter_policy GooglePubsubSubscription#dead_letter_policy}
        '''
        result = self._values.get("dead_letter_policy")
        return typing.cast(typing.Optional["GooglePubsubSubscriptionDeadLetterPolicy"], result)

    @builtins.property
    def enable_exactly_once_delivery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If 'true', Pub/Sub provides the following guarantees for the delivery of a message with a given value of messageId on this Subscriptions':  - The message sent to a subscriber is guaranteed not to be resent before the message's acknowledgement deadline expires.

        - An acknowledged message will not be resent to a subscriber.

        Note that subscribers may still receive multiple copies of a message when 'enable_exactly_once_delivery'
        is true if the message was published multiple times by a publisher client. These copies are considered distinct by Pub/Sub and have distinct messageId values

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#enable_exactly_once_delivery GooglePubsubSubscription#enable_exactly_once_delivery}
        '''
        result = self._values.get("enable_exactly_once_delivery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_message_ordering(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If 'true', messages published with the same orderingKey in PubsubMessage will be delivered to the subscribers in the order in which they are received by the Pub/Sub system.

        Otherwise, they
        may be delivered in any order.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#enable_message_ordering GooglePubsubSubscription#enable_message_ordering}
        '''
        result = self._values.get("enable_message_ordering")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def expiration_policy(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionExpirationPolicy"]:
        '''expiration_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#expiration_policy GooglePubsubSubscription#expiration_policy}
        '''
        result = self._values.get("expiration_policy")
        return typing.cast(typing.Optional["GooglePubsubSubscriptionExpirationPolicy"], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''The subscription only delivers the messages that match the filter.

        Pub/Sub automatically acknowledges the messages that don't match the filter. You can filter messages
        by their attributes. The maximum length of a filter is 256 bytes. After creating the subscription,
        you can't modify the filter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#filter GooglePubsubSubscription#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#id GooglePubsubSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to this Subscription.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#labels GooglePubsubSubscription#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def message_retention_duration(self) -> typing.Optional[builtins.str]:
        '''How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published.

        If
        retain_acked_messages is true, then this also configures the retention
        of acknowledged messages, and thus configures how far back in time a
        subscriptions.seek can be done. Defaults to 7 days. Cannot be more
        than 7 days ('"604800s"') or less than 10 minutes ('"600s"').

        A duration in seconds with up to nine fractional digits, terminated
        by 's'. Example: '"600.5s"'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#message_retention_duration GooglePubsubSubscription#message_retention_duration}
        '''
        result = self._values.get("message_retention_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#project GooglePubsubSubscription#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def push_config(self) -> typing.Optional["GooglePubsubSubscriptionPushConfig"]:
        '''push_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#push_config GooglePubsubSubscription#push_config}
        '''
        result = self._values.get("push_config")
        return typing.cast(typing.Optional["GooglePubsubSubscriptionPushConfig"], result)

    @builtins.property
    def retain_acked_messages(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether to retain acknowledged messages.

        If 'true', then
        messages are not expunged from the subscription's backlog, even if
        they are acknowledged, until they fall out of the
        messageRetentionDuration window.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#retain_acked_messages GooglePubsubSubscription#retain_acked_messages}
        '''
        result = self._values.get("retain_acked_messages")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["GooglePubsubSubscriptionRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#retry_policy GooglePubsubSubscription#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["GooglePubsubSubscriptionRetryPolicy"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GooglePubsubSubscriptionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#timeouts GooglePubsubSubscription#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePubsubSubscriptionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionDeadLetterPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_topic": "deadLetterTopic",
        "max_delivery_attempts": "maxDeliveryAttempts",
    },
)
class GooglePubsubSubscriptionDeadLetterPolicy:
    def __init__(
        self,
        *,
        dead_letter_topic: typing.Optional[builtins.str] = None,
        max_delivery_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dead_letter_topic: The name of the topic to which dead letter messages should be published. Format is 'projects/{project}/topics/{topic}'. The Cloud Pub/Sub service account associated with the enclosing subscription's parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have permission to Publish() to this topic. The operation will fail if the topic does not exist. Users should ensure that there is a subscription attached to this topic since messages published to a topic with no subscriptions are lost. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#dead_letter_topic GooglePubsubSubscription#dead_letter_topic}
        :param max_delivery_attempts: The maximum number of delivery attempts for any message. The value must be between 5 and 100. The number of delivery attempts is defined as 1 + (the sum of number of NACKs and number of times the acknowledgement deadline has been exceeded for the message). A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that client libraries may automatically extend ack_deadlines. This field will be honored on a best effort basis. If this parameter is 0, a default value of 5 is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#max_delivery_attempts GooglePubsubSubscription#max_delivery_attempts}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionDeadLetterPolicy.__init__)
            check_type(argname="argument dead_letter_topic", value=dead_letter_topic, expected_type=type_hints["dead_letter_topic"])
            check_type(argname="argument max_delivery_attempts", value=max_delivery_attempts, expected_type=type_hints["max_delivery_attempts"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_topic is not None:
            self._values["dead_letter_topic"] = dead_letter_topic
        if max_delivery_attempts is not None:
            self._values["max_delivery_attempts"] = max_delivery_attempts

    @builtins.property
    def dead_letter_topic(self) -> typing.Optional[builtins.str]:
        '''The name of the topic to which dead letter messages should be published. Format is 'projects/{project}/topics/{topic}'.

        The Cloud Pub/Sub service account associated with the enclosing subscription's
        parent project (i.e.,
        service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have
        permission to Publish() to this topic.

        The operation will fail if the topic does not exist.
        Users should ensure that there is a subscription attached to this topic
        since messages published to a topic with no subscriptions are lost.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#dead_letter_topic GooglePubsubSubscription#dead_letter_topic}
        '''
        result = self._values.get("dead_letter_topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_delivery_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of delivery attempts for any message. The value must be between 5 and 100.

        The number of delivery attempts is defined as 1 + (the sum of number of
        NACKs and number of times the acknowledgement deadline has been exceeded for the message).

        A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that
        client libraries may automatically extend ack_deadlines.

        This field will be honored on a best effort basis.

        If this parameter is 0, a default value of 5 is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#max_delivery_attempts GooglePubsubSubscription#max_delivery_attempts}
        '''
        result = self._values.get("max_delivery_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionDeadLetterPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubSubscriptionDeadLetterPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionDeadLetterPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionDeadLetterPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeadLetterTopic")
    def reset_dead_letter_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeadLetterTopic", []))

    @jsii.member(jsii_name="resetMaxDeliveryAttempts")
    def reset_max_delivery_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDeliveryAttempts", []))

    @builtins.property
    @jsii.member(jsii_name="deadLetterTopicInput")
    def dead_letter_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deadLetterTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryAttemptsInput")
    def max_delivery_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDeliveryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="deadLetterTopic")
    def dead_letter_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deadLetterTopic"))

    @dead_letter_topic.setter
    def dead_letter_topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionDeadLetterPolicyOutputReference, "dead_letter_topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadLetterTopic", value)

    @builtins.property
    @jsii.member(jsii_name="maxDeliveryAttempts")
    def max_delivery_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDeliveryAttempts"))

    @max_delivery_attempts.setter
    def max_delivery_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionDeadLetterPolicyOutputReference, "max_delivery_attempts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDeliveryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePubsubSubscriptionDeadLetterPolicy]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionDeadLetterPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubSubscriptionDeadLetterPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionDeadLetterPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionExpirationPolicy",
    jsii_struct_bases=[],
    name_mapping={"ttl": "ttl"},
)
class GooglePubsubSubscriptionExpirationPolicy:
    def __init__(self, *, ttl: builtins.str) -> None:
        '''
        :param ttl: Specifies the "time-to-live" duration for an associated resource. The resource expires if it is not active for a period of ttl. If ttl is not set, the associated resource never expires. A duration in seconds with up to nine fractional digits, terminated by 's'. Example - "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#ttl GooglePubsubSubscription#ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionExpirationPolicy.__init__)
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "ttl": ttl,
        }

    @builtins.property
    def ttl(self) -> builtins.str:
        '''Specifies the "time-to-live" duration for an associated resource.

        The
        resource expires if it is not active for a period of ttl.
        If ttl is not set, the associated resource never expires.
        A duration in seconds with up to nine fractional digits, terminated by 's'.
        Example - "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#ttl GooglePubsubSubscription#ttl}
        '''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionExpirationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubSubscriptionExpirationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionExpirationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionExpirationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionExpirationPolicyOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePubsubSubscriptionExpirationPolicy]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionExpirationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubSubscriptionExpirationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionExpirationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionPushConfig",
    jsii_struct_bases=[],
    name_mapping={
        "push_endpoint": "pushEndpoint",
        "attributes": "attributes",
        "oidc_token": "oidcToken",
    },
)
class GooglePubsubSubscriptionPushConfig:
    def __init__(
        self,
        *,
        push_endpoint: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        oidc_token: typing.Optional[typing.Union["GooglePubsubSubscriptionPushConfigOidcToken", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param push_endpoint: A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use "https://example.com/push". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#push_endpoint GooglePubsubSubscription#push_endpoint}
        :param attributes: Endpoint configuration attributes. Every endpoint has a set of API supported attributes that can be used to control different aspects of the message delivery. The currently supported attribute is x-goog-version, which you can use to change the format of the pushed message. This attribute indicates the version of the data expected by the endpoint. This controls the shape of the pushed message (i.e., its fields and metadata). The endpoint version is based on the version of the Pub/Sub API. If not present during the subscriptions.create call, it will default to the version of the API used to make such call. If not present during a subscriptions.modifyPushConfig call, its value will not be changed. subscriptions.get calls will always return a valid version, even if the subscription was created without this attribute. The possible values for this attribute are: - v1beta1: uses the push format defined in the v1beta1 Pub/Sub API. - v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#attributes GooglePubsubSubscription#attributes}
        :param oidc_token: oidc_token block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#oidc_token GooglePubsubSubscription#oidc_token}
        '''
        if isinstance(oidc_token, dict):
            oidc_token = GooglePubsubSubscriptionPushConfigOidcToken(**oidc_token)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionPushConfig.__init__)
            check_type(argname="argument push_endpoint", value=push_endpoint, expected_type=type_hints["push_endpoint"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument oidc_token", value=oidc_token, expected_type=type_hints["oidc_token"])
        self._values: typing.Dict[str, typing.Any] = {
            "push_endpoint": push_endpoint,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if oidc_token is not None:
            self._values["oidc_token"] = oidc_token

    @builtins.property
    def push_endpoint(self) -> builtins.str:
        '''A URL locating the endpoint to which messages should be pushed. For example, a Webhook endpoint might use "https://example.com/push".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#push_endpoint GooglePubsubSubscription#push_endpoint}
        '''
        result = self._values.get("push_endpoint")
        assert result is not None, "Required property 'push_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Endpoint configuration attributes.

        Every endpoint has a set of API supported attributes that can
        be used to control different aspects of the message delivery.

        The currently supported attribute is x-goog-version, which you
        can use to change the format of the pushed message. This
        attribute indicates the version of the data expected by
        the endpoint. This controls the shape of the pushed message
        (i.e., its fields and metadata). The endpoint version is
        based on the version of the Pub/Sub API.

        If not present during the subscriptions.create call,
        it will default to the version of the API used to make
        such call. If not present during a subscriptions.modifyPushConfig
        call, its value will not be changed. subscriptions.get
        calls will always return a valid version, even if the
        subscription was created without this attribute.

        The possible values for this attribute are:

        - v1beta1: uses the push format defined in the v1beta1 Pub/Sub API.
        - v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#attributes GooglePubsubSubscription#attributes}
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def oidc_token(
        self,
    ) -> typing.Optional["GooglePubsubSubscriptionPushConfigOidcToken"]:
        '''oidc_token block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#oidc_token GooglePubsubSubscription#oidc_token}
        '''
        result = self._values.get("oidc_token")
        return typing.cast(typing.Optional["GooglePubsubSubscriptionPushConfigOidcToken"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionPushConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionPushConfigOidcToken",
    jsii_struct_bases=[],
    name_mapping={
        "service_account_email": "serviceAccountEmail",
        "audience": "audience",
    },
)
class GooglePubsubSubscriptionPushConfigOidcToken:
    def __init__(
        self,
        *,
        service_account_email: builtins.str,
        audience: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_account_email: Service account email to be used for generating the OIDC token. The caller (for subscriptions.create, subscriptions.patch, and subscriptions.modifyPushConfig RPCs) must have the iam.serviceAccounts.actAs permission for the service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#service_account_email GooglePubsubSubscription#service_account_email}
        :param audience: Audience to be used when generating OIDC token. The audience claim identifies the recipients that the JWT is intended for. The audience value is a single case-sensitive string. Having multiple values (array) for the audience field is not supported. More info about the OIDC JWT token audience here: https://tools.ietf.org/html/rfc7519#section-4.1.3 Note: if not specified, the Push endpoint URL will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#audience GooglePubsubSubscription#audience}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionPushConfigOidcToken.__init__)
            check_type(argname="argument service_account_email", value=service_account_email, expected_type=type_hints["service_account_email"])
            check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
        self._values: typing.Dict[str, typing.Any] = {
            "service_account_email": service_account_email,
        }
        if audience is not None:
            self._values["audience"] = audience

    @builtins.property
    def service_account_email(self) -> builtins.str:
        '''Service account email to be used for generating the OIDC token.

        The caller (for subscriptions.create, subscriptions.patch, and
        subscriptions.modifyPushConfig RPCs) must have the
        iam.serviceAccounts.actAs permission for the service account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#service_account_email GooglePubsubSubscription#service_account_email}
        '''
        result = self._values.get("service_account_email")
        assert result is not None, "Required property 'service_account_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audience(self) -> typing.Optional[builtins.str]:
        '''Audience to be used when generating OIDC token.

        The audience claim
        identifies the recipients that the JWT is intended for. The audience
        value is a single case-sensitive string. Having multiple values (array)
        for the audience field is not supported. More info about the OIDC JWT
        token audience here: https://tools.ietf.org/html/rfc7519#section-4.1.3
        Note: if not specified, the Push endpoint URL will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#audience GooglePubsubSubscription#audience}
        '''
        result = self._values.get("audience")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionPushConfigOidcToken(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubSubscriptionPushConfigOidcTokenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionPushConfigOidcTokenOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionPushConfigOidcTokenOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudience")
    def reset_audience(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudience", []))

    @builtins.property
    @jsii.member(jsii_name="audienceInput")
    def audience_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audienceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailInput")
    def service_account_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="audience")
    def audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audience"))

    @audience.setter
    def audience(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionPushConfigOidcTokenOutputReference, "audience").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audience", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @service_account_email.setter
    def service_account_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionPushConfigOidcTokenOutputReference, "service_account_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountEmail", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePubsubSubscriptionPushConfigOidcToken]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionPushConfigOidcToken], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubSubscriptionPushConfigOidcToken],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionPushConfigOidcTokenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePubsubSubscriptionPushConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionPushConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionPushConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOidcToken")
    def put_oidc_token(
        self,
        *,
        service_account_email: builtins.str,
        audience: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param service_account_email: Service account email to be used for generating the OIDC token. The caller (for subscriptions.create, subscriptions.patch, and subscriptions.modifyPushConfig RPCs) must have the iam.serviceAccounts.actAs permission for the service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#service_account_email GooglePubsubSubscription#service_account_email}
        :param audience: Audience to be used when generating OIDC token. The audience claim identifies the recipients that the JWT is intended for. The audience value is a single case-sensitive string. Having multiple values (array) for the audience field is not supported. More info about the OIDC JWT token audience here: https://tools.ietf.org/html/rfc7519#section-4.1.3 Note: if not specified, the Push endpoint URL will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#audience GooglePubsubSubscription#audience}
        '''
        value = GooglePubsubSubscriptionPushConfigOidcToken(
            service_account_email=service_account_email, audience=audience
        )

        return typing.cast(None, jsii.invoke(self, "putOidcToken", [value]))

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @jsii.member(jsii_name="resetOidcToken")
    def reset_oidc_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOidcToken", []))

    @builtins.property
    @jsii.member(jsii_name="oidcToken")
    def oidc_token(self) -> GooglePubsubSubscriptionPushConfigOidcTokenOutputReference:
        return typing.cast(GooglePubsubSubscriptionPushConfigOidcTokenOutputReference, jsii.get(self, "oidcToken"))

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "attributesInput"))

    @builtins.property
    @jsii.member(jsii_name="oidcTokenInput")
    def oidc_token_input(
        self,
    ) -> typing.Optional[GooglePubsubSubscriptionPushConfigOidcToken]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionPushConfigOidcToken], jsii.get(self, "oidcTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEndpointInput")
    def push_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pushEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionPushConfigOutputReference, "attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="pushEndpoint")
    def push_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pushEndpoint"))

    @push_endpoint.setter
    def push_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionPushConfigOutputReference, "push_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePubsubSubscriptionPushConfig]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionPushConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubSubscriptionPushConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionPushConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "maximum_backoff": "maximumBackoff",
        "minimum_backoff": "minimumBackoff",
    },
)
class GooglePubsubSubscriptionRetryPolicy:
    def __init__(
        self,
        *,
        maximum_backoff: typing.Optional[builtins.str] = None,
        minimum_backoff: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param maximum_backoff: The maximum delay between consecutive deliveries of a given message. Value should be between 0 and 600 seconds. Defaults to 600 seconds. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#maximum_backoff GooglePubsubSubscription#maximum_backoff}
        :param minimum_backoff: The minimum delay between consecutive deliveries of a given message. Value should be between 0 and 600 seconds. Defaults to 10 seconds. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#minimum_backoff GooglePubsubSubscription#minimum_backoff}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionRetryPolicy.__init__)
            check_type(argname="argument maximum_backoff", value=maximum_backoff, expected_type=type_hints["maximum_backoff"])
            check_type(argname="argument minimum_backoff", value=minimum_backoff, expected_type=type_hints["minimum_backoff"])
        self._values: typing.Dict[str, typing.Any] = {}
        if maximum_backoff is not None:
            self._values["maximum_backoff"] = maximum_backoff
        if minimum_backoff is not None:
            self._values["minimum_backoff"] = minimum_backoff

    @builtins.property
    def maximum_backoff(self) -> typing.Optional[builtins.str]:
        '''The maximum delay between consecutive deliveries of a given message.

        Value should be between 0 and 600 seconds. Defaults to 600 seconds.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#maximum_backoff GooglePubsubSubscription#maximum_backoff}
        '''
        result = self._values.get("maximum_backoff")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_backoff(self) -> typing.Optional[builtins.str]:
        '''The minimum delay between consecutive deliveries of a given message.

        Value should be between 0 and 600 seconds. Defaults to 10 seconds.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#minimum_backoff GooglePubsubSubscription#minimum_backoff}
        '''
        result = self._values.get("minimum_backoff")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubSubscriptionRetryPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionRetryPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaximumBackoff")
    def reset_maximum_backoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBackoff", []))

    @jsii.member(jsii_name="resetMinimumBackoff")
    def reset_minimum_backoff(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumBackoff", []))

    @builtins.property
    @jsii.member(jsii_name="maximumBackoffInput")
    def maximum_backoff_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumBackoffInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumBackoffInput")
    def minimum_backoff_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumBackoffInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBackoff")
    def maximum_backoff(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumBackoff"))

    @maximum_backoff.setter
    def maximum_backoff(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionRetryPolicyOutputReference, "maximum_backoff").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBackoff", value)

    @builtins.property
    @jsii.member(jsii_name="minimumBackoff")
    def minimum_backoff(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumBackoff"))

    @minimum_backoff.setter
    def minimum_backoff(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionRetryPolicyOutputReference, "minimum_backoff").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumBackoff", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePubsubSubscriptionRetryPolicy]:
        return typing.cast(typing.Optional[GooglePubsubSubscriptionRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePubsubSubscriptionRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionRetryPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePubsubSubscriptionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#create GooglePubsubSubscription#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#delete GooglePubsubSubscription#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#update GooglePubsubSubscription#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#create GooglePubsubSubscription#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#delete GooglePubsubSubscription#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_pubsub_subscription#update GooglePubsubSubscription#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePubsubSubscriptionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePubsubSubscriptionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePubsubSubscription.GooglePubsubSubscriptionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePubsubSubscriptionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePubsubSubscriptionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePubsubSubscriptionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePubsubSubscriptionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePubsubSubscriptionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePubsubSubscription",
    "GooglePubsubSubscriptionBigqueryConfig",
    "GooglePubsubSubscriptionBigqueryConfigOutputReference",
    "GooglePubsubSubscriptionConfig",
    "GooglePubsubSubscriptionDeadLetterPolicy",
    "GooglePubsubSubscriptionDeadLetterPolicyOutputReference",
    "GooglePubsubSubscriptionExpirationPolicy",
    "GooglePubsubSubscriptionExpirationPolicyOutputReference",
    "GooglePubsubSubscriptionPushConfig",
    "GooglePubsubSubscriptionPushConfigOidcToken",
    "GooglePubsubSubscriptionPushConfigOidcTokenOutputReference",
    "GooglePubsubSubscriptionPushConfigOutputReference",
    "GooglePubsubSubscriptionRetryPolicy",
    "GooglePubsubSubscriptionRetryPolicyOutputReference",
    "GooglePubsubSubscriptionTimeouts",
    "GooglePubsubSubscriptionTimeoutsOutputReference",
]

publication.publish()
