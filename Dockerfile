FROM python:3.14-slim

WORKDIR /app

COPY student_app.py .
COPY test_student.py .

CMD ["python", "student_app.py"]