# 🛒 Django E-Commerce Web Application
 
A full-featured E-Commerce web application built with **Django**, **MySQL**, and **Bootstrap 5**. This project covers the complete online shopping experience — from product browsing to order placement.
 
---
 
## 📌 Project Overview
 
This is a fully functional E-Commerce platform developed using the Django web framework. It includes product management, user authentication, a shopping cart system, and order management — all backed by a MySQL database.
 
---
 
## ✨ Features
 
### 🛍️ Customer Features
- User Registration & Login (Authentication)
- Browse Products by Category
- Product Detail Page
- Add to Cart / Remove from Cart
- Place Orders
- Order History
 
### 🔧 Admin Features
- Django Admin Panel
- Add / Edit / Delete Products
- Manage Categories
- View & Manage Orders
- User Management
 
---
 
## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| **Backend** | Python 3.x, Django |
| **Database** | MySQL |
| **ORM** | Django ORM |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript |
| **Authentication** | Django Auth System |
| **Tools** | Git, GitHub, VS Code, Virtual Environment |
 
---
 
## 📁 Project Structure
 
```
 
## ⚙️ Installation & Setup
 
### 1. Clone the Repository
```bash
git clone https://github.com/6355492210/django-ecommerce.git
cd django-ecommerce
```
 
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```
 
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
 
### 4. Configure MySQL Database
In `settings.py`, update:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
 
### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
 
### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
 
### 7. Run Development Server
```bash
python manage.py runserver
```
 
Visit: `http://127.0.0.1:8000/`
Admin Panel: `http://127.0.0.1:8000/admin/`
 
---
 
## 🧠 What This Project Demonstrates
 
- Django MVT Architecture (Models, Views, Templates)
- Django ORM — complex queries, relationships
- MySQL Database integration
- User Authentication & Session Management
- Django Admin customization
- Responsive UI with Bootstrap 5
- URL routing & Template inheritance
- Static files management
 
---
 
## 📈 Future Improvements
 
- [ ] Django REST Framework (DRF) API integration
- [ ] Payment Gateway (Razorpay / Stripe)
- [ ] Product Search & Filter
- [ ] Product Reviews & Ratings
- [ ] Email Notifications
- [ ] Docker Deployment
 
---
 
## 👨‍💻 Author
 
**Vivek Vaghela**
- GitHub: [@6355492210](https://github.com/6355492210)
- LinkedIn: [linkedin.com/in/vaghelavivekm](https://www.linkedin.com/in/vaghelavivekm)
- Location: Rajkot, Gujarat
 
This project is open source and available under the [MIT License](LICENSE).
