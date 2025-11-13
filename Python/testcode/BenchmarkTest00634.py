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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00634', methods=['GET'])
	def BenchmarkTest00634_get():
		return BenchmarkTest00634_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00634', methods=['POST'])
	def BenchmarkTest00634_post():
		RESPONSE = ""

		import helpers.utils
		param = ""
		
		for name in request.headers.keys():
			if name.lower() in helpers.utils.commonHeaderNames:
				continue
		
			if request.headers.get_all(name):
				param = name
				break

		string7647 = ''
		data12 = ''
		copy = string7647
		string7647 = ''
		string7647 += param
		copy += 'SomeOKString'
		bar = copy

		import secrets
		from helpers.utils import mysession

		num = 'BenchmarkTest00634'[13:]
		user = f'SafeRicky{num}'
		cookie = f'rememberMe{num}'
		value = str(secrets.randbits(32))

		if cookie in mysession and request.cookies.get(cookie) == mysession[cookie]:
			RESPONSE += (
				f'Welcome back: {user}<br/>'
			)
		else:
			mysession[cookie] = value
			RESPONSE += (
				f'{user} has been remembered with cookie:'
				f'{cookie} whose value is: {mysession[cookie]}<br/>'
			)

		return RESPONSE

