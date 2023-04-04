﻿# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.

from .utils import AutoNumber


class CdmLogCode(AutoNumber):
    # Errors
    NONE = ()
    ERR_ADAPTER_NOT_FOUND = ()
    ERR_CYCLE_IN_OBJECT_DEFINITION = ()
    ERR_DOC_ALREADY_EXIST = ()
    ERR_DOC_ADAPTER_NOT_FOUND = ()
    ERR_DOC_ENTITY_DOC_SAVING_FAILURE = ()
    ERR_DOC_ENTITY_REPLACEMENT_FAILURE = ()
    ERR_DOC_IMPORT_SAVING_FAILURE = ()
    ERR_DOC_IS_NOT_FOLDER = ()
    ERR_DOC_PARTITION_SCHEMA_SAVING_FAILURE = ()
    ERR_DOC_SUB_MANIFEST_SAVING_FAILURE = ()
    ERR_DOC_SYMBOL_NOT_FOUND = ()
    ERR_DOC_WRT_DOC_NOT_FOUND = ()
    ERR_ENTITY_CREATION_FAILED = ()
    ERR_ENUM_CONVERSION_FAILURE = ()
    ERR_FETCHING_FILE_METADATA_NULL = ()
    ERR_INDEX_FAILED = ()
    ERR_INVALID_CAST = ()
    ERR_INVALID_PATH = ()
    ERR_MANIFEST_FILE_MOD_TIME_FAILURE = ()
    ERR_MISSING_INCREMENTAL_PARTITION_TRAIT = ()
    ERR_OBJECT_WITHOUT_OWNER_FOUND = ()
    ERR_PARTITION_FILE_MOD_TIME_FAILURE = ()
    ERR_PATH_IS_DUPLICATE = ()
    ERR_PATH_NULL_OBJECT_PATH = ()
    ERR_PERSIST_ADAPTER_NOT_FOUND_FOR_NAMESPACE = ()
    ERR_PERSIST_ADAPTER_WRITE_FAILURE = ()
    ERR_PERSIST_CARDINALITY_PROP_MISSING = ()
    ERR_PERSIST_CDM_ENTITY_FETCH_ERROR = ()
    ERR_PERSIST_CLASS_MISSING = ()
    ERR_PERSIST_CSV_PROCESSING_ERROR = ()
    ERR_PERSIST_DESERIALIZE_ERROR = ()
    ERR_PERSIST_DOC_CONVERSION_FAILURE = ()
    ERR_PERSIST_MODELJSON_DOC_CONVERSION_ERROR = ()
    ERR_PERSIST_DOC_NAME_LOAD_FAILURE = ()
    ERR_PERSIST_ENTITY_PATH_NOT_FOUND = ()
    ERR_PERSIST_ENTITY_ATTR_UNSUPPORTED = ()
    ERR_PERSIST_ENTITY_DECLARATION_MISSING = ()
    ERR_PERSIST_INCREMENTAL_CONVERSION_ERROR = ()
    ERR_PERSIST_MODEL_JSON_REF_ENTITY_INVALID_LOCATION = ()
    ERR_PERSIST_MODELJSON_ENTITY_PARSING_ERROR = ()
    ERR_PERSIST_FAILURE = ()
    ERR_PERSIST_FILE_PERSIST_ERROR = ()
    ERR_PERSIST_FILE_PERSIST_FAILED = ()
    ERR_PERSIST_FILE_READ_FAILURE = ()
    ERR_PERSIST_SAVE_LINK_DOCS = ()
    ERR_PERSIST_FILE_WRITE_FAILURE = ()
    ERR_PERSIST_MODELJSON_INVALID_ENTITY_PATH = ()
    ERR_PERSIST_MODELJSON_INVALID_EXTENSION_TRAIT = ()
    ERR_PERSIST_JSON_ATTR_CONTEXT_CONVERSION_ERROR = ()
    ERR_PERSIST_JSON_DATATYPE_CONVERSION_ERROR = ()
    ERR_PERSIST_JSON_DATATYPE_REF_CONVERSION_ERROR = ()
    ERR_PERSIST_JSON_IMPORT_CONVERSION_ERROR = ()
    ERR_PERSIST_JSON_OBJECT_REF_CONVERSION_ERROR = ()
    ERR_PERSIST_MODELJSON_ENTITY_ATTR_ERROR = ()
    ERR_PERSIST_MODELJSON_MODEL_ID_DUPLICATION = ()
    ERR_PERSIST_MODELJSON_MODEL_ID_NOT_FOUND = ()
    ERR_PERSIST_MODELJSON_TO_ATTR_CONVERSION_FAILURE = ()
    ERR_PERSIST_MODELJSON_FROM_ATTR_CONVERSION_FAILURE = ()
    ERR_PERSIST_MODELJSON_ENTITY_CONVERSION_ERROR = ()
    ERR_PERSIST_MODELJSON_ENTITY_DECLARATION_CONVERSION_ERROR = ()
    ERR_PERSIST_MODELJSON_ENTITY_DECLARATION_CONVERSION_FAILURE = ()
    ERR_PERSIST_MODELJSON_ENTITY_REF_CONVERSION_ERROR = ()
    ERR_PERSIST_NON_INCREMENTAL_CONVERSION_ERROR = ()
    ERR_PERSIST_NULL_DOC_NAME = ()
    ERR_PERSIST_OBJECT_NOT_FOUND = ()
    ERR_PERSIST_PROJ_INVALID_OPS_TYPE = ()
    ERR_PERSIST_PROJ_INVALID_TYPE = ()
    ERR_PERSIST_PROJ_UNSUPPORTED_PROP = ()
    ERR_PERSIST_SYMS_ADLS_ADAPTER_MISSING = ()
    ERR_PERSIST_SYMS_ADLS_ADAPTER_NOT_MOUNTED = ()
    ERR_PERSIST_SYMS_ATTR_CONVERSION_Failure = ()
    ERR_PERSIST_SYMS_ATTR_CONVERSION_Error = ()
    ERR_PERSIST_SYMS_ENTITY_FETCH_ERROR = ()
    ERR_PERSIST_SYMS_ENTITY_PATH_NULL = ()
    ERR_PERSIST_SYMS_ENTITY_DECL_CONVERSION_FAILURE = ()
    ERR_PERSIST_SYMS_ENTITY_DECL_CONVERSION_EXCEPTION = ()
    ERR_PERSIST_SYMS_MULTIPLE_OR_ZERO_TABLE_DEFINITION = ()
    ERR_PERSIST_SYMS_INVALID_DB_PROP_OBJECT = ()
    ERR_PERSIST_SYMS_INVALID_DB_OBJECT = ()
    ERR_PERSIST_SYMS_INCOMPATIBLE_FILE_TO_TYPE = ()
    ERR_PERSIST_SYMS_RELATIONSHIP_TYPE_NOT_SUPPORTED = ()
    ERR_PERSIST_SYMS_STORAGE_SOURCE_TRAIT_ERROR = ()
    ERR_PERSIST_SYMS_TABLE_FORMAT_TYPE_NOT_SUPPORTED = ()
    ERR_PERSIST_SYMS_TABLE_INVALID_DATA_LOCATION = ()
    ERR_PERSIST_SYMS_TABLE_MISSING_DATA_LOCATION = ()
    ERR_PERSIST_SYMS_UNKNOWN_DATA_FORMAT = ()
    ERR_PERSIST_SYMS_UNSUPPORTED_CDM_CONVERSION = ()
    ERR_PERSIST_SYMS_UNSUPPORTED_MANIFEST = ()
    ERR_PERSIST_UNSUPPORTED_JSON_SEM_VER = ()
    ERR_PERSIST_SYMS_UNSUPPORTED_TABLE_FORMAT = ()
    ERR_PERSIST_INVALID_MAX_CARDINALITY = ()
    ERR_PERSIST_INVALID_MIN_CARDINALITY = ()
    ERR_PROJ_FAILED_TO_RESOLVE = ()
    ERR_PROJ_INVALID_ATTR_STATE = ()
    ERR_PROJ_REF_ATTR_STATE_FAILURE = ()
    ERR_PROJ_RENAME_FORMAT_IS_NOT_SET = ()
    ERR_PROJ_SOURCE_ERROR = ()
    ERR_PROJ_STRING_ERROR = ()
    ERR_PROJ_UNSUPPORTED_ATTR_GROUPS = ()
    ERR_PROJ_UNSUPPORTED_SOURCE = ()
    ERR_REL_MAX_RESOLVED_ATTR_REACHED = ()
    ERR_RESOLUTION_FAILURE = ()
    ERR_RESOLVE_ENTITY_FAILURE = ()
    ERR_RESOLVE_NEW_ENTITY_NAME_NOT_SET = ()
    ERR_RESOLVE_FOLDER_NOT_FOUND = ()
    ERR_RESOLVE_MANIFEST_EXISTS = ()
    ERR_RESOLVE_MANIFEST_FAILED = ()
    ERR_RESOLVE_REFERENCE_FAILURE = ()
    ERR_STORAGE_ADAPTER_NOT_FOUND = ()
    ERR_STORAGE_CDM_STANDARDS_MISSING = ()
    ERR_STORAGE_FOLDER_NOT_FOUND = ()
    ERR_STORAGE_INVALID_ADAPTER_PATH = ()
    ERR_STORAGE_INVALID_PATH_FORMAT = ()
    ERR_STORAGE_MISSING_JSON_CONFIG = ()
    ERR_STORAGE_MISSING_NAMESPACE = ()
    ERR_STORAGE_MISSING_TYPE_JSON_CONFIG = ()
    ERR_STORAGE_NAMESPACE_MISMATCH = ()
    ERR_STORAGE_NAMESPACE_NOT_REGISTERED = ()
    ERR_STORAGE_NULL_ADAPTER = ()
    ERR_STORAGE_NULL_ADAPTER_CONFIG = ()
    ERR_STORAGE_NULL_CORPUS_PATH = ()
    ERR_STORAGE_NULL_NAMESPACE = ()
    ERR_STORAGE_OBJECT_NODE_CAST_FAILED = ()
    ERR_SYMBOL_NOT_FOUND = ()
    ERR_TRAIT_ARGUMENT_MISSING = ()
    ERR_TRAIT_ATTR_FETCH_ERROR = ()
    ERR_TRAIT_INVALID_ARGUMENT_VALUE_TYPE = ()
    ERR_TRAIT_RESOLUTION_FAILURE = ()
    ERR_UNEXPECTED_DATA_TYPE = ()
    ERR_UNEXPECTED_INCREMENTAL_PARTITION_TRAIT = ()
    ERR_UNEXPECTED_TYPE = ()
    ERR_UNRECOGNIZED_DATA_TYPE = ()
    ERR_UNSUPPORTED_REF = ()
    ERR_UNSUPPORTED_TYPE = ()
    ERR_VALDN_INTEGRITY_CHECK_FAILURE = ()
    ERR_VALDN_INVALID_CORPUS_PATH = ()
    ERR_VALDN_INVALID_DOC = ()
    ERR_VALDN_INVALID_MAX_CARDINALITY = ()
    ERR_VALDN_INVALID_MIN_CARDINALITY = ()
    ERR_VALDN_INVALID_EXPRESSION = ()
    ERR_VALDN_MISSING_DOC = ()
    ERR_VALDN_MISSING_LANGUAGE_TAG = ()
    ERR_REL_UNDEFINED = ()
    WARN_PARTITION_GLOB_AND_REGEX_PRESENT = ()
    WARN_DEPRECATED_RESOLUTION_GUIDANCE = ()
    WARN_DOC_CHANGES_DISCARDED = ()
    WARN_DOC_IMPORT_NOT_LOADED = ()
    WARN_PARTITION_FILE_FETCH_FAILED = ()
    WARN_LINK_ENT_IDENT_ARGS_NOT_SUPPORTED = ()
    WARN_PARTITION_INVALID_ARGUMENTS = ()
    WARN_PERSIST_CUSTOM_EXT_NOT_SUPPORTED = ()
    WARN_PERSIST_PARTITION_LOC_MISSING = ()
    WARN_PERSIST_FILE_MOD_COMPUTE_FAILED = ()
    WARN_PERSIST_FILE_READ_FAILURE = ()
    WARN_PERSIST_JSON_SEM_VER_INVALID_FORMAT = ()
    WARN_PERSIST_JSON_SEM_VER_MANDATORY = ()
    WARN_PERSIST_MODELJSON_REL_READ_FAILED = ()
    WARN_PERSIST_REL_UNDEFINED_SOURCE_ENTITY = ()
    WARN_PERSIST_REL_UNDEFINED_TARGET_ENTITY = ()
    WARN_PERSIST_SYMS_ENTITY_MISSING = ()
    WARN_PERSIST_SYMS_ENTITY_SKIPPED = ()
    WARN_PERSIST_SYMS_PROJ_NOT_EXIST = ()
    WARN_PERSIST_UNSUPPORTED_JSON_SEM_VER = ()
    WARN_PERSIST_ENTITY_MISSING = ()
    WARN_PERSIST_ENUM_NOT_FOUND = ()
    WARN_PERSIST_PARTITION_NAME_NULL = ()
    WARN_PROJ_CREATE_FOREIGN_KEY_TRAITS = ()
    WARN_PROJ_FK_WITHOUT_SOURCE_ENTITY = ()
    WARN_PROJ_ADD_ARTIFACT_ATTR_NOT_SUPPORTED = ()
    WARN_PROJ_RENAME_ATTR_NOT_SUPPORTED = ()
    WARN_RESOLVE_ATTR_FAILED = ()
    WARN_RESOLVE_ENTITY_FAILED = ()
    WARN_RESOLVE_IMPORT_FAILED = ()
    WARN_RESOLVE_OBJECT_FAILED = ()
    WARN_RESOLVE_REFERENCE_FAILURE = ()
    WARN_STORAGE_EXPECTED_PATH_PREFIX = ()
    WARN_STORAGE_REMOVE_ADAPTER_FAILED = ()
    WARN_ANNOTATION_TYPE_NOT_SUPPORTED = ()
    WARN_VALDN_ENTITY_NOT_DEFINED = ()
    WARN_VALDN_MAX_ORDINAL = ()
    WARN_VALDN_PRIMARY_KEY_MISSING = ()
    WARN_VALDN_ORDINAL_START_END_ORDER = ()
    WARN_TELEMETRY_INGESTION_FAILED = ()
    WARN_UN_MOUNT_CDM_NAMESPACE = ()
