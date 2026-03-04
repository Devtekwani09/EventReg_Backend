# Event Registration API

A FastAPI-based event registration system with user authentication, email verification, and secure password handling.

## Features

- User registration and authentication
- Email-based verification with OTP
- Secure password hashing using bcrypt_sha256
- JWT-based access and refresh tokens
- User profile management
- Database persistence with SQLAlchemy

## Project Structure

```
eventreg/
├── api/              # API route handlers
│   └── auth.py       # Authentication endpoints
├── db/               # Database configuration
│   └── database.py   # Database setup & session management
├── models/           # SQLAlchemy models
│   └── users.py      # User database model
├── schemas/          # Pydantic request/response schemas
│   └── user.py       # User validation schemas
├── services/         # Business logic
│   └── auth_service.py    # Authentication service logic
├── utils/            # Utility functions
│   ├── security.py   # Password hashing & JWT tokens
│   └── send_email.py # Email sending functionality
├── config.py         # Configuration settings
├── main.py           # FastAPI application entry point
└── .gitignore        # Git ignore file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd eventreg
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the root directory with the following variables:
```
DATABASE_URL=sqlite:///./eventreg.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

## Running the Application

Start the FastAPI development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- **POST** `/api/auth/register` - Register a new user
- **POST** `/api/auth/login` - Login and get access token
- **POST** `/api/auth/verify-otp` - Verify email with OTP

## Security

- Passwords are hashed using bcrypt_sha256 algorithm
- JWT tokens for stateless authentication
- Email verification for account confirmation
- Environment-based configuration for sensitive data

## Dependencies

Key packages used:
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for database operations
- **Passlib** - Password hashing
- **python-jose** - JWT token management
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## Database

SQLite is used by default for development. For production, consider using PostgreSQL or MySQL.

To initialize the database:
```bash
python -c "from db.database import engine; from models.users import Base; Base.metadata.create_all(bind=engine)"
```

## Development

### Running Tests
```bash
pytest
```

### Code Style
Follow PEP 8 guidelines. Use tools like `black` and `flake8` for formatting and linting.

## Troubleshooting

### Password Hashing Error
If you encounter "ValueError: password cannot be longer than 72 bytes", ensure `bcrypt_sha256` is used instead of plain `bcrypt` in the password context configuration.

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit your changes (`git commit -m 'Add amazing feature'`)
3. Push to the branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request
