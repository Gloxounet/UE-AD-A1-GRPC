import grpc
from concurrent import futures

from protos import user_pb2
from protos import user_pb2_grpc
from protos import base_pb2

# To make calls on booking
from protos import booking_pb2_grpc

import json

# Create a UserItem (see user.proto) from data structure used in data/users.json
def createUserItem(user):
   return user_pb2.UserItem(
      id=str(user["id"]),
      name=str(user["name"]),
      lastactive=str(user["last_active"])
   )

# Function to open grpc connection
def openConnection(serviceUrl) :
   return grpc.insecure_channel(serviceUrl)

# "Client" booking getter for Servicer on call GetUserBookings
def get_booking_by_userId(stub:booking_pb2_grpc.BookingStub,userId:base_pb2.UserID):
    booking = stub.GetBookingByUserId(userId)
    return booking

class UserServicer(user_pb2_grpc.UserServicer):

   def __init__(self):
      with open('{}/data/users.json'.format("."), "r") as jsf:
         self.db:list[str] = json.load(jsf)["users"]

   def GetUserById(self, request, context):
      for user in self.db:
         if user['id'] == request.id:
               print("User found!")
               return createUserItem(user)

   def GetAllUsers(self, request, context):
      print("Get all user called")
      for user in self.db:
         yield createUserItem(user)
      
   def GetUserBookings(self, request, context):
      with openConnection('localhost:3002') as channel :
         stub = booking_pb2_grpc.BookingStub(channel)
         userId = base_pb2.UserID(id=request.id)
         booking = get_booking_by_userId(stub,userId)
         return booking

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:3004')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
