# Dockerfile for React client

# Base image
FROM node:14

# Set working directory inside the container
WORKDIR /app

# Install dependencies (copy only package.json and package-lock.json if you have one)
COPY package*.json /app/
RUN npm install

# Copy the entire app directory into the container
COPY . /app

# Build the React app
RUN npm run build

# Command to run the React server (not needed for static file serving)
# CMD ["npm", "start"]
