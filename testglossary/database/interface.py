from sqlalchemy.orm import Session

from testglossary.database.entities import Term


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
