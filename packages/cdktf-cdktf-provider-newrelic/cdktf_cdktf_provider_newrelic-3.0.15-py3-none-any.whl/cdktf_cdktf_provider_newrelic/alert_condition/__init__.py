'''
# `newrelic_alert_condition`

Refer to the Terraform Registory for docs: [`newrelic_alert_condition`](https://www.terraform.io/docs/providers/newrelic/r/alert_condition).
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


class AlertCondition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.alertCondition.AlertCondition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition newrelic_alert_condition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        entities: typing.Sequence[jsii.Number],
        metric: builtins.str,
        name: builtins.str,
        policy_id: jsii.Number,
        term: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AlertConditionTerm", typing.Dict[str, typing.Any]]]],
        type: builtins.str,
        condition_scope: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gc_metric: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        user_defined_metric: typing.Optional[builtins.str] = None,
        user_defined_value_function: typing.Optional[builtins.str] = None,
        violation_close_timer: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition newrelic_alert_condition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param entities: The instance IDs associated with this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#entities AlertCondition#entities}
        :param metric: The metric field accepts parameters based on the type set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#metric AlertCondition#metric}
        :param name: The title of the condition. Must be between 1 and 128 characters, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#name AlertCondition#name}
        :param policy_id: The ID of the policy where this condition should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#policy_id AlertCondition#policy_id}
        :param term: term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#term AlertCondition#term}
        :param type: The type of condition. One of: (apm_app_metric, apm_jvm_metric, apm_kt_metric, browser_metric, mobile_metric, servers_metric). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#type AlertCondition#type}
        :param condition_scope: One of (application, instance). Choose application for most scenarios. If you are using the JVM plugin in New Relic, the instance setting allows your condition to trigger for specific app instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#condition_scope AlertCondition#condition_scope}
        :param enabled: Whether the condition is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#enabled AlertCondition#enabled}
        :param gc_metric: A valid Garbage Collection metric e.g. GC/G1 Young Generation. This is required if you are using apm_jvm_metric with gc_cpu_time condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#gc_metric AlertCondition#gc_metric}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#id AlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#runbook_url AlertCondition#runbook_url}
        :param user_defined_metric: A custom metric to be evaluated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#user_defined_metric AlertCondition#user_defined_metric}
        :param user_defined_value_function: One of: (average, min, max, total, sample_size). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#user_defined_value_function AlertCondition#user_defined_value_function}
        :param violation_close_timer: Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: 1, 2, 4, 8, 12 or 24. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#violation_close_timer AlertCondition#violation_close_timer}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AlertCondition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AlertConditionConfig(
            entities=entities,
            metric=metric,
            name=name,
            policy_id=policy_id,
            term=term,
            type=type,
            condition_scope=condition_scope,
            enabled=enabled,
            gc_metric=gc_metric,
            id=id,
            runbook_url=runbook_url,
            user_defined_metric=user_defined_metric,
            user_defined_value_function=user_defined_value_function,
            violation_close_timer=violation_close_timer,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTerm")
    def put_term(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AlertConditionTerm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AlertCondition.put_term)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTerm", [value]))

    @jsii.member(jsii_name="resetConditionScope")
    def reset_condition_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditionScope", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetGcMetric")
    def reset_gc_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcMetric", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRunbookUrl")
    def reset_runbook_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunbookUrl", []))

    @jsii.member(jsii_name="resetUserDefinedMetric")
    def reset_user_defined_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDefinedMetric", []))

    @jsii.member(jsii_name="resetUserDefinedValueFunction")
    def reset_user_defined_value_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDefinedValueFunction", []))

    @jsii.member(jsii_name="resetViolationCloseTimer")
    def reset_violation_close_timer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViolationCloseTimer", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="term")
    def term(self) -> "AlertConditionTermList":
        return typing.cast("AlertConditionTermList", jsii.get(self, "term"))

    @builtins.property
    @jsii.member(jsii_name="conditionScopeInput")
    def condition_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="entitiesInput")
    def entities_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "entitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="gcMetricInput")
    def gc_metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gcMetricInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="runbookUrlInput")
    def runbook_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runbookUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="termInput")
    def term_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AlertConditionTerm"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AlertConditionTerm"]]], jsii.get(self, "termInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userDefinedMetricInput")
    def user_defined_metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDefinedMetricInput"))

    @builtins.property
    @jsii.member(jsii_name="userDefinedValueFunctionInput")
    def user_defined_value_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDefinedValueFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="violationCloseTimerInput")
    def violation_close_timer_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "violationCloseTimerInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionScope")
    def condition_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "conditionScope"))

    @condition_scope.setter
    def condition_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "condition_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditionScope", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="entities")
    def entities(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "entities"))

    @entities.setter
    def entities(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "entities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entities", value)

    @builtins.property
    @jsii.member(jsii_name="gcMetric")
    def gc_metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcMetric"))

    @gc_metric.setter
    def gc_metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "gc_metric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcMetric", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metric"))

    @metric.setter
    def metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "metric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metric", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="runbookUrl")
    def runbook_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runbookUrl"))

    @runbook_url.setter
    def runbook_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "runbook_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runbookUrl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="userDefinedMetric")
    def user_defined_metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userDefinedMetric"))

    @user_defined_metric.setter
    def user_defined_metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "user_defined_metric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDefinedMetric", value)

    @builtins.property
    @jsii.member(jsii_name="userDefinedValueFunction")
    def user_defined_value_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userDefinedValueFunction"))

    @user_defined_value_function.setter
    def user_defined_value_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "user_defined_value_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDefinedValueFunction", value)

    @builtins.property
    @jsii.member(jsii_name="violationCloseTimer")
    def violation_close_timer(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "violationCloseTimer"))

    @violation_close_timer.setter
    def violation_close_timer(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertCondition, "violation_close_timer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "violationCloseTimer", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.alertCondition.AlertConditionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "entities": "entities",
        "metric": "metric",
        "name": "name",
        "policy_id": "policyId",
        "term": "term",
        "type": "type",
        "condition_scope": "conditionScope",
        "enabled": "enabled",
        "gc_metric": "gcMetric",
        "id": "id",
        "runbook_url": "runbookUrl",
        "user_defined_metric": "userDefinedMetric",
        "user_defined_value_function": "userDefinedValueFunction",
        "violation_close_timer": "violationCloseTimer",
    },
)
class AlertConditionConfig(cdktf.TerraformMetaArguments):
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
        entities: typing.Sequence[jsii.Number],
        metric: builtins.str,
        name: builtins.str,
        policy_id: jsii.Number,
        term: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AlertConditionTerm", typing.Dict[str, typing.Any]]]],
        type: builtins.str,
        condition_scope: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gc_metric: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        user_defined_metric: typing.Optional[builtins.str] = None,
        user_defined_value_function: typing.Optional[builtins.str] = None,
        violation_close_timer: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param entities: The instance IDs associated with this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#entities AlertCondition#entities}
        :param metric: The metric field accepts parameters based on the type set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#metric AlertCondition#metric}
        :param name: The title of the condition. Must be between 1 and 128 characters, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#name AlertCondition#name}
        :param policy_id: The ID of the policy where this condition should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#policy_id AlertCondition#policy_id}
        :param term: term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#term AlertCondition#term}
        :param type: The type of condition. One of: (apm_app_metric, apm_jvm_metric, apm_kt_metric, browser_metric, mobile_metric, servers_metric). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#type AlertCondition#type}
        :param condition_scope: One of (application, instance). Choose application for most scenarios. If you are using the JVM plugin in New Relic, the instance setting allows your condition to trigger for specific app instances. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#condition_scope AlertCondition#condition_scope}
        :param enabled: Whether the condition is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#enabled AlertCondition#enabled}
        :param gc_metric: A valid Garbage Collection metric e.g. GC/G1 Young Generation. This is required if you are using apm_jvm_metric with gc_cpu_time condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#gc_metric AlertCondition#gc_metric}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#id AlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#runbook_url AlertCondition#runbook_url}
        :param user_defined_metric: A custom metric to be evaluated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#user_defined_metric AlertCondition#user_defined_metric}
        :param user_defined_value_function: One of: (average, min, max, total, sample_size). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#user_defined_value_function AlertCondition#user_defined_value_function}
        :param violation_close_timer: Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: 1, 2, 4, 8, 12 or 24. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#violation_close_timer AlertCondition#violation_close_timer}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AlertConditionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument entities", value=entities, expected_type=type_hints["entities"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument term", value=term, expected_type=type_hints["term"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument condition_scope", value=condition_scope, expected_type=type_hints["condition_scope"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument gc_metric", value=gc_metric, expected_type=type_hints["gc_metric"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument runbook_url", value=runbook_url, expected_type=type_hints["runbook_url"])
            check_type(argname="argument user_defined_metric", value=user_defined_metric, expected_type=type_hints["user_defined_metric"])
            check_type(argname="argument user_defined_value_function", value=user_defined_value_function, expected_type=type_hints["user_defined_value_function"])
            check_type(argname="argument violation_close_timer", value=violation_close_timer, expected_type=type_hints["violation_close_timer"])
        self._values: typing.Dict[str, typing.Any] = {
            "entities": entities,
            "metric": metric,
            "name": name,
            "policy_id": policy_id,
            "term": term,
            "type": type,
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
        if condition_scope is not None:
            self._values["condition_scope"] = condition_scope
        if enabled is not None:
            self._values["enabled"] = enabled
        if gc_metric is not None:
            self._values["gc_metric"] = gc_metric
        if id is not None:
            self._values["id"] = id
        if runbook_url is not None:
            self._values["runbook_url"] = runbook_url
        if user_defined_metric is not None:
            self._values["user_defined_metric"] = user_defined_metric
        if user_defined_value_function is not None:
            self._values["user_defined_value_function"] = user_defined_value_function
        if violation_close_timer is not None:
            self._values["violation_close_timer"] = violation_close_timer

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
    def entities(self) -> typing.List[jsii.Number]:
        '''The instance IDs associated with this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#entities AlertCondition#entities}
        '''
        result = self._values.get("entities")
        assert result is not None, "Required property 'entities' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def metric(self) -> builtins.str:
        '''The metric field accepts parameters based on the type set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#metric AlertCondition#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The title of the condition. Must be between 1 and 128 characters, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#name AlertCondition#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> jsii.Number:
        '''The ID of the policy where this condition should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#policy_id AlertCondition#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def term(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["AlertConditionTerm"]]:
        '''term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#term AlertCondition#term}
        '''
        result = self._values.get("term")
        assert result is not None, "Required property 'term' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["AlertConditionTerm"]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of condition. One of: (apm_app_metric, apm_jvm_metric, apm_kt_metric, browser_metric, mobile_metric, servers_metric).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#type AlertCondition#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition_scope(self) -> typing.Optional[builtins.str]:
        '''One of (application, instance).

        Choose application for most scenarios. If you are using the JVM plugin in New Relic, the instance setting allows your condition to trigger for specific app instances.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#condition_scope AlertCondition#condition_scope}
        '''
        result = self._values.get("condition_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the condition is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#enabled AlertCondition#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gc_metric(self) -> typing.Optional[builtins.str]:
        '''A valid Garbage Collection metric e.g. GC/G1 Young Generation. This is required if you are using apm_jvm_metric with gc_cpu_time condition type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#gc_metric AlertCondition#gc_metric}
        '''
        result = self._values.get("gc_metric")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#id AlertCondition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runbook_url(self) -> typing.Optional[builtins.str]:
        '''Runbook URL to display in notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#runbook_url AlertCondition#runbook_url}
        '''
        result = self._values.get("runbook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_defined_metric(self) -> typing.Optional[builtins.str]:
        '''A custom metric to be evaluated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#user_defined_metric AlertCondition#user_defined_metric}
        '''
        result = self._values.get("user_defined_metric")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_defined_value_function(self) -> typing.Optional[builtins.str]:
        '''One of: (average, min, max, total, sample_size).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#user_defined_value_function AlertCondition#user_defined_value_function}
        '''
        result = self._values.get("user_defined_value_function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def violation_close_timer(self) -> typing.Optional[jsii.Number]:
        '''Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified.

        Must be: 1, 2, 4, 8, 12 or 24.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#violation_close_timer AlertCondition#violation_close_timer}
        '''
        result = self._values.get("violation_close_timer")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlertConditionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.alertCondition.AlertConditionTerm",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "threshold": "threshold",
        "time_function": "timeFunction",
        "operator": "operator",
        "priority": "priority",
    },
)
class AlertConditionTerm:
    def __init__(
        self,
        *,
        duration: jsii.Number,
        threshold: jsii.Number,
        time_function: builtins.str,
        operator: typing.Optional[builtins.str] = None,
        priority: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param duration: In minutes, must be in the range of 5 to 120, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#duration AlertCondition#duration}
        :param threshold: Must be 0 or greater. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#threshold AlertCondition#threshold}
        :param time_function: One of (all, any). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#time_function AlertCondition#time_function}
        :param operator: One of (above, below, equal). Defaults to equal. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#operator AlertCondition#operator}
        :param priority: One of (critical, warning). Defaults to critical. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#priority AlertCondition#priority}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AlertConditionTerm.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument time_function", value=time_function, expected_type=type_hints["time_function"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
            "threshold": threshold,
            "time_function": time_function,
        }
        if operator is not None:
            self._values["operator"] = operator
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def duration(self) -> jsii.Number:
        '''In minutes, must be in the range of 5 to 120, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#duration AlertCondition#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Must be 0 or greater.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#threshold AlertCondition#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_function(self) -> builtins.str:
        '''One of (all, any).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#time_function AlertCondition#time_function}
        '''
        result = self._values.get("time_function")
        assert result is not None, "Required property 'time_function' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''One of (above, below, equal). Defaults to equal.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#operator AlertCondition#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''One of (critical, warning). Defaults to critical.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_condition#priority AlertCondition#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlertConditionTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlertConditionTermList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.alertCondition.AlertConditionTermList",
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
            type_hints = typing.get_type_hints(AlertConditionTermList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AlertConditionTermOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AlertConditionTermList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AlertConditionTermOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AlertConditionTermList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AlertConditionTermList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AlertConditionTerm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AlertConditionTerm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AlertConditionTerm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlertConditionTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.alertCondition.AlertConditionTermOutputReference",
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
            type_hints = typing.get_type_hints(AlertConditionTermOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFunctionInput")
    def time_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeFunction")
    def time_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFunction"))

    @time_function.setter
    def time_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermOutputReference, "time_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFunction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AlertConditionTerm, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AlertConditionTerm, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AlertConditionTerm, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertConditionTermOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AlertCondition",
    "AlertConditionConfig",
    "AlertConditionTerm",
    "AlertConditionTermList",
    "AlertConditionTermOutputReference",
]

publication.publish()
