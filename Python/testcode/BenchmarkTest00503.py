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

	@app.route('/benchmark/redirect-00/BenchmarkTest00503', methods=['GET'])
	def BenchmarkTest00503_get():
		return BenchmarkTest00503_post()

	@app.route('/benchmark/redirect-00/BenchmarkTest00503', methods=['POST'])
	def BenchmarkTest00503_post():
		RESPONSE = ""

		param = request.headers.get("BenchmarkTest00503")
		if not param:
		    param = ""

		import markupsafe
		
		bar = markupsafe.escape(param)

		import flask

		return flask.redirect(bar)

		return RESPONSE

