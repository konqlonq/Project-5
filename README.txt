Linux Server Configuration version 1.0 16/03/2016

FILES
-----
- database_setup.py - sets up the database.
- populate_db.py - populates the database with example data.
- catalog.py - mainframe of the project.
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
	-Visit “http://ec2-52-37-36-221.us-west-2.compute.amazonaws.com/brands/(brand id goes here, 1-5)/items/JSON

-To access public data in XML format:
	-Vist “http://ec2-52-37-36-221.us-west-2.compute.amazonaws.com/brands/(brand id goes here, 1-5)/items/XML


References
——————————

askubuntu.com
stackoverflow.com
Digitalocean.com


GENERAL USAGE NOTES
---------------------

Terminal (to shh)
—————————————————
ssh -i ~/.ssh/udacity_key.rsa root@52.37.36.221 -p 2200


IP Address
——————————
52.37.36.221


SSH port
————————
Port 2200


Udacity Key
——————————-
MIIEpAIBAAKCAQEArNUkG//DjUQ+rHrPIIOtTPlrSC6dJjJyRlEpPIANlaSdRDOX
nyXjJqXfInTdvj/PzswIVG+LJHTg5WlYJ4F1PLQ6x71oI0eS+ZGzbRCA5vUhodNS
DciTSEFF1POdI1D1tmkpIuGPgBtzSjJtKamDI60wGE4Vt/vsQijwjBKMwtBOWSjI
GM2jg/vRpD/TpV3fSgzI5MIWuMf2jQJVOa+usQPDFxWJcrtCmR3JY9gycnxWN+/i
8FvoyzSHd6XwMEBGTEt/m4FX0ocHa6+B7zFAfZlg3vac/VT/fQ/8IVKaOKd0glb5
k7TQqa1z/NBkh8VvjwpJCYxowj1iySUpfCWGzwIDAQABAoIBAQCsPeozoSwgwA95
0xZTAAeY+8UH9bSVmZa7Ly1aZv+iz6APlR8Y8ygynwIGE9PdQzj1je8LPvK7TWPI
HblF/cV5zt/5qXB8IFuALs1S9yyPf2KaJMDUjb0COFLAzFwhExEdTiY55fMeJ705
B5I1AAN6baHNxxvr9Lvan3RDFEWF63D/hPp4arxkRrrIUPgbBEL/F6G+XmRQUUSi
2vJcs4XKDTCPX6PPXDgbd5dFJAkjSKx/YFOpgo/u5E+H0GtzrJkjcw34VsFZANgJ
P3BNVnDvcczuCteA7NRX1a9F/McnWHU9RyadJLSsrnBlE/0A8Kunz3BPn1NIP+Wu
KdD785pBAoGBAN8DtcvczP+PYn3d5rUDJVrn/qtBUn9xQUwjwkNeM3iyt/QwjsnL
iGiK9IpN4aWvMZBRQtJJwfcUO2jB+L7Fj5N+fZ8D6e5/hpmvqesBfzSJh6wWvE9h
uHB0OkMdDHB0UNXSwLh+QHzhjhIb6Nh/IaHSA4eenu29Z6x1OPFeTUvhAoGBAMZl
U9cdRapGFzFbUiMhJrfdjA+DIVBpFVC3/xUHmcE9BHckhIyNr5lBBttkY49xTotn
q5tXk+H90pe59/tMdE9jJ8h9M7LHOntDt1EyLPS+97bEHPJ9ePjERfiwEMIa6mza
cTHo8TvE0WPdHd1EeUATJK1cZS9jYOOiVAVj46ivAoGAXc3DtAIlwADhnqutlMnD
9p7KgeIx/yT2ID6SQZ/n6obR1UZvaPXRZJe+EEZ9+SDdqiRkBOu9SF4cNw4PwL58
i7+Su0X8KbM+PHqk8BJrHQAULxBJGOKzn6ljsEMRrmNedPH22iNQoLaG+Zr/r8CZ
tuUNUwgnNTyL1QBheTT/MkECgYAWq8ON5GFumL3TvQzAyOwEvMNhjmmDJ87wv2Xd
wFWYmGFnP/wJl7NGPwEKlwktfhQsp/cbNEHI5FlpTy4AQHdWDw2fwnbi6hNLvKw5
EhPDEAN8liJ8r0vgmYUpau0vUSYStE+VFXpjixUmZUEhZM66PLXHPbSuWpvax1T0
nLqKLwKBgQDPk4k8eCjlz4LR5y1Hpv+0AkAeO6rzGBSnm6XFiEhd7jyGdMRm51st
BR6azeVqyIkV6qAtEZbIuXMjnTEw11tHRQbY0w5nj7bpcNqewOjzlcJQR8jrEdww
ymWGYBSTd7AxqM4C0WrTIAFDjtUNi9enjntDxSBVBUm2y7cNbJWL9w==


