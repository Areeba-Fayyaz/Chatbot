# Django-Chatbot Project

## Project Overview
This Django-Chatbot is a sophisticated web application designed to offer a real-time interactive chat experience. It integrates Django's robust web development capabilities with Rasa's conversational AI, enhanced by WebSockets for live communication, and uses Celery with Redis for efficient background task processing and message queuing. The application is tailored for an engaging user experience with user authentication, personalized chat histories, and real-time response capabilities.

### Key Features
- **User Authentication:** Secure system for user registration and login, ensuring personalized experiences.
- **Chat History:** Maintains individual chat histories for each user, allowing for continuity in conversations.
- **Real-Time Interaction:** Leverages WebSockets for real-time messaging between users and the chatbot.
- **Conversational AI:** Powered by Rasa, capable of understanding and responding to user queries in natural language.
- **Asynchronous Task Processing:** Utilizes Celery with Redis for managing background tasks like saving chat messages in real-time.
- **Scalable Architecture:** Designed for scalability and efficient handling of multiple concurrent user interactions.

## Setup and Running the Application

### Prerequisites
- Python 3.8+
- Django 3.2+
- Rasa 2.8+
- Redis installed and running
- Celery 5.1+

### Installation Steps
#### Clone the Repository
```sh
git clone https://github.com/Areeba-Fayyaz/Chatbot.git
cd Chatbot

#### Virtual Environment Setup
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

#### Install Dependencies
```sh
pip install -r requirements.txt

#### Run Django Migrations
``` sh
python manage.py migrate

#### Running the Servers
Start the Django Server
```sh
python manage.py runserver

#### Start the Celery Worker
Open a new terminal and run:
```sh
celery -A mychatbot worker -l info -P gevent

##### Start the Rasa Server with API Enabled

#### Open a new terminal and run:
``` sh
rasa run --enable-api

Ensure Redis Server is Running
Redis should be running as a message broker for Celery.

#### Accessing the Application
Navigate to http://localhost:8000 in a web browser to interact with the chatbot.

By following these steps, your Django application will be able to interact with the Rasa server through API calls, enabling real-time communication in your chatbot.
