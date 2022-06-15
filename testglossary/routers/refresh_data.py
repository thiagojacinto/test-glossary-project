from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from testglossary.database import db_instance, interface
from testglossary.internal import exceptions, serializers
from testglossary.models import schemas

router = APIRouter(
    prefix="/refresh",
    tags=["refresh"],
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
        status.HTTP_403_FORBIDDEN: {"description": "Forbidden"},
    },
)


@router.post(
    path="/",
    summary="Add a new term into local database",
    description="Saves information of a new term into local database",
    status_code=status.HTTP_201_CREATED,
    response_model=serializers.Sucessfully_term_created,
)
async def add_new_term(
    received_term: schemas.CreateTerm, db: Session = Depends(db_instance.use_db)
):
    try:
        registered = interface.register_new_term(db, received_term)
        return serializers.Sucessfully_term_created(result=True, id=registered.id)
    except:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=exceptions.terms.get("UNPROCESSABLE_ENTITY"),
        )
