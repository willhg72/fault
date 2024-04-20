
# Simple Python REST API with Docker - EXAMPLE Project

## A fully functional EXAMPLE Project written in Python using FastAPI, that receive a point as latitude and Longitude parameters, and return the 10 more tectonic faults close that point.

I've developed a REST API hosted on GitHub that serves as a tool for accessing information about Colombian tectonic faults based on latitude and longitude coordinates provided by the user. Leveraging the FastAPI framework, this API efficiently retrieves data and returns the ten nearest tectonic faults. Its design prioritizes scalability, ensuring seamless performance as the user base grows. This project aims to provide a reliable and accessible resource for geospatial analysis, contributing to a deeper understanding of seismic activity


## Installation

* Create a local folder:
```bash
  md [<Project local folder>]
```

* Change to the new local folder:
```bash
  cd [<Project local folder>]
```

* Activate the VSCode editor:
```bash
  code .
```

* Activate a terminal inside VSCode.

* Create a virtual environment:
```bash
  python3 -m venv venv
```

* Install my-project with pip3:

```bash
  pip3 install -r requirements.txt
```
 Create Docker image:
  ```bash
  docker build -t fastapi-tectonic-fault .
```  

Docker container activation:
  ```bash
  docker run -d --name fastapi-tectonic-fault-container -p 80:80 fastapi-tectonic-fault 
``` 
* "If everything is okay, you will be able to access the Swagger documentation by navigating to the following URL:
  ```bash
  http://localhost/docs. 
  ``` 
## API Reference

#### Get Tectonic faults:

```http
  GET [<server address>]/distances?coordenates_lat=[Valid latitude]&coordenates_long=[valid longitude]
```
* Example API on Local Server:
```http
   http://localhost/distances?coordenates_lat=7.928234263111178&coordenates_long=-72.50830172354611
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `latitude` | `float` | **Required**.  valid range(>-90 and < 90)|
| `longitude` | `float` | **Required**. valid range(>-180 and < 180)  |


#### coordenates(latitude, longitude)

### It takes latitude and longitude coordinates and returns the distance, in kilometers, to the 10 closest tectonic faults.

```http
{
  "Falla de Las Mercedes": 39.45,
  "Falla de Pamplona": 56.21,
  "Falla del Trapiche": 58.63,
  "Falla de Morro Negro": 71.69,
  "Falla de Labateca": 74.44,
  "Falla de Tincalá": 76.42,
  "Falla del Ají": 78.44,
  "Falla de Quebrada Grande": 81.11,
  "Falla de Socotá": 84.26,
  "Falla de San Lorenzo": 86.02
}
```

## Authors

- [@willhg72](https://www.github.com/willhg72)


## How to tweak this project for your own uses

Since this is an example project, I recommend you to clone a rename this project to use your own porpouses. It's a good starter boilerplate.

## Find a bug?

If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with fix, reference the issue you created! 

## Known issues (work in progress)

* This example project is till ongoing. the creation of the Docker has not been completed.


## Like this project?

This is a part of my journey as a Python developer. If you're feeling generous, you could consider doing one or more of the following:

* You could buy me a coffee https://buymeacoffee.com/william.hernandez .
* You could recommend me to your boss.
* You could hire me.
* You could give me advice.
  