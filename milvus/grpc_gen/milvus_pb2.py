# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: milvus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='milvus.proto',
  package='milvus.grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cmilvus.proto\x12\x0bmilvus.grpc\x1a\x0cstatus.proto\"D\n\tTableName\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.milvus.grpc.Status\x12\x12\n\ntable_name\x18\x02 \x01(\t\"z\n\x0bTableSchema\x12*\n\ntable_name\x18\x01 \x01(\x0b\x32\x16.milvus.grpc.TableName\x12\x12\n\nindex_type\x18\x02 \x01(\x05\x12\x11\n\tdimension\x18\x03 \x01(\x03\x12\x18\n\x10store_raw_vector\x18\x04 \x01(\x08\"/\n\x05Range\x12\x13\n\x0bstart_value\x18\x01 \x01(\t\x12\x11\n\tend_value\x18\x02 \x01(\t\" \n\tRowRecord\x12\x13\n\x0bvector_data\x18\x01 \x03(\x02\"S\n\x0bInsertParam\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x30\n\x10row_record_array\x18\x02 \x03(\x0b\x32\x16.milvus.grpc.RowRecord\"I\n\tVectorIds\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.milvus.grpc.Status\x12\x17\n\x0fvector_id_array\x18\x02 \x03(\x03\"\x92\x01\n\x0bSearchParam\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12\x32\n\x12query_record_array\x18\x02 \x03(\x0b\x32\x16.milvus.grpc.RowRecord\x12-\n\x11query_range_array\x18\x03 \x03(\x0b\x32\x12.milvus.grpc.Range\x12\x0c\n\x04topk\x18\x04 \x01(\x03\"[\n\x12SearchInFilesParam\x12\x15\n\rfile_id_array\x18\x01 \x03(\t\x12.\n\x0csearch_param\x18\x02 \x01(\x0b\x32\x18.milvus.grpc.SearchParam\"+\n\x0bQueryResult\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\"m\n\x0fTopKQueryResult\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.milvus.grpc.Status\x12\x35\n\x13query_result_arrays\x18\x02 \x03(\x0b\x32\x18.milvus.grpc.QueryResult\"H\n\x0bStringReply\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.milvus.grpc.Status\x12\x14\n\x0cstring_reply\x18\x02 \x01(\t\"D\n\tBoolReply\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.milvus.grpc.Status\x12\x12\n\nbool_reply\x18\x02 \x01(\x08\"M\n\rTableRowCount\x12#\n\x06status\x18\x01 \x01(\x0b\x32\x13.milvus.grpc.Status\x12\x17\n\x0ftable_row_count\x18\x02 \x01(\x03\"\x16\n\x07\x43ommand\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\"C\n\x05Index\x12\x12\n\nindex_type\x18\x01 \x01(\x05\x12\r\n\x05nlist\x18\x02 \x01(\x03\x12\x17\n\x0findex_file_size\x18\x03 \x01(\x05\"[\n\nIndexParam\x12*\n\ntable_name\x18\x01 \x01(\x0b\x32\x16.milvus.grpc.TableName\x12!\n\x05index\x18\x02 \x01(\x0b\x32\x12.milvus.grpc.Index\"K\n\x12\x44\x65leteByRangeParam\x12!\n\x05range\x18\x01 \x01(\x0b\x32\x12.milvus.grpc.Range\x12\x12\n\ntable_name\x18\x02 \x01(\t2\xea\x07\n\rMilvusService\x12>\n\x0b\x43reateTable\x12\x18.milvus.grpc.TableSchema\x1a\x13.milvus.grpc.Status\"\x00\x12<\n\x08HasTable\x12\x16.milvus.grpc.TableName\x1a\x16.milvus.grpc.BoolReply\"\x00\x12:\n\tDropTable\x12\x16.milvus.grpc.TableName\x1a\x13.milvus.grpc.Status\"\x00\x12=\n\x0b\x43reateIndex\x12\x17.milvus.grpc.IndexParam\x1a\x13.milvus.grpc.Status\"\x00\x12<\n\x06Insert\x12\x18.milvus.grpc.InsertParam\x1a\x16.milvus.grpc.VectorIds\"\x00\x12\x44\n\x06Search\x12\x18.milvus.grpc.SearchParam\x1a\x1c.milvus.grpc.TopKQueryResult\"\x00\x30\x01\x12R\n\rSearchInFiles\x12\x1f.milvus.grpc.SearchInFilesParam\x1a\x1c.milvus.grpc.TopKQueryResult\"\x00\x30\x01\x12\x43\n\rDescribeTable\x12\x16.milvus.grpc.TableName\x1a\x18.milvus.grpc.TableSchema\"\x00\x12\x42\n\nCountTable\x12\x16.milvus.grpc.TableName\x1a\x1a.milvus.grpc.TableRowCount\"\x00\x12>\n\nShowTables\x12\x14.milvus.grpc.Command\x1a\x16.milvus.grpc.TableName\"\x00\x30\x01\x12\x37\n\x03\x43md\x12\x14.milvus.grpc.Command\x1a\x18.milvus.grpc.StringReply\"\x00\x12G\n\rDeleteByRange\x12\x1f.milvus.grpc.DeleteByRangeParam\x1a\x13.milvus.grpc.Status\"\x00\x12=\n\x0cPreloadTable\x12\x16.milvus.grpc.TableName\x1a\x13.milvus.grpc.Status\"\x00\x12\x42\n\rDescribeIndex\x12\x16.milvus.grpc.TableName\x1a\x17.milvus.grpc.IndexParam\"\x00\x12:\n\tDropIndex\x12\x16.milvus.grpc.TableName\x1a\x13.milvus.grpc.Status\"\x00\x62\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_TABLENAME = _descriptor.Descriptor(
  name='TableName',
  full_name='milvus.grpc.TableName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.grpc.TableName.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='milvus.grpc.TableName.table_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=111,
)


