from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from sqlalchemy.orm import Session

from testglossary.database import connection, entities, interface
from testglossary.internal import exceptions, serializers

router = APIRouter(
    prefix="/terms", tags=["terms"], responses={404: {"description": "Not found"}}
)

# Create tables
entities.Base.metadata.create_all(bind=connection.engine)

# Database Dependency


def use_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    path="/",
    summary="Terms lists",
    description="Returns a list of terms from the glossary",
    response_model=serializers.Paginated_terms_list,
)
async def list_terms(
    page: int | None = Query(default=0, title="Page number", example=0, ge=0),
    terms_per_page: int
    | None = Query(
        default=10, title="Number of terms listed by page", example=10, ge=1
    ),
    db: Session = Depends(use_db),
):
    """
    returns a list of terms from the glossary
    """
    if terms_list := interface.get_terms(
        db, page=page, results_per_page=terms_per_page
    ):
        paginated_terms_list = serializers.Paginated_ouput(
            result=terms_list, page=page, offset=terms_per_page
        )
        return paginated_terms_list

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=exceptions.terms.get(
            "EMPTY_LIST")
    )


@router.get(
    path="/search/{name}",
    summary="Search by term name",
    description="Search by specific test term name",
    response_model=serializers.Paginated_terms_list,
)
async def get_term_by_name(
    name: str = Path(None, title="Test term query string",
                     max_length=30, min_length=3),
    page: int | None = Query(default=0, title="Page number", example=0, ge=0),
    terms_per_page: int
    | None = Query(default=5, title="Number of terms listed by page", example=10, ge=1),
    db: Session = Depends(use_db),
):
    """
    Search for a term by its name
    """
    if db_terms := interface.get_term_by_name(
        db, term_name=name, page=page, results_per_page=terms_per_page
    ):
        paginated_terms_list = serializers.Paginated_ouput(
            result=db_terms, page=page, offset=terms_per_page
        )
        return paginated_terms_list

    raise HTTPException(
        status_code=404, detail=exceptions.terms.get("NOT_FOUND"))
