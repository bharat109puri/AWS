#!/usr/bin/python

from boto.route53.connection import Route53Connection

#### Connection Details
key = 'XXXXXXXXXXXXXXXX'
access = 'XXXXXXXXXXXXXXXXXXXXXXX'


if __name__ == '__main__':
	zones = {}
	route53 = Route53Connection(key, access)



# list existing hosted zones
results = route53.get_all_hosted_zones()

for zone in results['ListHostedZonesResponse']['HostedZones']:
	print "========================================"
	print zone['Name']
	print "\t%s" % zone['Id']
	zone_id = zone['Id'].replace('/hostedzone/', '')
	zones[zone['Name']] = zone_id
	sets = route53.get_all_rrsets(zone_id)
	for rset in sets:
		print "\t%s: %s %s @ %s" % (rset.name, rset.type, rset.resource_records, rset.ttl)

