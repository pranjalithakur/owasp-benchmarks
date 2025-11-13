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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00178', methods=['GET'])
	def BenchmarkTest00178_get():
		return BenchmarkTest00178_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00178', methods=['POST'])
	def BenchmarkTest00178_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00178")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf84331 = configparser.ConfigParser()
		conf84331.add_section('section84331')
		conf84331.set('section84331', 'keyA-84331', 'a_Value')
		conf84331.set('section84331', 'keyB-84331', param)
		bar = conf84331.get('section84331', 'keyA-84331')

		import helpers.utils

		fileName = None
		fd = None

		if '../' in bar:
			RESPONSE += (
				'File name must not include \'../\''
			)
			return RESPONSE

		try:
			fileName = f'{helpers.utils.TESTFILES_DIR}/{bar}'
			fd = open(fileName, 'rb')
			RESPONSE += (
				f'The beginning of file: \'{escape_for_html(fileName)}\' is:\n\n'
				f'{escape_for_html(fd.read(1000).decode('utf-8'))}'
			)
		except IOError as e:
			RESPONSE += (
				f'Problem reading from file \'{fileName}\': '
				f'{escape_for_html(e.strerror)}'
			)
		finally:
			try:
				if fd is not None:
					fd.close()
			except IOError:
				pass # "// we tried..."

		return RESPONSE