Summary of my work
——————————————————

1) Created a new user, grader 
	- sudo adduser grader

2) Gave grader sudo permission
	- sudo nano /etc/sudoers.d/grader
	- grader ADD=(ALL) NOPASSWD:ALL

3) Authorized key to grader
	- ls /home/grader
	- mkdir .ssh
	- cp /root/.ssh/authorized_keys /home/grader/.ssh/
	- chmod 700 .ssh
	- chmod 644 .ssh/authorized_keys
	- chown -R grader .ssh
	- chgrp -R grader .ssh

4) Changed SSH port 20 to 2200
	- nano /etc/ssh/sshd_config

5) Updated packages
	- sudo apt-get update
	- sudo apt-get upgrade

6) Configure the Fire Wall
	- sudo ufw default deny incoming
	- sudo ufw default allow outgoing
	- sudo ufw allow 2200/tcp
	- sudo ufw allow 80/tcp
	- sudo ufw allow 123/tcp
	- sudo ufw enable
	- sudo ufw status
			 
7) Protect SSH with fail2ban
	- sudo apt-get install fail2ban
	- sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
	- sudo nano /etc/fail2ban/jail.local
	- port 2200

8) Configure time zone
	- sudo dpkg-reconfigure tzdata

9) Install Apache to serve Python mod_wsgi
	- sudo apt-get install apache2
	- sudo aptitude install libapache2-mod-wsgi
	- sudo apt-get install libapache2-mod-wsgi python-dev

10) Install Postgresql
	- sudo apt-get install postgresql

11) Install Git
	- sudo apt-get install git

12) Clone project source repository
	- cd /var/www
	- sudo git clone https://github.com/konqlonq/Project-5.git
	- mv Project-5 catalog

13) Install pip and Python packages
	- sudo apt-get install python-pip
	- sudo pip install flask
	- sudo pip install httplib2
	- sudo pip install sqlalchemy
	- sudo pip install requests
	- sudo pip install oauth2client
	- sudo apt-get install python-psycopg2

14) Create Database USER with psql
	- sudo su - postgres
	- psql
	- CREATE USER catalog WITH PASSWORD 'secure password';
	- GRANT SELECT, INSERT, DELETE, UPDATE ON ALL TABLES IN SCHEMA public TO catalog;

15) Configure WSGI
	- sudo cp /var/www/catalog/catalog/catalog.conf /etc/apache2/sites-available
	- sudo mv /var/www/catalog/catalog/catalog.wsgi /var/www/catalog
	- sudo a2ensite catalog
	- sudo service apache2 restart

16) Create Database
	- python /var/www/catalog/catalog/database_setup.py 
	- python /var/www/catalog/catalog/populate_db.py

17) Configure G+ login
	- Add http://52.88.150.147 to Authorized JavaScript origins.
	- Add http://ec2-52-37-36-221.us-west-2.compute.amazonaws.com to Authorized JavaScript origins.
	- Added http://ec2-52-37-36-221.us-west-2.compute.amazonaws.com/0auth2callback
	- Re-download client_secrets.json and then up to server.

18) Restrict git access
	- cd /var/www/catalog
	- sudo nano .htaccess
	- RedirectMatch 404 /\.git

=======================

Author can be reached at:

Voice: +65 97582540
E-mail: konqlonq@gmail.com

