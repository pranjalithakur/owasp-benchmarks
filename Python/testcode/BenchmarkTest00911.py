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

	@app.route('/benchmark/cmdi-00/BenchmarkTest00911', methods=['GET'])
	def BenchmarkTest00911_get():
		return BenchmarkTest00911_post()

	@app.route('/benchmark/cmdi-00/BenchmarkTest00911', methods=['POST'])
	def BenchmarkTest00911_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00911")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf92454 = configparser.ConfigParser()
		conf92454.add_section('section92454')
		conf92454.set('section92454', 'keyA-92454', 'a_Value')
		conf92454.set('section92454', 'keyB-92454', param)
		bar = conf92454.get('section92454', 'keyA-92454')

		import os
		import subprocess
		import helpers.utils

		argList = []
		if "Windows" in os.name:
			argList.append("cmd.exe")
			argList.append("-c")
		else:
			argList.append("sh")
			argList.append("-c")
		argList.append(f"echo {bar}")

		proc = subprocess.run(argList, capture_output=True, encoding="utf-8")
		RESPONSE += (
			helpers.utils.commandOutput(proc)
		)

		return RESPONSE

