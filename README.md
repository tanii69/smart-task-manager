# Smart Task Manager

## Overview
A full-stack task management application built using Flask (backend), React (frontend), and SQLite database. The system allows users to create, view, and delete tasks with AI-based priority suggestions.

## Tech Stack
- Backend: Python, Flask
- Frontend: React
- Database: SQLite
- AI: Rule-based priority suggestion

## Features
- Add task
- Delete task
- View all tasks
- AI-based priority classification

## API Endpoints
- POST /tasks → Create task
- GET /tasks → Get all tasks
- DELETE /tasks/:id → Delete task

## AI Usage
A rule-based AI function assigns priority:
- High → exam, urgent
- Medium → assignment, project
- Low → others

## Setup Instructions

### Backend
cd backend  
venv\Scripts\activate  
python app.py  

### Frontend
cd frontend  
npm install  
npm start  

## Tradeoffs
- Used rule-based AI instead of external API for reliability and simplicity
- No authentication implemented to keep system simple

## Future Improvements
- Add user authentication
- Add task deadlines
- Use real AI model (OpenAI API)
- Add task editing