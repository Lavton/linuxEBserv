from app import app, status
from flask import Flask, jsonify, request
from random import randint

@app.route('/submit', methods=['POST'])
def send_solution():
    """
    function on submiting solution.
    Requires solution parametr - file of solution
    Optional parametr - makefile
    @return id of solution, which came into treatment
    """ 
    solution = request.form.get('solution', None)
    makefile = request.form.get('makefile', None)
    id = randint(1, 200000000)
    print("Hello", solution, id)
    return jsonify(id=id)

@app.route('/check', methods=['POST'])
def check():
    """
    function, that told about current status of solution.
    Required id parametr - id, that was returned by @send_solution
    @return status ("wait" or "ready") and, in case of "ready" - log and 
    result from 0 to 1
    """
    id = request.form.get('id', None)
    stat = status.Status.ready.value
    log = None
    result = 1.0
    return jsonify(status=stat, log=log, result=result)