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

	@app.route('/benchmark/redirect-00/BenchmarkTest00339', methods=['GET'])
	def BenchmarkTest00339_get():
		return BenchmarkTest00339_post()

	@app.route('/benchmark/redirect-00/BenchmarkTest00339', methods=['POST'])
	def BenchmarkTest00339_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_form_parameter("BenchmarkTest00339")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf44628 = configparser.ConfigParser()
		conf44628.add_section('section44628')
		conf44628.set('section44628', 'keyA-44628', 'a-Value')
		conf44628.set('section44628', 'keyB-44628', param)
		bar = conf44628.get('section44628', 'keyB-44628')

		import flask

		return flask.redirect(bar)

		return RESPONSE

