# Flux Infra Repository

This repositroy contains the infrastructure applications that are deployed to all clusters. The repository should be accessed using a ***GitRepository*** Flux resource with a reference to a specific tag. By accessing the repository with a tag reference we can controll the versions of apps at a more granular level.

## Available Resources

The below table lists the available resources at the current tag level **v1.0.1**

| Name | Version | Location |
|------|---------|----------|
| Cert Manager | v1.1.0 | ./cert-manager/app |
| Cert Manager CRDs | v1.1.0 | ./cert-manager/crds |
| JetStack HelmRepository | latest | ./sources |
