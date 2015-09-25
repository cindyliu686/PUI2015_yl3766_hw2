import sys
import json
import urllib2

if __name__ == '__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
	request = urllib2.urlopen(url)
	busjsonfile = json.load(request)
	
	#Text code for local file:
	#primaryfile = open(sys.argv[1],'r')  #try both original file and formatted file 
	#busjsonfile = json.load(primaryfile)

	vc = busjsonfile["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"] # vs is a list

	print 'Bus Line : B52' 
	print 'Number of Active Buses : %s' % len(vc)

	n = 0
	for bus in vc[:5]:
		print 'Bus %i is at latitude %f and longitude %f' % (n,bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],
			bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
		n += 1