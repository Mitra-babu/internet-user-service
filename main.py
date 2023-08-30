import uvicorn
from fastapi import FastAPI, Request
from router import country_resource, region_resource, population_resource

app = FastAPI()
app.include_router(country_resource.router)
# # app.include_router(region_resource.router)
app.include_router(population_resource.router)

if __name__ == "__main__":
    uvicorn.run(app)
