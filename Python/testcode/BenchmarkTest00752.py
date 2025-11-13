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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00752', methods=['GET'])
	def BenchmarkTest00752_get():
		return BenchmarkTest00752_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00752', methods=['POST'])
	def BenchmarkTest00752_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00752")
		param = ""
		if values:
			param = values[0]

		num = 86
		
		if 7 * 42 - num > 200:
			bar = 'This_should_always_happen'
		else:
			bar = param

		import os
		import helpers.utils

		fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
		if os.path.exists(fileName):
			RESPONSE += ( f"File \'{escape_for_html(fileName)}\' exists." )
		else:
			RESPONSE += ( f"File \'{escape_for_html(fileName)}\' does not exist." )

		return RESPONSE

