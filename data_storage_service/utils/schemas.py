from pydantic import BaseModel


class ApiRequestSchema(BaseModel):
    api_url: str
    unique_combination: list
    # api_auth: str  # Авторизация для API (?)
    # retry: bool  # Флаг, отвечающий за retry + можно добавить retry_config.
