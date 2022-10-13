import os
from dotenv import load_dotenv
from pathlib import Path

import grpc

from protos import base_pb2, movie_pb2_grpc, movie_pb2

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

MOVIE_PORT = os.getenv('MOVIE_PORT')


def movie_id_callback(call_future):
    print(call_future.result())


def get_movie_by_id(stub: movie_pb2_grpc.MovieStub, id):
    movie = stub.GetMovieByID.future(id)
    movie.add_done_callback(movie_id_callback)


def get_list_movies(stub: movie_pb2_grpc.MovieStub):
    allmovies = stub.GetListMovies(base_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))


def get_movies_by_title(stub: movie_pb2_grpc.MovieStub, title):
    movies = stub.GetMoviesByTitle(title)
    for movie in movies:
        print(f"Found {movie}")


def get_movies_by_director(stub: movie_pb2_grpc.MovieStub, director):
    movies = stub.GetMoviesByDirector(director)
    for movie in movies:
        print(f"Found {movie}")


# Movie service tester
def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel(f'127.0.0.1:{MOVIE_PORT}') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)

        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)

        print("-------------- GetListMovies --------------")
        get_list_movies(stub)

        print("-------------- GetMoviesByTitle --------------")
        title = movie_pb2.MovieTitle(title="creed")
        get_movies_by_title(stub, title)

        print("-------------- GetMoviesByDirector --------------")
        director = movie_pb2.MovieDirector(director="ridley")
        get_movies_by_director(stub, director)

        channel.close()
