Cloud Computing(CS 6065) Homework 1

This is web application for prime number testing. 
It takes a number and then checks if it is a prime number or not. 
If the number is not prime than it will return the show the statement that the number is not prime and 2 factors of the number, to prove that it is not prime. 
The application used POST method to send data. The web application is deployed on an AWS EC2 linux instance running on cloud. 

Files used in application
•	Hwflask.py
•	Index.html
•	Final.html

Steps for deployment
•	I uploaded all files on the var/www/html directory.
•	I have used WSGI server for python to deploy the application.
•	I configured httpd.config file and also created a .wsgi file for the python file, so that the application can run on wsgi server. In the editing, I entered the path to the folder containing the files.

Running this application
Enter the ec2-instance’s domain ‘ec2-13-58-7-4.us-east-2.compute.amazonaws.com’ in the browser’s url field.



