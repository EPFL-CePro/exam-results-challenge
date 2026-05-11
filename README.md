# Exam Results Challenge

This repository contains a small Django project used to manage exam results.

## Goal

Your task is to complete the project so that it exposes a simple API endpoint returning the students who passed an exam.

If something is unclear or incomplete, feel free to make reasonable assumptions and document them briefly.

We are also interested in how you handle ambiguity and technical trade-offs.


**Please fork this repository and submit your solution by sharing the link to your fork.**

# Expected time

About **1–2 hours**.

Please do not spend more than approximately **3 hours** on this exercise.

The goal is not to build something perfect or production-ready, but to show how you work:

* your reasoning,
* code clarity,
* pragmatic decisions,
* and ability to communicate assumptions and trade-offs.

Clean and maintainable code is preferred over unnecessary complexity.

# Use of AI tools

You may use AI tools (ChatGPT, Copilot, Claude, etc.) if you wish.

However, you should fully understand and be able to explain any code you submit.



The repository already contains sample data (about 200 records) to help you test your endpoint.

---

# Setup

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Load sample data:

```bash
python manage.py loaddata data/sample_data.json
```

Run the server:

```bash
python manage.py runserver
```

The API will be available at:

```
http://localhost:8000/api/results/passed/
```

---

## Run with Docker

The repository contains a **basic Docker configuration that may require small adjustments** to run the project correctly.

Your goal is to make the project start with:

```bash
docker compose up --build
```

Once the container is running, you may need to run:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py loaddata data/sample_data.json
```

The API should then be available at:

```
http://localhost:8000/api/results/passed/
```

---

# Tasks

## 1. Implement the endpoint

Complete the following endpoint:

```http
GET /api/results/passed/
```

It should return all results with a score greater than or equal to `10`, sorted by descending score.

Example response:

```json
[
  {"student_name": "Alice", "course": "Mathematics", "score": 14.5},
  {"student_name": "Chloé", "course": "Physics", "score": 12.0}
]
```

---

## 2. Support an optional query parameter

The endpoint should also support:

```http
GET /api/results/passed/?min_score=12
```

---

## 3. Add at least one automated test

You may use Django's test framework.

---

## 4. Make the project runnable with Docker

The provided Docker configuration is intentionally minimal.

Make the project start correctly using:

```bash
docker compose up --build
```

---

# Submission

**Please fork this repository and submit your solution by sharing the link to your fork.**

Small and meaningful commits are appreciated.

Feel free to explain your choices in the Pull Request description.

---

# Improvements

If you had more time, what would you improve in this project?

A short paragraph or bullet list is enough.

---

# Notes

- Keep things simple.
- Clean and readable code is preferred over unnecessary complexity.
- If something is incomplete, explain what you would do next.

---

# Bonus

If you have time, add:

- input validation for `min_score`
- a small README section explaining your choices
- an improvement proposal
