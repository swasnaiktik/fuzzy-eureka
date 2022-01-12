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
   git clone git@github.com:swasnaiktik/fuzzy-eureka.git
   ```
2. Enter the project directory and run Docker Compose
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

![Screenshot (82)](https://user-images.githubusercontent.com/26603306/149097612-6a0ec24f-2744-4ff2-bffa-60626fc85094.png)

![Screenshot (83)](https://user-images.githubusercontent.com/26603306/149097628-88abf7d6-b725-4abe-8c2b-037627073537.png)

![Screenshot (84)](https://user-images.githubusercontent.com/26603306/149097665-4a2d912a-8016-4a68-99cb-184f55b492ad.png)

### Shipment Management

![Screenshot (85)](https://user-images.githubusercontent.com/26603306/149097713-1415b316-7cff-4e0c-a2fd-ecf1829d3e21.png)

![Screenshot (86)](https://user-images.githubusercontent.com/26603306/149097738-39856020-d163-476b-959b-735e3ed67f18.png)

![Screenshot (89)](https://user-images.githubusercontent.com/26603306/149097755-3689c2d2-c8cf-4440-90e1-0799218e8dce.png)

## Contact

* Email: swastikn@buffalo.edu
* [LinkedIn](https://www.linkedin.com/in/swastikn/)
