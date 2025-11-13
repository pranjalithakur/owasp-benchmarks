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

	@app.route('/benchmark/weakrand-03/BenchmarkTest00875', methods=['GET'])
	def BenchmarkTest00875_get():
		return BenchmarkTest00875_post()

	@app.route('/benchmark/weakrand-03/BenchmarkTest00875', methods=['POST'])
	def BenchmarkTest00875_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00875")
		if not param:
			param = ""

		map50727 = {}
		map50727['keyA-50727'] = 'a-Value'
		map50727['keyB-50727'] = param
		map50727['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map50727['keyB-50727']
		bar = map50727['keyA-50727']

		import random
		import base64
		from helpers.utils import mysession

		num = 'BenchmarkTest00875'[13:]
		user = f'SafeBarbara{num}'
		cookie = f'rememberMe{num}'
		value = str(base64.b64encode(random.SystemRandom().randbytes(32)))

		if cookie in mysession and request.cookies.get(cookie) == mysession[cookie]:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
		else:
			mysession[cookie] = value
			RESPONSE += (
				f'{user} has been remembered with cookie: '
				f'{cookie} whose value is: {mysession[cookie]}<br/>'
			)

		return RESPONSE

