import dpkt
import socket
import pygeoip
from typing import Dict

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def retKML(dstip: str, srcip: str) -> str:
    dst: Dict[str, float] = gi.record_by_name(dstip)
    src: Dict[str, float] = gi.record_by_name('x.xxx.xxx.xxx')
    try:
        dstlongitude: float = dst['longitude']
        dstlatitude: float  = dst['latitude']
        srclongitude: float = src['longitude']
        srclatitude: float = src['latitude']
        kml: str = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f, %6f\n%6f, %6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''

def plotIPs(pcap: dpkt.pcap.Reader) -> str:
    kmlPts: str = ''
    for(ts, buf) in pcap:
        try:
            eth: dpkt.ethernet.Ethernet = dpkt.ethernet.Ethernet(buf)
            ip: dpkt.ip.IP = eth.data
            src: str = socket.inet_ntoa(ip.src)
            dst: str = socket.inet_ntoa(ip.dst)
            KML: str = retKML(dst, src)
            kmlPts += KML
        except:
            pass
    return kmlPts

def main() -> None:
    f = open('wire.pcap', 'rb')
    pcap: dpkt.pcap.Reader = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="https://www.opengis.net/kml/2.2">\n<Document>\n'\
        '<Style id="transBluePoly">'\
            '<LineStyle>'\
            '<width>1.5</width>'\
            '<color>501400E6</color>'\
            '</LineStyle>'\
            '</Style>'
    kmlfooter: str = '</Document>\n</kml>\n'
    kmldoc: str = kmlheader + plotIPs(pcap) + kmlfooter
    print(kmldoc)

if __name__ == "__main__":
    main()

