from flask import Flask
from os import getenv

app = Flask(__name__)
app.config['APPLICATION_ROOT']='/src'
app.secret_key = getenv("SECRET_KEY")

import routes

if __name__=='__main__':
    app.run()
