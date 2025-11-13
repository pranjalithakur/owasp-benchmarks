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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00531', methods=['GET'])
	def BenchmarkTest00531_get():
		return BenchmarkTest00531_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00531', methods=['POST'])
	def BenchmarkTest00531_post():
		RESPONSE = ""

		param = ""
		headers = request.headers.getlist("BenchmarkTest00531")
		
		if headers:
			param = headers[0]

		import configparser
		
		bar = 'safe!'
		conf18258 = configparser.ConfigParser()
		conf18258.add_section('section18258')
		conf18258.set('section18258', 'keyA-18258', 'a_Value')
		conf18258.set('section18258', 'keyB-18258', param)
		bar = conf18258.get('section18258', 'keyA-18258')

		import pathlib
		import helpers.utils

		testfiles = pathlib.Path(helpers.utils.TESTFILES_DIR)
		p = (testfiles / bar).resolve()

		if not str(p).startswith(str(testfiles)):
			RESPONSE += (
				"Invalid Path."
			)
			return RESPONSE
		
		if p.exists():
			RESPONSE += ( f"File \'{escape_for_html(str(p))}\' exists." )
		else:
			RESPONSE += ( f"File \'{escape_for_html(str(p))}\' does not exist." )

		return RESPONSE

