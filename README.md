Ansible Role Hostapd
=========

:warning: This role is under development, some important (and possibly breaking) changes may happend. Don't use it in production level environments but you can eventually base your own role on this one :hammer:

:grey_exclamation: Before using this role, please know that all my Ansible role are fully written and accustomed to my IT infrastructure. So, even if they are as generic as possible they will not necessarily fill your needs, I advice you to carrefully analyse what they do and evaluate their capability to be installed securely on your servers.

This roles configure the Hostapd daemon to create a Wifi access point using a network card.

## Features

Currently this role provide the following features :

  * hostapd installation
  * minimal configuration
  * monitoring items for
    * Zabbix
  * [local facts](#facts)

## Requirements

### OS Family

This role is available for Debian only

### Dependencies

--


## Role Variables

The variables that can be passed to this role and a brief description about them are as follows:

| Name                               | Types/Values    | Description                                                                                             |
| -----------------------------------| ----------------|-------------------------------------------------------------------------------------------------------- |
| hostapd__facts                     | Boolean         | Install the local fact script                                                                           |
| hostapd__monitoring                | String          | The name of the monitoring "profile" to use. Available 'zabbix')                                        |
| hostapd__service_enabled           | Boolean         | Enable or not the service                                                                               |
| hostapd__service_configure_systemd | Boolean         | Replace the default initd script by a systemd service to prevent hostapd to be down on 'restart' command|
| hostapd__interface                 | String          | The name of the network interface to bind hostapd to                                                    |
| hostapd__ssid                      | String          | The SSID of the Wifi network                                                                            |
| hostapd__wpa_passphrase            | String          | The passphrase of the Wifi access point                                                                 |
| hostapd__ignore_broadcast_ssid     | Boolean         | If true, the SSID will be hidden                                                                        |
| hostapd__accept_mac                | List of string  | List of authorized mac addresses                                                                        |
| hostapd__deny_mac                  | List of string  | List of authorized mac addresses                                                                        |


## Facts

By default the local fact are installed and expose the following variables :


* ```ansible_local.hostapd.version_full```


## Example Playbook

To use this role create or update your playbook according the following example :


```
    - hosts: servers
      roles:
         - hostapd
      vars:
        hostapd__service_configure_systemd: True
        hostapd__interface: 'wlan0'
        hostapd__ssid: 73850e2cf192ccdf
        hostapd__wpa_passphrase: '{{ value from ansible vault }}'
        hostapd__ignore_broadcast_ssid: 0
```


## License

MIT