_TABLESCHEMA = _descriptor.Descriptor(
  name='TableSchema',
  full_name='milvus.grpc.TableSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='milvus.grpc.TableSchema.table_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_type', full_name='milvus.grpc.TableSchema.index_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimension', full_name='milvus.grpc.TableSchema.dimension', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_raw_vector', full_name='milvus.grpc.TableSchema.store_raw_vector', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=235,
)


_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='milvus.grpc.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_value', full_name='milvus.grpc.Range.start_value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_value', full_name='milvus.grpc.Range.end_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=284,
)


_ROWRECORD = _descriptor.Descriptor(
  name='RowRecord',
  full_name='milvus.grpc.RowRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_data', full_name='milvus.grpc.RowRecord.vector_data', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=318,
)


_INSERTPARAM = _descriptor.Descriptor(
  name='InsertParam',
  full_name='milvus.grpc.InsertParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='milvus.grpc.InsertParam.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_record_array', full_name='milvus.grpc.InsertParam.row_record_array', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=403,
)


_VECTORIDS = _descriptor.Descriptor(
  name='VectorIds',
  full_name='milvus.grpc.VectorIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.grpc.VectorIds.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector_id_array', full_name='milvus.grpc.VectorIds.vector_id_array', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=405,
  serialized_end=478,
)


_SEARCHPARAM = _descriptor.Descriptor(
  name='SearchParam',
  full_name='milvus.grpc.SearchParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='milvus.grpc.SearchParam.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_record_array', full_name='milvus.grpc.SearchParam.query_record_array', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_range_array', full_name='milvus.grpc.SearchParam.query_range_array', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topk', full_name='milvus.grpc.SearchParam.topk', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=627,
)


