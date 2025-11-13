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

	@app.route('/benchmark/xxe-00/BenchmarkTest00858', methods=['GET'])
	def BenchmarkTest00858_get():
		return BenchmarkTest00858_post()

	@app.route('/benchmark/xxe-00/BenchmarkTest00858', methods=['POST'])
	def BenchmarkTest00858_post():
		RESPONSE = ""

		import helpers.separate_request
		
		wrapped = helpers.separate_request.request_wrapper(request)
		param = wrapped.get_query_parameter("BenchmarkTest00858")
		if not param:
			param = ""

		import configparser
		
		bar = 'safe!'
		conf89511 = configparser.ConfigParser()
		conf89511.add_section('section89511')
		conf89511.set('section89511', 'keyA-89511', 'a_Value')
		conf89511.set('section89511', 'keyB-89511', param)
		bar = conf89511.get('section89511', 'keyA-89511')

		import xml.dom.minidom
		import xml.sax.handler

		try:
			parser = xml.sax.make_parser()
			# all features are disabled by default
			parser.setFeature(xml.sax.handler.feature_external_ges, True)

			doc = xml.dom.minidom.parseString(bar, parser)

			out = ''
			processing = [doc.documentElement]
			while processing:
				e = processing.pop(0)
				if e.nodeType == xml.dom.Node.TEXT_NODE:
					out += e.data
				else:
					processing[:0] = e.childNodes

			RESPONSE += (
				f'Your XML doc results are: <br>{escape_for_html(out)}'
			)
		except:
			RESPONSE += (
				f'There was an error reading your XML doc:<br>{escape_for_html(bar)}'
			)

		return RESPONSE

