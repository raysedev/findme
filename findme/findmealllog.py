import shodan

SHODAN_API_KEY = "Your API Key Here"

api = shodan.Shodan(SHODAN_API_KEY)

try:
	# Search Shodan
	results = api.search('apache')

	# Show the results
	print 'Results found: %s' % results['total']
	for result in results['matches']:
		print 'IP: %s' % result['ip_str']
		print result['data']
		print ''
except shodan.APIError, e:
	print 'Error: %s' % e
