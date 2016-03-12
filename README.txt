Catalog version 1.0 27/02/2016

FILES
-----
- database_setup.py - sets up the database.
- populate_db.py - populates the database with example data.
- project.py - mainframe of the project.
- client_secrets.json - information for G+ Oauth2 API
- static
	-mystyles.css - Aesthetic aspect of the web-app.
-Templates
	-login.html - login page
	-index.html - home page
	-profile.html - page where user can Create, Update and Delete their posts.
	-EditItem.html - Edit page
	-DeleteItem.html - Delete page
	-Items.html - Catalog page for viewing
	-NewItem.html - Creating new items in catalog


XML and JSON exports API end-points (For developers)
-----------------------------------------
-Brand 1 = Apple
	-Brand 2 = Samsung
	-Brand 3 = LG
	-Brand 4 = Sony
	-Brand 5 = Huawei

-To access public data in JSON format:
	-Visit “http://localhost:8080/brands/(brand id goes here, 1-5)/items/JSON

-To access public data in XML format:
	-Vist “http://localhost:8080/brands/(brand id goes here, 1-5)/items/XML


GENERAL USAGE NOTES
---------------------
-This project is tasked to build a catalog web-app. I have chosen to do a catalog page providing information about the latest mobile phones. Site map looks a bit like this:

Brands:
	1)Apple
		- Model 1
		- Model 2
		- Model 3
		- etc.
	2)Samsung
	3)LG
	4)Sony
	5)Huawei

-With this web-app, users must have a G+ account to begin with. Once logged in, they can view the mobile phones available in the market in the catalog page. They may also choose to contribute to the catalog by creating a post of a mobile phone of their choice and also to edit or delete it later if they wish to. However, they may only edit and delete posts that they created themselves.

-Please note:
1)This app is set to run on port 8080 @ localhost:8080.
2)This app requires a few modules to be installed before you can run it on your local host which include
	-flask
	-elementtree
	-sqlalchemy
	-oauth2client
	-httplib2
	-json
	-requests

- To Run the Catalog Web-app:
	1) Launch Terminal
	2) Type “cd fullstack/vagrant” (or where else your working directory is.)
	3) Type “vagrant up” to boot your VM.
	4) Type “vagrant ssh” to login.
	5) Type “cd vagrant/catalog” (or where else your working directory is.)
	6) Type “python database_setup.py” to set up the DB.
	7) Type “python populate_db.py to populate the DB with example data.
	8) Type “python project.py to start the server on port 8080 of your local host.
	9) Open your web browser and enter “http://localhost:8080/brands/“ to start.
	10) Login using your G+ account.
	11) Logout of the Web-app after you are done viewing.
=======================

Author can be reached at:

Voice: +65 97582540
E-mail: konqlonq@gmail.com

