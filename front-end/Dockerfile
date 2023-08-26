# Use an official Node.js runtime as the base image
FROM node:14

# Copy the rest of your application code
# This copies the folder the Dockerfile is in
COPY . .

# Install project dependencies
RUN npm install

# Define build arguments with default values
# These will be used if no env variables were set by docker-compose or githut workflow yml file
# If you change one of these values, it'll only take effect if you do "docker compose up --build"
ARG REACT_APP_API_URL=http://0.0.0.0:8000/predict 
ARG REACT_APP_API_WORKS=true

# Set the environment variables using build arguments
ENV REACT_APP_API_URL=$REACT_APP_API_URL
ENV REACT_APP_API_WORKS=$REACT_APP_API_WORKS

# Expose the port your React app will run on
# This doesn't map anything like docker run -p 8080:3000 would, it's just metadata for docker
EXPOSE 3000

# Start your React app
CMD ["npm", "start"]
