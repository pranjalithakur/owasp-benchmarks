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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00095', methods=['GET'])
	def BenchmarkTest00095_get():
		return BenchmarkTest00095_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00095', methods=['POST'])
	def BenchmarkTest00095_post():
		RESPONSE = ""

		param = request.form.get("BenchmarkTest00095")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf8581 = configparser.ConfigParser()
		conf8581.add_section('section8581')
		conf8581.set('section8581', 'keyA-8581', 'a-Value')
		conf8581.set('section8581', 'keyB-8581', param)
		bar = conf8581.get('section8581', 'keyB-8581')

		import helpers.utils

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			with open(fileName, 'wb') as fd:
				RESPONSE += (
					f'Now ready to write to file: {escape_for_html(fileName)}'
				)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE

