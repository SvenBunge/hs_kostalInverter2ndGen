# Kostal-Wechselrichter ModbusTCP (14460)

Gira Homeserver 4 Logikmodule to poll power values from the 2nd Generation of Kostal solar energy inverter via Modbus TCP.
Compatible with Kostal PIKO 12-20 (with green front) - Not compatible with PIKO and full grey front, Plenticore or PIKO IQ / CI.

**Important: Please update your inverter firmware before you use this plugin!**

## Developer Notes

Developed for the GIRA HomeServer 4.12
Licensed under the LGPL to keep all copies & forks free!

:exclamation: **If you fork this project and distribute the module by your own CHANGE the Logikbaustein-ID because 14460 is only for this one and registered to @SvenBunge !!** :exclamation:

If something doesn't work like expected: Just open an issue. Even better: Fix the issue and fill a pull request.

## Installation

Download a [release](https://github.com/SvenBunge/hs_kostalInverter2ndGen/releases) and install the module / Logikbaustein like others in Experte.
You find the module in the category "Energiemanagement". Just pic the IP address, port and unit-id of your inverter and wire the output to your communication objects. 

The latest version of the module is also available in the [KNX-User Forum Download Section](https://service.knx-user-forum.de/?comm=download&id=14460)

## Documentation

This module fetches power information and states from home solar power inverters 2nd generation of the manufacturer "Kostal". It has been tested with the *Kostal PIKO 15 * with 3 strings attached.

More [detailed documentation](doc/log14460.md)

For further questions use the [Promotion Thread](https://knx-user-forum.de/forum/%C3%B6ffentlicher-bereich/knx-eib-forum/1559910-logikbaustein-kostal-wechselrichter-via-modbus-tcp-abfragen) of the KNX User Forum (German)

### Keep notice

* All outputs are triggered by a change value (sbc).

## Build from scratch

1. Download [Schnittstelleninformation](http://www.hs-help.net/hshelp/gira/other_documentation/Schnittstelleninformationen.zip) from GIRA Homepage
2. Decompress zip, use `HSL SDK/2-0/framework` Folder for development.
3. Checkout this repo to the `projects/hs_kostalInverter2ndGen` folder
4. Run the generator.pyc (`python2 ./generator.pyc hs_kostalInverter2ndGen`)
5. Import the module `release/14660_kostalInverter2ndGen.hsl` into the Experte Software
6. Use the module in your logic editor

You can replace step 4 with the `./buildRelease.sh` script. With the help of the markdown2 python module (`pip install markdown2`) it creates the documentation and packages the `.hslz` file. This file is also installable in step 5 and adds the module documentation into the Experte-Tool.  
 
## Libraries

* requests
  * certifi
  * chardet
  * idna
  * urllib3

The shipped libraries may distributed under a different license conditions. Respect those licenses as well!
