# Predicting Online Shoppers Purchasing Intention 
----------------------
## Problem Description     
E-commerce marketing and sales departments goal is to trigger visitors to purchase. For example, offering promotion sales, packages, rewards etc. and these are very useful. What if the departments knew each individual visitor intention, The offers would be personalized and tailored to each one.        

----------------------
## Dataset    
Online shoppers activity data is from UCI Machine Learning Repository. The dataset was formed so that each session would belong to a different user in a 1-year period to avoid any tendency to a specific campaign, special day, user profile, or period.       
The dataset consists of:       
- feature vectors belonging to 12,330 sessions. 
- 10 numerical and 8 categorical attributes. 
The 'Revenue' attribute can be used as the class label. (more about features inside the notebook)    

        
### Numerical Features
|Feature name	|Feature description	|Min. value	|Max. value	|SD|
|---|---|---|---|---|
|Administrative|	Number of pages visited by the visitor about account management	|0|	27|	3.32|
|Administrative duration|	Total amount of time (in seconds) spent by the visitor on account management related pages|	0|	3398|	176.70|
|Informational|	Number of pages visited by the visitor about Web site, communication and address information of the shopping site	|0	|24	|1.26|
|Informational duration|	Total amount of time (in seconds) spent by the visitor on informational pages|	0|	2549|	140.64|
|Product related|	Number of pages visited by visitor about product related pages|	0|	705|	44.45|
|Product related duration|	Total amount of time (in seconds) spent by the visitor on product related pages	|0	|63,973|	1912.25|
|Bounce rate|	Average bounce rate value of the pages visited by the visitor	|0	|0.2	|0.04|
|Exit rate|	Average exit rate value of the pages visited by the visitor	|0	|0.2	|0.05|
|Page value|	Average page value of the pages visited by the visitor	|0	|361	|18.55|
|Special day	|Closeness of the site visiting time to a special day	|0	|1.0	|0.19|
     
-------------------------     
              
### Categorical Features
|Feature name	|Feature description|	Number of categorical values|
|---|---|---|
|OperatingSystems	|Operating system of the visitor	|8|
|Browser	|Browser of the visitor	|13|
|Region	|Geographic region from which the session has been started by the visitor	|9|
|TrafficType	|Traffic source by which the visitor has arrived at the Web site (e.g., banner, SMS, direct)	|20|
|VisitorType	|Visitor type as “New Visitor,” “Returning Visitor,” and “Other”	|3|
|Weekend	|Boolean value indicating whether the date of the visit is weekend	|2|
|Month	|Month value of the visit date	|12|
|Revenue	|Class label indicating whether the visit has been finalized with a transaction|2|
----------------------------------     
    
*Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018).*
[Link](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset)

----------------------
## Objective       
Built a cloud-based service to predict whether the shoppers will purchase or not based on the their activity.
    
----------------------
## Steps
- EDA and ML modeling
    - Python and Jupiter notebook
- Dependency and environment management
    - Conda, pipenv
- Deployment 
    - Flask
- Containerization
    - Docker
- Cloud deployment
    - AWS Elastic Beanstalk
----------------------  
``` 
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── Screenshots 
├── lr_model.bin                    <- pickled model
├── online_shoppers_intention.csv   <- dataset
├── predict-test-cloud.py           <- cloud test sample
├── predict-test.py                 <- local test sample
├── predict.py                      <- Flask app
├── shoppers.ipynb                  <- ML notebook
└── train.py                        <- script to train the model
```
-----------------------------  
## Requirements
```
[packages]
numpy = "*"
scikit-learn = "==1.1.1"
flask = "*"
gunicorn = "*"

[dev-packages]
awsebcli = "*"

[requires]
python_version = "3.9"
python_full_version = "3.9.13"
````
## Try it!
run the web app locally on Ubuntu
``` bash 
> gunicorn --bind=0.0.0.0:9696 predict:app
```
run it with docker
``` bash
> docker run -it --rm --entrypoint=bash shoppers-img
> docker run -it --rm -p 9696:9696 shoppers-img
```
run it on cloud with AWS Elastic Beanstalk
``` bash
> eb create shoppers-serving-env
```    
- output a URL copy it
