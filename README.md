# care24-assignment

API for Content management system:

To run the project clone it first and create and activate virtual environment and then run command "pip install -r requirements.txt"
after installing all packages you are good to go.

1. The system has 2 types of user role, admin and author.
2. Author can register using api endpoint => (http://127.0.0.1:8000/author-register/).
3. Author can login using api endpoint =>  (http://127.0.0.1:8000/author-login/).
4. For registering admin user i used django admin panel.
5. For login Use this endpoint => (http://127.0.0.1:8000/api/token/), 
   after login you will get JWT access and refresh token for loggend in user (You can use Postman, Thunder Client etc ).
    
6. Content API endpoint => (http://127.0.0.1:8000/content/), make sure you pass the access token of author/admin. 
   a. Anonymous user can only view the resources.
   b. Admin user can view, edit and delete all the contents created by any authors but can not create content.
   c. A logged in author can create content for him only and can perform CRUD.
   d. Users can search content by matching terms in title, body, summary and categories.
      if you are using postman then you can search like this => http://127.0.0.1:8000/content/?search=bus  it will give all
      the matching records from fields [title, body, summary, categories] or if you are anonymous user you can hit 
      api => (http://127.0.0.1:8000/content/) in the browser where you will see a filter button you can search from there too.
      
      
Points which is not coverd in the project:
  1. create admin user using seeding.
  2. Use Test-Driven Development.
  
  * Working on it soon it'll be done.    



 For making post request you can refer this screenshot   
![Screenshot (188)](https://github.com/anilkumar541/care24-assignment/assets/59431789/123f928b-1508-47f3-b7b8-0f4c557944ca)




Thanks.
