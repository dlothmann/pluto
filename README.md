# Pluto Port Scanner

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/35cb96c3e9fa4bf9938a95f057dc68de)](https://www.codacy.com/gh/dlothmann/pluto/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dlothmann/pluto&amp;utm_campaign=Badge_Grade)

Pluto Port Scanner is a Python tool for scanning tcp ports.

## Installation

Clone the repo to your computer 

```git
git clone https://github.com/dlothmann/pluto.git
```

## Usage

```bash
portscan.py -H <ADDRESS> -p1 <PORT>

```
Other Arguments

````bash
-H  | Host Address or IP Address
-p1 | When only one port than port you would scan otherwise Startport of the range
````
Optinal
````bash
-p2 | End Portrange
-a  | Show closed and open ports
````

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[BSD 3 Clause Clear](https://choosealicense.com/licenses/bsd-3-clause-clear/)
