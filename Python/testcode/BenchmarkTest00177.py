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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00177', methods=['GET'])
	def BenchmarkTest00177_get():
		return BenchmarkTest00177_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00177', methods=['POST'])
	def BenchmarkTest00177_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00177")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf63043 = configparser.ConfigParser()
		conf63043.add_section('section63043')
		conf63043.set('section63043', 'keyA-63043', 'a-Value')
		conf63043.set('section63043', 'keyB-63043', param)
		bar = conf63043.get('section63043', 'keyB-63043')

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

