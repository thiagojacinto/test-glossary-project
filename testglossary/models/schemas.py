from pydantic import BaseModel


class TermBase(BaseModel):
    """Basic usage of Test Term model"""

    name: str
    definition: str


class Term(TermBase):
    """Test Term that shows the language info"""

    id: int
    language_id: int
    acronym: str | None

    class Config:
        orm_mode = True


class CreateTerm(Term):
    version: int
    language_id: int


class Language(BaseModel):
    """Basic usage of Language model"""

    id: int
    language: str | None

    class Config:
        orm_mode = True
