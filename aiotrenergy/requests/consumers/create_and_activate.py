from pydantic import HttpUrl, Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.consumers.create_and_activate import ConsumersCreateAndActivateResponse


class ConsumersCreateAndActivateRequest(TrenergyRequest):
    __api_path__ = "consumers/bootstrap-order"
    __response__ = ConsumersCreateAndActivateResponse
    __rest_method__ = RestMethod.POST

    payment_period: int = Field(json_schema_extra=BODY_LOCATION)
    address: str = Field(json_schema_extra=BODY_LOCATION)
    auto_renewal: bool = Field(json_schema_extra=BODY_LOCATION)
    resource_amount: int = Field(None, json_schema_extra=BODY_LOCATION)
    name: str | None = Field(json_schema_extra=BODY_LOCATION)
    webhook_url: HttpUrl | None = Field(None, json_schema_extra=BODY_LOCATION)
