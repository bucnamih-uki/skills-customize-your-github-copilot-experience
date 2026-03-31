# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable, modern REST APIs using FastAPI framework. You'll create a fully functional API with data validation, error handling, and interactive documentation.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project and Create Basic API

#### Description
Install FastAPI and Uvicorn, then create a basic API server with a few simple endpoints. This foundation will help you understand how FastAPI handles requests and responses.

#### Requirements
Completed API should:

- Install FastAPI and Uvicorn using pip
- Create a FastAPI application instance
- Define at least 2 GET endpoints that return JSON responses
- Run the server using Uvicorn on localhost:8000
- Include a root endpoint that returns a welcome message

### 🛠️ Implement Data Models and Request Validation

#### Description
Create Pydantic models to define request and response data structures. Use FastAPI's built-in validation to ensure data integrity and provide automatic type checking.

#### Requirements
Completed API should:

- Define 2+ Pydantic models for request/response data
- Implement POST endpoints that accept request bodies
- Use type hints for all parameters and returns
- Return appropriate HTTP status codes (200, 201, 400, etc.)
- Include at least one endpoint that validates and processes request data

### 🛠️ Add Error Handling and API Documentation

#### Description
Implement comprehensive error handling and leverage FastAPI's automatic documentation features. Create endpoints that handle edge cases gracefully and provide helpful error messages to API consumers.

#### Requirements
Completed API should:

- Handle validation errors with meaningful error responses
- Implement custom error handling for specific scenarios
- Use HTTPException for error scenarios
- Verify that interactive API docs are available at `/docs`
- Include docstrings for all endpoints that appear in API documentation
- Test all endpoints to ensure they work correctly
