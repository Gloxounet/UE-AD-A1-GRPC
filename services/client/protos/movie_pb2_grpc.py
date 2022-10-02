# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import base_pb2 as protos_dot_base__pb2
from protos import movie_pb2 as protos_dot_movie__pb2


class MovieStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMovieByID = channel.unary_unary(
                '/Movie/GetMovieByID',
                request_serializer=protos_dot_movie__pb2.MovieID.SerializeToString,
                response_deserializer=protos_dot_movie__pb2.MovieData.FromString,
                )
        self.GetListMovies = channel.unary_stream(
                '/Movie/GetListMovies',
                request_serializer=protos_dot_base__pb2.Empty.SerializeToString,
                response_deserializer=protos_dot_movie__pb2.MovieData.FromString,
                )
        self.GetMoviesByTitle = channel.unary_stream(
                '/Movie/GetMoviesByTitle',
                request_serializer=protos_dot_movie__pb2.MovieTitle.SerializeToString,
                response_deserializer=protos_dot_movie__pb2.MovieData.FromString,
                )
        self.GetMoviesByDirector = channel.unary_stream(
                '/Movie/GetMoviesByDirector',
                request_serializer=protos_dot_movie__pb2.MovieDirector.SerializeToString,
                response_deserializer=protos_dot_movie__pb2.MovieData.FromString,
                )


class MovieServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMovieByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetListMovies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMoviesByTitle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMoviesByDirector(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MovieServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMovieByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMovieByID,
                    request_deserializer=protos_dot_movie__pb2.MovieID.FromString,
                    response_serializer=protos_dot_movie__pb2.MovieData.SerializeToString,
            ),
            'GetListMovies': grpc.unary_stream_rpc_method_handler(
                    servicer.GetListMovies,
                    request_deserializer=protos_dot_base__pb2.Empty.FromString,
                    response_serializer=protos_dot_movie__pb2.MovieData.SerializeToString,
            ),
            'GetMoviesByTitle': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMoviesByTitle,
                    request_deserializer=protos_dot_movie__pb2.MovieTitle.FromString,
                    response_serializer=protos_dot_movie__pb2.MovieData.SerializeToString,
            ),
            'GetMoviesByDirector': grpc.unary_stream_rpc_method_handler(
                    servicer.GetMoviesByDirector,
                    request_deserializer=protos_dot_movie__pb2.MovieDirector.FromString,
                    response_serializer=protos_dot_movie__pb2.MovieData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Movie', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Movie(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMovieByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Movie/GetMovieByID',
            protos_dot_movie__pb2.MovieID.SerializeToString,
            protos_dot_movie__pb2.MovieData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetListMovies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Movie/GetListMovies',
            protos_dot_base__pb2.Empty.SerializeToString,
            protos_dot_movie__pb2.MovieData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMoviesByTitle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Movie/GetMoviesByTitle',
            protos_dot_movie__pb2.MovieTitle.SerializeToString,
            protos_dot_movie__pb2.MovieData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMoviesByDirector(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Movie/GetMoviesByDirector',
            protos_dot_movie__pb2.MovieDirector.SerializeToString,
            protos_dot_movie__pb2.MovieData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
