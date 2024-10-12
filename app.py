# Santosh Khanal
# C0921949
# 12 Oct, 2024

from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient(os.getenv('MONGODB_URI'))
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