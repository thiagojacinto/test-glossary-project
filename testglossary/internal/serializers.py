from pydantic import BaseModel

from testglossary.models.schemas import Term


class Paginated_ouput(BaseModel):
    """
    Paginated response output serializer.
    """

    result: list | dict | None
    page: int = 0
    offset: int = 0


class Paginated_terms_list(Paginated_ouput):
    """
    Specialized paginated response for a Test Terms list
    """

    result: list[Term]
