# Flux Infra Repository

This repositroy contains the infrastructure applications that are deployed to all clusters. The repository should be accessed using a ***GitRepository*** Flux resource with a reference to a specific tag. By accessing the repository with a tag reference we can controll the versions of apps at a more granular level.

## Available Resources

The below table lists the available resources:

Name | Type | Version | Location
-----|------|---------|---------
cert-manager | HelmRelease | Chart Version: 1.1.0 | /Users/steve/GitHub/stevejr/flux-infra/cert-manager/app/release.yaml
amazon-cloudwatch-fluent-bit | HelmRelease | Chart Version: 0.15.8 | /Users/steve/GitHub/stevejr/flux-infra/apps/amazon-cloudwatch-fluent-bit/release.yaml
vm-operator (Container: manager)| Deployment | Container Image: victoriametrics/operator:v0.22.1 | /Users/steve/GitHub/stevejr/flux-infra/apps/victoria-metrics/operator/manager.yaml
metrics-server | HelmRelease | Chart Version: 3.7.0 | /Users/steve/GitHub/stevejr/flux-infra/apps/metrics-server/release.yaml
cert-manager | HelmRelease | Chart Version: 1.7.1 | /Users/steve/GitHub/stevejr/flux-infra/apps/cert-manager/release.yaml
chartmuseum | HelmRelease | Chart Version: 2.15.0 | /Users/steve/GitHub/stevejr/flux-infra/apps/chartmuseum/release.yaml
grafana | HelmRelease | Chart Version: 6.9.1 | /Users/steve/GitHub/stevejr/flux-infra/apps/grafana/release.yaml
cluster-autoscaler | HelmRelease | Chart Version: 9.4.0 | /Users/steve/GitHub/stevejr/flux-infra/apps/cluster-autoscaler/release.yaml
prometheus-blackbox-exporter | HelmRelease | Chart Version: 4.10.2 | /Users/steve/GitHub/stevejr/flux-infra/apps/prometheus-blackbox-exporter/release.yaml
prometheus | HelmRelease | Chart Version: 14.11.0 | /Users/steve/GitHub/stevejr/flux-infra/apps/prometheus/release.yaml
