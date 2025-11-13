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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00428', methods=['GET'])
	def BenchmarkTest00428_get():
		return BenchmarkTest00428_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00428', methods=['POST'])
	def BenchmarkTest00428_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00428" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf3150 = configparser.ConfigParser()
		conf3150.add_section('section3150')
		conf3150.set('section3150', 'keyA-3150', 'a_Value')
		conf3150.set('section3150', 'keyB-3150', param)
		bar = conf3150.get('section3150', 'keyA-3150')

		if not bar.startswith('\'') or not bar.endswith('\'') or '\'' in bar[1:-1]:
			RESPONSE += (
				"Eval argument must be a plain string literal."
			)
			return RESPONSE		

		try:
			RESPONSE += (
				eval(bar)
			)
		except:
			RESPONSE += (
				f'Error evaluating expression \'{escape_for_html(bar)}\''
			)

		return RESPONSE

