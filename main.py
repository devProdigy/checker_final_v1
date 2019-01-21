from app import app
from flask import render_template
from flask import request
from checker import *


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

    return render_template('checked-code.html',code_text=code, res=results)


if __name__ == '__main__':
    app.run(debug=True)

