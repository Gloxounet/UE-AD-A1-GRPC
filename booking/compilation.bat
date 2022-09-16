python -m grpc_tools.protoc -I=./protos --python_out=. --grpc_python_out=. booking.proto
copy /y ".\booking_pb2_grpc.py" "..\client"
copy /y ".\booking_pb2.py" "..\client"