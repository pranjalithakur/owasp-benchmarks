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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00874', methods=['GET'])
	def BenchmarkTest00874_get():
		return BenchmarkTest00874_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00874', methods=['POST'])
	def BenchmarkTest00874_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00874")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf19250 = configparser.ConfigParser()
		conf19250.add_section('section19250')
		conf19250.set('section19250', 'keyA-19250', 'a_Value')
		conf19250.set('section19250', 'keyB-19250', param)
		bar = conf19250.get('section19250', 'keyA-19250')

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest00874'[13:]
		user = f'SafeRandy{num}'
		cookie = f'rememberMe{num}'
		value = str(random.SystemRandom().getrandbits(32))

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

