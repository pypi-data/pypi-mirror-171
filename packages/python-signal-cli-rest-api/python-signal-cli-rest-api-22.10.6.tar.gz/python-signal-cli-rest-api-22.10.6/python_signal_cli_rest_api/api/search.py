"""
search handler
"""

from traceback import format_exc
from typing import List

from pydantic import BaseModel
from sanic import Blueprint
from sanic.exceptions import BadRequest
from sanic.log import logger
from sanic.response import json
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import ResponseBadRequest
from python_signal_cli_rest_api.lib.helper import is_registered
from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

search_v1 = Blueprint("search_v1", url_prefix="/search")


class SearchV1GetParams(BaseModel):
    """
    SearchV1GetParams
    """

    numbers: List[str]


class SearchV1GetResponse(BaseModel):
    """
    SearchV1GetResponse
    """

    number: str
    registered: bool


@search_v1.get("/", version=1)
@openapi.tag("Search")
@openapi.parameter(
    "numbers",
    List[str],
    required=True,
    location="query",
    description="Numbers to check",
)
@openapi.response(
    200,
    {
        "application/json": List[SearchV1GetResponse],
    },
    description="OK",
)
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description(
    "Check if one or more phone numbers are registered with the Signal Service."
)
@validate(query=SearchV1GetParams)
async def search_v1_get(
    request, query: SearchV1GetParams
):  # pylint: disable=unused-argument
    """
    Check if one or more phone numbers are registered with the Signal Service.
    """
    numbers = request.args.getlist("numbers")
    try:
        accounts = jsonrpc({"method": "listAccounts"}).get("result", [])
        network_result = []
        for account in accounts:
            network_result = is_registered(
                recipients=numbers, number=account.get("number")
            )
            if network_result:
                break
        return json(network_result, 200)
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc
