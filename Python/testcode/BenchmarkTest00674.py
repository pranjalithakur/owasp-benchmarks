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

	@app.route('/benchmark/xss-00/BenchmarkTest00674', methods=['GET'])
	def BenchmarkTest00674_get():
		return BenchmarkTest00674_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00674', methods=['POST'])
	def BenchmarkTest00674_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00674")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf19540 = configparser.ConfigParser()
		conf19540.add_section('section19540')
		conf19540.set('section19540', 'keyA-19540', 'a_Value')
		conf19540.set('section19540', 'keyB-19540', param)
		bar = conf19540.get('section19540', 'keyA-19540')


		otherarg = "static text"
		RESPONSE += (
			'bar is \'{0}\' and otherarg is \'{1}\''.format(bar, otherarg)
		)

		return RESPONSE

