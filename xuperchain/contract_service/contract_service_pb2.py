# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contract_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import xuperchain.contract.contract_pb2 as contract__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contract_service.proto',
  package='xchain.contract.svc',
  syntax='proto3',
  serialized_options=b'\n\032com.baidu.xuper.contractpbH\003Z:github.com/xuperchain/xuperchain/core/contractsdk/go/pbrpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x63ontract_service.proto\x12\x13xchain.contract.svc\x1a\x0e\x63ontract.proto2\xb2\x01\n\nNativeCode\x12W\n\x04\x43\x61ll\x12&.xchain.contract.sdk.NativeCallRequest\x1a\'.xchain.contract.sdk.NativeCallResponse\x12K\n\x04Ping\x12 .xchain.contract.sdk.PingRequest\x1a!.xchain.contract.sdk.PingResponse2\xf4\n\n\x07Syscall\x12N\n\tPutObject\x12\x1f.xchain.contract.sdk.PutRequest\x1a .xchain.contract.sdk.PutResponse\x12N\n\tGetObject\x12\x1f.xchain.contract.sdk.GetRequest\x1a .xchain.contract.sdk.GetResponse\x12W\n\x0c\x44\x65leteObject\x12\".xchain.contract.sdk.DeleteRequest\x1a#.xchain.contract.sdk.DeleteResponse\x12Z\n\x0bNewIterator\x12$.xchain.contract.sdk.IteratorRequest\x1a%.xchain.contract.sdk.IteratorResponse\x12T\n\x07QueryTx\x12#.xchain.contract.sdk.QueryTxRequest\x1a$.xchain.contract.sdk.QueryTxResponse\x12]\n\nQueryBlock\x12&.xchain.contract.sdk.QueryBlockRequest\x1a\'.xchain.contract.sdk.QueryBlockResponse\x12W\n\x08Transfer\x12$.xchain.contract.sdk.TransferRequest\x1a%.xchain.contract.sdk.TransferResponse\x12\x63\n\x0c\x43ontractCall\x12(.xchain.contract.sdk.ContractCallRequest\x1a).xchain.contract.sdk.ContractCallResponse\x12u\n\x12\x43rossContractQuery\x12..xchain.contract.sdk.CrossContractQueryRequest\x1a/.xchain.contract.sdk.CrossContractQueryResponse\x12x\n\x13GetAccountAddresses\x12/.xchain.contract.sdk.GetAccountAddressesRequest\x1a\x30.xchain.contract.sdk.GetAccountAddressesResponse\x12K\n\x04Ping\x12 .xchain.contract.sdk.PingRequest\x1a!.xchain.contract.sdk.PingResponse\x12T\n\x07PostLog\x12#.xchain.contract.sdk.PostLogRequest\x1a$.xchain.contract.sdk.PostLogResponse\x12U\n\x0bGetCallArgs\x12\'.xchain.contract.sdk.GetCallArgsRequest\x1a\x1d.xchain.contract.sdk.CallArgs\x12Z\n\tSetOutput\x12%.xchain.contract.sdk.SetOutputRequest\x1a&.xchain.contract.sdk.SetOutputResponse\x12Z\n\tEmitEvent\x12%.xchain.contract.sdk.EmitEventRequest\x1a&.xchain.contract.sdk.EmitEventResponseBZ\n\x1a\x63om.baidu.xuper.contractpbH\x03Z:github.com/xuperchain/xuperchain/core/contractsdk/go/pbrpcb\x06proto3'
  ,
  dependencies=[contract__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_NATIVECODE = _descriptor.ServiceDescriptor(
  name='NativeCode',
  full_name='xchain.contract.svc.NativeCode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=64,
  serialized_end=242,
  methods=[
  _descriptor.MethodDescriptor(
    name='Call',
    full_name='xchain.contract.svc.NativeCode.Call',
    index=0,
    containing_service=None,
    input_type=contract__pb2._NATIVECALLREQUEST,
    output_type=contract__pb2._NATIVECALLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='xchain.contract.svc.NativeCode.Ping',
    index=1,
    containing_service=None,
    input_type=contract__pb2._PINGREQUEST,
    output_type=contract__pb2._PINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NATIVECODE)

DESCRIPTOR.services_by_name['NativeCode'] = _NATIVECODE


_SYSCALL = _descriptor.ServiceDescriptor(
  name='Syscall',
  full_name='xchain.contract.svc.Syscall',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=245,
  serialized_end=1641,
  methods=[
  _descriptor.MethodDescriptor(
    name='PutObject',
    full_name='xchain.contract.svc.Syscall.PutObject',
    index=0,
    containing_service=None,
    input_type=contract__pb2._PUTREQUEST,
    output_type=contract__pb2._PUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetObject',
    full_name='xchain.contract.svc.Syscall.GetObject',
    index=1,
    containing_service=None,
    input_type=contract__pb2._GETREQUEST,
    output_type=contract__pb2._GETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteObject',
    full_name='xchain.contract.svc.Syscall.DeleteObject',
    index=2,
    containing_service=None,
    input_type=contract__pb2._DELETEREQUEST,
    output_type=contract__pb2._DELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NewIterator',
    full_name='xchain.contract.svc.Syscall.NewIterator',
    index=3,
    containing_service=None,
    input_type=contract__pb2._ITERATORREQUEST,
    output_type=contract__pb2._ITERATORRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryTx',
    full_name='xchain.contract.svc.Syscall.QueryTx',
    index=4,
    containing_service=None,
    input_type=contract__pb2._QUERYTXREQUEST,
    output_type=contract__pb2._QUERYTXRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryBlock',
    full_name='xchain.contract.svc.Syscall.QueryBlock',
    index=5,
    containing_service=None,
    input_type=contract__pb2._QUERYBLOCKREQUEST,
    output_type=contract__pb2._QUERYBLOCKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Transfer',
    full_name='xchain.contract.svc.Syscall.Transfer',
    index=6,
    containing_service=None,
    input_type=contract__pb2._TRANSFERREQUEST,
    output_type=contract__pb2._TRANSFERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ContractCall',
    full_name='xchain.contract.svc.Syscall.ContractCall',
    index=7,
    containing_service=None,
    input_type=contract__pb2._CONTRACTCALLREQUEST,
    output_type=contract__pb2._CONTRACTCALLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CrossContractQuery',
    full_name='xchain.contract.svc.Syscall.CrossContractQuery',
    index=8,
    containing_service=None,
    input_type=contract__pb2._CROSSCONTRACTQUERYREQUEST,
    output_type=contract__pb2._CROSSCONTRACTQUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAccountAddresses',
    full_name='xchain.contract.svc.Syscall.GetAccountAddresses',
    index=9,
    containing_service=None,
    input_type=contract__pb2._GETACCOUNTADDRESSESREQUEST,
    output_type=contract__pb2._GETACCOUNTADDRESSESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='xchain.contract.svc.Syscall.Ping',
    index=10,
    containing_service=None,
    input_type=contract__pb2._PINGREQUEST,
    output_type=contract__pb2._PINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostLog',
    full_name='xchain.contract.svc.Syscall.PostLog',
    index=11,
    containing_service=None,
    input_type=contract__pb2._POSTLOGREQUEST,
    output_type=contract__pb2._POSTLOGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCallArgs',
    full_name='xchain.contract.svc.Syscall.GetCallArgs',
    index=12,
    containing_service=None,
    input_type=contract__pb2._GETCALLARGSREQUEST,
    output_type=contract__pb2._CALLARGS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetOutput',
    full_name='xchain.contract.svc.Syscall.SetOutput',
    index=13,
    containing_service=None,
    input_type=contract__pb2._SETOUTPUTREQUEST,
    output_type=contract__pb2._SETOUTPUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EmitEvent',
    full_name='xchain.contract.svc.Syscall.EmitEvent',
    index=14,
    containing_service=None,
    input_type=contract__pb2._EMITEVENTREQUEST,
    output_type=contract__pb2._EMITEVENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYSCALL)

DESCRIPTOR.services_by_name['Syscall'] = _SYSCALL

# @@protoc_insertion_point(module_scope)
