"""
Copyright (C) 2021 Kaskada Inc. All rights reserved.

This package cannot be used, copied or distributed without the express
written permission of Kaskada Inc.

For licensing inquiries, please contact us at info@kaskada.com.
"""

from kaskada.client import Client
from typing import List
import kaskada
import kaskada.api.v1alpha.compute_pb2 as pb
import kaskada.api.v1alpha.query_pb2 as queryPb
import kaskada.formatters
from kaskada.slice_filters import SliceFilter
from typing import Union
import datetime

import grpc
from kaskada.utils import get_timestamp


def query(
    query: str,
    with_views: List[pb.WithView] = [],
    result_behavior: str = "all-results",
    response_as: str = "parquet",
    data_token_id: str = None,
    dry_run: bool = False,
    changed_since_time: Union[str, datetime.datetime, None] = None,
    final_result_time: Union[str, datetime.datetime, None] = None,
    limits: pb.QueryRequest.Limits = None,
    slice_filter: SliceFilter = None,
    experimental: bool = False,
    client: Client = None,
) -> pb.StreamQueryResponse:
    """
    Performs a query

    Args:
        query (str): The query to perform
        with_views (List[pb.WithView], optional):
            A list of views to use in the query, in addition to the views stored in the system.
        result_behavior (str, optional):
            Determines which results are returned. Either "all-results" (default), or "final-results" which returns
            only the final values for each entity.
        responsed_as (str, optional):
            Determines how the response is returned.  Either "parquet" (default) or "redis-bulk".
            Note: if "redis-bulk", result_behavior is assumed to be "final-results".
        data_token_id (str, optional):
            Enables repeatable queries. Queries performed against the same dataToken are always ran the same input data.
        dry_run(bool, optional):
            When `True`, the query is validated and if there are no errors, the resultant schema is returned.
            No actual computation of results is performed.
        changed_since_time (datetime.datetime, optional):
            Configure the inclusive datetime after which results will be output.
        final_result_time (datetime.datetime, optional):
            Configure the upper bound of final result behavior queries.
        limits (pb.QueryRequest.Limits, optional):
            Configure limits on the output set.
        slice_filter (SliceFilter, optional):
            Enables slice filter. Currently, only slice entity percent filters are supported. Defaults to None.
        experimental(bool, optional):
            When `True`, then experimental features are allowed. Data returned when using this flag is not
            guaranteed to be correct.
        client (Client, optional):
            The Kaskada Client. Defaults to kaskada.KASKADA_DEFAULT_CLIENT.

    Returns:
        compute_pb.QueryResponse: Response from the API
    """

    if client is None:
        client = kaskada.KASKADA_DEFAULT_CLIENT

    if slice_filter is None:
        slice_filter = kaskada.KASKADA_DEFAULT_SLICE

    change_since_time = get_timestamp(changed_since_time)
    final_result_time = get_timestamp(final_result_time)

    try:
        kaskada.validate_client(client)

        request_args = {
            "data_token_id": data_token_id,
            "dry_run": dry_run,
            "experimental_features": experimental,
            "changed_since_time": change_since_time,
            "final_result_time": final_result_time,
            "limits": limits,
            "query": query,
            "with_views": with_views,
        }

        if result_behavior == "final-results":
            request_args["result_behavior"] = "RESULT_BEHAVIOR_FINAL_RESULTS"
            if final_result_time is not None:
                request_args[
                    "result_behavior"
                ] = "RESULT_BEHAVIOR_FINAL_RESULTS_AT_TIME"
        else:
            request_args["result_behavior"] = "RESULT_BEHAVIOR_ALL_RESULTS"
        if response_as == "redis-bulk":
            request_args["redis_bulk"] = {}
        else:
            request_args["parquet"] = {}

        if slice_filter is not None:
            request_args["slice_request"] = slice_filter.to_request()

        in_ipython = kaskada.formatters.in_ipython()
        if in_ipython:
            from IPython.display import display, clear_output

            request_args["stream_metrics"] = True

        request = pb.StreamQueryRequest(**request_args)
        response = pb.StreamQueryResponse()

        responses = client.computeStub.StreamQuery(
            request, metadata=client.get_metadata()
        )
        for resp in responses:
            response.MergeFrom(resp)
            if in_ipython:
                clear_output(wait=True)
                display(response)

        if in_ipython:
            clear_output(wait=True)
        return response
    except grpc.RpcError as e:
        kaskada.handleGrpcError(e)
    except Exception as e:
        kaskada.handleException(e)


