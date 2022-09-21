python -m grpc_tools.protoc -I=./protos --python_out=. --grpc_python_out=. user.proto
copy /y ".\user_pb2_grpc.py" "..\client"
copy /y ".\user_pb2.py" "..\client"