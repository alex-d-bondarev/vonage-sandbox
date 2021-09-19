from logging.config import fileConfig

from flask import Flask

app = Flask(__name__)
fileConfig("logging.cfg")