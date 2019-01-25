import subprocess
import pydocstyle


def flake8_checker():
    p = subprocess.Popen(["flake8", "code.txt"], stdout=subprocess.PIPE)
    result = str(p.communicate())
    arr = result.split('code.txt:')
    arr.pop(0)
    return arr


def mypy_checker():
    p = subprocess.Popen(["flake8", "code.txt"], stdout=subprocess.PIPE)
    result = str(p.communicate())
    arr = result.split('code.txt:')
    arr.pop(0)
    return arr


def pydocstyle_checker():
    result = list(pydocstyle.checker.check(["code.txt"]))
    return result


def coverage_checker():
    ps = subprocess.Popen(('coverage', 'run', 'code.txt'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('coverage', 'report'), stdin=ps.stdout)
    ps.wait()
    result = [str(output)]
    return result
