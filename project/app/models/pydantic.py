from pydantic import BaseModel, AnyHttpUrl


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl
