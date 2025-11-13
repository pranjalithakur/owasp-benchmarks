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

	@app.route('/benchmark/deserialization-00/BenchmarkTest00910', methods=['GET'])
	def BenchmarkTest00910_get():
		return BenchmarkTest00910_post()

	@app.route('/benchmark/deserialization-00/BenchmarkTest00910', methods=['POST'])
	def BenchmarkTest00910_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00910")
		if not param:
			param = ""

		bar = "alsosafe"
		if param:
			lst = []
			lst.append('safe')
			lst.append(param)
			lst.append('moresafe')
			lst.pop(0)
			bar = lst[1]

		import pickle
		import base64
		import helpers.utils

		helpers.utils.sharedstr = "no pickles to be seen here"

		try:
			unpickled = pickle.loads(base64.urlsafe_b64decode(bar))
		except:
			RESPONSE += (
				'Unpickling failed!'
			)
			return RESPONSE

		RESPONSE += (
			f'shared string is {helpers.utils.sharedstr}'
		)

		return RESPONSE

