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

	@app.route('/benchmark/xss-00/BenchmarkTest00353', methods=['GET'])
	def BenchmarkTest00353_get():
		return BenchmarkTest00353_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00353', methods=['POST'])
	def BenchmarkTest00353_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00353" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf28092 = configparser.ConfigParser()
		conf28092.add_section('section28092')
		conf28092.set('section28092', 'keyA-28092', 'a_Value')
		conf28092.set('section28092', 'keyB-28092', param)
		bar = conf28092.get('section28092', 'keyA-28092')


		RESPONSE += (
			f'Parameter value: {bar}'
		)

		return RESPONSE

