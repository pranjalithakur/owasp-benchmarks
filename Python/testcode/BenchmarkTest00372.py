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

	@app.route('/benchmark/xpathi-00/BenchmarkTest00372', methods=['GET'])
	def BenchmarkTest00372_get():
		return BenchmarkTest00372_post()

	@app.route('/benchmark/xpathi-00/BenchmarkTest00372', methods=['POST'])
	def BenchmarkTest00372_post():
		RESPONSE = ""

		param = ""
		for name in request.form.keys():
			if "BenchmarkTest00372" in request.form.getlist(name):
				param = name
				break

		map15527 = {}
		map15527['keyA-15527'] = 'a-Value'
		map15527['keyB-15527'] = param
		map15527['keyC'] = 'another-Value'
		bar = map15527['keyB-15527']

		import elementpath
		import xml.etree.ElementTree as ET
		import helpers.utils

		if '\'' in bar:
			RESPONSE += (
				"Employee ID must not contain apostrophes"
			)
			return RESPONSE

		try:
			root = ET.parse(f'{helpers.utils.RES_DIR}/employees.xml')
			query = f"/Employees/Employee[@emplid=\'{bar}\']"
			nodes = elementpath.select(root, query)
			node_strings = []
			for node in nodes:
				node_strings.append(' '.join([e.text for e in node]))

			RESPONSE += (
				f'Your XPATH query results are: <br>[ {', '.join(node_strings)} ]'
			)
		except:
			RESPONSE += (
				f'Error parsing XPath Query: \'{escape_for_html(query)}\''
			)

		return RESPONSE

