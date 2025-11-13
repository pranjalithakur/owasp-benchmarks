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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00427', methods=['GET'])
	def BenchmarkTest00427_get():
		return BenchmarkTest00427_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00427', methods=['POST'])
	def BenchmarkTest00427_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00427" in request.form.getlist(name):
				param = name
				break

		import configparser
		
		bar = 'safe!'
		conf79107 = configparser.ConfigParser()
		conf79107.add_section('section79107')
		conf79107.set('section79107', 'keyA-79107', 'a-Value')
		conf79107.set('section79107', 'keyB-79107', param)
		bar = conf79107.get('section79107', 'keyB-79107')

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

