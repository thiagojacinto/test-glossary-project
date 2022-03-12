from fastapi import APIRouter

router = APIRouter(
    prefix="/terms", tags=["terms"], responses={404: {"description": "Not found"}}
)


@router.get(
    path="/",
    summary="Terms lists",
    description="Returns a list of terms from the glossary",
)
async def list_terms():
    """
    returns a list of terms from the glossary
    """
    return [{}]
