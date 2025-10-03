#Use Python lsim image
FROM python:3.11-slim

#Set working directory
WORKDIR /app

#Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy Application
COPY app.py .
COPY test_app.py .

#Expose Flask Port
EXPOSE 5000

#Run the app
CMD ["python", "app.py"]

