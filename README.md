# Installation

- At reg.ru
  - Login to your account
  - Settings - API allowed IP addresses for connecting via API - Add your external public IP, from which your will connect with API
  - To connect with API use login/password of the personal account (you can also add an additional password (use with the main login) in the personal account - Settings - API)
  - there is a limit of API connections - 1200/hour
- At Zabbix server
  - copy *.py scripts to /usr/lib/zabbix/externalscripts
  - import template *.xml into Zabbix
  - Create host "REG.RU___<reg.ru_account_login>"
  - Add macros in the host:
    - {$REGRU_USER} - reg.ru account login,
    - {$REGRU_PASS} - reg.ru account password
  - Attach template to the host
  - Discovery rule will get array of domains
  - items and Triggers will be created
