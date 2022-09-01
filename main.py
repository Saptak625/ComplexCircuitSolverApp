from flask import Flask, render_template, request
from forms import CircuitCodeForm
from circuit_solver import CircuitSolver

app = Flask('Complex Circuit Solver')
app.config['SECRET_KEY'] = '7b7e30111ddc1f8a5b1d80934d336798'

@app.route('/')
@app.route('/home')
def homepage():
  return render_template('home.html')

@app.route('/solver', methods=['GET', 'POST'])
def solver():
  submitted = False
  form = CircuitCodeForm()
  results = None
  if form.validate_on_submit():
    submitted=True
    circuitCodeInput = request.form['circuitCode']
    with open('webInput.crc', 'w') as f:
      f.write(circuitCodeInput)
    circuitSolver = CircuitSolver('webInput.crc')
    circuitSolver.solve()
    results = circuitSolver.showCircuit()
  return render_template('solver.html', form=form, submitted=submitted, results=results)

app.run(host='0.0.0.0', port=8080, debug=True)
