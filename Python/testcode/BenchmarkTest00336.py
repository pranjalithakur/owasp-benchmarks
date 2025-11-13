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

	@app.route('/benchmark/xss-00/BenchmarkTest00336', methods=['GET'])
	def BenchmarkTest00336_get():
		return BenchmarkTest00336_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00336', methods=['POST'])
	def BenchmarkTest00336_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00336")
		if not param:
			param = ""

		map30382 = {}
		map30382['keyA-30382'] = 'a-Value'
		map30382['keyB-30382'] = param
		map30382['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map30382['keyB-30382']
		bar = map30382['keyA-30382']


		RESPONSE += (
			'The value of the bar parameter is now in a custom header.'
		)

		RESPONSE = make_response((RESPONSE, {'yourBenchmarkTest00336': bar}))
		

		return RESPONSE

