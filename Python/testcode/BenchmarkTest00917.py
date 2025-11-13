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

	@app.route('/benchmark/deserialization-00/BenchmarkTest00917', methods=['GET'])
	def BenchmarkTest00917_get():
		return BenchmarkTest00917_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00917', methods=['POST'])
	def BenchmarkTest00917_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00917")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf10263 = configparser.ConfigParser()
		conf10263.add_section('section10263')
		conf10263.set('section10263', 'keyA-10263', 'a_Value')
		conf10263.set('section10263', 'keyB-10263', param)
		bar = conf10263.get('section10263', 'keyA-10263')

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

