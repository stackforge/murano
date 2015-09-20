#    Copyright (c) 2014 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import semantic_version

EXPRESSION_MEMORY_QUOTA = 512 * 1024
ITERATORS_LIMIT = 2000

CTX_ACTIONS_ONLY = '?actionsOnly'
CTX_ALLOW_PROPERTY_WRITES = '$?allowPropertyWrites'
CTX_ARGUMENT_OWNER = '$?argumentOwner'
CTX_ATTRIBUTE_STORE = '$?attributeStore'
CTX_CALLER_CONTEXT = '$?callerContext'
CTX_CURRENT_INSTRUCTION = '$?currentInstruction'
CTX_CURRENT_EXCEPTION = '$?currentException'
CTX_CURRENT_METHOD = '$?currentMethod'
CTX_ENVIRONMENT = '$?environment'
CTX_EXECUTOR = '$?executor'
CTX_PACKAGE_LOADER = '$?packageLoader'
CTX_SKIP_FRAME = '$?skipFrame'
CTX_THIS = '$?this'
CTX_TYPE = '$?type'
CTX_VARIABLE_SCOPE = '$?variableScope'
CTX_YAQL_ENGINE = '$?yaqlEngine'

DM_OBJECTS = 'Objects'
DM_OBJECTS_COPY = 'ObjectsCopy'
DM_ATTRIBUTES = 'Attributes'

META_NO_TRACE = '?noTrace'

CORE_LIBRARY = 'io.murano'
CORE_LIBRARY_OBJECT = 'io.murano.Object'

RUNTIME_VERSION_1_0 = semantic_version.Version('1.0.0')
RUNTIME_VERSION_2_0 = semantic_version.Version('2.0.0')