_SEARCHINFILESPARAM = _descriptor.Descriptor(
  name='SearchInFilesParam',
  full_name='milvus.grpc.SearchInFilesParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_id_array', full_name='milvus.grpc.SearchInFilesParam.file_id_array', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_param', full_name='milvus.grpc.SearchInFilesParam.search_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=629,
  serialized_end=720,
)


_QUERYRESULT = _descriptor.Descriptor(
  name='QueryResult',
  full_name='milvus.grpc.QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='milvus.grpc.QueryResult.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='milvus.grpc.QueryResult.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=765,
)


_TOPKQUERYRESULT = _descriptor.Descriptor(
  name='TopKQueryResult',
  full_name='milvus.grpc.TopKQueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.grpc.TopKQueryResult.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query_result_arrays', full_name='milvus.grpc.TopKQueryResult.query_result_arrays', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=767,
  serialized_end=876,
)


_STRINGREPLY = _descriptor.Descriptor(
  name='StringReply',
  full_name='milvus.grpc.StringReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.grpc.StringReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_reply', full_name='milvus.grpc.StringReply.string_reply', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=878,
  serialized_end=950,
)


_BOOLREPLY = _descriptor.Descriptor(
  name='BoolReply',
  full_name='milvus.grpc.BoolReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.grpc.BoolReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_reply', full_name='milvus.grpc.BoolReply.bool_reply', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=952,
  serialized_end=1020,
)


_TABLEROWCOUNT = _descriptor.Descriptor(
  name='TableRowCount',
  full_name='milvus.grpc.TableRowCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='milvus.grpc.TableRowCount.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_row_count', full_name='milvus.grpc.TableRowCount.table_row_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1022,
  serialized_end=1099,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='milvus.grpc.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='milvus.grpc.Command.cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1101,
  serialized_end=1123,
)


_INDEX = _descriptor.Descriptor(
  name='Index',
  full_name='milvus.grpc.Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index_type', full_name='milvus.grpc.Index.index_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nlist', full_name='milvus.grpc.Index.nlist', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_file_size', full_name='milvus.grpc.Index.index_file_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1125,
  serialized_end=1192,
)


_INDEXPARAM = _descriptor.Descriptor(
  name='IndexParam',
  full_name='milvus.grpc.IndexParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='milvus.grpc.IndexParam.table_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='milvus.grpc.IndexParam.index', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1194,
  serialized_end=1285,
)


_DELETEBYRANGEPARAM = _descriptor.Descriptor(
  name='DeleteByRangeParam',
  full_name='milvus.grpc.DeleteByRangeParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='milvus.grpc.DeleteByRangeParam.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='milvus.grpc.DeleteByRangeParam.table_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1287,
  serialized_end=1362,
)

