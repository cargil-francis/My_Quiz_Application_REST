
# My_Quiz_Application_REST

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      </li>
	      <ul>
		       <li><a href="#built-with">Built With</a></li>
	     </ul>
	    <li>
	      <a href="#getting-started">Getting Started</a></li>
	      <ul>
	        <li><a href="#installation">Installation</a></li>
	        <li><a href="#prerequisites">Prerequisites</a></li>
</ul>
<li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
 
    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

MY_Quiz_Application_Rest is a python project created using DjangoRestframework.
An Online Quiz Application with  Admin and Users. Various features are included in the project

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[Django]: https://docs.djangoproject.com/en/4.1/
[Django Restframework]: https://www.django-rest-framework.org/
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/cargil-francis/My_Quiz_Application_REST.git
   ```
2. CD to project
   ```sh
   cd My_Quiz_Application_REST
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



Follow the given steps to run the project in your localhost. 

### Prerequisites
* Install Python
  ```
  $ sudo apt install python3
  ```
* Create an environment
  ```
  $ python3 -m venv venv
  ```
  
* Activate environment
  ```
  $ source env/bin/activate
  ```

* Install dependencies
  ```
  $ (venv)  python -m pip install -r requirements.txt
  ```

* Make migrations
  ```
  $ (venv)  python3 manage.py makemigrations
  ```

* Migrate models
  ```
  $ (venv)  python3 manage.py migrate
  ```

* Run the project
  ```
  $ (venv)  python3 manage.py runserver
  ```




<!-- USAGE EXAMPLES -->
## Usage

Screenshots of the project using Postman
*User Registeration
![Screenshot from 2023-03-03 03-19-00](https://user-images.githubusercontent.com/96044398/222565868-763c8400-bc26-4942-bc30-77066fdf11fd.png)

*Login Using JWT Token
![Screenshot from 2023-03-03 03-19-00](https://user-images.githubusercontent.com/96044398/222567093-fc256c86-d55e-4ee4-8cb9-45dd04cde1b4.png)
 
*User Profile
![Screenshot from 2023-03-03 03-26-31](https://user-images.githubusercontent.com/96044398/222567679-27bb6a42-7b49-4089-8a8a-79ac46f889a3.png)

* Quiz Analytics
![Screenshot from 2023-02-26 23-31-28](https://user-images.githubusercontent.com/96044398/221428024-73ff2e4b-e2ec-47a0-9aac-300339e2a416.png)

* Quiz Listing
![Screenshot from 2023-02-26 23-32-27](https://user-images.githubusercontent.com/96044398/221428034-10f9b7e1-520a-41bc-977d-6e210be228dd.png)



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
- [x] User Authentication: Users should be able to sign up, log in, and log out. The authentication system should use JWT tokens.
- [x] Quiz Creation: Users should be able to create quizzes. Each quiz should have a title and a set of questions with multiple choices.
- [x] Quiz Taking: Users should be able to take quizzes. Each quiz should have a set of questions with multiple choices, and the user should be able to select their answer. After the user has completed the quiz, the system should display their score.
- [x] Quiz Results: Users should be able to view their quiz results. The system should display the user's score for each quiz they have taken.
- [x] Quiz Listing: The system should display a list of available quizzes that users can take.
- [x] Quiz Filtering: Users should be able to filter quizzes by topic, difficulty level, and date created.
- [x] Quiz Analytics: The system should display analytics on each quiz, such as the average score, the number of times the quiz has been taken, and the percentage of users who have passed the quiz.
- [x] User Profile: Users should be able to view their profile, which should display their username, email, and a list of quizzes they have created.
- [x] User Management: Admin users should be able to manage users, including creating, editing, and deleting user accounts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>






