@echo off

for %%t in (user, booking, showtime, movie) do (
    echo Handling %%t...
    if not exist ".\%%t\pb2" mkdir .\%%t\pb2
    python -m grpc_tools.protoc -I=./protos --python_out=./%%t/pb2/ --grpc_python_out=./%%t/pb2/ %%t.proto
    copy /y ".\%%t\pb2\%%t_pb2_grpc.py" ".\client"
    copy /y ".\%%t\pb2\%%t_pb2.py" ".\client"
)
echo done.

echo Handling dependecies...
for %%d in (base) do (
    for %%t in (user, booking, showtime, movie) do (
        echo Handling dependecy %%d in %%t...
        python -m grpc_tools.protoc -I=./protos --python_out=./%%t/pb2/ --grpc_python_out=./%%t/pb2/ %%d.proto
    )
    REM Copie des dépendances dans le client
    python -m grpc_tools.protoc -I=./protos --python_out=./client/ --grpc_python_out=./client/ %%d.proto
)

echo Handling custom dependecies...