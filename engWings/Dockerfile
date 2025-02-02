# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt to the container at /app
COPY requirements.txt /app/

# Step 4: Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the current directory contents into the container at /app
COPY . /app/

# Step 6: Expose the port Django will run on
EXPOSE 8000
# Step 7: Set the default command to run Django server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
