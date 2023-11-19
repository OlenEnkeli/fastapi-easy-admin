
from north_admin.types import FieldType
from pydantic import BaseModel, ConfigDict


class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class DTOBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class ColumnDTO(DTOBase):
    column_type: FieldType
    nullable: bool

    is_get_available: bool
    is_list_available: bool
    is_create_available: bool
    is_update_available: bool
    is_sortable: bool


class FilterDTO(DTOBase):
    title: str
    field_type: FieldType


class ModelInfoDTO(DTOBase):
    title: str
    emoji: str
    pkey_column:  str
    soft_delete_column: str | None = None
    filters: list[FilterDTO]
    columns: dict[str, ColumnDTO]
