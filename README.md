# Splunk APPRISE Alert

# About
Send Splunk Alerts to any of the 50+ services supported by AppRise Server - Including Telegram, Slack, Teams, PushBullet, Email ... and the list goes on!

This add-on requires a [AppRise server](https://github.com/caronc/apprise") to function.

Splunk APPRISE Alerts send a JSON payload to APPRISE, so it should work with all services even if they take different parameters and fields.

# News
- 30/09/20: Initial Upload
- 29/09/20: Butchered this together

# Installation
I build this for personal use, I may get round to uploading it to SplunkBase, but for now, you will need to manually install it:
- Clone or download the repository 
- Place contents on SPLUNK_HOME/etc/apps/apprise_alerts
- Restart Splunk

# Configuration:
Before using this add-on, it needs to be configured in Splunk. This can be done in the Splunk UI under 

- *Settings > Alert Actions > Setup AppRise Alert*

Here you need to provide the URL to your APPRISE server, for example

- http://apprise.home.com:8000/

**Note** you must **NOT** include the /notify/\<key> part of the URL, /notify/ is automatically added, and they \<KEY> is defined as part of the Alert Action (see Usage below)

Alternatively, this can be done by updating and placing the below config in local/alert_actions.conf

    [apprise_alert]
    param.server = <<URL>>
    param.secret_key = <<Not Used>>


# Usage

Create an alert in Splunk as you normally would, under the "Trigger Actions" drown, select send APPRISE Alert. Provide the following 3 fields:

- **Key**: This is the APPRISE key for provider you want to you, i.e. http://apprise:8000/cfg/\<KEY> or http://apprise:8000/notify/\<KEY>
- **JSON**: This is the payload that will be sent AppRise, you can populate it with results/tokens from Splunk
    + https://github.com/caronc/apprise-api
    + https://docs.splunk.com/Documentation/Splunk/8.0.6/AdvancedDev/ModAlertsLog
- **Priority**: Does nothing at the moment

[![N|Solid](https://raw.githubusercontent.com/projx/splunk-apprise-alerts/master/screenshots/splunk_alert_1.png)](https://github.com/projx/splunk-apprise-alerts/)


# Acknowledgements:
Splunk Arise Alert is heavily based-upon work done by https://github.com/FieldofClay

APPRISE is developed by Chris Carson - https://github.com/caronc

# Legal bit
You can freely copy and butcher this as you like, I claim no rights on this. I offer no gaurantee this works. By downloading this, you acknowledge and accept full liability for any damage or mental anguish usage may cause