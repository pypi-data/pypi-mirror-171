# python-verifonePED

**Basic communication with Verifone PED (i.e. VX820) & Ocius VX Evolution software.

A very quick-and-dirty module to create an object for a verifone device, perform login/logout, and send a transaction to the device.
Needs more work, but makes the device perform a transaction.


## Installing
`pip install verifonePED`

## Example

Send a transaction for £1.00:
```
from verifonePED import verifone_device

my_ped = verifone_device(ip_address='192.168.20.161', username='1113', password='1113')

my_ped.login()

if my_ped.logged_in:
    print('Transaction Status =', my_ped.transaction(1.00))
else:
    print('Error logging in!')
```
