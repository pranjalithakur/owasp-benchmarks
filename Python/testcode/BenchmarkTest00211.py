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

	@app.route('/benchmark/xpathi-00/BenchmarkTest00211', methods=['GET'])
	def BenchmarkTest00211_get():
		return BenchmarkTest00211_post()

	@app.route('/benchmark/xpathi-00/BenchmarkTest00211', methods=['POST'])
	def BenchmarkTest00211_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00211")
		param = ""
		if values:
			param = values[0]

		import configparser
		
		bar = 'safe!'
		conf37760 = configparser.ConfigParser()
		conf37760.add_section('section37760')
		conf37760.set('section37760', 'keyA-37760', 'a_Value')
		conf37760.set('section37760', 'keyB-37760', param)
		bar = conf37760.get('section37760', 'keyA-37760')

		import lxml.etree
		import helpers.utils

		try:
			fd = open(f'{helpers.utils.RES_DIR}/employees.xml', 'rb')
			root = lxml.etree.parse(fd)
			query = f'/Employees/Employee[@emplid=\'{bar}\']'
			run_query = lxml.etree.XPath(query)
			nodes = run_query(root)
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

