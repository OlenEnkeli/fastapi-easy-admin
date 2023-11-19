import json
from json import JSONDecodeError

from typing import Callable, Type

from pydantic import BaseModel
from fastapi import Query, HTTPException
from random_unicode_emoji import random_emoji


def set_origin_to_pydantic_schema(schema: BaseModel, function: Callable) -> Callable:
    function.__annotations__['origin'] = schema # noqa
    return function


def generate_random_emoji() -> str:
    return str(random_emoji(count=1)[0][0])


def filters_dict(filters: str = Query(...)):
    try:
        return json.loads(filters)
    except JSONDecodeError as e:
        raise HTTPException(
            status_code=422,
            detail=f'Invalida json in filters params: {e}'
        ) from e
