'''
OWASP Benchmark for Python v0.1

This file is part of the Open Web Application Security Project (OWASP) Benchmark Project.
For details, please see https://owasp.org/www-project-benchmark.

The OWASP Benchmark is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation, version 3.

The OWASP Benchmark is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

  Author: Theo Cartsonis
  Created: 2025
'''

from flask import redirect, url_for, request, make_response, render_template
from helpers.utils import escape_for_html

def init(app):

	@app.route('/benchmark/trustbound-00/BenchmarkTest00505', methods=['GET'])
	def BenchmarkTest00505_get():
		return BenchmarkTest00505_post()

	@app.route('/benchmark/trustbound-00/BenchmarkTest00505', methods=['POST'])
	def BenchmarkTest00505_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00505")
		if not param:
		    param = ""

		string16692 = 'help'
		string16692 += param
		string16692 += 'snapes on a plane'
		bar = string16692[4:-17]

		import flask

		flask.session[bar] = '12345'

		RESPONSE += (
			f'Item: \'{escape_for_html(bar)}'
			'\' with value: 12345 saved in session.'
		)

		return RESPONSE

