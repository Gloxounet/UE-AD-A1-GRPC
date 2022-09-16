python -m grpc_tools.protoc -I=./protos --python_out=. --grpc_python_out=. movie.proto
copy /y ".\movie_pb2_grpc.py" "..\client"
copy /y ".\movie_pb2.py" "..\client"