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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01022', methods=['GET'])
	def BenchmarkTest01022_get():
		return BenchmarkTest01022_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01022', methods=['POST'])
	def BenchmarkTest01022_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf45923 = configparser.ConfigParser()
		conf45923.add_section('section45923')
		conf45923.set('section45923', 'keyA-45923', 'a_Value')
		conf45923.set('section45923', 'keyB-45923', param)
		bar = conf45923.get('section45923', 'keyA-45923')

		import helpers.utils

		fileName = None
		fd = None

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			with open(fileName, 'rb') as fd:
				RESPONSE += (
					f'The beginning of file: \'{escape_for_html(fileName)}\' is:\n\n'
					f'{escape_for_html(fd.read(1000).decode('utf-8'))}'
				)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{fileName}\': '
				f'{escape_for_html(e.strerror)}'
			)

		return RESPONSE

