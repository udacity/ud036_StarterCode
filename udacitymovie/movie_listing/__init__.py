import pkg_resources
import yaml

resource_package = __name__
__movie_listing_yaml = pkg_resources.resource_string(
    resource_package, 
    'movie_listing.yaml'
)
movie_listing = yaml.load(__movie_listing_yaml)
