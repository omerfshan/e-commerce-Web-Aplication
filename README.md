# Product-management-Aplication

## Overview
This project is a fully functional e-commerce website built using the Django framework. It includes essential features such as product browsing, user authentication,product CRUD
---

## Features

### User Functionality:
- **User Registration and Authentication**: 
  - Sign-up, login, logout functionality.
  - Secure password management with Django's authentication system.


### Product Management:
- **Product Browsing**:
  - Browse products by categories.
  - Search for products by name or keywords.
- **Product Details**:
  - View detailed product descriptions, prices, and availability.

### Admin Functionality:
- **Product Management**:
  - Add, edit, or delete products.
  - Manage categories and inventory.
- **User Management**:
  - Manage user accounts.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/django-ecommerce-site.git
   cd django-ecommerce-site
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)


---

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with descriptive messages.
4. Push your changes and create a Pull Request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements
- Django Documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
