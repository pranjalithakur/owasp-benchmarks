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

	@app.route('/benchmark/codeinj-00/BenchmarkTest01174', methods=['GET'])
	def BenchmarkTest01174_get():
		return BenchmarkTest01174_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest01174', methods=['POST'])
	def BenchmarkTest01174_post():
		RESPONSE = ""

		import helpers.separate_request
		scr = helpers.separate_request.request_wrapper(request)
		param = scr.get_safe_value("BenchmarkTest01174")

		import configparser
		
		bar = 'safe!'
		conf80725 = configparser.ConfigParser()
		conf80725.add_section('section80725')
		conf80725.set('section80725', 'keyA-80725', 'a-Value')
		conf80725.set('section80725', 'keyB-80725', param)
		bar = conf80725.get('section80725', 'keyB-80725')

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

