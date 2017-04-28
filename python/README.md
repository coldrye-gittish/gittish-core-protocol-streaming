# gittish-core-protocol-streaming



## Build System Requirements

Please refer to 
https://github.com/coldrye-gittish/gittish-build-python/blob/master/README.md#build-system-requirements
for more information.


## Setting up the Workspace

Please refer to 
https://github.com/coldrye-gittish/gittish-build-python/blob/master/README.md#setting-up-the-workspace
for more information.


## Project Dependencies

See the project dependencies of the containing project.


## External Package Dependencies

TBD:additional-external-package-dependencies

Please refer to 
* https://github.com/coldrye-gittish/gittish-build-common/blob/master/README.md#external-package-dependencies
* https://github.com/coldrye-gittish/gittish-build-protocol/blob/master/README.md#external-package-dependencies
* https://github.com/coldrye-gittish/gittish-build-python/blob/master/README.md#external-package-dependencies
for more information.


## Project Layout

* Makefile

  This is the make file you will be using for building the sources and
  distribution package. There should be no need for editing this. Keeping this
  free of any customization will allow you to simply copy over the Makefile
  from the python protocol template in case that there are any changes to the
  build process.

* gittish/protocol

  All custom extensions to the protocol go into here. In addition, the protobuf
  sources will be generated into this package as well.

* Makefile.package.in

  Source files required for the build process and for the packaging process
  need to be added to the PACKAGE_SRC variable.

* dev_requirements.txt

  Add to here the requirements used during development.

* requirements.txt

  Add to here the runtime requirements. The information herein will be included
  with the distribution package on build.

* CHANGELOG.md

  Please record here all the changes made to the protocol and the package as
  well.

* MANIFEST.in

  Add additional source files to be included with the python source package.
  Normally, you will not have to make any changes to this.

* META.in

  Fill in required meta information. The information herein will be included
  with the distribution package on build.

* setup.py

  Normally, you will not have to make any customizations to this file and you
  should refrain from doing so unless your package requires it.

* VERSION

  This specifies the package version. The version is directly derived from the
  protocol version (major/minor release number).

  When making changes to the package, only the patch version number must be
  increased.

  You can use the script gittish-build-common/scripts/semver to bump the major/
  minor release version or patch version or bump the available tag.


## Configuring the Build Process

In order to configure the overall build process, you must run the `configure`
script from the containing project.

```
cd <WORKSPACE_ROOT>/gittish-core-protocol-streaming
./configure
```

This will create the `CONFIG.in` file that is required by this sub project.
