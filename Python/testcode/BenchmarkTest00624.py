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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00624', methods=['GET'])
	def BenchmarkTest00624_get():
		return BenchmarkTest00624_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest00624', methods=['POST'])
	def BenchmarkTest00624_post():
		RESPONSE = ""

		import helpers.utils
		param = ""
		
		for name in request.headers.keys():
			if name.lower() in helpers.utils.commonHeaderNames:
				continue
		
			if request.headers.get_all(name):
				param = name
				break

		map72992 = {}
		map72992['keyA-72992'] = 'a-Value'
		map72992['keyB-72992'] = param
		map72992['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map72992['keyB-72992']
		bar = map72992['keyA-72992']

		import pathlib
		import helpers.utils

		try:
			testfiles = pathlib.Path(helpers.utils.TESTFILES_DIR)
			p = testfiles / bar
			RESPONSE += (
				f'The beginning of file: \'{escape_for_html(str(p))}\' is:\n\n'
				f'{escape_for_html(p.read_text()[:1000])}'
			)
		except OSError:
			RESPONSE += (
				f'Problem reading from file \'{fileName}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE

