from pydantic import BaseModel


class TermBase(BaseModel):
    """Basic usage of Test Term model"""

    name: str
    definition: str
    acronym: str | None


class Term(TermBase):
    """Test Term that shows the language info"""

    id: int
    language_id: int

    class Config:
        orm_mode = True


class CreateTerm(TermBase):
    version: int
    language_id: int


class Language(BaseModel):
    """Basic usage of Language model"""

    id: int
    language: str | None

    class Config:
        orm_mode = True
