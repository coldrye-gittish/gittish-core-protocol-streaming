# Copyright 2017 Carsten Klein
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from template gittish-build-python/templates/protocol

# do not edit 
LEVEL := ../../
BUILD_CONFIG_COMMON := $(abspath $(LEVEL)gittish-build-common/CONFIG.in)
BUILD_CONFIG_PROTOCOL := $(abspath $(LEVEL)gittish-build-protocol/CONFIG.in)
BUILD_CONFIG_PYTHON := $(abspath $(LEVEL)gittish-build-python/CONFIG.in)
BUILD_CONFIG_PROJECT := $(abspath ../CONFIG.in)

-include $(BUILD_CONFIG_COMMON)
ifndef GTS_BUILD_COMMON
$(error Run $(BUILD_CONFIG_COMMON:%/CONFIG.in=%)/configure first)
endif

-include $(BUILD_CONFIG_PROTOCOL)
ifndef GTS_BUILD_PROTOCOL
$(error Run $(BUILD_CONFIG_PROTOCOL:%/CONFIG.in=%)/configure first)
endif

-include $(BUILD_CONFIG_PYTHON)
ifndef GTS_BUILD_PYTHON
$(error Run $(BUILD_CONFIG_PYTHON:%/CONFIG.in=%)/configure first)
endif

-include $(BUILD_CONFIG_PROJECT)
ifndef GTS_BUILD_PROJECT
$(error Run $(BUILD_CONFIG_PROJECT:%/CONFIG.in=%)/configure first)
endif

ifndef __GTS_BUILD_PYTHON_PROTOCOL__
include $(GTS_BUILD_PYTHON)/Makefile.protocol.in
endif

# vim: noexpandtab:ts=2:sw=2:
