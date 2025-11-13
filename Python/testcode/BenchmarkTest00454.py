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

	@app.route('/benchmark/xss-00/BenchmarkTest00454', methods=['GET'])
	def BenchmarkTest00454_get():
		return BenchmarkTest00454_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00454', methods=['POST'])
	def BenchmarkTest00454_post():
		RESPONSE = ""

		param = request.headers.get("Referer")
		if not param:
		    param = ""

		import configparser
		
		bar = 'safe!'
		conf5528 = configparser.ConfigParser()
		conf5528.add_section('section5528')
		conf5528.set('section5528', 'keyA-5528', 'a_Value')
		conf5528.set('section5528', 'keyB-5528', param)
		bar = conf5528.get('section5528', 'keyA-5528')


		otherarg = "static text"
		RESPONSE += (
			'bar is \'{0}\' and otherarg is \'{1}\''.format(bar, otherarg)
		)

		return RESPONSE

