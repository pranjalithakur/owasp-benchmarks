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

	@app.route('/benchmark/xss-00/BenchmarkTest00415', methods=['GET'])
	def BenchmarkTest00415_get():
		return BenchmarkTest00415_post()

	@app.route('/benchmark/xss-00/BenchmarkTest00415', methods=['POST'])
	def BenchmarkTest00415_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00415" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf88136 = configparser.ConfigParser()
		conf88136.add_section('section88136')
		conf88136.set('section88136', 'keyA-88136', 'a-Value')
		conf88136.set('section88136', 'keyB-88136', param)
		bar = conf88136.get('section88136', 'keyB-88136')


		RESPONSE += (
			'The value of the bar parameter is now in a custom header.'
		)

		RESPONSE = make_response((RESPONSE, {'yourBenchmarkTest00415': bar}))
		

		return RESPONSE

