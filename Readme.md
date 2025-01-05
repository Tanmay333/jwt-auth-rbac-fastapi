Here's what you should include in your `README.md` file for each endpoint:

---

# FastAPI Project API

## Setup Instructions
1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment:**
   - **Unix/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows (cmd):**
     ```cmd
     venv\Scripts\activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
---

## Endpoints

### **User Endpoints**

#### **Register a New User**
- **Endpoint:** `POST /register`
- **Description:** Registers a new user with a username, password, and role.
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string",
    "role": "string"
  }
  ```
- **Response:**
  ```json
  {
    "username": "string",
    "role": "string"
  }
  ```

#### **User Login**
- **Endpoint:** `POST /login`
- **Description:** Authenticates a user and returns a JWT token.
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```

---

### **Project Endpoints**

#### **Get All Projects**
- **Endpoint:** `GET /projects/`
- **Description:** Fetch all projects (requires authentication).
- **Response:**
  ```json
  [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

#### **Create a New Project (Admin Only)**
- **Endpoint:** `POST /projects/`
- **Description:** Creates a new project (Admin access required).
- **Request Body:**
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response:**
  ```json
  {
    "id": "string",
    "name": "string",
    "description": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### **Update a Project (Admin Only)**
- **Endpoint:** `PUT /projects/{project_id}`
- **Description:** Updates project details (Admin access required).
- **Request Body:**
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response:**
  ```json
  {
    "id": "string",
    "name": "string",
    "description": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### **Delete a Project (Admin Only)**
- **Endpoint:** `DELETE /projects/{project_id}`
- **Description:** Deletes a project by its ID (Admin access required).
- **Response:** 
  - **Status:** `204 No Content`

---

### **Authentication**
- All protected routes require an `Authorization` header with a valid JWT token:  
  ```bash
  Authorization: Bearer <token>
  ```

---

Let me know if you need any adjustments or more details!