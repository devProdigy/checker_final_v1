import os
import jinja2
from flask import Flask, render_template, request
from checker import flake8_checker, mypy_checker, pydocstyle_checker, coverage_checker


def create_app() -> Flask:
    app = Flask(__name__, static_url_path='/static')

    project_path = os.path.dirname(app.root_path)
    templates_path = os.path.join(project_path, 'templates')
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(['/templates', project_path, templates_path]),
    ])
    app.jinja_loader = my_loader

    app.static_folder = [
        os.path.join(project_path, 'static'),
    ]

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/checked_code', methods=['POST'])
    def update():
        code = request.form['code']
        flake8_checkbox = request.form.get('Flake8')
        mypy_checkbox = request.form.get('MyPy')
        pydocstyle_checkbox = request.form.get('PyDocStyle')
        coverage_checkbox = request.form.get('Coverage')

        with open('code.txt', 'w') as f:
            f.write(code)

        results = {}
        if flake8_checkbox == 'on':
            results['Flake8'] = flake8_checker()

        if mypy_checkbox == 'on':
            results['MyPy'] = mypy_checker()

        if pydocstyle_checkbox == 'on':
            results['PyDocStyle'] = pydocstyle_checker()

        if coverage_checkbox == 'on':
            results['Coverage'] = coverage_checker()

        return render_template('checked-code.html', code_text=code, res=results)

    return app
