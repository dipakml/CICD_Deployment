## CI/CD Pipeline- Prediction of Concrete Compressive Strength Using Machine Learning 

### This project demonstrates the application of the MlOps principles & implement CI/CD pipeline with github actions, dockerizing the app & deploy it on Azure cloud for seamless integration & deployment

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/concrete.png" width=800>

### Table of Content
  * [Overview](#overview)
  * [Dataset Information](#dataset-information)
  * [Attribute Information](#attribute-information)
  * [Motivation](#motivation)
  * [Demo](#demo)
  * [Steps in project execution](#steps-in-project-execution)
  * [Technical Aspect](#technical-aspect)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Note](#note)



### Overview 
The compressive strength of the concrete is one of the most common performance measures which determines the quality of Concrete. This is generally determined by a standard crushing test on a concrete cylinder. This requires engineers to build small concrete cylinders with different combinations of raw materials and test these cylinders for strength variations with a change in each raw material. The recommended wait time for testing the cylinder is 28 days to ensure correct results. This consumes a lot of time and requires a lot of labour to prepare different prototypes and test them. Also, this method is prone to human error and one small mistake can cause the wait time to drastically increase.
Machine learning techniques can be used to prepare a mathematical model which can predict the compressive strength of concrete without performing the physical tests. This type of digital simulation will save lot of time, money & efforts which is required for physical testing. 

In this project, let's apply machine learning techniques and develop a web based application to predict the compressive strength of concrete based on its composition.


###  Dataset Information
The actual concrete compressive strength (MPa) for a given mixture under a specific age (days) was determined from laboratory.
The data has 8 quantitative input variables, and 1 quantitative output variable, and 1030 instances (observations).

Original Owner and Donor
Prof. I-Cheng Yeh
Department of Information Management
Chung-Hua University,
Hsin Chu, Taiwan 30067, R.O.C.
e-mail:icyeh@chu.edu.tw
TEL:886-3-5186511



### Attribute Information

Name -- Data Type -- Measurement -- Description

Cement (component 1) -- quantitative -- kg in a m3 mixture -- Input Variable

Blast Furnace Slag (component 2) -- quantitative -- kg in a m3 mixture -- Input Variable

Fly Ash (component 3) -- quantitative -- kg in a m3 mixture -- Input Variable

Water (component 4) -- quantitative -- kg in a m3 mixture -- Input Variable

Superplasticizer (component 5) -- quantitative -- kg in a m3 mixture -- Input Variable

Coarse Aggregate (component 6) -- quantitative -- kg in a m3 mixture -- Input Variable

Fine Aggregate (component 7) -- quantitative -- kg in a m3 mixture -- Input Variable

Age(component 8) -- quantitative -- Day (1~365) -- Input Variable

Concrete compressive strength -- quantitative -- MPa -- Output Variable


### Motivation
The motivation was to use machine learning experiments to develop a web based application to predict the compressive strength of concrete based on its composition. This effort will save physical testing & give the results on a single click.
This project demonstrates the application of the MlOps principles & implement CI/CD pipeline with github actions, dockerizing the app & deploy it on Azure cloud for seamless integration & deployment.



### Demo
Azure deployment Web application Snapshot:

<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/cicd_app.png" width=600>


### Steps in project execution

- Data gathering 
- Descriptive Analysis 
- Data Visualizations 
- Data Preprocessing 
- Data Modelling 
- Model Evaluation 
- Creating a flask web app
- Create a github repositiory & push the relevent files
- Install Docker desktop on local machine
- Log in to Azure Portal & create container registry
- Get the username(registry name) & password(from access keys), here username is cicd121
- Build the Docker image of the Source Code by using following in command prompt:
  docker login cicd121.azurecr.io
  docker build -t cicd121.azurecr.io/cicd121:latest
- Push the Docker image to Container Registry:
  docker push cicd121.azurecr.io/cicd121:latest
- Launch the Web App Server in Azure
- Pull the Docker image from the container registry to Web App server and run
    

### Technical Aspect 

- Training a machine learning model using scikit-learn. Multiple algorithms are used to come up with best performing algorithm.
- Building and hosting a flask web app on Azure cloud. 
- A user has to input key attributes as mentioned above.
- Once it gets all the fields information , the prediction is displayed. 
### Technologies Used  
![](https://forthebadge.com/images/badges/made-with-python.svg) 
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/streamlit.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/heroku.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/numpy.png" width=160>
<img target="_blank" src="https://github.com/dipakml/Prediction-of-Concrete-Compressive-Strength/blob/master/Logo_Images/pandas.jpeg" width=160>

### Installation 
- Clone this repository and unzip it.
- After downloading, cd into the working directory.
- Begin a new virtual environment with Python and activate it.
- Install the required packages using pip install -r requirements.txt
- Execute the command: python app.py


### Note:
- Webapp can handle concurrency upto some extent but can be scaled.









