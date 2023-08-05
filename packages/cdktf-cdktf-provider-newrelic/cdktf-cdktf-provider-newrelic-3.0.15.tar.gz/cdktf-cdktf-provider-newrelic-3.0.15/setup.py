import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-newrelic",
    "version": "3.0.15",
    "description": "Prebuilt newrelic Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-newrelic.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-newrelic.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_newrelic",
        "cdktf_cdktf_provider_newrelic._jsii",
        "cdktf_cdktf_provider_newrelic.alert_channel",
        "cdktf_cdktf_provider_newrelic.alert_condition",
        "cdktf_cdktf_provider_newrelic.alert_muting_rule",
        "cdktf_cdktf_provider_newrelic.alert_policy",
        "cdktf_cdktf_provider_newrelic.alert_policy_channel",
        "cdktf_cdktf_provider_newrelic.api_access_key",
        "cdktf_cdktf_provider_newrelic.application_settings",
        "cdktf_cdktf_provider_newrelic.cloud_aws_govcloud_integrations",
        "cdktf_cdktf_provider_newrelic.cloud_aws_govcloud_link_account",
        "cdktf_cdktf_provider_newrelic.cloud_aws_integrations",
        "cdktf_cdktf_provider_newrelic.cloud_aws_link_account",
        "cdktf_cdktf_provider_newrelic.cloud_azure_integrations",
        "cdktf_cdktf_provider_newrelic.cloud_azure_link_account",
        "cdktf_cdktf_provider_newrelic.cloud_gcp_integrations",
        "cdktf_cdktf_provider_newrelic.cloud_gcp_link_account",
        "cdktf_cdktf_provider_newrelic.dashboard",
        "cdktf_cdktf_provider_newrelic.data_newrelic_account",
        "cdktf_cdktf_provider_newrelic.data_newrelic_alert_channel",
        "cdktf_cdktf_provider_newrelic.data_newrelic_alert_policy",
        "cdktf_cdktf_provider_newrelic.data_newrelic_application",
        "cdktf_cdktf_provider_newrelic.data_newrelic_cloud_account",
        "cdktf_cdktf_provider_newrelic.data_newrelic_entity",
        "cdktf_cdktf_provider_newrelic.data_newrelic_key_transaction",
        "cdktf_cdktf_provider_newrelic.data_newrelic_plugin",
        "cdktf_cdktf_provider_newrelic.data_newrelic_plugin_component",
        "cdktf_cdktf_provider_newrelic.data_newrelic_synthetics_monitor",
        "cdktf_cdktf_provider_newrelic.data_newrelic_synthetics_monitor_location",
        "cdktf_cdktf_provider_newrelic.data_newrelic_synthetics_secure_credential",
        "cdktf_cdktf_provider_newrelic.entity_tags",
        "cdktf_cdktf_provider_newrelic.events_to_metrics_rule",
        "cdktf_cdktf_provider_newrelic.infra_alert_condition",
        "cdktf_cdktf_provider_newrelic.insights_event",
        "cdktf_cdktf_provider_newrelic.notification_channel",
        "cdktf_cdktf_provider_newrelic.notification_destination",
        "cdktf_cdktf_provider_newrelic.nrql_alert_condition",
        "cdktf_cdktf_provider_newrelic.nrql_drop_rule",
        "cdktf_cdktf_provider_newrelic.one_dashboard",
        "cdktf_cdktf_provider_newrelic.one_dashboard_raw",
        "cdktf_cdktf_provider_newrelic.plugins_alert_condition",
        "cdktf_cdktf_provider_newrelic.provider",
        "cdktf_cdktf_provider_newrelic.service_level",
        "cdktf_cdktf_provider_newrelic.synthetics_alert_condition",
        "cdktf_cdktf_provider_newrelic.synthetics_monitor",
        "cdktf_cdktf_provider_newrelic.synthetics_monitor_script",
        "cdktf_cdktf_provider_newrelic.synthetics_multilocation_alert_condition",
        "cdktf_cdktf_provider_newrelic.synthetics_secure_credential",
        "cdktf_cdktf_provider_newrelic.workload"
    ],
    "package_data": {
        "cdktf_cdktf_provider_newrelic._jsii": [
            "provider-newrelic@3.0.15.jsii.tgz"
        ],
        "cdktf_cdktf_provider_newrelic": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdktf>=0.13.0, <0.14.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.69.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
