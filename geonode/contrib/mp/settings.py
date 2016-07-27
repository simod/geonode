
# make geonode mapping clients to use tiles directly from the disk
# REQURES WEB SERVER CONFIGURATION TO SERVE FILE_CACHE_DIRECTORY
USE_DISK_CACHE = False

# create mapproxy cache for all geonode layers
USE_DJMP_FOR_GEONODE_LAYERS = True

DJMP_AUTHORIZATION_CLASS = 'geonode.contrib.mp.authorisation.GeoNodeDJMPAuthorization'