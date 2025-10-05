Django_Blog Authentication System Documentation
Overview

The authentication system in django_blog provides secure user management including:

Registration: Users can create new accounts with a username and email.

Login/Logout: Users can securely log in and log out.

Profile Management: Users can view and update their account information (username, email, and optionally profile picture and bio).

Security Features: CSRF protection, password hashing, and restricted access to profile pages.

This system uses Django’s built-in authentication framework combined with custom views and forms for profile management.

Components
1. Registration

Form: CustomUserCreationForm (extends UserCreationForm with an email field).

View: register() in accounts/views.py.

Template: register.html

URL: /accounts/register/

Process:

User enters a username, email, and password.

Form validates data (password match, unique username/email).

User is saved in the database with hashed password.

Redirects to login page.

2. Login

View: Django’s built-in LoginView.

Template: login.html

URL: /accounts/login/

Process:

User enters username and password.

Credentials are validated against the database.

If valid, user session is created and user is redirected to LOGIN_REDIRECT_URL (profile page).

If invalid, an error message is displayed.

Security:

CSRF token is included in the form.

Passwords are hashed in the database; raw passwords are never stored.

3. Logout

View: Django’s built-in LogoutView.

Template: Optional logout.html.

URL: /accounts/logout/

Process:

Ends the user’s session.

Redirects to LOGOUT_REDIRECT_URL (login page).

4. Profile Management

Forms:

UserUpdateForm (update username and email)

ProfileUpdateForm (optional: update bio and profile picture)

View: profile() in accounts/views.py

Template: profile.html

URL: /accounts/profile/

Process:

Page displays current account info.

Users can submit updated info via POST request.

Form validation occurs and updates are saved to the database.

User is redirected back to profile page after successful update.

Access Control: Only authenticated users can access this page (@login_required decorator).

Optional Extended Profile:

A Profile model linked to User can store additional info like bio and profile_picture.

Profile is automatically created via Django signals when a user registers.

5. Security Features

CSRF Protection

All forms include {% csrf_token %}.

Prevents cross-site request forgery attacks.

Password Hashing

Uses Django’s default PBKDF2 algorithm with salt.

Passwords stored securely in database.

Access Control

Profile pages protected with @login_required.

Redirects unauthorized users to login page.

Media Security

Profile images served from MEDIA_ROOT.

Ensure MEDIA_URL ends with a / in settings.py.

How to Test Authentication Features
Registration

Visit /accounts/register/.

Fill in username, email, password, and confirm password.

Submit the form.

Verify you are redirected to the login page.

Check the database to confirm the new user is created with a hashed password.

Login

Visit /accounts/login/.

Enter your username and password.

Submit the form.

Verify you are redirected to /accounts/profile/.

Try entering wrong credentials to check error messages.

Logout

While logged in, visit /accounts/logout/.

Verify that you are redirected to the login page.

Attempt to access /accounts/profile/ — you should be redirected to login.

Profile Update

Login and visit /accounts/profile/.

Update username, email, bio, or profile picture.

Submit the form.

Verify that changes are saved in the database and displayed on the profile page.

Test uploading images to ensure media handling works.

Notes

All forms must include {% csrf_token %}.

Passwords are never stored or displayed in plaintext.

Use DEBUG = False in production and serve media via proper storage (not the development server).