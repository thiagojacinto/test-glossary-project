from sqlalchemy.orm import Session

from testglossary.database.entities import Term
from testglossary.models.schemas import CreateTerm


def get_terms(db: Session, page: int = 0, results_per_page: int = 30):
    """
    Return all test terms, paginated
    """
    return db.query(Term).offset(page).limit(results_per_page).all()


def get_term_by_name(
    db: Session, term_name: str, page: int = 0, results_per_page: int = 5
):
    """
    Search for a test term by its name
    """
    return (
        db.query(Term)
        .where(Term.name.ilike("%{}%".format(term_name)))
        .offset(page)
        .limit(results_per_page)
        .all()
    )


def register_new_term(db: Session, term_data: CreateTerm):
    """
    Register a test term into database
    """
    db_new_term = Term(
        name=term_data.name,
        definition=term_data.definition,
        acronym=term_data.acronym,
        version=term_data.version,
        language_id=term_data.language_id,
    )
    db.add(db_new_term)
    db.commit()
    db.refresh(db_new_term)
    return db_new_term


def get_term_by_acronym(
    db: Session, term_acronym: str, page: int = 0, results_per_page: int = 5
):
    """
    Search for a test term by its acronym
    """
    return (
        db.query(Term)
        .where(Term.acronym.ilike("%{}%".format(term_acronym)))
        .offset(page)
        .limit(results_per_page)
        .all()
    )
