from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.config.database import DB_URL
from app.routes.api import api
import uvicorn
from fastapi import status

class App:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()
        self.log_database_url()
        self.setup_validation_error_handler()

    def setup_routes(self):
        self.app.include_router(api, prefix="/api/v1")
        
        @self.app.get("/")
        def read_root():
            return {"message": "Server is running"}

    def setup_validation_error_handler(self):
        # Custom handler for validation errors
        @self.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(request: Request, exc: RequestValidationError):
            errors = exc.errors()
            error_details = []
            
            for err in errors:
                field = err.get('loc')[-1] 
                message = err.get('msg')   
                error_details.append({
                    'field': field,
                    'message': message
                })
            
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={"status": "failed", "message": "Validation Error", "errors": error_details}
            )

    def log_database_url(self):
        print(f"DB_URL: {DB_URL}")

def get_app():
    return App().app

app = get_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8888)
