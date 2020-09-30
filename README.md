# Splunk APPRISE Alert
Send Splunk Alerts to any of the 50+ services supported by AppRise Server - Including Telegram, Slack, Teams, PushBullet, Email ... and the list goes on!

This add-on requires a [AppRise server](https://github.com/caronc/apprise") to function.

Splunk APPRISE Alerts send a JSON payload to APPRISE, so it should work with all services even if they take different parameters and fields.

## Install
- Clone or download the repository 
- Place contents on SPLUNK_HOME/etc/apps/apprise_alerts
- Restart Splunk

## Configuration:
Before using this add-on, it needs to be configured in Splunk. This can be done in the Splunk UI under 

- *Settings > Alert Actions > Setup AppRise Alert*

Here you need to provide the URL to your APPRISE server, for example

- http://apprise.home.com:8000/

**Note** you must **NOT** include the /notify/\<key> part of the URL, this is automatically added.

Alternatively, this can be done by updating and placing the below config in local/alert_actions.conf

    [apprise_alert]
    param.server = <<URL>>
    param.secret_key = <<Not Used>>


## Usage

Create an alert in Splunk as you normally would, under the "Trigger Actions" drown, select send APPRISE Alert. Provide the following 3 fields:

- **Key**: This is the APPRISE key for provider you want to you, i.e. http://apprise:8000/cfg/\<KEY> or http://apprise:8000/notify/\<KEY>
- **JSON**: This is the payload that will be sent AppRise, you can populate it with results/tokens from Splunk
    + https://github.com/caronc/apprise-api
    + https://docs.splunk.com/Documentation/Splunk/8.0.6/AdvancedDev/ModAlertsLog
- **Priority**: Does nothing at the moment

[![N|Solid](https://raw.githubusercontent.com/projx/splunk-apprise-alerts/master/screenshots/splunk_alert_1.png)](https://github.com/projx/splunk-apprise-alerts/)