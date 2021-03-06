from IPython.html.widgets import Widget, DOMWidget
from IPython.utils.traitlets import Unicode, Bytes, Instance, Any
from IPython.display import display

import base64
from PIL import Image
import StringIO
from numpy import array, ndarray

class WebCamera(DOMWidget):
    _view_name = Unicode('WebCameraView', sync=True)
    imageurl = Unicode('', sync=True)
    image = Instance(ndarray)

    def _imageurl_changed(self, name, new):
        head, data = new.split(',', 1)
        im = Image.open(StringIO.StringIO(base64.b64decode(data)))
        self.image = array(im)

class Link(Widget):
    _view_name = Unicode('LinkView', sync=True)
    widgets = Any(sync=True) # TODO: eventful list or tuple
