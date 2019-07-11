from flask import Flask
from jinja2 import Template
from socket import gethostname

# some bits of text for the page.
template_data = open('web/index.html', 'rt').read()

template = Template(template_data)
output = template.render(hostname=gethostname())

# EB looks for an 'application' callable by default.
application = Flask("Application")

@application.route('/')
def index():
    return output


@application.route('/health_check')
def health_check():
    return 'Everything is A-OK!'


# run the app.
if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
