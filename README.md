# KidzPass

Welcome to KidzPass, a graphical authentication mechanism for children.
This application was created to test graphical authentication as a viable alternative to text-based password for young
children aged 3-5.

<u><b>SETUP</b></u>

If you would like to run KidzPass locally:
1. simply run the manage.py
2. command: runserver
3. You're good to go.

If you would like to run KidzPass on another device, the quickest, easiest way to do this is to setup up all devices on
the same network:
1. Get the IP address of the system you will be running KidzPass from
2. Add it to the 'ALLOWED_HOSTS' section in the Django_GraphicalPasswords/settings.py
3. Change the IP address and port number in /static/javascript/ip_port.js
4. run manage.py
5. command: runserver [ip:port]
6. Done!


<u><b>ADDING PICTURES TO KIDZPASS</b></u>

Currently, images for both user(names) and password images are stored locally within the application. I realise this
isn't the best way to do this but since KidzPass is a prototype system designed to test a concept please be patient.

Images are stored in /static/images under 'PasswordImages' and & 'UserImages'. You'll need to add the images or change
the ones in here to do so.

If you're changing an image - just change the image in static.

If you're adding a new password image:
1. Add it to its respective file.
2. Add the file address to the 'arrayImages' array in the following format
'/static/images/PasswordImages/[imagenumber].jpg' in /templates/graphical_login.html
3. Add the file address to the 'arrayImages' array in the following format
'/static/images/PasswordImages/[imagenumber].jpg' in /templates/select_graphical_password.html

If you're adding a new username image:
1. Add it to its respective file.
2. Add the file address to the 'images' array in the following format
new Image([imagenumber], "static/images/UserImages/[imagenumber].JPG", "[username]", false), in /templates/reg_select_user.html
3. Add the file address to the 'arrayImages' array in the following format
'/static/images/UserImages/[imagenumber].jpg' in /templates/username_selection.html

TO ACCESS ADMIN PANEL - http://[IP:port]/admin/

CREDS - admin:admin

<u><b>*** DISCLAIMER ***</b></u> 

This is a Prototype system and is not ready for commercial release to general public. This application is part of an
educational project to learn and study the concept of graphical passwords and to test to a theory with study
participants.

