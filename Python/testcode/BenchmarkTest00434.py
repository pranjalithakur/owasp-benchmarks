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

	@app.route('/benchmark/cmdi-00/BenchmarkTest00434', methods=['GET'])
	def BenchmarkTest00434_get():
		return BenchmarkTest00434_post()

	@app.route('/benchmark/cmdi-00/BenchmarkTest00434', methods=['POST'])
	def BenchmarkTest00434_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00434" in request.form.getlist(name):
				param = name
				break

		map33702 = {}
		map33702['keyA-33702'] = 'a-Value'
		map33702['keyB-33702'] = param
		map33702['keyC'] = 'another-Value'
		bar = map33702['keyB-33702']

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

