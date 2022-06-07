#!/bin/sh
find . -name "*.proto" | while read line
do
  python3 -m grpc_tools.protoc -I. --python_out=. --proto_path=. --grpc_python_out=. $line
done
