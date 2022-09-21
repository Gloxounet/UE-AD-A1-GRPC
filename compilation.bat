@echo off

for %%t in (user, booking, showtime, movie) do (
    echo Handling %%t...
    if not exist ".\%%t\pb2" mkdir .\%%t\pb2
    python -m grpc_tools.protoc -I=./protos --python_out=./%%t/pb2/ --grpc_python_out=./%%t/pb2/ %%t.proto
    copy /y ".\%%t\pb2\%%t_pb2_grpc.py" ".\client"
    copy /y ".\%%t\pb2\%%t_pb2.py" ".\client"
)
echo done.