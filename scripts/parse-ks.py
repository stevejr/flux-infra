#!/usr/bin/env python

import glob
import sys
import yaml
import os
import hashlib

root_dir = sys.argv[1]
# root_dir = dir_path = os.path.dirname(os.path.realpath(__file__))
# print('root_dir = ' + root_dir)

readme = '''# Flux Infra Repository

This repositroy contains the infrastructure applications that are deployed to all clusters. The repository should be accessed using a ***GitRepository*** Flux resource with a reference to a specific tag.

By accessing the repository with a tag reference we can control the versions of apps at a more granular level.

## Available Resources

The below table lists the available resources:

'''

table = []
table.append(
    "Name | Type | Version | Location\n"
    "-----|------|---------|---------"
)

if __name__ == "__main__":
    # print("Start processing repo")
    # root_dir needs a trailing slash (i.e. /root/dir/)
    for filename in glob.iglob(root_dir + '**/**/*.yaml', recursive=True):
        with open(filename) as f:
            # use safe_load instead load
            for dataMap in yaml.safe_load_all(f):
                if "kind" in dataMap and dataMap["kind"] == "HelmRelease":
                    # print("Filename with a HelmRelease: %s " % filename)
                    # print("Chart Name: %s, Chart Version: %s \n" % (dataMap['spec']['chart']['spec']['sourceRef']['name'], dataMap['spec']['chart']['spec']['version']))
                    # print("File contents: \n %s \n" % dataMap)
                    table.append(
                        f"{dataMap['metadata']['name']} | HelmRelease | Chart Version: {dataMap['spec']['chart']['spec']['version']} | {os.path.relpath(filename)}"
                    )
                if "kind" in dataMap and dataMap["kind"] == "Deployment":
                    # print("Filename with a Deployment: %s " % filename)
                    # print("File contents: \n %s \n" % dataMap)
                    for container in dataMap['spec']['template']['spec']['containers']:
                        # print("Deployment Name: %s, Image Name: %s \n" %(dataMap['metadata']['name'], container['image']))
                        table.append(
                            f"{dataMap['metadata']['name']} (Container: {container['name']})| Deployment | Container Image: {container['image']} | {os.path.relpath(filename)}"
                        )
    # print("Finished processing repo")

    with open('README.md', 'w') as f:
        # print("Updating README.md")
        f.write(readme)
        f.write("\n".join(table))
