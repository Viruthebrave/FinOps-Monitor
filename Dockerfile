# Step 1: Use Python base image
FROM python:3.10-alpine


# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy project files
COPY app/ /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port
EXPOSE 5000

# Step 6: Run the application
CMD ["python", "main.py"]
