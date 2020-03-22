from dataclasses import asdict
from typing import Dict, List, Optional, Union

import httpx

from ..client import AuthenticatedClient, Client
from ..errors import ApiResponseError
from ..models.abc_response import ABCResponse


async def ping_ping_get(
    *, client: Client,
) -> Union[
    ABCResponse,
]:
    """ A quick check to see if the system is running  """
    url = f"{client.base_url}/ping"

    with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=client.get_headers(),)

    if response.status_code == 200:
        return ABCResponse.from_dict(response.json())
    else:
        raise ApiResponseError(response=response)