#!/bin/bash
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -f|--force) force="$2"; shift ;; 
        -r|--repo) repo="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

echo "Initializing Helm..."
# helm init --client-only
echo "Packaging chart updates..."
for d in charts/* ; do
    echo "Packaging $d..."
    HELM_S3_MODE=3
    helm package -u -d dist/ $d
done

echo "Pushing chart updates to repo $repo..."
for d in dist/* ; do
    echo "Pushing $d..."
    HELM_S3_MODE=3
    if [[ $force = "true" ]]
    then
        helm s3 push --force $d $repo
    else
        helm s3 push $d $repo 
    fi
done

echo "Finished!"
