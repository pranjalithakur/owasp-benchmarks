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

	@app.route('/benchmark/deserialization-00/BenchmarkTest00741', methods=['GET'])
	def BenchmarkTest00741_get():
		return BenchmarkTest00741_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00741', methods=['POST'])
	def BenchmarkTest00741_post():
		RESPONSE = ""

		param = request.args.get("BenchmarkTest00741")
		if not param:
			param = ""

		map19474 = {}
		map19474['keyA-19474'] = 'a-Value'
		map19474['keyB-19474'] = param
		map19474['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map19474['keyB-19474']
		bar = map19474['keyA-19474']

		import yaml

		try:
			yobj = yaml.safe_load(bar)

			RESPONSE += (
				yobj['text']
			)
		except:
			RESPONSE += (
				"There was an error loading the configuration"
			)

		return RESPONSE

