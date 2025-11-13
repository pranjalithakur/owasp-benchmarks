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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00087', methods=['GET'])
	def BenchmarkTest00087_get():
		return BenchmarkTest00087_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00087', methods=['POST'])
	def BenchmarkTest00087_post():
		RESPONSE = ""

		param = request.form.get("BenchmarkTest00087")
		if not param:
			param = ""

		map48394 = {}
		map48394['keyA-48394'] = 'a-Value'
		map48394['keyB-48394'] = param
		map48394['keyC'] = 'another-Value'
		bar = "safe!"
		bar = map48394['keyB-48394']
		bar = map48394['keyA-48394']

		import helpers.utils

		if '../' in bar:
			RESPONSE += (
				'File name must not contain \'../\''
			)
			return RESPONSE

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

