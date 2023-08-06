# Production Service Application Fact Sheet: {{appName}}

This document provides a summary of the **{{appName}}** service application and its associated resources in the production environment.

## Basic Info

{% if accountAlias %}
**AWS Account:** [{{account}} ({{accountAlias}})](https://{{accountAlias}}.signin.{{awsLink}}/console)
{% else %}
**AWS Account:** [{{account}}](https://{{account}}.signin.{{awsLink}}/console)
{% endif %}

**GovCloud:** {{govCloud}}

**Region:** {{region}}

## Deployment Information

| Cluster Name | Env | Customer | Service Url | App Secret | Spring Active Profile |
| ------------ | --- | -------- | ----------- | ---------- | --------------------- |
{% for sdi in serviceDeploymentInformation %}
| {{sdi.clusterName}} | {{sdi.env}} | {{sdi.customer}} | https://{{sdi.serviceUrl}} | [{{sdi.appSecret}}](https://{{region}}.console.{{awsLink}}/secretsmanager/secret?name={{sdi.appSecret}}&region={{region}}) | {{sdi.springActiveProfile}} |
{% endfor %}

## RDS Instance Information

| Cluster Name | Env | RDS Instance Identifier | RDS Instance Endpoint | RDS Instance Login |
| ------------ | --- | ----------------------- | --------------------- | ------------------ |
{% for rii in rdsInstanceInformation %}
| {{rii.clusterName}} | {{rii.env}} | [{{rii.rdsInstanceIdentifier}}](https://{{region}}.console.{{awsLink}}/rds/home?region={{region}}#database:id={{rii.rdsInstanceIdentifier}};is-cluster=false) | {{rii.rdsInstanceEndpoint}} | [{{rii.rdsInstanceLoginCredential}}](https://{{region}}.console.{{awsLink}}/secretsmanager/secret?name={{rii.rdsInstanceLoginCredential}}&region={{region}}) |
{% endfor %}

## Database Information

| Cluster Name | Env | Customer | Database Name | Database Schema | Database Users |
| ------------ | --- | -------- | ------------- | --------------- | -------------- |
{% for dbi in databaseInformation %}
| {{dbi.clusterName}} | {{dbi.env}} | {{dbi.customer}} | {{dbi.databaseName}} | {{dbi.databaseSchema}} | {% for user in dbi.databaseUsers %}[{{user}}](https://{{region}}.console.{{awsLink}}/secretsmanager/secret?name={{user}}&region={{region}}), {% endfor %} |
{% endfor %}

## Other Information

**ECR Repository:** https://{{region}}.console.{{awsLink}}/ecr/repositories/private/{{account}}/{{ecr}}?region={{region}}