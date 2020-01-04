from flask import (
    Blueprint, redirect, render_template, request, url_for
)

bp = Blueprint('start_page', __name__)

@bp.route('/')
def index():
    return 'hello world'

