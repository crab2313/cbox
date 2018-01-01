#!/usr/bin/python3

from flask import Flask, g
from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)