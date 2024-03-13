# Use an official Python runtime as a parent image
FROM python:3.10

COPY . .

# Install MongoDB client tools
RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add - \
    && echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/5.0 main" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list \
    && apt-get update \
    && apt-get install -y mongodb-org-tools mongodb-mongosh

# Set environment variables
ENV MONGODB_USERNAME=admin
ENV MONGODB_PASSWORD=admin
ENV MONGODB_HOST=mongodb
ENV MONGODB_PORT=27017
ENV MONGODB_DATABASE=dofusdb
ENV PYTHONPATH="/src"

# Copy init-mongo.sh script into the container
COPY ./data/init-mongo.sh /docker-entrypoint-initdb.d/init-mongo.sh

# Set execute permissions for the script
RUN chmod +x /docker-entrypoint-initdb.d/init-mongo.sh

# Run app.py when the container launches
CMD ["bash", "-c", "/docker-entrypoint-initdb.d/init-mongo.sh"]