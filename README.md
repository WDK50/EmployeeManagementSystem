🧑‍💼 Employee Management System (Django CRUD)

📘 Overview
The Employee Management System is a web-based application built with Python (Django Framework) that allows users to manage employee records efficiently.  
It supports CRUD (Create, Read, Update, Delete) operations, advanced filtering, searching, and CSV export.  
Each logged-in user can manage their own employees, while the superuser has access to all records.

---

🎯 Purpose
The purpose of this project is to demonstrate:
- Practical understanding of Django’s MVC (Model-View-Template) architecture.  
- How to implement user authentication and role-based data access (user vs. superuser).  
- The integration of features like pagination, search filters, email notifications, and file uploads in a professional Django app.


🧩 Key Features
- 🔐 User Authentication – Custom login and signup system using Django’s built-in auth.
- 👥 Role-Based Access –  
  - Superusers: Can view, edit, and delete all employee records.  
  - Normal users: Can only manage employees they created.  
- 📤 CSV Export – Download all employee records in CSV format.  
- 📨 Email Integration – Send welcome emails to new employees.  
- 🔎 Search & Filter – Search employees by name, email, contact, status, or gender.  
- 🧾 Pagination – Paginated employee list view for better navigation.  
- 📸 Profile Upload – Upload and display employee profile images.  
- 🕓 Timestamping – Tracks when each record was created.

---

 🧠 Concepts Used
 1. Django Core Concepts
- Models, Views, Templates (MVT pattern)
- ModelForm and form validation
- URL routing and dynamic URL parameters
- Django ORM with filters and Q objects

 2. Authentication & Authorization
- Custom login/signup forms
- `login_required` decorator
- User-based filtering (`created_by` field)
- Superuser privileges

 3. Frontend Integration
- Bootstrap 5 UI for responsive design
- Dynamic search with JavaScript and AJAX

 4. Additional Django Features
- `Paginator` for pagination
- `messages` framework for user feedback
- `send_mail` for email notifications
- `FileField` for image uploads
- REST API support via Django REST Framework
