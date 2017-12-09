# [START vendor]
from google.appengine.ext import vendor
import tempfile
# Add any libraries installed in the "lib" folder.
vendor.add('lib')
# [END vendor]

tempfile.SpooledTemporaryFile = tempfile.TemporaryFile
