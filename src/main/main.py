import logging

import coloredlogs
from fastapi import FastAPI

from .endpoints import router
from .containers import Container


logger = logging.getLogger(__package__)
coloredlogs.install(
    level=logging.INFO,
    logger=logger,
    fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
)


container = Container()

container.database().create_database(wipe=container.config.database.wipe)

app = FastAPI()
app.container = container
app.include_router(router)
