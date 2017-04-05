# coding: utf-8
from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/diligent')
def diligent():
    return render_template('diligent.html')


