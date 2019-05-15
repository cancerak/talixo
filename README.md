# Talixo
Talixo recruitment task - python/django API
## database models - structure
Every database model has pk attribute (django builtin). Additional field are listed below.
### Car
    car_model: foreign key
    number_plate: unique, max 10 characters
    year: production year
### Car model
    category: economy, business, first
    engine: normal, hybrid, electric
    name: car model name
    passengers: passengers limit
    manufacturer: foreign key
### Manufacturer
	name: car manufacturer name
## API features
### List methods
	uri: /cars_api/car/
#### POST
	creates new car or prints an error if given value is not valid
#### GET
	gets cars list
### Detail methods
	uri: /cars_api/car/<pk>/
#### GET
	gets car details by its primary key
#### DELETE
	deletes car by its primary key
#### PUT
	updates car by its primary key
### Example of Car object POST in json
	{
		"car_model": {
			"category": "business",
			"engine": "electric",
			"manufacturer": {
				"name": "Mazda"
			},
			"name": "CX-3",
			"passengers": 5
		},
		"number_plate": "KR 00227",
		"year": 2018
	}
