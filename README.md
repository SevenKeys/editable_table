Editable table. Consist of fields user can change on client side. For this purpose AJAX used.

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

editabletable.com
