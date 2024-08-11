<div align="center">
  <a href="https://cloud-station.io">
    <img src="https://server.cloud-station.io/cloudstation/cs_icon.png" alt="CloudStation Logo" width="50">
  </a>
  <h3 align="center">CloudStation FastAPI Starter</h3>
  <p align="center">
    Deploy your FastAPI application seamlessly with CloudStation.
    <br />
    <a href="https://cloud-station.io">Visit CloudStation</a> ·
    <a href="https://documentation.cloud-station.io/s/ce6e8846-8aec-4337-a850-5188b6dc6d6e">Documentation</a> ·
    <a href="https://blog.cloud-station.io">Blog</a>
  </p>
</div>

## Overview

This repository showcases a simple FastAPI application for managing a collection of books. It can be effortlessly deployed on CloudStation, allowing you to focus on writing code without worrying about infrastructure.

## Getting Started

Follow these steps to get your FastAPI Books API running on CloudStation.

### Prerequisites

Ensure you have a CloudStation account. If you don't have one yet, sign up [here](https://www.cloud-station.io/signup).

### Quick Deploy

To deploy this application instantly, click the button below:

<p align="center">
  <a href="https://www.cloud-station.io/template-store/fastapi">
    <img src="https://server.cloud-station.io/cloudstation/Deploy_TO_CS.gif" alt="Deploy to CloudStation" width="250"">
  </a>
</p>

### Step-by-Step Deployment (For Customization)

If you want to customize the application before deployment, follow these steps:

1. **Fork the Repository:**
   Click the Fork button at the top-right of this repository to create your own copy.

2. **Deploy the Application:**
   - Navigate to the CloudStation [Dashboard](https://www.cloud-station.io/dashboard/project).
   - Create a new project.
   - Click on `Add New` and select **GitHub**.
   - In the repositories list, select the repository you just forked.
   - Choose a subdomain for your App i.e `fastapi-books`, and click **Deploy**.

#### Automatic Build with Nixpacks

CloudStation uses Nixpacks, a build system that automatically detects the programming language and framework of your application. For this FastAPI application, Nixpacks identifies it as a Python project and manages the entire build process seamlessly.

### Access Your Application

Once deployed, your application will be accessible at https://fastapi-books.cloud-station.app.

### Application Structure

This FastAPI Books API consists of the following files:

- `main.py`: The main entry point of the application, containing all API routes.
- `requirements.txt`: Lists the Python dependencies for the project.

### API Endpoints

- `GET /`: Welcome message
- `POST /books/`: Create a new book
- `GET /books/`: Get all books
- `GET /books/{book_id}`: Get a specific book
- `PUT /books/{book_id}`: Update a specific book
- `DELETE /books/{book_id}`: Delete a specific book

### Customization

To modify the application, make changes in your forked repository and push them. CloudStation will automatically rebuild and redeploy your application.

### Contributing

We welcome contributions to enhance this example application. Feel free to fork the repository, create a feature branch, and submit a pull request.

### Support

For support, visit our [Help Center](https://documentation.cloud-station.io/s/ce6e8846-8aec-4337-a850-5188b6dc6d6e) or reach out via [Slack](https://join.slack.com/t/cloudstationio/shared_invite/zt-20kougo40-Kd1196QzZ7bwUA0oPfZORA).

## Connect with Us

<p align="center">
  <a href="https://www.cloud-station.io/">Website</a> · 
  <a href="https://twitter.com/CloudStation_io">Twitter</a> · 
  <a href="https://join.slack.com/t/cloudstationio/shared_invite/zt-20kougo40-Kd1196QzZ7bwUA0oPfZORA">Slack</a>
</p>
