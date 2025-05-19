# Stage 1: Build the application
FROM node:18-alpine as builder

WORKDIR /xpress-way

# Copy only the necessary files for installation
COPY package*.json ./
RUN npm ci

# Copy the rest of the application
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the application
FROM nginx:alpine

# Copy the build output to Nginx's HTML directory
COPY --from=builder /xpress-way/dist /usr/share/nginx/html

# Copy a custom Nginx configuration (ensure it's SPA-friendly)
#COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for the application
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]