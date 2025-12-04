# Property Sales and Rental Management (PSRM)

![Project Homepage](https://lh3.googleusercontent.com/pw/AP1GczMRaGjPid7gurARnqIrh1I281jOIESnlRR5SuyG5cWKM8GJ9oGQjGuNefKA6c_Y0DtdrBOgMnNsCHE7qO6lY_E0GUvDsVew5AB5ZX7jT8RLI12efGh7vQrCAFVf2L5sz1y-Ttp8Pd0FG2SVVIMcbUFCjw=w1815-h1021-s-no)

## Overview

PSRM is a comprehensive web application built with Django designed to bridge the gap between property owners and prospective tenants. It facilitates a seamless experience for listing, searching, and managing rental or sale properties. The platform includes distinct workflows for owners, tenants, and administrators, ensuring a tailored experience for each user type.

## Features

### 🏠 For Tenants
- **Property Discovery**: Browse and search for properties based on location, price, and description.
- **Advanced Filtering**: Sort properties by price (low-to-high or high-to-low).
- **Direct Communication**: Contact property owners directly via email or the built-in messaging system.
- **Profile Management**: Manage personal details and contact information.
- **AI Assistant**: Integrated chatbot powered by Google Gemini to answer queries.

### 🔑 For Owners
- **Property Management**: Upload, edit, and delete property listings with multiple images and detailed descriptions.
- **Contract Generation**: Generate professional rental contracts in PDF format.
- **Tenant Interaction**: Receive inquiries and reply to tenant messages directly from the dashboard.
- **Occupancy Tracking**: Manage the availability status of listed properties.

### 🛠️ General Features
- **User Authentication**: Secure registration and login for all user roles.
- **Responsive Design**: User-friendly interface accessible on various devices.
- **Admin Dashboard**: Centralized control for managing users and platform content.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Database**: SQLite (Default)
- **AI Integration**: Google Gemini API
- **PDF Generation**: xhtml2pdf

## Project Structure

The project is organized into modular applications:

- **`psrm`**: Main project configuration (settings, URLs).
- **`tenentapp`**: Handles tenant-facing features (homepage, search, profile, messaging).
- **`ownerapp`**: Handles owner-facing features (property management, contracts, dashboard).
- **`adminapp`**: Manages administrative tasks and user roles.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd PS6/PS6
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, ensure you have `django`, `google-generativeai`, `xhtml2pdf`, and `pillow` installed)*

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the application:**
    Open your browser and navigate to `http://127.0.0.1:8000/`

## Configuration

- **Gemini API Key**: Update the `API_KEY` in `tenentapp/views.py` and `ownerapp/views.py` with your own Google Gemini API key.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
   