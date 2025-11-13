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

	@app.route('/benchmark/codeinj-00/BenchmarkTest01100', methods=['GET'])
	def BenchmarkTest01100_get():
		return BenchmarkTest01100_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest01100', methods=['POST'])
	def BenchmarkTest01100_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		map30057 = {}
		map30057['keyA-30057'] = 'a-Value'
		map30057['keyB-30057'] = param
		map30057['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map30057['keyB-30057']
		bar = map30057['keyA-30057']

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

