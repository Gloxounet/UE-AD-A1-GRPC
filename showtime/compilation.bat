set proto=showtime
python -m grpc_tools.protoc -I=./protos --python_out=. --grpc_python_out=. %proto%.proto
copy /y ".\%proto%_pb2_grpc.py" "..\client"
copy /y ".\%proto%_pb2.py" "..\client"