# Flux Infra Repository

This repositroy contains the infrastructure applications that are deployed to all clusters. The repository should be accessed using a ***GitRepository*** Flux resource with a reference to a specific tag.

By accessing the repository with a tag reference we can control the versions of apps at a more granular level.

## Available Resources

The below table lists the available resources:

Name | Type | Version | Location
-----|------|---------|---------
amazon-cloudwatch-fluent-bit | HelmRelease | Chart Version: 0.15.8 | apps/amazon-cloudwatch-fluent-bit/release.yaml
chartmuseum | HelmRelease | Chart Version: 2.15.0 | apps/chartmuseum/release.yaml
prometheus | HelmRelease | Chart Version: 14.11.0 | apps/prometheus/release.yaml
vm-operator (Container: manager)| Deployment | Container Image: victoriametrics/operator:v0.22.1 | apps/victoria-metrics/operator/manager.yaml
grafana | HelmRelease | Chart Version: 6.9.1 | apps/grafana/release.yaml
metrics-server | HelmRelease | Chart Version: 3.7.0 | apps/metrics-server/release.yaml
prometheus-blackbox-exporter | HelmRelease | Chart Version: 4.10.2 | apps/prometheus-blackbox-exporter/release.yaml
cluster-autoscaler | HelmRelease | Chart Version: 9.4.0 | apps/cluster-autoscaler/release.yaml
cert-manager | HelmRelease | Chart Version: 1.1.0 | apps/cert-manager/release.yaml