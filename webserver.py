from flask import Flask

app = Flask(__name__)

import start_page
app.register_blueprint(start_page.bp)
app.add_url_rule('/', endpoint = 'index')


app.run(host='0.0.0.0', port='80',debug= 'True')

