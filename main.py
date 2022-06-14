from operator import index
from flask import Flask, render_template


class Site(Flask):
    def __init__(self):
        super().__init__(__name__)

    def routes(self):
        @self.route('/')
        def home(): 
            return render_template("index.html")

        
        @self.route('/sobre')
        def about(): 
            return render_template("about.html")


site = Site()
site.routes()
site.run()
