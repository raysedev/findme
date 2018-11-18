import shodan

SHODAN_API_KEY = "Your API Key Here"

api = shodan.Shodan(SHODAN_API_KEY)

def start():

	try:
		# Search Shodan
		results = api.search('apache')

		# Show the results
		for result in results['matches']:
			print '%s' % result['ip_str']
	except shodan.APIError, e:
		print 'Error: %s' % e
