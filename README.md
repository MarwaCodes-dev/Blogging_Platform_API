# Blogging Platform API Documentation

## Overview

This API provides functionalities for user management, blog creation, and interaction with various resources such as tags and categories. Users can register, log in, update profiles, manage blogs, and delete resources as needed.

---

## Endpoints

### 1. **User Registration**
   - **URL:** `/api/register/`
   - **Method:** `POST`
   - **Body:**
     ```json
     {
       "username": "string",
       "email": "string",
       "password": "string",
       "bio": "string",
       "profile_pic": "string (optional)"
     }
     ```
   - **Responses:**
     - **201 Created:** User registration successful
     - **400 Bad Request:** Input validation errors

### 2. **User Login**
   - **URL:** `/api/login/`
   - **Method:** `POST`
   - **Body:**
     ```json
     {
       "username": "string",
       "password": "string"
     }
     ```
   - **Responses:**
     - **200 OK:** Login successful with an authentication token
       ```json
       {
         "username": "string",
         "token": "string"
       }
       ```
     - **400 Bad Request:** Incorrect username or password

### 3. **User Profile Update**
   - **URL:** `/api/profile/update/`
   - **Method:** `PUT`
   - **Headers:**
     - `Authorization: Token <your-token-here>`
   - **Body:**
     ```json
     {
       "bio": "string (optional)",
       "profile_pic": "string (optional)"
     }
     ```
   - **Responses:**
     - **200 OK:** Profile updated successfully
     - **400 Bad Request:** Invalid input

### 4. **User Logout**
   - **URL:** `/api/logout/`
   - **Method:** `POST`
   - **Headers:**
     - `Authorization: Token <your-token-here>`
   - **Response:**
     - **200 OK:** Successfully logged out

---

### Blog Management

#### 1. **Create a New Blog**
   - **URL:** `/api/blog/create/`
   - **Method:** `POST`
   - **Body:**
     ```json
     {
       "title": "string",
       "content": "string",
       "tags": ["string"],
       "category": "string"
     }
     ```
   - **Responses:**
     - **201 Created:** Blog post successfully created
     - **400 Bad Request:** Validation errors

#### 2. **Update an Existing Blog**
   - **URL:** `/api/blog/update/{id}/`
   - **Method:** `PUT`
   - **Headers:**
     - `Authorization: Token <your-token-here>`
   - **Body:**
     ```json
     {
       "title": "string (optional)",
       "content": "string (optional)",
       "tags": ["string (optional)"],
       "category": "string (optional)"
     }
     ```
   - **Responses:**
     - **200 OK:** Blog updated successfully
     - **400 Bad Request:** Invalid data

#### 3. **Delete a Blog**
   - **URL:** `/api/blog/delete/{id}/`
   - **Method:** `DELETE`
   - **Headers:**
     - `Authorization: Token <your-token-here>`
   - **Response:**
     - **204 No Content:** Blog deleted
     - **404 Not Found:** Blog not found

---

### Tags & Categories

#### 1. **Delete a Tag**
   - **URL:** `/api/tag/delete/{id}/`
   - **Method:** `DELETE`
   - **Response:**
     - **204 No Content:** Tag successfully deleted
     - **404 Not Found:** Tag not found

#### 2. **Create a Category**
   - **URL:** `/api/category/create/`
   - **Method:** `POST`
   - **Body:**
     ```json
     {
       "name": "string"
     }
     ```
   - **Headers:** 
     - `Authorization: <admin-token-required>`
   - **Response:**
     - **201 Created:** Category successfully created
     - **400 Bad Request:** Input validation errors

---
