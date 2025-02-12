# PandaJobs

A modern job board web application with a Django backend and Vue.js frontend. Users can register, login, post job listings, and search for jobs using both local and external job sources.

## Features
- User registration and authentication
- Job posting by employers
- Job application submission
- Advanced job search with local and external sources
- Admin panel for managing users, job listings, and applications
- Modern, responsive UI with Vue.js
- Real-time job search with dynamic filtering

## Technologies Used
### Backend
- Django: Web framework for backend development
- Django REST Framework: For building the REST API
- Django CORS Headers: For handling Cross-Origin Resource Sharing
- PostgreSQL: Database (optional, can use SQLite for development)

### Frontend
- Vue.js 3: Progressive JavaScript framework
- Vue Router: For client-side routing
- Axios: For making HTTP requests
- Tailwind CSS: For styling
- Headless UI: For accessible UI components
- Heroicons: For beautiful icons

## Installation and Setup

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SeyiAyo/PandaJobs.git
   cd PandaJobs
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your RapidAPI key and other required variables

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Install Node.js from https://nodejs.org/

2. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. Start the Vue development server:
   ```bash
   npm run dev
   ```

4. Access the application:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000

## Development

### Backend API Endpoints
- `/api/jobs/`: List and create jobs
- `/api/jobs/<id>/`: Retrieve, update, and delete jobs
- `/api/jobs/search/`: Search jobs (both local and external)
- `/api/auth/`: Authentication endpoints

### Frontend Structure
- `src/views/`: Page components
- `src/components/`: Reusable UI components
- `src/assets/`: Static assets
- `src/router/`: Route definitions

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License.
