@echo off

for %%t in (user, booking, showtime, movie) do (
    echo Handling %%t...
    python -m grpc_tools.protoc -I=./protos --python_out=./%%t/ --grpc_python_out=./%%t/ %%t.proto
    copy /y ".\%%t\%%t_pb2_grpc.py" ".\client"
    copy /y ".\%%t\%%t_pb2.py" ".\client"
)
echo done.