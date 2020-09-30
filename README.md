## AppRise Alert Action
Adds an alert action to Splunk that sends an alert via an AppRise server. 

This add-on requires a [AppRise server](https://github.com/caronc/apprise") to function.

Before using this add-on, it needs to be configured in Splunk. This can be done in the Splunk UI under *Settings>Alert Actions>Setup AppRise Alert Action*. Alternatively, this can be done by updating and placing the below config in local/alert_actions.conf

    [apprise_alert]
    param.server = <<URL>>
    param.secret_key = <<secret_key>>