_TABLENAME.fields_by_name['status'].message_type = status__pb2._STATUS
_TABLESCHEMA.fields_by_name['table_name'].message_type = _TABLENAME
_INSERTPARAM.fields_by_name['row_record_array'].message_type = _ROWRECORD
_VECTORIDS.fields_by_name['status'].message_type = status__pb2._STATUS
_SEARCHPARAM.fields_by_name['query_record_array'].message_type = _ROWRECORD
_SEARCHPARAM.fields_by_name['query_range_array'].message_type = _RANGE
_SEARCHINFILESPARAM.fields_by_name['search_param'].message_type = _SEARCHPARAM
_TOPKQUERYRESULT.fields_by_name['status'].message_type = status__pb2._STATUS
_TOPKQUERYRESULT.fields_by_name['query_result_arrays'].message_type = _QUERYRESULT
_STRINGREPLY.fields_by_name['status'].message_type = status__pb2._STATUS
_BOOLREPLY.fields_by_name['status'].message_type = status__pb2._STATUS
_TABLEROWCOUNT.fields_by_name['status'].message_type = status__pb2._STATUS
_INDEXPARAM.fields_by_name['table_name'].message_type = _TABLENAME
_INDEXPARAM.fields_by_name['index'].message_type = _INDEX
_DELETEBYRANGEPARAM.fields_by_name['range'].message_type = _RANGE
DESCRIPTOR.message_types_by_name['TableName'] = _TABLENAME
DESCRIPTOR.message_types_by_name['TableSchema'] = _TABLESCHEMA
DESCRIPTOR.message_types_by_name['Range'] = _RANGE
DESCRIPTOR.message_types_by_name['RowRecord'] = _ROWRECORD
DESCRIPTOR.message_types_by_name['InsertParam'] = _INSERTPARAM
DESCRIPTOR.message_types_by_name['VectorIds'] = _VECTORIDS
DESCRIPTOR.message_types_by_name['SearchParam'] = _SEARCHPARAM
DESCRIPTOR.message_types_by_name['SearchInFilesParam'] = _SEARCHINFILESPARAM
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT
DESCRIPTOR.message_types_by_name['TopKQueryResult'] = _TOPKQUERYRESULT
DESCRIPTOR.message_types_by_name['StringReply'] = _STRINGREPLY
DESCRIPTOR.message_types_by_name['BoolReply'] = _BOOLREPLY
DESCRIPTOR.message_types_by_name['TableRowCount'] = _TABLEROWCOUNT
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Index'] = _INDEX
DESCRIPTOR.message_types_by_name['IndexParam'] = _INDEXPARAM
DESCRIPTOR.message_types_by_name['DeleteByRangeParam'] = _DELETEBYRANGEPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TableName = _reflection.GeneratedProtocolMessageType('TableName', (_message.Message,), {
  'DESCRIPTOR' : _TABLENAME,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.TableName)
  })
_sym_db.RegisterMessage(TableName)

TableSchema = _reflection.GeneratedProtocolMessageType('TableSchema', (_message.Message,), {
  'DESCRIPTOR' : _TABLESCHEMA,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.TableSchema)
  })
_sym_db.RegisterMessage(TableSchema)

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {
  'DESCRIPTOR' : _RANGE,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.Range)
  })
_sym_db.RegisterMessage(Range)

RowRecord = _reflection.GeneratedProtocolMessageType('RowRecord', (_message.Message,), {
  'DESCRIPTOR' : _ROWRECORD,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.RowRecord)
  })
_sym_db.RegisterMessage(RowRecord)

InsertParam = _reflection.GeneratedProtocolMessageType('InsertParam', (_message.Message,), {
  'DESCRIPTOR' : _INSERTPARAM,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.InsertParam)
  })
_sym_db.RegisterMessage(InsertParam)

VectorIds = _reflection.GeneratedProtocolMessageType('VectorIds', (_message.Message,), {
  'DESCRIPTOR' : _VECTORIDS,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.VectorIds)
  })
_sym_db.RegisterMessage(VectorIds)

SearchParam = _reflection.GeneratedProtocolMessageType('SearchParam', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPARAM,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.SearchParam)
  })
_sym_db.RegisterMessage(SearchParam)

SearchInFilesParam = _reflection.GeneratedProtocolMessageType('SearchInFilesParam', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHINFILESPARAM,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.SearchInFilesParam)
  })
_sym_db.RegisterMessage(SearchInFilesParam)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULT,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.QueryResult)
  })
_sym_db.RegisterMessage(QueryResult)

TopKQueryResult = _reflection.GeneratedProtocolMessageType('TopKQueryResult', (_message.Message,), {
  'DESCRIPTOR' : _TOPKQUERYRESULT,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.TopKQueryResult)
  })
_sym_db.RegisterMessage(TopKQueryResult)

StringReply = _reflection.GeneratedProtocolMessageType('StringReply', (_message.Message,), {
  'DESCRIPTOR' : _STRINGREPLY,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.StringReply)
  })
_sym_db.RegisterMessage(StringReply)

BoolReply = _reflection.GeneratedProtocolMessageType('BoolReply', (_message.Message,), {
  'DESCRIPTOR' : _BOOLREPLY,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.BoolReply)
  })
