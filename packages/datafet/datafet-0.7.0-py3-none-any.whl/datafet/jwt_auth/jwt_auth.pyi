import logging
from ..aws_operations import (
    get_secret_binary as get_secret_binary,
    s3_get_object_bytes as s3_get_object_bytes,
    s3_put_object_bytes as s3_put_object_bytes,
    ses_send_email as ses_send_email,
)
from ..custom_types import (
    Clients as Clients,
    Config as Config,
    CustomError as CustomError,
    HttpError as HttpError,
    HttpSuccess as HttpSuccess,
    JwtParam as JwtParam,
    LoginHash as LoginHash,
    MagicLinkDomain as MagicLinkDomain,
    MagicLinkDto as MagicLinkDto,
    MagicLinkInternal as MagicLinkInternal,
    RoleEnum as RoleEnum,
    WhoAmI as WhoAmI,
)
from ..http_return import (
    http_200_json as http_200_json,
    http_400_json as http_400_json,
    http_403_json as http_403_json,
    http_500_json as http_500_json,
    http_error as http_error,
    http_error_to_json_response as http_error_to_json_response,
)
from _typeshed import Incomplete
from ecdsa import SigningKey as SigningKey, VerifyingKey as VerifyingKey
from fastapi import APIRouter as APIRouter, Request as Request
from fastapi.responses import JSONResponse as JSONResponse

LOG: logging.Logger

class Auth:
    default_algorithm: str
    boto3_config: Incomplete
    clients: Incomplete
    config: Incomplete
    def __init__(self, config: Config): ...
