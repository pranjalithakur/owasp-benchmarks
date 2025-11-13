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

	@app.route('/benchmark/xss-00/BenchmarkTest00368', methods=['GET'])
	def BenchmarkTest00368_get():
		return BenchmarkTest00368_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00368', methods=['POST'])
	def BenchmarkTest00368_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00368" in request.form.getlist(name):
				param = name
				break

		map66599 = {}
		map66599['keyA-66599'] = 'a-Value'
		map66599['keyB-66599'] = param
		map66599['keyC'] = 'another-Value'
		bar = map66599['keyB-66599']


		otherarg = "static text"
		RESPONSE += (
			'bar is \'%s\' and otherarg is \'%s\'' % (bar, otherarg)
		)

		return RESPONSE

