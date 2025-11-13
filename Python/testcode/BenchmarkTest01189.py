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

	@app.route('/benchmark/codeinj-00/BenchmarkTest01189', methods=['GET'])
	def BenchmarkTest01189_get():
		response = make_response(render_template('web/codeinj-00/BenchmarkTest01189.html'))
		response.set_cookie('BenchmarkTest01189', '%27RESPONSE+%2B%3D+%5C%27ECHOOO%5C%27%27',
			max_age=60*3,
			secure=True,
			path=request.path,
			domain='localhost')
		return response
		return BenchmarkTest01189_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest01189', methods=['POST'])
	def BenchmarkTest01189_post():
		RESPONSE = ""

		import urllib.parse
		param = urllib.parse.unquote_plus(request.cookies.get("BenchmarkTest01189", "noCookieValueSupplied"))


		if not param.startswith('\'') or not param.endswith('\'') or '\'' in param[1:-1]:
			RESPONSE += (
				"Exec argument must be a plain string literal."
			)
			return RESPONSE

		try:
			exec(param)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(param)}\''
			)

		return RESPONSE


