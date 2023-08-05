"""
register and verify
"""

from traceback import format_exc
from typing import Optional

from pydantic import BaseModel
from sanic import Blueprint
from sanic.exceptions import BadRequest
from sanic.log import logger
from sanic.response import json
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import ResponseBadRequest
from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

register_v1 = Blueprint("register_v1", url_prefix="/register")
verify_v1 = Blueprint("verify_v1", url_prefix="/register")


class RegisterV1PostParams(BaseModel):
    """
    RegisterV1PostParams
    """

    captcha: Optional[str]
    use_voice: Optional[bool] = False


@register_v1.middleware("request")
async def register_post_dummy_body(request):
    """
    Create empty dummy body for @validate
    if there is none in request
    """
    if not request.body:
        request.body = b"{}"


@register_v1.post("/<number:path>", version=1)
@openapi.tag("Devices")
@openapi.parameter("number", str, required=True, location="path")
@openapi.body({"application/json": RegisterV1PostParams})
@openapi.response(201, {"application/json": None}, description="Created")
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description("Register a phone number with the signal network.")
@validate(RegisterV1PostParams)
async def register_post(
    request, number, body: RegisterV1PostParams
):  # pylint: disable=unused-argument
    """
    Register a phone number.
    """
    try:
        params = {
            "account": number,
        }
        if body.captcha:
            params.update({"captcha": body.captcha})
        if body.use_voice:
            params.update({"voice": body.use_voice})
        result = jsonrpc({"method": "register", "params": params})
        # successful verification just returns None
        if not result:
            raise BadRequest(result)
        return json(None, 201)
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc


class VerifyV1PostParams(BaseModel):
    """
    VerifyV1PostParams
    """

    pin: Optional[str] = ""


@verify_v1.middleware("request")
async def verify_post_dummy_body(request):
    """
    Create empty dummy body for @validate
    if there is none in request
    """
    if not request.body:
        request.body = b"{}"


@verify_v1.post("/<number:path>/verify/<token:path>", version=1)
@openapi.tag("Devices")
@openapi.parameter("number", str, required=True, location="path")
@openapi.parameter("token", str, required=True, location="path")
@openapi.body({"application/json": VerifyV1PostParams})
@openapi.response(201, {"application/json": None}, description="Created")
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description("Verify a registered phone number with the signal network.")
@validate(VerifyV1PostParams)
async def verify_post(
    request, number, token, body: VerifyV1PostParams
):  # pylint: disable=unused-argument
    """
    Verify a registered phone number.
    """
    try:
        params = {
            "account": number,
            "verificationCode": token,
        }
        if body.pin:
            params.update({"pin": body.pin})
        result = jsonrpc({"method": "verify", "params": params})
        # successful verification just returns None
        if not result:
            raise BadRequest(result)
        return json(None, 201)
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc
