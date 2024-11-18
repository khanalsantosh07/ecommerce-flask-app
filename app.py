# Santosh Khanal
# C0921949
# 18 Nov, 2024

from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Access MongoDB credentials using environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

# MongoDB URI template using the environment variables
MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.v7xn9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MongoDB Atlas connection using the URI
client = MongoClient(MONGODB_URI)
db = client.get_database('shop_db')
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = list(products_collection.find())
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)