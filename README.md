# Deliverable 2 - Web Project
## Implementation
- Users are allowed to Log In and Register using forms, which create a User entity on the database.
- Users can create new Company entities and give access to other users into It.
- Inside every Company entity, users can create Departments and give acces to other users that are included on the Company.
- With every department all department users are allowed to create projects and tasks.
- Ability to edit all model entities. (Company and Department) can be edited the users inside them. Task can have the name edited by a form on the Project.
- Ability to delete model entities(only the users that created them).
- Added a API to acced Cities information to create the Company.
- Added testing (Unit testing and behave testing).
## Behave Testing
The tests that are done by behave, test all the actions a user can do. From registering and logging In, till creating models.
The cases are done inside the feature files and can be seen they're implementation on the steps folder.
## Unit Testing
The test we have developed have the purpose of emulating several functions of our application, therefore we have made them end to end.
Those tests create users, projects and entities.
The "Delete" function is also tested there.
