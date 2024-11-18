# Cats, Coffee and Covers
## Project Overview
### Target Audience
### Problem Statement

## Agile methodology

## Back-end documentation
### User stories
**Must haves**

- *As a user I can create an account so that I can access feature for logged in users.*
- SUCCESS CRITERIA:
- Users can create an account with a username and password
- Users can access certain content as a logged in user but not a logged out user

- *As a user, I have a customisable profile page where I can display information about myself.*
- SUCCESS CRITERIA:
- Users can read their own and others profile pages
- Users can edit their own profile pages but NOT others
- Some information will be optional and not displayed

- *As a user, I can log-in to the site to access content that can only be accessed by logged-in users.*
- SUCCESS CRITERIA:
- Users can log-in and log-out easily

- *As a user, I can create book reviews to share my views with the community.*
- SUCCESS CRITERIA:
- User can create a review with Book Title, Author, Genre, Rating (/5*), Content review and an optional photo

- *As a user I can view the review page so that I can read the review.*
- SUCCESS CRITERIA:
- Clicking on the review makes it easier to read

- *As the review owner I can edit my review so that I can make corrections or update my post after it was created*
- SUCCESS:
- The user who created the review can edit the review
- Other users cannot edit the review

- *As the review owner I can delete my review.*
- SUCCESS CRITERIA:
- The user who created the review has the option to delete it
- Other users cannot delete the review

**Should haves**

- *As a user, I can search for a review by book title or genre so that I can find reviews I'm interested in.*
- SUCCESS CRITERIA:
- ability to search for reviews by Book Title, Author, Genre and Reviewer

**Could haves**

- *As a user, I can comment on book reviews so that I can share my views with others.*
- SUCCESS CRITERIA:
- ability to comment on reviews as a user

- *As a user I can 'like' reviews to show that I like them.*
- SUCCESS CRITERIA:
- the ability to like posts

- *As a user I am able to 'follow' my favourite profiles so I can keep up to date with their content.*
- SUCCESS CRITERIA:
- ability to 'follow' another user

- *As a user, I can't upload images which are too big and will disrupt the aesthetic of the page.*
- *As a developer, the user can't upload images which are too big and could cause storage issues.*
- SUCCESS CRITERIA:
- If a user tries to upload a large image, they will receive an error message and the photo won't be uploaded.

### Wireframes 

### Database
1. Navigate to [PostgreSQL](https://dbs.ci-dbs.net/) from Code Institute.
2. Enter your email address in the input field provided.
3. Click Submit.
4. Wait while the database is created.
5. Check your email.
6. You now have a URL you can use to connect your app to your database.

### Deployment

Site is deployed with Heroku which is a cloud platform that lets developers create, deploy, monitor and manage apps.
The deployed site can be found [here](https://catscoffeecovers-448595c73efd.herokuapp.com/).
These steps assume that you have a Heroku account and are logged in. 

**Creating an app**
1. Go to the Dashboard
2. Click 'New' > 'Create new app'
3. Choose a unique app name, choose the closest region and press 'Create app'
4. Click on 'Settings' and then 'Reveal Config Vars'
5. Add a key of 'DATABASE_URL' - the value will be the URL you were emailed when creating your database.
6. The app has been created

**Deploying**
1. Go to the app Dashboard
2. Click the 'Settings' tab
3. Click 'Reveal Config Vars' and add these Config Vars:
- (KEY)CLOUDINARY_URL: (VALUE) Copy the Cloudinary URL from your env.py file without quotation marks
- (KEY)SECRET_KEY: (VALUE) Make up a completely new Secret Key that is NOT the same as the one in settings or env - there are many online Secret Key generators you can search for. 
- (KEY)DISABLE_COLLECTSTATIC: (VALUE)1
4. Click the 'Deploy' tab
5. In the Deployment method section, click "Connect to GitHub"
6. Search for the repo you want to connect and click 'Connect'
7. Scroll down and click "Deploy Branch" in the Manual deploy section
8. Your app has been deployed! You can find it in "Open app".

**Cloning a repository**
1. On GitHub.com, navigate to the repository you want to clone.
2. Click the "Code" button (found above the list of files).
3. Copy the URL for the repository.
4. Open Git Bash or your chosen terminal.
5. Navigate to the directory where you want to clone the repository.
6. Type: git clone https://github.com/elamont174/ey-up-me-pup.git
7. Press Enter to create your local clone.

**Forking a repository**
1. 'Forking' the GitHub repository means creating a copy which can be viewed/changed without changing the original.
2. To fork a GitHub repository:
3. Login to GitHub and navigate to the repository you want to fork.
4. Click the "Fork" button (found above the Settings button).
5. You will now have a copy of the original repository in your GitHub account.

*Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Run the server: python3 manage.py runserver
- Stop the app once it's loaded: CTRL+C or ⌘+C
- Make any necessary migrations: python3 manage.py makemigrations
- Migrate the data to the database: python3 manage.py migrate
- Create a superuser: python3 manage.py createsuperuser


### Security

### Testing 
Please see separate TESTING.md file for all testing.

## Front-end documentation
### User experience
### Design
#### Colour scheme
#### Typography
### Wireframes
### Features
#### Profiles
#### Reviews
#### Comments
#### Followers
#### Navigation
### Responsiveness
### Accessibility
### Deployment
### Testing
Please see separate TESTING.md file for all testing.

## Future improvements

## React Components

## Languages

## Technologies used

## Credits
https://stackoverflow.com/questions/70612439/csrf-failed-origin-checking-failed-http-localhost8000-does-not-match-any
https://forum.djangoproject.com/t/django-csrf-trusted-and-allowed-hosts-issues/23842/6

## Acknowledgements 