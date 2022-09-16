import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/booking.json'.format("."), "r") as jsf:
            self.db:list[str] = json.load(jsf)["booking"]

    def GetBookingByID(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.id:
                print("Booking found!")
                return booking_pb2.BookingData() #TODO
        return booking_pb2.MovieData() #TODO

    def GetListBooking(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingData() #TODO
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
