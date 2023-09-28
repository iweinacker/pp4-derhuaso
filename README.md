# Booking Project - DerHuaso Restaurant

The DerHuaso Restaurant website is designed to be a responsive website that allows visitors to view it on a range of devices. It allows the user to book a table for the restaurant and also allows the admin to administer those bookings.

(Image of amiresponsive)

Link to Deployed Project [here]()

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Wireframes](#Wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
  * [How to Fork](#How-to-Fork)
  * [How to Clone](#How-to-Clone)
   
* [Testing](#testing)

* [Credits](#credits)
  

---


## User Experience (UX)

DerHuaso is a restaurant website that allows users to make reservations for tables between 2 to 6 people. When making a reservation, the administrator will be able to review the client’s information in order to confirm or reject the reservation in case of unavailability or any other reason.

Additionally, the administrator can add, modify, or delete reservations on the website as an administrator.

### User Stories

- Gather General Requirements and Visual Layout:
As a developer, I need to understand the general requirements and visual layout of the booking app to guide incremental development.
- Initial Django Project Setup:
As a developer, I should set up the initial Django project files in my development environment and deploy them to Heroku so that I can identify and resolve deployment issues at an early stage.
- Create Bootstrap Template:
- As a developer, I have to implement a basic Bootstrap template for the booking website to meet the minimum viable design requirements.
iv. Create Booking Model:
- As an admin user, I can add booking models in the admin area so that I can ensure that the information populates relevant sections on the frontend template.
v. Create Admin Account:
- As an admin user, I can create a superuser account so that I can access the admin area and manage content for the booking app.
vi. Make a Booking:
- As a site user, I can create a reservation directly from the website so that I can receive a confirmation which will allow me to be sure that my reservation was successfully received.
vii. Onscreen Login/Logout Notifications:
- As a site user, I should see on-screen notifications so that I can confirm that I have logged in or logged out successfully.
vii. Test and Validate Technologies:
- As a developer, I have to validate HTML, CSS, JavaScript, and Python code using validation tools so that I can ensure conformity to standards.
ix. Implement Automatic Unit Tests:
- As a developer, I will create automatic unit tests to showcase coding competency and enhance code quality.
x. Final Deployment:
- As a developer, I will deploy the final version of the Booking project to Heroku so that it matches the development environment.

### Future Development

i. Modify or delete booking on user dashboard
- As a Site User, I can modify or remove a reservation from my dashboard so that I can correct any mistakes or cancel the reservation if it is no longer required.
ii. Avoid double bookings
- As a Developer, I have to create a model that avoids double booking so that different users cannot book the same table on the same day.
iii. Create Feedback Model
As an admin user, I can manage and view feedback details in the admin area so that I can approve feedback for display.
iv. Provide Feedback after the restaurant's experience.
- As a Site User, I can provide feedback using the feedback button on my dashboard so that I can share my opinion about the service.
v. Contact Admin via Email
- As a Site User, I can use a contact form to send an email to the admin with inquiries or requests for assistance.
vi. Receive Reservation Email Notifications
- As an Admin User, I can send email notifications to confirm when a reservation is created, approved, updated, or canceled. This ensures that I can manage my bookings effectively.

## Design

### Colour Scheme

![image](https://github.com/iweinacker/pp4-derhuaso/assets/130374663/00a492da-8343-4dc2-8a28-ea6600baf741)

As the focus of the restaurant is Chilean cuisine, it seemed appropriate to copy the color palette of the flag itself, as it combines the feeling of belonging to the Chilean people and at the same time attracts people who want to immerse themselves in the culture.


### Wireframes

The initial wireframes were created in Balsamiq to understand how the site would work. These wireframes helped drive the creation of User Stories, the logic required, and overall design artwork decisions.

![image](https://github.com/iweinacker/pp4-derhuaso/assets/130374663/c7e33430-a598-4188-85ee-10b7bd8a75cc)


## Features

The website is comprised of three pages, three of which are accessible from the navigation menu: the home page, registration page, and log in page. Once you register or log in, the website automatically changes to the home page and logs you out.

### General features

All Pages on the website have:

All pages on the website have a **responsive navigation bar** at the top, which allows users to navigate through the site. To the right of the navigation bar are the links to the website's pages, such as home, log in, and register. This implementation gives the site a clean look and promotes a good user experience, as users are accustomed to seeing this option when navigating a site on mobile devices.

Additionally, all pages have a **footer** that contains contact information and social media links for the web page.

**Home Page**:
- The home page contains a **hero image** with a welcome message. After that, an alert message mentions the availability of the restaurant.
- Following that, the website contains an **"about us" section** that briefly explains the history and purpose of the restaurant.
- The page is then divided into two columns:
    - The first column explains Chilean cuisine and wine.
    - The right column, which is the main purpose of the app, is the **booking form**. When you make a reservation, it will automatically send the information to the admin. In case of a successful booking or if there is a problem with the booking, a message will appear at the top of the page with the corresponding message. In case of an error, it will explain the reason for it¹.

**LogIn**, **LogOut**, and **Register**:
- On these three pages, only either a form or an "are you sure" option appears, depending on the action you are taking¹.

### Future Implementations

A reservation management page will be created for people who have registered and made a reservation. This page will display the reservation information and allow users to modify or delete their reservations if necessary.

Another page will be created for all users, whether registered or not. This page will serve as the restaurant menu.

### Accessibility

I have been mindful during coding to ensure that the website is as accessible-friendly as possible. I have achieved this by:

- Using semantic HTML.
- Providing information for screen readers.
- Ensuring that there is a sufficient color contrast throughout the site.
- Ensuring menus are accessible by marking the current page as current for screen readers.

## Technologies Used

### Languages Used

1. HTML5.
2. CSS.
3. JavaScript.
4. Python.

### Frameworks, Libraries & Programs Used

1. Django - database framework.
2. ElephantSQL - database hosting.
3. Cloudinary - media hosting.
4. Bootstrap
5. Balsamiq - Used to create wireframes.
6. Git - For version control.
7. Github - To save and store the files for the website.
8. Google Fonts - To import the fonts used on the website.
9. Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.
10. Am I Responsive? To show the website image on a range of devices.

## Deployment & Local Development

1. Install Django and supporting libraries
2. Create an external database on Elephantsql
3. Setup Cloudinary to store media and static files
4. Create the Heroku App
5. Update database details in project settings
6. Add Config Vars in Heroku
7. Connect GitHub repo to Heroku as the deployment method
8. Setup media, static and templates folders in project
9. Create proc file
10. Commit to GitHub
11. Deploy branch in Heroku and check

### Local Development

#### How to Fork

To fork the DerHuaso repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, kera-cudmore/Bully-Book-Club.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the DerHuaso repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project.
3. Click on the code button, select whether you would like to clone with HTTPS,  GitHub and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

1. Incremental testing.
2. Early user observation test.
3. HTML, CSS, JSHINT, PYLINT, Lighthouse.
4. Browser Compatability tests.
5. Django Automated Testing using Unittest

## Credits

All the following people, links, Youtube channels, and sites have helped me as a guidance for developing DerHuaso. I humbly thank everyone for their help, both directly and indirectly, or as an inspiration in the development of the code and its functionality.

Special thanks to the CodeInstitute team, who without their help and guidance, this would not be possible.

The links will be found below: 

- [django project](https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/)
- [StackOverflow](https://stackoverflow.com/questions/31627253/django-modelform-with-bootstrap)
- [codemy.com](https://www.youtube.com/watch?v=6-XXvUENY_8)
- [w3collective](https://w3collective.com/restaurant-landing-page-bootstrap/)
- [ByteGrad](https://www.youtube.com/watch?v=UqE8b1BtXTs)
- [geeksforgeeks](https://www.geeksforgeeks.org/overriding-the-save-method-django-models/)
- [rstan-dev: yoomoov project](https://github.com/rstan-dev/pp4-yoomoov)
