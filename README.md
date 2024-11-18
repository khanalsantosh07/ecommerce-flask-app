Assignment 02: E-Commerce Flask Application

Objective: In this assignment, you will create a Flask web application with two routes:

- a homepage (/) and,
- a products page (/products).

The application will connect to a MongoDB Atlas database to fetch and display product
information, which includes a product’s name, tag, price, and image path (local to the
Flask app). You will use Jinja2 templates to create dynamic content and Bootstrap for
styling the product page

Images:
<img src= "static/images/Screenshot 2024-10-12 at 7.59.17 PM.png">
<img src= "static/images/Screenshot 2024-10-12 at 7.59.37 PM.png">


Assignment 4:

# ecommerce-flask-app
## Flask Application with MongoDB and Unit Tests

### Tests
1. **Route Test**: Verifies invalid HTTP methods return correct status codes.
2. **Database Read Operation**: Ensures MongoDB is accessible and responding.
3. **Database Write Operation**: Checks that documents can be inserted and queried successfully.

### CI/CD Integration
- The GitHub Actions workflow automatically runs all unit tests whenever code is pushed to the repository.
