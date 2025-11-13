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

	@app.route('/benchmark/weakrand-01/BenchmarkTest00479', methods=['GET'])
	def BenchmarkTest00479_get():
		return BenchmarkTest00479_post()

	@app.route('/benchmark/weakrand-01/BenchmarkTest00479', methods=['POST'])
	def BenchmarkTest00479_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00479")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf38098 = configparser.ConfigParser()
		conf38098.add_section('section38098')
		conf38098.set('section38098', 'keyA-38098', 'a_Value')
		conf38098.set('section38098', 'keyB-38098', param)
		bar = conf38098.get('section38098', 'keyA-38098')

		import secrets
		from helpers.utils import mysession

		num = 'BenchmarkTest00479'[13:]
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

