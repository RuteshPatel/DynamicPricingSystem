# Dynamic Pricing and Discount System

## Project Description
This project implements a dynamic pricing and discount system using Django and Django Rest Framework (DRF). It leverages class inheritance to manage different types of products and discounts effectively. The system includes:

- **Product Management**: Base product class with derived classes for seasonal and bulk products, each implementing their unique pricing logic.
- **Discount Management**: A base discount class with derived classes for percentage and fixed amount discounts, applying specific discount logic.
- **Order Management**: An order class that calculates the total price by utilizing product and discount classes, capable of handling bulk and seasonal pricing.

## Git Cloning
To clone the repository, run the following command in your terminal:
```bash
git clone https://github.com/RuteshPatel/DynamicPricingSystem.git
cd DynamicPricingSystem
```

## Virtual Environment Creation and Activation
### It is recommended to create a virtual environment for the project. You can do this using the following commands:

- For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
- For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

## Installing Dependencies
### Once the virtual environment is activated, install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Database Migration
### Before running the application, ensure that the database is set up correctly. Run the following command to apply migrations:

```bash
python manage.py migrate
```

## Running the Server
### You can start the development server with the following command:

```bash
python manage.py runserver
```
### After executing this command, you should see output indicating that the server is running, typically accessible at http://127.0.0.1:8000/.

### API Endpoints
 - **Products**: Manage products and view product-related information.
    ```bash
    [GET]  http://127.0.0.1:8000/api/products/
    [POST] http://127.0.0.1:8000/api/products/
    
    [GET]  http://127.0.0.1:8000/api/products/seasonal/
    [POST] http://127.0.0.1:8000/api/products/seasonal/
   
    [GET]  http://127.0.0.1:8000/api/products/bulk/
    [POST] http://127.0.0.1:8000/api/products/bulk/
   ```
 - **Discounts**: Manage discounts applicable to products.
    ```bash 
    [GET]  http://127.0.0.1:8000/api/discounts/
    [POST] http://127.0.0.1:8000/api/discounts/
   
    [GET]  http://127.0.0.1:8000/api/discounts/percentage/
    [POST] http://127.0.0.1:8000/api/discounts/percentage/
   
    [GET]  http://127.0.0.1:8000/api/discounts/fixed/
    [POST] http://127.0.0.1:8000/api/discounts/fixed/
   ```
 - **Orders**: Create and manage orders, applying discounts dynamically.
```bash
    [GET] http://127.0.0.1:8000/api/orders/
    [POST] http://127.0.0.1:8000/api/orders/
   ```

### POSTMAN Collections
### https://documenter.getpostman.com/view/17096834/2sAXxY5Uir