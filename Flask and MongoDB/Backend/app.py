from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__, template_folder='../Frontend/Templates')

# Replace with your MongoDB Atlas URI
client = MongoClient("mongodb+srv://dummy:1234@cluster0.cxmny1h.mongodb.net/?appName=Cluster0")   
db = client['mydb']
collection = db['users']

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/', methods=['GET', 'POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)