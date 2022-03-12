from fastapi import APIRouter, status

router = APIRouter(
    prefix="/healthcheck",
    tags=["logs"],
    responses={500: {"description": "Internal server error"}},
)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def retrieve_check():
    """
    returns an OK if server is up
    """
    return {"status": "OK"}
