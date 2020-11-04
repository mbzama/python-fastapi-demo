import databases
import sqlalchemy
import logging
import os
import json
from fastapi import FastAPI
from sqlalchemy import text

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

db_string = "postgresql://{0}:{1}@{2}/{3}".format(os.getenv("POSTGRES_USER"),
                                                  os.getenv("POSTGRES_PASSWORD"),
                                                  os.getenv("DATABASE_URL"),
                                                  os.getenv("DATABASE"))

database = databases.Database(db_string)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(db_string)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("Connecting to database: "+db_string)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    logger.info("Disconnecting from database: " + db_string)
    await database.disconnect()


@app.get("/")
def read_root():
    return {
            "Message": "API is up and running",
            "DATABASE": [os.getenv("DATABASE_URL"), os.getenv("POSTGRES_USER"), os.getenv("POSTGRES_PASSWORD")],
            "AUTHENTICATION": os.getenv("AUTHENTICATION")
    }

# res1: data1 ---> select data1 as res1,
# res2: data2
@app.get("/metrics")
def read_item():
    with engine.connect() as con:
        rs = con.execute(text('select id, data1 as res1, data2 as res2 from metrics m where m.id = :val'), {'val': '1000000'})
        # metrics = []
        for v in rs:
            for column, value in v.items():
                logger.info('column: ' + format(column) + ', value: ' + format(value))
                # metrics.__add__({format(column) : format(value)})
    return {"metrics": v.items()}