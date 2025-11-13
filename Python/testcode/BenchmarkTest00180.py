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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00180', methods=['GET'])
	def BenchmarkTest00180_get():
		return BenchmarkTest00180_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00180', methods=['POST'])
	def BenchmarkTest00180_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00180")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf84140 = configparser.ConfigParser()
		conf84140.add_section('section84140')
		conf84140.set('section84140', 'keyA-84140', 'a_Value')
		conf84140.set('section84140', 'keyB-84140', param)
		bar = conf84140.get('section84140', 'keyA-84140')

		import os
		import helpers.utils

		fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
		if os.path.exists(fileName):
			RESPONSE += ( f"File \'{escape_for_html(fileName)}\' exists." )
		else:
			RESPONSE += ( f"File \'{escape_for_html(fileName)}\' does not exist." )

		return RESPONSE

