A Django-based job board web application for posting and searching job listings. Users can register, login, and post job listings, while also searching for jobs based on various criteria. Includes features for job seekers to apply for jobs and for employers to manage job postings.

Features:
User registration and authentication
Job posting by employers
Job application submission
Admin panel for managing users, job listings, and 


Technologies Used:
Django: Web framework for backend development
HTML, CSS, JavaScript: Frontend technologies
Tailwind: Frontend framework for styling


Installation and Usage:
1. Clone the repository:
   git clone https://github.com/SeyiAyo/PandaJobs.git

2. Install dependencies:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver

5. Access the application at http://localhost:8000/

Render deploy:
Create the Render service from [render.yaml](/home/rehd/Desktop/PandaJobs/render.yaml), replace the Docker Hub username placeholder in that file, set `DJANGO_SECRET_KEY` in Render, and create a GitHub secret named `RENDER_DEPLOY_HOOK_URL`. After a successful Docker build on the `rehd-devops` branch, GitHub Actions will trigger Render to deploy the freshly built `sha-...` image.
