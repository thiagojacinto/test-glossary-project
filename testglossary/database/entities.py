from sqlalchemy import Column, ForeignKey, Integer, String

from testglossary.database.connection import Base


class Term(Base):
    """Test term to be explained"""

    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    acronym = Column(String)
    definition = Column(String)
    version = Column(Integer)
    language_id = Column(Integer, ForeignKey("languages.id"), index=True)


class Language(Base):
    """Choose language of test term translation"""

    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, unique=True)
