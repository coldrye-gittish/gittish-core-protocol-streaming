# gittish-core-protocol-streaming



## Build System Requirements

Please refer to 
https://github.com/coldrye-gittish/gittish-build-protocol/blob/master/README.md#build-system-requirements
for more information.


## Setting up the Workspace

Please refer to 
https://github.com/coldrye-gittish/gittish-build-protocol/blob/master/README.md#setting-up-the-workspace
for more information.


## Project Dependencies

* gittish-build-common

* gittish-build-protocol

* gittish-build-python


## External Package Dependencies

n/a


## Project Layout

* Makefile

  This is the make file you will be using for building the sources and
  distribution package. There should be no need for editing this. Keeping this
  free of any customization will allow you to simply copy over the Makefile
  from the standard template in case that there are any changes to the build
  process.

* PROTOCOL.md

  This file is initially not present and can be regenerated using

```
make protocol-doc
```

  It may then be checked in in order to provide a human readable API
  documentation for the protocol.

* src/gittish/protocol

  The protobuf sources go into here. There are a few conventions that need to
  be followed.

  1. Each GRPC service definitions goes into a separate source file, prefixed
     by `service_`.

  2. No messages or enumeration must be defined in the GRPC service source
     files.

* Makefile.proto.in

  In here, you will define the PROTO_SRC and the GRPC_SRC. All service
  definitions will be added to GRPC_SRC while the remaining protobuf sources
  will be added to PROTO_SRC. If you require external protobuf definitions,
  these must be added to PROTO_INC_DIR.

* Makefile.subdirs.in

  Each runtime specific sub project must be appended to the SUBDIRS variable.

* <runtime>

  Runtime specific sub project folders, e.g. `python`. Provided that you use
  the templates from the gittish-build-\* projects, sub projects will be 
  integrated into the build process automatically as soon as they get added to
  the SUBDIRS variable.

* VERSION

  This specifies the protocol version. Each change to the protocol requires a
  new feature release, meaning that one cannot increase the patch version number
  but instead must directly increase the minor release version number by one.

  When making changes to the protocol and bumping its version, the dependent
  versions of the sub projects must also be adjusted.

  This is due to the fact that available sub projects will reuse the major and
  minor release version number from the protocol version.

  You can use the script gittish-build-common/scripts/semver to bump the major/
  minor release version or bump the available tag.


## Configuring the Build Process

In order to configure the overall build process, you must run the `configure`
script.

```
cd <WORKSPACE_ROOT>/gittish-core-protocol-streaming
./configure
```

This will create the `CONFIG.in` file that is required by all the other projects.
