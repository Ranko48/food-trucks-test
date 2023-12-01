# Food Trucks Finder

<h2>
	Thank you for visiting my project.
	The main idea of this project is to find the nearest food trucks around you or anyplace.
	The project is built by Django + React + Sqlite3.
</h2>


## Back End

<h4>How to run this project (On Linux)</h4>

- I used python 3.10.12 and Django 4.2.7 and sqlite for database handling.
- I prefer to use `venv` to run this project.
- Here is the list of commands to set environment.
	- To setup venv: `python3 -m venv venv`
	- To active venv: `source venv/bin/activate`
	- To install dependency packages: `pip install -r requirements.txt`
- Migration database using sqlite3
	- `python3 manage.py makemigrations`
	- if you use Ubuntu 22.04, please run this command <b>InitSpatialMetaDataFull(1)</b>  to fix error: `python3 manage.py shell -c "import django;django.db.connection.cursor().execute('SELECT InitSpatialMetaData(1);')";`
	- `python3 manage.py migrate --run-syncdb`
	- To populate database from CSV file to run this command: `python3 manage.py populate_foodtrucks`
- Run project
	- `python3 manage.py runserver`
- Here are some commands to easy to get results.
	- You can get the nearest food trucks of your current location `python3 manage.py find_my_trucks`
	- You can get the nearest food trucks of any location `python3 manage.py find_food_trucks`

<h4>
	Test API
</h4>

- You can test API with PostMan and Web Browser
- The form of API link is this. (http://localhost:8000/api/nearby-food-trucks/?latitude={latitude}&longitude={longitude}) 
- And here is example link to test API (http://localhost:8000/api/nearby-food-trucks/?latitude=37.794331003246846&longitude=-122.39581105302317)

## Front End

<h4>How does this project work?</h4>

  - The main idea of this project is to find the nearest food trucks at least 5.
  - At first, the center of the Google Map is your current location.
  - You can drag Marker to anyplace or input number to update the location of Marker.
  - You can click the <b>Find</b> button to search the nearest food trucks.
  - You can click the Markers which present the nearest food trucks to see the information of food trucks.

<h4>How to run this project?</h4>

- `npm install`
- `npm start`

