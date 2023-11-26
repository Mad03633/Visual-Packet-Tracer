# Visual Packet Tracer

## Overview

Visual Packet Tracer is a Python project that reads network packet data from a pcap file, extracts source and destination IP addresses, and generates a KML file for visualizing the communication paths on a map.

## Requirements

- Python 3
- dpkt library
- pygeoip library
- GeoLiteCity.dat database file

## Usage

1. Install the required libraries:
   ```
   pip install dpkt pygeoip
   ```

2. Download the GeoLiteCity.dat database file and place it in the project directory.
https://github.com/mbcc2006/GeoLiteCity-data 

3. Capture network traffic using Wireshark:
- Open Wireshark and start capturing traffic on the desired interface.
- Once you have captured enough data, stop the capture.
- Save the captured packets as a pcap file (e.g., wire.pcap).

4. Run the main.py script:
```
python main.py
```
This will output the KML directly to the console.

## File Structure

- main.py: The main script containing the code for reading pcap files, extracting IP addresses, and generating KML.
- GeoLiteCity.dat: The GeoIP database file used for retrieving geographical information based on IP addresses.

## Output
The KML output will be displayed in the console. You can copy and paste this output into a new KML file or use a redirection command to save it to a file:
```
python main.py > output.kml
```

## Notes
Ensure the 'wire.pcap' file is captured using Wireshark and is present in the project directory.
In case of missing geographical information for an IP address, the corresponding entry will be skipped in the visualization.

## Acknowledgments
This project uses the dpkt and pygeoip libraries for handling packet data and GeoIP information, respectively.

