# FastAPI CRUD User API

This is a simple CRUD (Create, Read, Update, Delete) User API built with FastAPI, designed for managing user information. The API is hosted on AWS Lambda and utilizes FastAPI for handling HTTP requests.

## API Endpoints

### 1. Get User
- **Endpoint:** `/get-user`
- **Method:** `GET`
- **Description:** Retrieve information for a specific user.
- **Sample Curl:**
  ```bash
  curl https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/get-user?user_id=<user_id>
  ```

### 2. Get Users
- **Endpoint:** `/get-users`
- **Method:** `GET`
- **Description:** Retrieve information for all users.
- **Sample Curl:**
  ```bash
  curl https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/get-users
  ```

### 3. Create User
- **Endpoint:** `/create-user`
- **Method:** `POST`
- **Description:** Create a new user with the provided information.
- **Request Body (JSON):**
  ```json
  {
    "user_id": "<user_id>",
    "full_name": "<full_name>",
    "mob_num": "<mob_num>",
    "pan_num": "<pan_num>"
  }
  ```
- **Sample Curl:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"user_id": "<user_id>", "full_name": "<full_name>", "mob_num": "<mob_num>", "pan_num": "<pan_num>"}' https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/create-user
  ```

### 4. Delete User
- **Endpoint:** `/delete-user`
- **Method:** `DELETE`
- **Description:** Delete a user by their ID.
- **Sample Curl:**
  ```bash
  curl -X DELETE https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/delete-user?user_id=<user_id>
  ```

### 5. Update User
- **Endpoint:** `/update-user`
- **Method:** `PUT`
- **Description:** Update user information with the provided data.
- **Request Body (JSON):**
  ```json
  {
    "user_id": "<user_id>",
    "full_name": "<full_name>",
    "mob_num": "<mob_num>",
    "pan_num": "<pan_num>"
  }
  ```
- **Sample Curl:**
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"user_id": "<user_id>", "full_name": "<full_name>", "mob_num": "<mob_num>", "pan_num": "<pan_num>"}' https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/update-user
  ```

## Validation
- Both the `create-user` and `update-user` endpoints are validated for syntax.
- Ensure that the request body follows the provided JSON format.

## AWS Lambda Hosted URL
The API is hosted on AWS Lambda. You can access it using the following URL: [https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/](https://4cls57wwkb5ulg4yp4nvenot5a0exskt.lambda-url.ap-south-1.on.aws/)