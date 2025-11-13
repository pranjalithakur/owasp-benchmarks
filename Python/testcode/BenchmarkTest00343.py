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

	@app.route('/benchmark/trustbound-00/BenchmarkTest00343', methods=['GET'])
	def BenchmarkTest00343_get():
		return BenchmarkTest00343_post()

	@app.route('/benchmark/trustbound-00/BenchmarkTest00343', methods=['POST'])
	def BenchmarkTest00343_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00343")
		if not param:
			param = ""

		map13482 = {}
		map13482['keyA-13482'] = 'a-Value'
		map13482['keyB-13482'] = param
		map13482['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map13482['keyB-13482']
		bar = map13482['keyA-13482']

		import flask

		flask.session['userid'] = bar

		RESPONSE += (
			f'Item: \'userid\' with value \'{escape_for_html(bar)}'
			'\'saved in session.'
		)

		return RESPONSE

