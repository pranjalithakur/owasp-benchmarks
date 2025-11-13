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

	@app.route('/benchmark/xpathi-01/BenchmarkTest01034', methods=['GET'])
	def BenchmarkTest01034_get():
		return BenchmarkTest01034_post()

	@app.route('/benchmark/xpathi-01/BenchmarkTest01034', methods=['POST'])
	def BenchmarkTest01034_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf51694 = configparser.ConfigParser()
		conf51694.add_section('section51694')
		conf51694.set('section51694', 'keyA-51694', 'a_Value')
		conf51694.set('section51694', 'keyB-51694', param)
		bar = conf51694.get('section51694', 'keyA-51694')

		import elementpath
		import xml.etree.ElementTree as ET
		import helpers.utils

		try:
			root = ET.parse(f'{helpers.utils.RES_DIR}/employees.xml')
			nodes = elementpath.select(root, f"/Employees/Employee[@emplid=\'{bar.replace('\'', '&apos;')}\']")
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

