from flask import Flask
from flask_assets import Environment, Bundle
#from flask_cache import Cache


    
## allow templates to reload: https://github.com/pallets/flask/pull/1910
class MyFlask(Flask):
    def create_jinja_environment(self):
        self.config['TEMPLATES_AUTO_RELOAD'] = True
        return Flask.create_jinja_environment(self)
app = MyFlask(__name__)

#cache = Cache(config=app.config['CACHE_ARGS'])
#cache.init_app(app)

## Assets: Bundle dependencies for speed
assets = Environment(app)
js = Bundle("bootstrap-4.1.3-dist/js/bootstrap.min.js")
assets.register("js_core", js)

css = Bundle("bootstrap-4.1.3-dist/css/bootstrap.min.css",
             "css/style.css")
assets.register("css_core", css)

## rendering
from app import views
