# CS-340 Client/Server Development Portfolio

## Project Two: Grazioso Salvare Dashboard

This repository contains the final dashboard code and CRUD Python module developed for the Grazioso Salvare project. 

### Reflection on the project

### How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
I write maintainable programs by utilizing object-oriented principles, modular design, descriptive variable names, and thorough in-line comments. Creating the CRUD Python module allowed me to abstract complex database queries into simple, reusable methods. The main advantage of this approach is separation of concerns; the front-end dashboard code stays clean because it doesn't need to process raw database logic. In the future, this exact CRUD module could be imported into any other Python application (like a mobile app backend or a different web framework) to seamlessly interact with MongoDB without having to rewrite the database connection code.

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
As a computer scientist, I approach problems by breaking them down into smaller, testable components using the Model-View-Controller (MVC) design pattern. For Grazioso Salvare, I first ensured the database (Model) was properly indexed, then built the CRUD middleware, and finally developed the interactive dashboard (View/Controller). This project differed from previous assignments by requiring full-stack integration rather than writing isolated scripts. In the future, my strategy for database creation will always begin with analyzing the client's specific data filtering needs before designing the schema or the user interface.

### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientists solve complex problems by designing efficient, automated software solutions. This matters because software reduces human error, automates tedious tasks, and makes massive amounts of data actionable. For a company like Grazioso Salvare, this specific project transforms thousands of raw, unreadable animal shelter records into an intuitive visual tool. Instead of manually sorting through spreadsheets, the company can now use the dashboard to instantly identify and rescue the perfect dogs for life-saving training.
