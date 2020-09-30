#Options for AppRise Alert Action

action.apprise_alert = [0|1]
* Enable AppRise Alert Action

action.apprise_alert.param.url = <string>
* Override global url of your AppRise server
* (optional)

action.apprise_alert.param.secret_key = <string>
* Override global app secret key to use
* (optional)

action.apprise_alert.param.key = <string>
* Alert Key
* (optional)

action.apprise_alert.param.json = <string>
* json content
* (required)

action.apprise_alert.param.priority = [0-10]
* Alert priority. 0=Min, 1-3=Low, 3-7=Normal, >7=High
* (required)
