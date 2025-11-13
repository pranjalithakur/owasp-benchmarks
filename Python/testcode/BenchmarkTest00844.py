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

	@app.route('/benchmark/xss-00/BenchmarkTest00844', methods=['GET'])
	def BenchmarkTest00844_get():
		return BenchmarkTest00844_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00844', methods=['POST'])
	def BenchmarkTest00844_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00844")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf1036 = configparser.ConfigParser()
		conf1036.add_section('section1036')
		conf1036.set('section1036', 'keyA-1036', 'a_Value')
		conf1036.set('section1036', 'keyB-1036', param)
		bar = conf1036.get('section1036', 'keyA-1036')


		otherarg = "static text"
		RESPONSE += (
			f'bar is \'{bar}\' and otherarg is \'{otherarg}\''
		)

		return RESPONSE

