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

Django Blog – Blog Post Features Documentation
Overview

The blog post module allows users to create, read, update, and delete (CRUD) blog posts. Access to certain actions is restricted based on user authentication and ownership of posts.

Models
Post

Fields:

title (CharField) – Title of the post.

content (TextField) – Main content of the post.

author (ForeignKey to User) – Automatically set to the logged-in user when creating a post.

created_at (DateTimeField) – Automatically set on creation.

Permissions:

Any user can view posts.

Only the author can edit or delete their posts.

Views
PostListView

Type: ListView

URL: /posts/

Functionality: Lists all blog posts in reverse chronological order.

Accessible to: All users.

PostDetailView

Type: DetailView

URL: /posts/<int:pk>/

Functionality: Displays a single blog post.

Accessible to: All users.

PostCreateView

Type: CreateView

URL: /posts/new/

Functionality: Allows logged-in users to create new posts.

Permissions: Requires authentication.

Notes: Author is automatically set to the logged-in user.

PostUpdateView

Type: UpdateView

URL: /posts/<int:pk>/edit/

Functionality: Allows the author to edit their post.

Permissions: User must be logged in and the author of the post.

PostDeleteView

Type: DeleteView

URL: /posts/<int:pk>/delete/

Functionality: Allows the author to delete their post.

Permissions: User must be logged in and the author of the post.

Success URL: Redirects to /posts/.

Forms
PostForm

ModelForm for the Post model.

Fields: title, content.

Usage: Used in PostCreateView and PostUpdateView for data validation and input rendering.

Permissions Summary

All users: Can view posts (PostListView and PostDetailView).

Authenticated users: Can create new posts (PostCreateView).

Post authors: Can edit or delete only their own posts (PostUpdateView and PostDeleteView).

Unauthorized access: Users attempting to edit or delete posts they do not own are denied via UserPassesTestMixin.

Usage

Create a Post

Navigate to /posts/new/ while logged in.

Fill in the title and content.

Submit the form; you will be redirected to the post detail page.

View Posts

Navigate to /posts/ to see a list of all posts.

Click on a post title to see the full content.

Edit/Delete Post

Navigate to /posts/<post_id>/edit/ or /posts/<post_id>/delete/ as the author.

Unauthorized users attempting to access these URLs will be blocked.

Notes

All forms include CSRF protection.

Passwords and authentication are handled securely by Django.

Styling is consistent across post pages using styles.css.

URLs are intuitive and RESTful for easy navigation.