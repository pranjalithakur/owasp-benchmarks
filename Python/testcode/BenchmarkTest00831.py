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

	@app.route('/benchmark/deserialization-00/BenchmarkTest00831', methods=['GET'])
	def BenchmarkTest00831_get():
		return BenchmarkTest00831_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00831', methods=['POST'])
	def BenchmarkTest00831_post():
		RESPONSE = ""

		values = request.args.getlist("BenchmarkTest00831")
		param = ""
		if values:
			param = values[0]

		map69063 = {}
		map69063['keyA-69063'] = 'a-Value'
		map69063['keyB-69063'] = param
		map69063['keyC'] = 'another-Value'
		bar = map69063['keyB-69063']

		import yaml

		try:
			yobj = yaml.load(bar, Loader=yaml.Loader)

			RESPONSE += (
				yobj['text']
			)
		except:
			RESPONSE += (
				"There was an error loading the configuration"
			)

		return RESPONSE

