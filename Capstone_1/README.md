# Predicting Online Shoppers Purchasing Intention 
----------------------
**Problem Description**     
E-commerce marketing and sales departments goal is to trigger visitors to purchase. For example, offering promotion sales, packages, rewards etc. and these are very useful. What if the departments knew each individual visitor intension, The offers would be personalized and tailored to each one.        

----------------------
**Dataset**     
Online shoppers activity data is from UCI Machine Learning Repository. The dataset was formed so that each session would belong to a different user in a 1-year period to avoid any tendency to a specific campaign, special day, user profile, or period.       
The dataset consists of:       
- feature vectors belonging to 12,330 sessions. 
- 10 numerical and 8 categorical attributes. 
The 'Revenue' attribute can be used as the class label. (more about features inside the notebook)


Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018).

----------------------
**Objective**
- Build a cloud-based service to predict whether the shoppers will purchase or not based on the their activity.
----------------------
- EDA and modeling
    - NumPy
    - Pandas
    - Matplotlib
    - Seaborn
    - Scikit-learn
    - Pickle
- Dependency and enviroment management
    - Conda
    - Pipenv
- Deployment 
    - Flask
- Containerization
    - Docker
- Cloud deployment
    - AWS Elastic Beanstalk

# Repo Content
- Jupytier notebook
- Python scripts for train and predict locally and on cloud (AWS Elastic Beanstalk)
- Pickled model
- Environment dependencies
- Dockerfile
- Screenshots 