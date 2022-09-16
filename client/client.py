import grpc

import movie_pb2
import movie_pb2_grpc


def get_movie_by_id(stub:movie_pb2_grpc.MovieStub, id):
    movie = stub.GetMovieByID(id)
    print(movie)


def get_list_movies(stub:movie_pb2_grpc.MovieStub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))

def get_movies_by_title(stub:movie_pb2_grpc.MovieStub,title):
    movies = stub.GetMoviesByTitle(title)
    for movie in movies :
        print(f"Found {movie}")

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
        channel.close()


if __name__ == '__main__':
    run()
