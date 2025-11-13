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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00266', methods=['GET'])
	def BenchmarkTest00266_get():
		return BenchmarkTest00266_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00266', methods=['POST'])
	def BenchmarkTest00266_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00266")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf30925 = configparser.ConfigParser()
		conf30925.add_section('section30925')
		conf30925.set('section30925', 'keyA-30925', 'a_Value')
		conf30925.set('section30925', 'keyB-30925', param)
		bar = conf30925.get('section30925', 'keyA-30925')

		try:
			exec(bar)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(bar)}\''
			)

		return RESPONSE

