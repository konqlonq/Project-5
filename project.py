# List of imports for this project
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Brand, Item, User
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
app = Flask(__name__)

# Login_required decerator 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if login_session.get('credentials') is None:
            flash('Login is required')
            return redirect('/login')
        return f(*args,**kwargs)
    return decorated_function


# Configurations for G+ Login function
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

# Connect to Database and create database session
engine = create_engine('postgresql://catalog:password@localhost/brands')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

# G+ Login function
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

# Creates a new user if user does not exist yet in DB
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
        login_session['user_id'] = user_id   

    output = ''
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("Welcome %s!" % login_session['username'])
    print "done!"
    return output

    

# G+ logout function
@app.route('/gdisconnect')
def gdisconnect():
    if 'credentials' not in login_session:
        flash("You need to login first!")
        response = redirect('/login')
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session['credentials']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    del login_session['credentials']
    del login_session['gplus_id']
    del login_session['username']
    del login_session['email']
    del login_session['picture']
    response = redirect('/login')
    return response

# Functions to create new users
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(userId=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# API end-point for XML format
@app.route('/brands/<int:brand_id>/items/XML')
def brandsCatalogXML(brand_id):
    if 'username' not in login_session:
        response = make_response(json.dumps("You are not authorized, Login is required"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        brand = session.query(Brand).filter_by(id=brand_id).one()
        items = session.query(Item).filter_by(brand_id=brand_id).all()
    
    root = Element('html')
    for i in items:
        body = SubElement(root, 'body')
        ID = SubElement(body, 'ID')
        ID.text = str(i.id)
        name = SubElement(body, 'name')
        name.text = i.name
        price = SubElement(body, 'price')
        price.text = i.price
        description = SubElement(body, 'description')
        description.text = i.description
        image = SubElement(body, 'image')
        image.text = i.image
        print tostring(root)

    return app.response_class(tostring(root), mimetype='application/xml')

# API end-point for JSON format
@app.route('/brands/<int:brand_id>/items/JSON')
def brandsCatalogJSON(brand_id):
    if 'username' not in login_session:
        response = make_response(json.dumps("You are not authorized, Login is required"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:    
        brand = session.query(Brand).filter_by(id=brand_id).one()
        items = session.query(Item).filter_by(brand_id=brand_id).all()
        return jsonify(Items=[i.serialize for i in items])

# API end-point for JSON format(Individual Items)
@app.route('/brands/<int:brand_id>/items/<int:item_id>/JSON')
def ItemJSON(brand_id, item_id):
    if 'username' not in login_session:
        response = make_response(json.dumps("You are not authorized, Login is required"), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        items = session.query(Item).filter_by(id=item_id).one()
        return jsonify(Item=items.serialize)

# Renders the Home Page
@app.route('/')
@app.route('/brands/')
def index():
    items = session.query(Item).all()
    return render_template('index.html',items=items)

# Renders the profile page
@app.route('/profile/')
@login_required
def profile():
    items = session.query(Item).filter_by(user_id=login_session['username'])
    user = session.query(User).get(login_session['user_id'])
    return render_template('profile.html', items=items, user=user)

# Renders the catalog Page
@app.route('/brands/<int:brand_id>/items')
def brandsCatalog(brand_id):
    brand = session.query(Brand).filter_by(id=brand_id).one()
    items = session.query(Item).filter_by(brand_id=brand.id)
    return render_template('items.html', brand=brand, items=items, brand_id=brand_id)

# Renders the New Item page
@app.route('/brands/new', methods=['GET', 'POST'])
@login_required
def newItem():
    if request.method == 'POST':
        newItem = Item(name= request.form['name'], brand_id=request.form['brand'], 
        price=request.form['price'], description=request.form['description'], 
        image=request.form['image'], user_id=login_session['username'])
        session.add(newItem)
        session.commit()
        flash("New menu Item created!")
        return redirect('/profile')
    else:
        return render_template('newItem.html')

# Renders the Edit Item page
@app.route('/brands/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def editItem(item_id):
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if editedItem.user_id != login_session['username']:
        flash("You are not authorized to edit this item")
        return redirect('profile')
    else:
        if request.method == 'POST':
            if request.form['name']:
                editedItem.name = request.form['name']
            if request.form['description']:
                editedItem.description = request.form['description']
            if request.form['price']:
                editedItem.price = request.form['price']
            session.add(editedItem)
            session.commit()
            flash("Item has been edited!")
            return redirect('/profile')
        else:
            return render_template(
                'editItem.html',item_id=item_id, item=editedItem)

# Renders the delete Item page
@app.route('/brands/<int:item_id>/delete', methods=['GET', 'POST'])
@login_required
def deleteItem(item_id):
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if itemToDelete.user_id != login_session['username']:
        flash("You are not authorized to delete this item")
        return redirect('profile')
    else:
        if request.method == 'POST':
            session.delete(itemToDelete)
            session.commit()
            flash("Item has been deleted!")
            return redirect('/profile')
        else:
            return render_template('deleteItem.html', item=itemToDelete)

# Set local host settings
if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=8080)