import os
import time

print(os.getcwd())

os.system('python parseModel.py')

os.system('python parseForm.py')

os.system('python parseUrls.py')

os.system('python parseView.py')

os.system('python tools.py')


parent_dir = os.getcwd()
chir_dir = parent_dir +'\\application'
# print(chir_dir)
os.chdir(chir_dir)
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py runserver')