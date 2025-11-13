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

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01014', methods=['GET'])
	def BenchmarkTest01014_get():
		return BenchmarkTest01014_post()

	@app.route('/benchmark/pathtraver-01/BenchmarkTest01014', methods=['POST'])
	def BenchmarkTest01014_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf47305 = configparser.ConfigParser()
		conf47305.add_section('section47305')
		conf47305.set('section47305', 'keyA-47305', 'a-Value')
		conf47305.set('section47305', 'keyB-47305', param)
		bar = conf47305.get('section47305', 'keyB-47305')

		import helpers.utils

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			fd = open(fileName, 'wb')
			RESPONSE += (
				f'Now ready to write to file: {escape_for_html(fileName)}'
			)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{escape_for_html(fileName)}\': '
				f'{escape_for_html(e.strerror)}'
			)
		finally:
			try:
				if fd is not None:
					fd.close()
			except IOError:
				pass # "// we tried..."

		return RESPONSE

