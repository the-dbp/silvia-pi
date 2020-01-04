from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
power_gpio =14 
GPIO.setup(power_gpio,GPIO.OUT)

bp = Blueprint('start_page', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/on')
def on():
    GPIO.output(power_gpio,1)
    return redirect(url_for('index'))

@bp.route('/off')
def off():
    GPIO.output(power_gpio,0)
    return redirect(url_for('index'))

