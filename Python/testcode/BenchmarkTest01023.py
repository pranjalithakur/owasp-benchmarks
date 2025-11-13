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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01023', methods=['GET'])
	def BenchmarkTest01023_get():
		return BenchmarkTest01023_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01023', methods=['POST'])
	def BenchmarkTest01023_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		bar = "This should never happen"
		if 'should' not in bar:
		        bar = "Ifnot case passed"

		import helpers.utils

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			with open(fileName, 'wb') as fd:
				RESPONSE += (
					f'Now ready to write to file: {escape_for_html(fileName)}'
				)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE

