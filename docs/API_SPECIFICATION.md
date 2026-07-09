# TapGol API Specification 📡

## Base URL
```
http://localhost:5000/api
```

---

## Authentication Endpoints

### 1. Sign Up
```
POST /auth/signup
Content-Type: application/json

Request:
{
  "email": "user@example.com",
  "password": "securepassword123",
  "username": "footballfan"
}

Response (201):
{
  "id": 1,
  "email": "user@example.com",
  "username": "footballfan",
  "token": "eyJhbGc..."
}
```

### 2. Login
```
POST /auth/login
Content-Type: application/json

Request:
{
  "email": "user@example.com",
  "password": "securepassword123"
}

Response (200):
{
  "id": 1,
  "email": "user@example.com",
  "token": "eyJhbGc..."
}
```

---

## Groups Endpoints

### 3. Create Group
```
POST /groups
Authorization: Bearer <token>
Content-Type: application/json

Request:
{
  "name": "Fußball Montag",
  "description": "Jeden Montag um 19:00"
}

Response (201):
{
  "id": 1,
  "name": "Fußball Montag",
  "description": "Jeden Montag um 19:00",
  "created_by": 1,
  "members_count": 1
}
```

### 4. Get All Groups
```
GET /groups
Authorization: Bearer <token>

Response (200):
[
  {
    "id": 1,
    "name": "Fußball Montag",
    "description": "Jeden Montag um 19:00",
    "members_count": 5
  }
]
```

### 5. Join Group
```
POST /groups/:group_id/join
Authorization: Bearer <token>

Response (200):
{
  "message": "Successfully joined group",
  "group_id": 1
}
```

---

## Messages Endpoints

### 6. Send Message
```
POST /messages
Authorization: Bearer <token>
Content-Type: application/json

Request:
{
  "group_id": 1,
  "text": "Wer kommt heute?"
}

Response (201):
{
  "id": 1,
  "group_id": 1,
  "user_id": 1,
  "text": "Wer kommt heute?",
  "created_at": "2024-07-09T10:30:00Z"
}
```

### 7. Get Group Messages
```
GET /messages?group_id=1
Authorization: Bearer <token>

Response (200):
[
  {
    "id": 1,
    "username": "footballfan",
    "text": "Wer kommt heute?",
    "created_at": "2024-07-09T10:30:00Z"
  }
]
```

---

## Polls Endpoints

### 8. Create Poll
```
POST /polls
Authorization: Bearer <token>
Content-Type: application/json

Request:
{
  "group_id": 1,
  "question": "Wer kommt zum Match?",
  "options": ["Ja", "Nein", "Vielleicht"]
}

Response (201):
{
  "id": 1,
  "group_id": 1,
  "question": "Wer kommt zum Match?",
  "options": [
    {"id": 1, "text": "Ja", "votes": 0},
    {"id": 2, "text": "Nein", "votes": 0},
    {"id": 3, "text": "Vielleicht", "votes": 0}
  ],
  "created_at": "2024-07-09T10:30:00Z"
}
```

### 9. Vote on Poll
```
POST /polls/:poll_id/vote
Authorization: Bearer <token>
Content-Type: application/json

Request:
{
  "option_id": 1
}

Response (200):
{
  "id": 1,
  "question": "Wer kommt zum Match?",
  "options": [
    {"id": 1, "text": "Ja", "votes": 1},
    {"id": 2, "text": "Nein", "votes": 0},
    {"id": 3, "text": "Vielleicht", "votes": 0}
  ]
}
```

### 10. Get Poll Results
```
GET /polls/:poll_id
Authorization: Bearer <token>

Response (200):
{
  "id": 1,
  "question": "Wer kommt zum Match?",
  "options": [
    {"id": 1, "text": "Ja", "votes": 3},
    {"id": 2, "text": "Nein", "votes": 1},
    {"id": 3, "text": "Vielleicht", "votes": 2}
  ]
}
```

---

## Error Responses

### 400 - Bad Request
```json
{
  "error": "Invalid input",
  "message": "Email is required"
}
```

### 401 - Unauthorized
```json
{
  "error": "Unauthorized",
  "message": "Invalid or expired token"
}
```

### 404 - Not Found
```json
{
  "error": "Not found",
  "message": "Group not found"
}
```

### 500 - Server Error
```json
{
  "error": "Internal server error",
  "message": "Something went wrong"
}
```

---

## Status Codes

| Code | Bedeutung |
|------|----------|
| 200 | OK - Erfolgreich |
| 201 | Created - Erfolgreich erstellt |
| 400 | Bad Request - Ungültige Eingabe |
| 401 | Unauthorized - Authentifizierung erforderlich |
| 404 | Not Found - Ressource nicht gefunden |
| 500 | Server Error - Fehler auf dem Server |
