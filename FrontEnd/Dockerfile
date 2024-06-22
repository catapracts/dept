# Dockerfile for React client without Nginx

# Base image
FROM node:14

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json if you have one
COPY package*.json /app/

# Install dependencies
RUN npm install

# Copy the entire app directory into the container
COPY . /app

# Build the React app
RUN npm run build

# Expose the port on which the React app will run (usually 3000)
EXPOSE 3000

# Command to run the React server (for development mode)
CMD ["npm", "start"]
