from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'This thing works!'

number_of_visit = 0

@app.route('/get_visits')
def get_visits():
    return f"visits till now: {number_of_visit}"

@app.route('/visit')
def visit():
    global number_of_visit
    number_of_visit += 1
    return f"visits: {number_of_visit}"

@app.route('/set_visits/<visits>')
def set_visits(visits):
    global number_of_visit

    try:
        number_of_visit = int(visits)
    except ValueError:
        return f"Invalid visits value: {visits}"

    return f"visits: {number_of_visit}"

@app.route('/set_visits_with_validation/<int:visits>')
def set_visits_with_validation(visits):
    return set_visits(visits)


@app.route('/goto/<domain>/path/<path:subpath>')
def goto(domain, subpath):
    return redirect(f"https://{domain}/{subpath}")

# e.g. http://localhost:5101/goto/google.com/path/maps/place/Bengaluru