def queryV2(
    query: str,
    with_views: List[pb.WithView] = [],
    result_behavior: str = "all-results",
    response_as: str = "parquet",
    data_token_id: str = None,
    dry_run: bool = False,
    changed_since_time: Union[str, datetime.datetime, None] = None,
    final_result_time: Union[str, datetime.datetime, None] = None,
    limits: queryPb.Query.Limits = None,
    slice_filter: SliceFilter = None,
    experimental: bool = False,
    client: Client = None,
) -> pb.StreamQueryResponse:
    """
    Performs a query

    Args:
        query (str): The query to perform
        with_views (List[pb.WithView], optional):
            A list of views to use in the query, in addition to the views stored in the system.
        result_behavior (str, optional):
            Determines which results are returned. Either "all-results" (default), or "final-results" which returns
            only the final values for each entity.
        responsed_as (str, optional):
            Determines how the response is returned.  Either "parquet" (default) or "redis-bulk".
            Note: if "redis-bulk", result_behavior is assumed to be "final-results".
        data_token_id (str, optional):
            Enables repeatable queries. Queries performed against the same dataToken are always ran the same input data.
        dry_run(bool, optional):
            When `True`, the query is validated and if there are no errors, the resultant schema is returned.
            No actual computation of results is performed.
        changed_since_time (datetime.datetime, optional):
            Configure the inclusive datetime after which results will be output.
        limits (pb.QueryRequest.Limits, optional):
            Configure limits on the output set.
        slice_filter (SliceFilter, optional):
            Enables slice filter. Currently, only slice entity percent filters are supported. Defaults to None.
        experimental(bool, optional):
            When `True`, then experimental features are allowed. Data returned when using this flag is not
            guaranteed to be correct.
        client (Client, optional):
            The Kaskada Client. Defaults to kaskada.KASKADA_DEFAULT_CLIENT.

    Returns:
        compute_pb.QueryResponse: Response from the API
    """

    if client is None:
        client = kaskada.KASKADA_DEFAULT_CLIENT

    if slice_filter is None:
        slice_filter = kaskada.KASKADA_DEFAULT_SLICE

    change_since_time = get_timestamp(changed_since_time)
    final_result_time = get_timestamp(final_result_time)

    try:
        kaskada.validate_client(client)

        query_options = {
            "dry_run": dry_run,
            "experimental_features": experimental,
            "stream_metrics": False,
        }

        query_request = {
            "expression": query,
            "data_token_id": data_token_id,
            "changed_since_time": change_since_time,
            "final_result_time": final_result_time,
            "limits": limits,
        }

        if result_behavior == "final-results":
            query_request["result_behavior"] = "RESULT_BEHAVIOR_FINAL_RESULTS"
            if final_result_time is not None:
                query_request[
                    "result_behavior"
                ] = "RESULT_BEHAVIOR_FINAL_RESULTS_AT_TIME"
        else:
            query_request["result_behavior"] = "RESULT_BEHAVIOR_ALL_RESULTS"
        if response_as == "redis-bulk":
            query_request["redis_bulk"] = {}
        else:
            query_request["parquet"] = {}

        if slice_filter is not None:
            query_request["slice"] = slice_filter.to_request()

        in_ipython = kaskada.formatters.in_ipython()
        if in_ipython:
            query_options["stream_metrics"] = True

        request_args = {"query_request": query_request, "query_options": query_options}
        request = pb.StreamQueryV2Request(**request_args)
        return executeQuery(request, client)
    except grpc.RpcError as e:
        kaskada.handleGrpcError(e)
    except Exception as e:
        kaskada.handleException(e)


def executeQuery(request: pb.StreamQueryV2Request, client: Client):
    response = pb.StreamQueryV2Response()
    in_ipython = kaskada.formatters.in_ipython()
    if in_ipython:
        from IPython.display import display, clear_output
    responses = client.computeStub.StreamQueryV2(
        request, metadata=client.get_metadata()
    )
    for resp in responses:
        response.MergeFrom(resp)
        if in_ipython:
            clear_output(wait=True)
            display(response)

    if in_ipython:
        clear_output(wait=True)
    return response
