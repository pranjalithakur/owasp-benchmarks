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

	@app.route('/benchmark/xss-00/BenchmarkTest00439', methods=['GET'])
	def BenchmarkTest00439_get():
		return BenchmarkTest00439_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00439', methods=['POST'])
	def BenchmarkTest00439_post():
		RESPONSE = ""

		param = request.headers.get("Referer")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf92030 = configparser.ConfigParser()
		conf92030.add_section('section92030')
		conf92030.set('section92030', 'keyA-92030', 'a-Value')
		conf92030.set('section92030', 'keyB-92030', param)
		bar = conf92030.get('section92030', 'keyB-92030')


		RESPONSE += (
			f'Parameter value: {bar}'
		)

		return RESPONSE

