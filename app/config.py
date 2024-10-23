from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "vehicle_allocation"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

settings = Settings()
