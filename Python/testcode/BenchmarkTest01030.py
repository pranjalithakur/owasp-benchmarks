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

	@app.route('/benchmark/sqli-00/BenchmarkTest01030', methods=['GET'])
	def BenchmarkTest01030_get():
		return BenchmarkTest01030_post()

	@app.route('/benchmark/sqli-00/BenchmarkTest01030', methods=['POST'])
	def BenchmarkTest01030_post():
		RESPONSE = ""

		parts = request.path.split("/")
		param = parts[1]
		if not param:
			param = ""

		bar = "This should never happen"
		if 'should' not in bar:
		        bar = "Ifnot case passed"

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

