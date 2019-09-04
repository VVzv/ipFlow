# !/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import dpkt, socket
import geoip2.database

reader = geoip2.database.Reader('./GeoIP/GeoLite2-City.mmdb')

def retGeoStr(ip):
    try:
        rec = reader.city(ip)
        # city = rec.city.name
        country = rec.country.iso_code
        # geo_loc = '%s,%s' %(country, city)
        geo_loc = country
        return geo_loc
    except Exception, e:
        return 'Unknown/Intranet'

def getPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[*] Src: [%s]%s --> [%s]%s' %(retGeoStr(src), src, retGeoStr(dst), dst)
        except:
            pass

def main():
    f = open('./test.pcapng')
    pcap = dpkt.pcapng.Reader(f)
    getPcap(pcap)

if __name__ == '__main__':
    main()
