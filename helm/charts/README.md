# Helm Charts

This directory contains helm charts for base infrastructure apps that we have had to modify.

## Chart gloo-os-with-ui

This is a clone of chart `gloo-os-with-ui` from the [Gloo OS UI Helm Repository](https://storage.googleapis.com/gloo-os-ui-helm) based on chart version 1.6.21.

The chart has been modified as follows:

- ./gloo-os-with-ui/charts/gloo/templates/6.5-gateway-certgen-job.yaml: This template now includes `nodeSelector` and `tolerations` statements based on the user
supplying them in `gloo.gateway.certGenJob.nodeSelector` and `gloo.gateway.certGenJob.tolerations`. This is because Helm 3.x does not currently support a post-render on
receiving chart hook manifests - see [this issue](https://github.com/helm/helm/issues/7891)

### Change History

|Date|Version|Reason|
|----|-------|------|
|19/04/2021|v1.6.26|Fix Envoy CVEs|

## Chart metabase

This is a clone of chart `metabase` from the [Metabase Unofficial Community Repo](https://pmint93.github.io/helm-charts) based on chart version 0.13.3.

The chart has been modified as follows:

- ./values.yaml: New values added to create a persistent volume. When set this allows for the h2 in-memory db to be written to disk and saved so it can survive a pod restart
- ./templates/deployment.yaml: Updated to set the environment variable `MB_DB_FILE` if persistence is enabled. Add in the new volume mount and volume `data` if persistence is enabled.
- ./templates/pvc.yaml: New template to create a PVC if persistence is enabled.

### Change History

|Date|Version|Reason|
|----|-------|------|
|10/05/2021|v0.0.1|Initial release|

## Change Process

To update the chart the following should be done:

- Navigate to ./helm/charts
- Update your helm repos and then pull the version needed, for example for version 1.6.26:

    ```bash
    helm repo update
    helm pull gloo-os-with-ui/gloo-os-with-ui --version 1.6.26
    ```

- Untar the downloaded chart over the existing one
- Review the changes between versions. Make sure to revert the following changes:
  - Remove the .gitIgnore file in ./helm/charts/gloo-os-with-ui
  - Add back in the changes to  ./helm/charts/gloo-os-with-ui/charts/gloo/templates/6.5-gateway-certgen-job.yaml for the nodeSelector and tolerations fields
- Commit and push the changes back to the repo and Flux should then reconile and deploy the version of Gloo downloaded  

## Chart istio-operator

This is a copy of the istio-operator chart that is included in the official [istio 1.10.3 release](https://istio.io/latest/docs/setup/getting-started/#download)

The chart has not been modified in anyway.

### Change History

|Date|Version|Reason|
|----|-------|------|
|19/08/2021|v0.0.1|Initial release|

### Change Process

To update the chart the following should be done:

- Download the version of Istio required - [Downloads](https://istio.io/latest/docs/setup/getting-started/#download)
- Copy the contents from `./manifests/charts/istio-operator` from the download Istio release to `./helm/charts/istio-operator`
- Review the changes between versions and update as needed
- Commit and push the changes back to the repo and Flux should then reconile and deploy the version of Istio-Operator downloaded. This will cause both the Operator and Istio components to have an
[In-place Upgrade](https://istio.io/latest/docs/setup/upgrade/helm/). It may be preferrable to perform a [Canary Upgrade](https://istio.io/latest/docs/setup/install/operator/#canary-upgrade) which will
allow both the existing and new Istio control plane to co-exist and be tested together.
