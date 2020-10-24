# fynd_assignment

Heroku APP name - imdb-movie-service
Postman Collection - https://www.getpostman.com/collections/ba06e12280b234327afd
Admin User Authentication Token - "admin1234"

Admin User has been created - 
User - (username, password, auth_token)  - ['admin', 'password', 'admin1234']

Permissions have been created - 
1. 'movie_create'
2. 'movie_update'
3. 'movie_delete'

Permissions have been assigned to the admin user


Models - 
1. Users = (id, username, password, auth_token)
2. Permissions - (id, permission_code, permission_name)
3. UserPermissionMap - (Username, Permission_code)
4. Movies - (id, name, director, imdb_score, genre, popularity_99)

APIS - 
1. Movie Creation  - (Auth key is mandatory)
2. Movie Search - (query fields -(name, director))
3. Movie Update - (Auth key is mandatory)
4. Movie Delete - (Auth key is mandatory)


Scaling Solutions
Non-Functional Requirements:
1. The system should be highly reliable, any movie created should not be lost.
2. The system should be highly available.

DB Solution
1. We should segregate our read traffic from write traffic. We can distribute our read traffic on different servers.
2. We can have master-slave configurations where writes will go to master first and then gets applied at all the slaves.
3. DB sharding - We can store the movies of a particular language on one server or one director.

Caching
We can cache Movies that are frequently accessed. We can start with 20% of daily traffic and, based on User's usage
pattern, we can adjust how many cache servers we need

MetaData storage
If the details of a movie expands we can store the search fields in postgres as Metadata and other details in a file system.


Things to DO - 
1. Create API for User CRUD operations
2. Create API for user login and generate User authentication Token using modules like JWT token. 
3. The Token should have an expiry so they can be stored in redis with an specified expiry time. 
4. Create API for User logout.