_sym_db.RegisterMessage(BoolReply)

TableRowCount = _reflection.GeneratedProtocolMessageType('TableRowCount', (_message.Message,), {
  'DESCRIPTOR' : _TABLEROWCOUNT,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.TableRowCount)
  })
_sym_db.RegisterMessage(TableRowCount)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.Command)
  })
_sym_db.RegisterMessage(Command)

Index = _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), {
  'DESCRIPTOR' : _INDEX,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.Index)
  })
_sym_db.RegisterMessage(Index)

IndexParam = _reflection.GeneratedProtocolMessageType('IndexParam', (_message.Message,), {
  'DESCRIPTOR' : _INDEXPARAM,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.IndexParam)
  })
_sym_db.RegisterMessage(IndexParam)

DeleteByRangeParam = _reflection.GeneratedProtocolMessageType('DeleteByRangeParam', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBYRANGEPARAM,
  '__module__' : 'milvus_pb2'
  # @@protoc_insertion_point(class_scope:milvus.grpc.DeleteByRangeParam)
  })
_sym_db.RegisterMessage(DeleteByRangeParam)



_MILVUSSERVICE = _descriptor.ServiceDescriptor(
  name='MilvusService',
  full_name='milvus.grpc.MilvusService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1365,
  serialized_end=2367,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTable',
    full_name='milvus.grpc.MilvusService.CreateTable',
    index=0,
    containing_service=None,
    input_type=_TABLESCHEMA,
    output_type=status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HasTable',
    full_name='milvus.grpc.MilvusService.HasTable',
    index=1,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=_BOOLREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropTable',
    full_name='milvus.grpc.MilvusService.DropTable',
    index=2,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateIndex',
    full_name='milvus.grpc.MilvusService.CreateIndex',
    index=3,
    containing_service=None,
    input_type=_INDEXPARAM,
    output_type=status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='milvus.grpc.MilvusService.Insert',
    index=4,
    containing_service=None,
    input_type=_INSERTPARAM,
    output_type=_VECTORIDS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='milvus.grpc.MilvusService.Search',
    index=5,
    containing_service=None,
    input_type=_SEARCHPARAM,
    output_type=_TOPKQUERYRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SearchInFiles',
    full_name='milvus.grpc.MilvusService.SearchInFiles',
    index=6,
    containing_service=None,
    input_type=_SEARCHINFILESPARAM,
    output_type=_TOPKQUERYRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeTable',
    full_name='milvus.grpc.MilvusService.DescribeTable',
    index=7,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=_TABLESCHEMA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CountTable',
    full_name='milvus.grpc.MilvusService.CountTable',
    index=8,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=_TABLEROWCOUNT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ShowTables',
    full_name='milvus.grpc.MilvusService.ShowTables',
    index=9,
    containing_service=None,
    input_type=_COMMAND,
    output_type=_TABLENAME,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Cmd',
    full_name='milvus.grpc.MilvusService.Cmd',
    index=10,
    containing_service=None,
    input_type=_COMMAND,
    output_type=_STRINGREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteByRange',
    full_name='milvus.grpc.MilvusService.DeleteByRange',
    index=11,
    containing_service=None,
    input_type=_DELETEBYRANGEPARAM,
    output_type=status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PreloadTable',
    full_name='milvus.grpc.MilvusService.PreloadTable',
    index=12,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=status__pb2._STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeIndex',
    full_name='milvus.grpc.MilvusService.DescribeIndex',
    index=13,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=_INDEXPARAM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropIndex',
    full_name='milvus.grpc.MilvusService.DropIndex',
    index=14,
    containing_service=None,
    input_type=_TABLENAME,
    output_type=status__pb2._STATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MILVUSSERVICE)

DESCRIPTOR.services_by_name['MilvusService'] = _MILVUSSERVICE

# @@protoc_insertion_point(module_scope)
