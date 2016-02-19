from app import app, Status
from random import randint

@app.route('/submit', methods=['POST'])
def send_solution():
	solution = request.form.get('solution', None)
	makefile = request.form.get('makefile', None)
	id = randint(1, 200000000)
	return jsonify(id=id)

@app.route('check', methods['POST'])
def check():
	id = request.form.get('id', None)
	status = Status.ready
	log = None
	result = 1.0
	return jsonify(status=status, log=log, result=result)