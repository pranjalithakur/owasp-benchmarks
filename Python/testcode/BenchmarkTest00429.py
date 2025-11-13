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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00429', methods=['GET'])
	def BenchmarkTest00429_get():
		return BenchmarkTest00429_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00429', methods=['POST'])
	def BenchmarkTest00429_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00429" in request.form.getlist(name):
				param = name
				break

		map56584 = {}
		map56584['keyA-56584'] = 'a-Value'
		map56584['keyB-56584'] = param
		map56584['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map56584['keyB-56584']
		bar = map56584['keyA-56584']

		if not bar.startswith('\'') or not bar.endswith('\'') or '\'' in bar[1:-1]:
			RESPONSE += (
				"Eval argument must be a plain string literal."
			)
			return RESPONSE		

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

