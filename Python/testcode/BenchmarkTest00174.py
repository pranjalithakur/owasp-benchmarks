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

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00174', methods=['GET'])
	def BenchmarkTest00174_get():
		return BenchmarkTest00174_post()

	@app.route('/benchmark/pathtraver-00/BenchmarkTest00174', methods=['POST'])
	def BenchmarkTest00174_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00174")
		param = ""
		if values:
			param = values[0]

		string56895 = 'help'
		string56895 += param
		string56895 += 'snapes on a plane'
		bar = string56895[4:-17]

		import codecs
		import helpers.utils

		try:
			fileTarget = codecs.open(f'{helpers.utils.TESTFILES_DIR}/{bar}','r','utf-8')

			RESPONSE += (
				f"Access to file: \'{escape_for_html(fileTarget.name)}\' created."
			)

			RESPONSE += (
				" And file already exists."
			)

		except FileNotFoundError:
			RESPONSE += (
				" But file doesn't exist yet."
			)

		return RESPONSE

