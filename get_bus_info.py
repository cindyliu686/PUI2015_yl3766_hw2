import sys
import json
import urllib2
import csv

if __name__ == '__main__':
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
	request = urllib2.urlopen(url)
	busjsonfile = json.load(request)
	vc = busjsonfile["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

	with open(sys.argv[3],'wb') as csvfile:
		filewriter = csv.writer(csvfile)

		for bus in vc:
			Latitude = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
			Longitude = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
			Stop_Name = bus["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"]
			Stop_Status = bus["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Distances"]["PresentableDistance"]
			if bus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
				Stop_Name = "N/A"
				Stop_Status = "N/A"
			row = [Latitude,Longitude,Stop_Name,Stop_Status]
			filewriter.writerow(row)
