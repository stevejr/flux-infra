# Using Helm with private S3 Bucket

To use helm with a S3 bucket you must first install the [helm-s3 plugin](https://github.com/hypnoglow/helm-s3). This will allow the
`s3://` protocol to be supported.

## Initialising a New S3 Repository

To initialise a new repository that will be hosted in S3:

```bash
HELM_S3_MODE=3
helm s3 init s3://bucket-name/charts
```

This command generates an empty index.yaml and uploads it to the S3 bucket under `/charts` key.

To work with this repo by it's name, first you need to add it using native helm command:

```bash
HELM_S3_MODE=3
helm repo add mynewrepo s3://bucket-name/charts
```

## Pushing Charts to S3

To push a chart to a S3 bucket:

```bash
HELM_S3_MODE=3
helm s3 push <packaged chart> mynewrepo
```

In some cases you may want to replace an existing chart version. To do so, add --force flag to a push command:

```bash
HELM_S3_MODE=3
helm s3 push --force <packaged chart> mynewrepo
```

## Reindex Charts in S3

If your repository somehow became inconsistent or broken, you can use reindex to recreate the index in accordance with the charts in the repository.

```bash
HELM_S3_MODE=3
helm s3 reindex mynewrepo
```
