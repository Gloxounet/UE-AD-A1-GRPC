import os
import json
from dotenv import load_dotenv
import requests
from pathlib import Path
import grpc

from protos import user_pb2
from protos import user_pb2_grpc

from protos import base_pb2

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

USER_PORT = os.getenv('USER_PORT')

#USER
def get_user_by_id(stub:user_pb2_grpc.UserStub,userId:base_pb2.UserID):
    user = stub.GetUserById(userId)
    print(user)
    return user

def get_list_users(stub):
    users = stub.GetAllUsers(base_pb2.Empty())
    for user in users :
        print(user)
    return users

def get_user_bookings(stub:user_pb2_grpc.UserStub,userId:base_pb2.UserID):
    booking = stub.GetUserBookings(userId)
    print(booking)
    return booking

#User service tester
def main():
    with grpc.insecure_channel(f'127.0.0.1:{USER_PORT}') as channel:
        stub = user_pb2_grpc.UserStub(channel)

        print("-------------- GetUserById --------------")
        userId = base_pb2.UserID(id="jim_halpert")
        get_user_by_id(stub,userId)

        print("-------------- GetAllUsers --------------")
        get_list_users(stub)

        print("-------------- GetUserBookings --------------")
        userId = base_pb2.UserID(id="dwight_schrute")
        get_user_bookings(stub,userId)

        channel.close()