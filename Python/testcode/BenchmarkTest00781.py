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

	@app.route('/benchmark/weakrand-02/BenchmarkTest00781', methods=['GET'])
	def BenchmarkTest00781_get():
		return BenchmarkTest00781_post()

	@app.route('/benchmark/weakrand-02/BenchmarkTest00781', methods=['POST'])
	def BenchmarkTest00781_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00781")
		param = ""
		if values:
			param = values[0]

		map85207 = {}
		map85207['keyA-85207'] = 'a-Value'
		map85207['keyB-85207'] = param
		map85207['keyC'] = 'another-Value'
		bar = map85207['keyB-85207']

		import random
		from helpers.utils import mysession

		num = 'BenchmarkTest00781'[13:]
		user = f'Isaac{num}'
		cookie = f'rememberMe{num}'
		value = str(random.randint(0, 2**32))

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

