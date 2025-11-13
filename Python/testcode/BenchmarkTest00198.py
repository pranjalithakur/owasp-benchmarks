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

	@app.route('/benchmark/sqli-00/BenchmarkTest00198', methods=['GET'])
	def BenchmarkTest00198_get():
		return BenchmarkTest00198_post()

	@app.route('/benchmark/sqli-00/BenchmarkTest00198', methods=['POST'])
	def BenchmarkTest00198_post():
		RESPONSE = ""

		values = request.form.getlist("BenchmarkTest00198")
		param = ""
		if values:
			param = values[0]

		map35082 = {}
		map35082['keyA-35082'] = 'a-Value'
		map35082['keyB-35082'] = param
		map35082['keyC'] = 'another-Value'
		bar = map35082['keyB-35082']

		import helpers.db_sqlite

		sql = f'SELECT username from USERS where password = ?'
		con = helpers.db_sqlite.get_connection()
		cur = con.cursor()
		cur.execute(sql, (bar,))
		RESPONSE += (
			helpers.db_sqlite.results(cur, sql)
		)
		con.close()

		return RESPONSE

