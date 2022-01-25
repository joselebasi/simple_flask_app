import os
import sys
import logging

from flask import Flask
from flask import render_template, request
from currency_converter import CurrencyConverter

app = Flask(__name__)

stdout_fileno = sys.stdout 
sample_input = ['Hi', 'Hello from AskPython', 'exit']

logging.basicConfig(format='%(levelname)s : %(asctime)s : Clase : main.py : Linea : %(lineno)d - %(message)s', \
                    level = logging.WARNING, filename = '/var/log/burocredito.log')

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/", methods=["POST"])
def my_form_post():
    
    for ip in sample_input:
        # Prints to stdout
        stdout_fileno.write(ip + '\n')
    
    logging.warning('warning: log en var/log')

    c = CurrencyConverter()

    euros = request.form["euros"]

    usd = round(c.convert(euros, "EUR", "USD"), 2)

    return render_template("form.html", euros=euros, usd=usd)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))