Editable table. Consist of fields user can change on client side. For this purpose AJAX used. Also project runs on apache2 server.

You need:

$ cd /var/www

$ sudo -s

$ virtualenv env

$ cd env

$ git clone https://github.com/SevenKeys/Editable_table.git

$ source scripts/activate(Windows) or $ source bin/activate(Linux)

$ cd Editable_table

$ pip install -r requirements.txt

$ python manage.py syncdb

$ python manage.py collectstatic

$ mv web_app.conf /etc/apache2/sites-available/web_app.conf

$ chown www-data /var/www/env/Editable_table/

$chown www-data /var/www/env/Editable_table/db.tables

$ service apache2 restart

http://www.editabletable.com