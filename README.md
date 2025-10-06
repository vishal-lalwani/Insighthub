# InsightHub — AI-Powered Feedback Management System  

---

## Overview  

**InsightHub** is a Flask-based feedback management system that collects user feedback, performs **sentiment analysis**, and provides actionable insights for admins.  
It’s fully **Dockerized**, integrates **MySQL** for structured data storage, and supports **role-based authentication** via **JWT tokens**.

> Designed for businesses to analyze customer sentiment and improve product experience.

---

## Features  

- Submit feedback with category and rating.  
- Automatic sentiment detection using **TextBlob**.  
- **JWT-based Authentication** (User/Admin).  
- View personal feedback history via APIs.  
- Admin analytics with sentiment summaries.  
- One-command **Docker** deployment.  
- Persistent storage using **MySQL**.  

---

## System Architecture  
```
Frontend (Postman / Future UI)
↓
Flask REST API ←→ MySQL Database
↓
Sentiment Analysis (TextBlob)
↓
Admin Analytics & Insights
```

---

## Tech Stack  

| Category | Technology |
|-----------|-------------|
| **Language** | Python 3.10 |
| **Framework** | Flask |
| **Database** | MySQL |
| **Containerization** | Docker & Docker Compose |
| **Auth** | JWT (Flask-JWT-Extended) |
| **Sentiment Analysis** | TextBlob |
| **Testing** | Postman |
| **Version Control** | Git, GitHub |

---

## Installation  
---

#### Clone the Repository  
```bash
git clone https://github.com/your-username/insighthub.git
cd insighthub
```

### Create .env File  
SECRET_KEY=your_secret_key  
JWT_SECRET_KEY=your_jwt_secret_key  
MYSQL_HOST=db  
MYSQL_USER=root  
MYSQL_PASSWORD=your_password  
MYSQL_DB=insighthub  

### Build and Run with Docker  
docker-compose up --build  

### Your services will start as:  
Flask API: http://127.0.0.1:5000  
MySQL: inside Docker container  

### Authentication  
Include your JWT token in the Authorization Header for protected routes:  
Authorization: Bearer <access_token>  
You receive this token after a successful signup or login.  

## API Endpoints
---

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /signup | Register a new user |
| POST | /login | Login and get JWT token |

### User Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /feedback | Submit feedback |
| GET | /my-feedbacks | View your feedback history |

### Admin Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /admin/feedbacks | View all user feedback |
| GET | /admin/analytics | View sentiment and rating analytics |

### Testing with Postman
---
1. Open Postman and create a new Collection named InsightHub.  
2. Add all API routes listed above.  
3. Test signup/login to get a JWT token.  
4. Use {{access_token}} as an environment variable in Authorization header.  

### Postman Test Script Example
```bash
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

var jsonData = pm.response.json();
if (jsonData.access_token) {
    pm.environment.set("access_token", jsonData.access_token);
}
```

### Example Feedback Response
```bash
{
  "id": 3,
  "category": "Design",
  "feedback_text": "The dashboard layout could be more intuitive.",
  "rating": 3,
  "sentiment": "Neutral",
  "sentiment_score": -0.15,
  "user_id": 2,
  "created_at": "2025-10-06T11:27:28"
}
```

## Folder Structure
```
insighthub/
│
├── app.py
├── models.py
├── routes/
│   ├── auth_routes.py
│   ├── feedback_routes.py
│   └── admin_routes.py
├── utils/
│   ├── sentiment_analyzer.py
│   └── jwt_helper.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── .env
```

### Future Enhancements

- Frontend Dashboard with Analytics Visualization
- Export feedback data to CSV/Excel
- Email notifications for admins
- Enhanced NLP models using Transformers
