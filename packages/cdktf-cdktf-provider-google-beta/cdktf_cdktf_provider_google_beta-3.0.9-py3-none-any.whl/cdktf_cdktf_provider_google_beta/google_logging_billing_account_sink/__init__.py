'''
# `google_logging_billing_account_sink`

Refer to the Terraform Registory for docs: [`google_logging_billing_account_sink`](https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink).
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


class GoogleLoggingBillingAccountSink(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSink",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink google_logging_billing_account_sink}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        billing_account: builtins.str,
        destination: builtins.str,
        name: builtins.str,
        bigquery_options: typing.Optional[typing.Union["GoogleLoggingBillingAccountSinkBigqueryOptions", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclusions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleLoggingBillingAccountSinkExclusions", typing.Dict[str, typing.Any]]]]] = None,
        filter: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink google_logging_billing_account_sink} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param billing_account: The billing account exported to the sink. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#billing_account GoogleLoggingBillingAccountSink#billing_account}
        :param destination: The destination of the sink (or, in other words, where logs are written to). Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The writer associated with the sink must have access to write to the above resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#destination GoogleLoggingBillingAccountSink#destination}
        :param name: The name of the logging sink. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#name GoogleLoggingBillingAccountSink#name}
        :param bigquery_options: bigquery_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#bigquery_options GoogleLoggingBillingAccountSink#bigquery_options}
        :param description: A description of this sink. The maximum length of the description is 8000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#description GoogleLoggingBillingAccountSink#description}
        :param disabled: If set to True, then this sink is disabled and it does not export any log entries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#disabled GoogleLoggingBillingAccountSink#disabled}
        :param exclusions: exclusions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#exclusions GoogleLoggingBillingAccountSink#exclusions}
        :param filter: The filter to apply when exporting logs. Only log entries that match the filter are exported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#filter GoogleLoggingBillingAccountSink#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#id GoogleLoggingBillingAccountSink#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSink.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleLoggingBillingAccountSinkConfig(
            billing_account=billing_account,
            destination=destination,
            name=name,
            bigquery_options=bigquery_options,
            description=description,
            disabled=disabled,
            exclusions=exclusions,
            filter=filter,
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

    @jsii.member(jsii_name="putBigqueryOptions")
    def put_bigquery_options(
        self,
        *,
        use_partitioned_tables: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param use_partitioned_tables: Whether to use BigQuery's partition tables. By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned tables the date suffix is no longer present and special query syntax has to be used instead. In both cases, tables are sharded based on UTC timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#use_partitioned_tables GoogleLoggingBillingAccountSink#use_partitioned_tables}
        '''
        value = GoogleLoggingBillingAccountSinkBigqueryOptions(
            use_partitioned_tables=use_partitioned_tables
        )

        return typing.cast(None, jsii.invoke(self, "putBigqueryOptions", [value]))

    @jsii.member(jsii_name="putExclusions")
    def put_exclusions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleLoggingBillingAccountSinkExclusions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSink.put_exclusions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExclusions", [value]))

    @jsii.member(jsii_name="resetBigqueryOptions")
    def reset_bigquery_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBigqueryOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetExclusions")
    def reset_exclusions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusions", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

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
    @jsii.member(jsii_name="bigqueryOptions")
    def bigquery_options(
        self,
    ) -> "GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference":
        return typing.cast("GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference", jsii.get(self, "bigqueryOptions"))

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(self) -> "GoogleLoggingBillingAccountSinkExclusionsList":
        return typing.cast("GoogleLoggingBillingAccountSinkExclusionsList", jsii.get(self, "exclusions"))

    @builtins.property
    @jsii.member(jsii_name="writerIdentity")
    def writer_identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writerIdentity"))

    @builtins.property
    @jsii.member(jsii_name="bigqueryOptionsInput")
    def bigquery_options_input(
        self,
    ) -> typing.Optional["GoogleLoggingBillingAccountSinkBigqueryOptions"]:
        return typing.cast(typing.Optional["GoogleLoggingBillingAccountSinkBigqueryOptions"], jsii.get(self, "bigqueryOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="billingAccountInput")
    def billing_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionsInput")
    def exclusions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleLoggingBillingAccountSinkExclusions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleLoggingBillingAccountSinkExclusions"]]], jsii.get(self, "exclusionsInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="billingAccount")
    def billing_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "billingAccount"))

    @billing_account.setter
    def billing_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "billing_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingAccount", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSink, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSinkBigqueryOptions",
    jsii_struct_bases=[],
    name_mapping={"use_partitioned_tables": "usePartitionedTables"},
)
class GoogleLoggingBillingAccountSinkBigqueryOptions:
    def __init__(
        self,
        *,
        use_partitioned_tables: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param use_partitioned_tables: Whether to use BigQuery's partition tables. By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned tables the date suffix is no longer present and special query syntax has to be used instead. In both cases, tables are sharded based on UTC timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#use_partitioned_tables GoogleLoggingBillingAccountSink#use_partitioned_tables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkBigqueryOptions.__init__)
            check_type(argname="argument use_partitioned_tables", value=use_partitioned_tables, expected_type=type_hints["use_partitioned_tables"])
        self._values: typing.Dict[str, typing.Any] = {
            "use_partitioned_tables": use_partitioned_tables,
        }

    @builtins.property
    def use_partitioned_tables(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Whether to use BigQuery's partition tables.

        By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned tables the date suffix is no longer present and special query syntax has to be used instead. In both cases, tables are sharded based on UTC timezone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#use_partitioned_tables GoogleLoggingBillingAccountSink#use_partitioned_tables}
        '''
        result = self._values.get("use_partitioned_tables")
        assert result is not None, "Required property 'use_partitioned_tables' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleLoggingBillingAccountSinkBigqueryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="usePartitionedTablesInput")
    def use_partitioned_tables_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "usePartitionedTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="usePartitionedTables")
    def use_partitioned_tables(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "usePartitionedTables"))

    @use_partitioned_tables.setter
    def use_partitioned_tables(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference, "use_partitioned_tables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePartitionedTables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleLoggingBillingAccountSinkBigqueryOptions]:
        return typing.cast(typing.Optional[GoogleLoggingBillingAccountSinkBigqueryOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleLoggingBillingAccountSinkBigqueryOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSinkConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "billing_account": "billingAccount",
        "destination": "destination",
        "name": "name",
        "bigquery_options": "bigqueryOptions",
        "description": "description",
        "disabled": "disabled",
        "exclusions": "exclusions",
        "filter": "filter",
        "id": "id",
    },
)
class GoogleLoggingBillingAccountSinkConfig(cdktf.TerraformMetaArguments):
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
        billing_account: builtins.str,
        destination: builtins.str,
        name: builtins.str,
        bigquery_options: typing.Optional[typing.Union[GoogleLoggingBillingAccountSinkBigqueryOptions, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exclusions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleLoggingBillingAccountSinkExclusions", typing.Dict[str, typing.Any]]]]] = None,
        filter: typing.Optional[builtins.str] = None,
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
        :param billing_account: The billing account exported to the sink. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#billing_account GoogleLoggingBillingAccountSink#billing_account}
        :param destination: The destination of the sink (or, in other words, where logs are written to). Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The writer associated with the sink must have access to write to the above resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#destination GoogleLoggingBillingAccountSink#destination}
        :param name: The name of the logging sink. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#name GoogleLoggingBillingAccountSink#name}
        :param bigquery_options: bigquery_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#bigquery_options GoogleLoggingBillingAccountSink#bigquery_options}
        :param description: A description of this sink. The maximum length of the description is 8000 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#description GoogleLoggingBillingAccountSink#description}
        :param disabled: If set to True, then this sink is disabled and it does not export any log entries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#disabled GoogleLoggingBillingAccountSink#disabled}
        :param exclusions: exclusions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#exclusions GoogleLoggingBillingAccountSink#exclusions}
        :param filter: The filter to apply when exporting logs. Only log entries that match the filter are exported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#filter GoogleLoggingBillingAccountSink#filter}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#id GoogleLoggingBillingAccountSink#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(bigquery_options, dict):
            bigquery_options = GoogleLoggingBillingAccountSinkBigqueryOptions(**bigquery_options)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument billing_account", value=billing_account, expected_type=type_hints["billing_account"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument bigquery_options", value=bigquery_options, expected_type=type_hints["bigquery_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "billing_account": billing_account,
            "destination": destination,
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
        if bigquery_options is not None:
            self._values["bigquery_options"] = bigquery_options
        if description is not None:
            self._values["description"] = description
        if disabled is not None:
            self._values["disabled"] = disabled
        if exclusions is not None:
            self._values["exclusions"] = exclusions
        if filter is not None:
            self._values["filter"] = filter
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
    def billing_account(self) -> builtins.str:
        '''The billing account exported to the sink.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#billing_account GoogleLoggingBillingAccountSink#billing_account}
        '''
        result = self._values.get("billing_account")
        assert result is not None, "Required property 'billing_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> builtins.str:
        '''The destination of the sink (or, in other words, where logs are written to).

        Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" The writer associated with the sink must have access to write to the above resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#destination GoogleLoggingBillingAccountSink#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the logging sink.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#name GoogleLoggingBillingAccountSink#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bigquery_options(
        self,
    ) -> typing.Optional[GoogleLoggingBillingAccountSinkBigqueryOptions]:
        '''bigquery_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#bigquery_options GoogleLoggingBillingAccountSink#bigquery_options}
        '''
        result = self._values.get("bigquery_options")
        return typing.cast(typing.Optional[GoogleLoggingBillingAccountSinkBigqueryOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this sink. The maximum length of the description is 8000 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#description GoogleLoggingBillingAccountSink#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to True, then this sink is disabled and it does not export any log entries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#disabled GoogleLoggingBillingAccountSink#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exclusions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleLoggingBillingAccountSinkExclusions"]]]:
        '''exclusions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#exclusions GoogleLoggingBillingAccountSink#exclusions}
        '''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleLoggingBillingAccountSinkExclusions"]]], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''The filter to apply when exporting logs. Only log entries that match the filter are exported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#filter GoogleLoggingBillingAccountSink#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#id GoogleLoggingBillingAccountSink#id}.

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
        return "GoogleLoggingBillingAccountSinkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSinkExclusions",
    jsii_struct_bases=[],
    name_mapping={
        "filter": "filter",
        "name": "name",
        "description": "description",
        "disabled": "disabled",
    },
)
class GoogleLoggingBillingAccountSinkExclusions:
    def __init__(
        self,
        *,
        filter: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param filter: An advanced logs filter that matches the log entries to be excluded. By using the sample function, you can exclude less than 100% of the matching log entries Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#filter GoogleLoggingBillingAccountSink#filter}
        :param name: A client-assigned identifier, such as "load-balancer-exclusion". Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#name GoogleLoggingBillingAccountSink#name}
        :param description: A description of this exclusion. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#description GoogleLoggingBillingAccountSink#description}
        :param disabled: If set to True, then this exclusion is disabled and it does not exclude any log entries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#disabled GoogleLoggingBillingAccountSink#disabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkExclusions.__init__)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if disabled is not None:
            self._values["disabled"] = disabled

    @builtins.property
    def filter(self) -> builtins.str:
        '''An advanced logs filter that matches the log entries to be excluded.

        By using the sample function, you can exclude less than 100% of the matching log entries

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#filter GoogleLoggingBillingAccountSink#filter}
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A client-assigned identifier, such as "load-balancer-exclusion".

        Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#name GoogleLoggingBillingAccountSink#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of this exclusion.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#description GoogleLoggingBillingAccountSink#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to True, then this exclusion is disabled and it does not exclude any log entries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_logging_billing_account_sink#disabled GoogleLoggingBillingAccountSink#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleLoggingBillingAccountSinkExclusions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleLoggingBillingAccountSinkExclusionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSinkExclusionsList",
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
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkExclusionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleLoggingBillingAccountSinkExclusionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkExclusionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleLoggingBillingAccountSinkExclusionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleLoggingBillingAccountSinkExclusions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleLoggingBillingAccountSinkExclusions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleLoggingBillingAccountSinkExclusions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleLoggingBillingAccountSinkExclusionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleLoggingBillingAccountSink.GoogleLoggingBillingAccountSinkExclusionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleLoggingBillingAccountSinkExclusionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsOutputReference, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleLoggingBillingAccountSinkExclusions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleLoggingBillingAccountSinkExclusions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleLoggingBillingAccountSinkExclusions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleLoggingBillingAccountSinkExclusionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleLoggingBillingAccountSink",
    "GoogleLoggingBillingAccountSinkBigqueryOptions",
    "GoogleLoggingBillingAccountSinkBigqueryOptionsOutputReference",
    "GoogleLoggingBillingAccountSinkConfig",
    "GoogleLoggingBillingAccountSinkExclusions",
    "GoogleLoggingBillingAccountSinkExclusionsList",
    "GoogleLoggingBillingAccountSinkExclusionsOutputReference",
]

publication.publish()
