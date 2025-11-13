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

	@app.route('/benchmark/weakrand-03/BenchmarkTest01200', methods=['GET'])
	def BenchmarkTest01200_get():
		return BenchmarkTest01200_post()

	@app.route('/benchmark/weakrand-03/BenchmarkTest01200', methods=['POST'])
	def BenchmarkTest01200_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest01200" in request.form.getlist(name):
				param = name
				break


		import random
		import base64
		from helpers.utils import mysession

		num = 'BenchmarkTest01200'[13:]
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


