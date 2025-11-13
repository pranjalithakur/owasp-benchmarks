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

	@app.route('/benchmark/trustbound-00/BenchmarkTest00604', methods=['GET'])
	def BenchmarkTest00604_get():
		return BenchmarkTest00604_post()

	@app.route('/benchmark/trustbound-00/BenchmarkTest00604', methods=['POST'])
	def BenchmarkTest00604_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00604")
		
		if headers:
			param = headers[0]

		map92506 = {}
		map92506['keyA-92506'] = 'a-Value'
		map92506['keyB-92506'] = param
		map92506['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map92506['keyB-92506']
		bar = map92506['keyA-92506']

		import flask

		flask.session[bar] = '12345'

		RESPONSE += (
			f'Item: \'{escape_for_html(bar)}'
			'\' with value: 12345 saved in session.'
		)

		return RESPONSE

