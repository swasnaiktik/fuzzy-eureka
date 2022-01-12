# Shopify Backend Intern Challenge Summer 2022

[Challenge Link](https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit) additional objective: Shipment creation

<!-- ABOUT THE PROJECT -->
## About The Project

Are your starting a new business and have a lot of inventory products to maintain. No wories the Logistron 5000 is here to help you with all your logistic problems. Easy set up, Easy to use interface, Secure, Efficient and Data persistent.

You can create an Inventory Item, List the items, Update the items, and Delete the items. 

Along with this you can create shipments and once created (reflecting sent out the shipment) the changes in the quantity of the Inventory Item is reflected.

### Expandability

Function Expandability and Efficiency were central goals in the development process of this application.

* Application is built with Flask Factory pattern to ensure scalability in the codebase size.
* All data is stored such as creation time and name, quantity, description for creating new features.
* Data is stored in SQL database and the data is related to each other with relations.
* Precautions have been taken to prevent security issues such as injection attacks, csrf attack etc.
* This Application can be easily deployed as it is Dockerized.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/)
* [Pytest](https://docs.pytest.org/en/6.2.x/)
* [Bootstrap](https://getbootstrap.com/)
* [Docker](https://www.docker.com/)

<!-- GETTING STARTED -->
## Getting Started

These are the instructions required to run Application locally
### Prerequisites
* Docker
  * According to your machine operating system follow one of the tutorials
  * [Linux](https://docs.docker.com/engine/install/ubuntu/)
  * [Windows](https://docs.docker.com/desktop/windows/insta)
  * [Mac OS](https://docs.docker.com/desktop/mac/install/)
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/swasnaiktik/fuzzy-eureka.git
   ```
2. Run Docker Compose
   ```sh
   docker-compose up
   ```
3. Wait till container is up and running
4. Go To in your browser
   ```sh
   localhost:5000
   ```

<!-- USAGE EXAMPLES -->
## Usage

This section will take you through how the Logistron 5000 should be used.

### Inventory Management

### Shipment Management

## Contact

* Email: swastikn@buffalo.edu
* [LinkedIn](https://www.linkedin.com/in/swastikn/)
