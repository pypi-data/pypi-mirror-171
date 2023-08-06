# Production UI Application Fact Sheet: {{appName}}

This document provides a summary of the **{{appName}}** ui application and its associated resources in the production environment.

## Basic Info

{% if accountAlias %}
**AWS Account:** [{{account}} ({{accountAlias}})](https://{{accountAlias}}.signin.{{awsLink}}/console)
{% else %}
**AWS Account:** [{{account}}](https://{{account}}.signin.{{awsLink}}/console)
{% endif %}

**GovCloud:** {{govCloud}}

**Region:** {{region}}

## Deployment Information

| Cluster Name | Env | Customer | UI Url |
| ------------ | --- | -------- | ------ |
{% for udi in uiDeploymentInformation %}
| {{udi.clusterName}} | {{udi.env}} | {{udi.customer}} | https://{{udi.uiUrl}} |
{% endfor %}

## S3 Buckets and CloudFront Distributions

| Cluster Name | Env | S3 Bucket | CloudFront Distribution |
| ------------ | --- | --------- | ----------------------- |
{% for uio in uiOther %}
| {{uio.clusterName}} | {{uio.env}} | [{{uio.s3Bucket}}](https://console.{{awsLink}}/s3/buckets/{{uio.s3Bucket}}?region={{region}}&tab=objects) | {% if govCloud %} N/A {% else %} [{{uio.cloudfrontDistribution}}](https://{{region}}.console.aws.amazon.com/cloudfront/v3/home?region={{region}}#/distributions/{{uio.cloudfrontDistribution}}) {% endif %} |
{% endfor %}

**S3 Builds Bucket:** [{{buildsBucket}}](https://console.{{awsLink}}/s3/buckets/{{buildsBucket}}?region={{region}}&tab=objects)

{% if govCloud %} 
## VPC Endpoint

| Cluster Name | VPC Endpoint |
| ------------ | ------------ |
{% for vpce in vpcEndpoint %}
| {{vpce.clusterName}} | {{vpce.vpcEndpoint}} |
{% endfor %}

{% endif %}
