from fastapi import APIRouter, FastAPI, status
from fastapi.responses import RedirectResponse

from testglossary.internal import health_check
from testglossary.internal.api_versions import API_versions
from testglossary.routers import terms

from testglossary.database import connection, entities

app = FastAPI(
    title="TestGlossary API",
    description="API service that retrieve information about test concepts as a glossary.",
    contact={
        "name": "Thiago Jacinto",
        "url": "https://www.linkedin.com/in/thiago-jacinto/",
    },
    docs_url="/api/docs",
    redoc_url="/api/redocs",
    openapi_url="/api/openapi.json",
)
active_API_version = API_versions.v1.value
active_API_version_router = APIRouter(prefix="/{}".format(active_API_version))

active_API_version_router.include_router(terms.router)
active_API_version_router.include_router(health_check.router)

app.include_router(active_API_version_router, prefix="/api")


@app.get(path="/")
async def redirect_root_to():
    path_redirect = "/api/{}/healthcheck".format(active_API_version)
    return RedirectResponse(
        url=path_redirect, status_code=status.HTTP_308_PERMANENT_REDIRECT
    )


# Create tables
entities.Base.metadata.create_all(bind=connection.engine)
