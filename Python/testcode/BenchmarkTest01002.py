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

	@app.route('/benchmark/codeinj-00/BenchmarkTest01002', methods=['GET'])
	def BenchmarkTest01002_get():
		return BenchmarkTest01002_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest01002', methods=['POST'])
	def BenchmarkTest01002_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest01002" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest01002"}\'."
		param = query_string[paramLoc + len("BenchmarkTest01002") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		import configparser
		
		bar = 'safe!'
		conf19987 = configparser.ConfigParser()
		conf19987.add_section('section19987')
		conf19987.set('section19987', 'keyA-19987', 'a-Value')
		conf19987.set('section19987', 'keyB-19987', param)
		bar = conf19987.get('section19987', 'keyB-19987')

		if not bar.startswith('\'') or not bar.endswith('\'') or '\'' in bar[1:-1]:
			RESPONSE += (
				"Exec argument must be a plain string literal."
			)
			return RESPONSE

		try:
			exec(bar)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(bar)}\''
			)

		return RESPONSE

