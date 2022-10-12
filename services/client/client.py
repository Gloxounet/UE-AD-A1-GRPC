from subprocess import call
import grpc

from protos import movie_pb2
from protos import movie_pb2_grpc

from protos import booking_pb2
from protos import booking_pb2_grpc

from protos import showtime_pb2
from protos import showtime_pb2_grpc

from protos import user_pb2
from protos import user_pb2_grpc

from protos import base_pb2

#MOVIES
# Future implementation for movie service
def movie_id_callback(call_future):
    print(call_future.result())

def get_movie_by_id(stub:movie_pb2_grpc.MovieStub, id):
    movie = stub.GetMovieByID.future(id)
    movie.add_done_callback(movie_id_callback)

def get_list_movies(stub:movie_pb2_grpc.MovieStub):
    allmovies = stub.GetListMovies(base_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))

def get_movies_by_title(stub:movie_pb2_grpc.MovieStub,title):
    movies = stub.GetMoviesByTitle(title)
    for movie in movies :
        print(f"Found {movie}")

def get_movies_by_director(stub:movie_pb2_grpc.MovieStub,director):
    movies = stub.GetMoviesByDirector(director)
    for movie in movies :
        print(f"Found {movie}")

# Movie service tester
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)

        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)

        print("-------------- GetListMovies --------------")
        get_list_movies(stub)
        
        print("-------------- GetMoviesByTitle --------------")
        title = movie_pb2.MovieTitle(title="creed")
        get_movies_by_title(stub,title)

        print("-------------- GetMoviesByDirector --------------")
        director = movie_pb2.MovieDirector(director="ridley")
        get_movies_by_director(stub,director)

        channel.close()



#BOOKINGS
def get_booking_by_userId(stub:booking_pb2_grpc.BookingStub,userId):
    booking = stub.GetBookingByUserId(userId)
    print(booking)

def get_list_bookings(stub:booking_pb2_grpc.BookingStub):
    bookings = stub.GetAllBookings(base_pb2.Empty())
    for booking in bookings:
        print("Booking from %s" % (booking.userId))

# Booking service tester
def run2():
    with grpc.insecure_channel('localhost:3002') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        
        print("-------------- GetBookingById --------------")
        userId = base_pb2.UserID(id="dwight_schrute")
        get_booking_by_userId(stub=stub,userId=userId)

                
        print("-------------- GetListBookings --------------")
        get_list_bookings(stub=stub)



        channel.close()


#SHOWTIME
def get_movies_by_date(stub, date):
    movies = stub.GetMoviesByDate(date)
    print(movies)

# Showtime service tester
def run3():
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)

        print("-------------- GetMoviesByDate --------------")
        date = showtime_pb2.Date(date="20151202")
        get_movies_by_date(stub=stub, date=date)


        channel.close()


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
def run4():
    with grpc.insecure_channel('localhost:3004') as channel:
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


if __name__ == '__main__':
    run()
    run2()
    run3()
    run4()
    pass
