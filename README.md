# django-tutorial-02
connecting to mysql server.
#install mysql
->sudo apt update
->sudo apt install mysql-server
->sudo mysql_secure_installation
#set up mysql server
step 1. sudo mysql -u root -p

step 2. USE mysql;

step 3. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin';

Here 'admin' is your new password, yo can change it.

step 4. exit
#create django app. tutorail-01 explains

#Install MySQL Database Connector
First ensure that you have python3-dev installed.
 You can install python3-dev by running the following command:
 ->sudo apt install python3-dev

 We can now install the necessary Python and MySQL development headers and libraries:
 ->sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev

Once the installation is complete, we will use pip3 to install the mysqlclient library from PyPi. Since our version of pip points to pip3, we can just use pip
->pip install mysqlclient

#create database in mysql, i use graphical userinterface phpmyadmin
->sudo apt update
->sudo apt install phpmyadmin php-mbstring php-gettext
The installation process adds the phpMyAdmin Apache configuration file into the /etc/apache2/conf-enabled/ directory, where it is read automatically. The only thing you need to do is explicitly enable the mbstring PHP extension, which you can do by typing:
->sudo phpenmod mbstring
Afterwards, restart Apache for your changes to be recognized:
->sudo systemctl restart apache2

#####if phpMyAdmin does not come on web browser,
edit and include
->Include /etc/phpmyadmin/apache.conf

...to the /etc/apache2/apache2.conf file and restarting the service.
