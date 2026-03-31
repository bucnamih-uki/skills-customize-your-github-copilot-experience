"""
FastAPI REST API Starter Code

This starter code provides a foundation for building REST APIs with FastAPI.
Complete the tasks to build a fully functional API with data validation and error handling.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize FastAPI application
app = FastAPI(
    title="REST API Assignment",
    description="Building REST APIs with FastAPI framework",
    version="1.0.0"
)

# TODO: Define Pydantic models for data validation
# Example: Create models for request/response data structures


# TODO: Create a root endpoint that returns a welcome message
@app.get("/")
async def read_root():
    """Welcome endpoint"""
    pass


# TODO: Implement additional GET endpoints
# Example endpoints to consider:
# - GET /items - return a list of items
# - GET /items/{item_id} - return a specific item


# TODO: Implement POST endpoints with request body validation
# Example endpoints to consider:
# - POST /items - create a new item
# - PUT /items/{item_id} - update an item
# - DELETE /items/{item_id} - delete an item


# TODO: Add error handling for edge cases
# Consider:
# - What happens if an item is not found?
# - How should validation errors be handled?
# - What HTTP status codes are appropriate?


if __name__ == "__main__":
    import uvicorn
    # Run the application with: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
