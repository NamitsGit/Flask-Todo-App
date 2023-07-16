# Flask-Todo-App
A todo app which demonstrates Python Flask framework, uses SQLite (CRUD operations) database and Bootstrap v5.3 for frontend.

# What is a todo?
A todo is a table record representing a real-world task (performing action X at place Y).

A todos table is stored in the SQLite database as follows



|      Column      |                    Description                    |
|:-----------------|:--------------------------------------------------|
| sno | (Integer) Serial Number of the todo, will be the primary key through which the todo will be uniquely identified in the database |
| title | (String) The title/name of the todo |
| description | (String) The detailed description of the todo which is used to describe the entire todo in detail |
| date_created | (DateTime) The date when the specific todo was created |


So the todos table will look something like this



|   sno   |   title   |                description                |                date_created                |
|:--------|:----------|:------------------------------------------|:------------------------------------------:|
|1|Todo1|Bring ice-cream from the shop|2023-07-16 21:33:88.123456|
|2|...|...|...|

