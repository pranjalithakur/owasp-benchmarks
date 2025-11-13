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

	@app.route('/benchmark/redirect-00/BenchmarkTest00600', methods=['GET'])
	def BenchmarkTest00600_get():
		return BenchmarkTest00600_post()

	@app.route('/benchmark/redirect-00/BenchmarkTest00600', methods=['POST'])
	def BenchmarkTest00600_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00600")
		
		if headers:
			param = headers[0]

		num = 86
		
		if 7 * 42 - num > 200:
			bar = 'This_should_always_happen'
		else:
			bar = param

		import flask

		return flask.redirect(bar)

		return RESPONSE

