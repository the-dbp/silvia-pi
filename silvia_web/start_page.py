from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from RPi import GPIO
GPIO.setmode(GPIO.BCM)
power_gpio =14 
steam_gpio =7
brew_gpio = (3,4)
GPIO.setup(steam_gpio,GPIO.OUT)
GPIO.setup(power_gpio,GPIO.OUT)
GPIO.setup(brew_gpio,GPIO.OUT)
GPIO.output(power_gpio,1)
GPIO.output(steam_gpio,0)
GPIO.output(brew_gpio,1)


bp = Blueprint('start_page', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/on')
def on():
    GPIO.output(power_gpio,0)
    return redirect(url_for('index'))

@bp.route('/off')
def off():
    GPIO.output(power_gpio,1)
    return redirect(url_for('index'))

@bp.route('/son')
def steam_on():
    GPIO.output(steam_gpio,1)
    return redirect(url_for('index'))

@bp.route('/soff')
def steam_off():
    GPIO.output(steam_gpio,0)
    return redirect(url_for('index'))

import subprocess
import os

@bp.route('/maint')
def maintenance():
    script_path = os.path.join(os.path.dirname(__file__), "../io/maintenance_task.py")
    try:
        subprocess.Popen(["python", script_path])  # Run script in the background
    except Exception as e:
        print(f"Error starting subprocess: {e}")
    return redirect(url_for('index'))
