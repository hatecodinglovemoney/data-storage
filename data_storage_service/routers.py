import requests
from fastapi import FastAPI

from data_storage_service.database import get_data
from data_storage_service.database import record_data
from data_storage_service.utils.exceptions import ApiRequestError
from data_storage_service.utils.helpers import hash_data
from data_storage_service.utils.schemas import ApiRequestSchema

app = FastAPI()


@app.post("/record_data")
def get_and_record_data(request_data: ApiRequestSchema) -> None:
    response = requests.get(request_data.api_url)
    if response.status_code != 200:
        raise ApiRequestError(f"API response status code: {response.status_code}")
        # Или retry (тогда добавить проверку на наличие флага в request_data).
    response_body = response.json()
    unique_values = {key: response_body[key] for key in request_data.unique_combination}
    hashed_identifier = hash_data(data=unique_values)
    record_data(
        hashed_identifier=hashed_identifier,
        data=response_body,
        api_url=request_data.api_url,
    )


@app.get("/get_data")
def get_data_by_url(collection_name: str):  # TODO: Удалить это
    return get_data(collection_name=collection_name)
