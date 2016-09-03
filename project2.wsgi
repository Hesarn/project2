import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path = ['/var/www/project2'] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'Project2.settings'

application = get_wsgi_application()


