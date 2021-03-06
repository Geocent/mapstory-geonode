from .local_key import *
MEDIA_ROOT = '{{media_root}}'
DATABASE_PASSWORD = '{{ pgpass }}'
OGC_SERVER['default']['PASSWORD'] = '{{ gspass }}'
OGC_SERVER['default']['PUBLIC_LOCATION'] = 'http://{{ nginx_server_name }}/geoserver/'
LOCAL_CONTENT = False

HAYSTACK_SEARCH = True
# Avoid permissions prefiltering
SKIP_PERMS_FILTER = False
# Update facet counts from Haystack
HAYSTACK_FACET_COUNTS = False
HAYSTACK_CONNECTIONS = {
   'default': {
       'ENGINE': 'mapstory.search.elasticsearch_backend.MapStoryElasticsearchSearchEngine',
       'URL': 'http://127.0.0.1:9200/',
       'INDEX_NAME': 'geonode',
       },
   }
SKIP_PERMS_FILTER = True
HAYSTACK_SIGNAL_PROCESSOR = 'mapstory.search.signals.RealtimeSignalProcessor'


MAPSTORY_APPS = (

 'mapstory.apps.boxes',
 'mapstory.apps.flag', # - temporarily using this instead of the flag app for django because they need to use AUTH_USER_MODEL

)



INSTALLED_APPS += MAPSTORY_APPS
