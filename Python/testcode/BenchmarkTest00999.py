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

	@app.route('/benchmark/codeinj-00/BenchmarkTest00999', methods=['GET'])
	def BenchmarkTest00999_get():
		return BenchmarkTest00999_post()

	@app.route('/benchmark/codeinj-00/BenchmarkTest00999', methods=['POST'])
	def BenchmarkTest00999_post():
		RESPONSE = ""

		import urllib.parse
		
		query_string = request.query_string.decode('utf-8')
		paramLoc = query_string.find("BenchmarkTest00999" + '=')
		if paramLoc == -1:
			return f"request.query_string did not contain expected parameter \'{"BenchmarkTest00999"}\'."
		param = query_string[paramLoc + len("BenchmarkTest00999") + 1:]
		ampLoc = param.find('&')
		if ampLoc != -1:
			param = param[:ampLoc]
		
		param = urllib.parse.unquote_plus(param)

		import configparser
		
		bar = 'safe!'
		conf83950 = configparser.ConfigParser()
		conf83950.add_section('section83950')
		conf83950.set('section83950', 'keyA-83950', 'a-Value')
		conf83950.set('section83950', 'keyB-83950', param)
		bar = conf83950.get('section83950', 'keyB-83950')

		try:
			exec(bar)
		except:
			RESPONSE += (
				f'Error executing statement \'{escape_for_html(bar)}\''
			)

		return RESPONSE

