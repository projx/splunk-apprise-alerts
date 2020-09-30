import os, datetime, sys, requests, json, re


def eprint(msg):
    message = str(datetime.datetime.now().isoformat()) + " " + str(msg)
    filehandle = open("/Applications/Splunk/var/log/splunk/apprise.log", "a")
    filehandle.write(message + '\n')
    filehandle.close()

# For testing only...
# alert = {
#     "configuration" : {
#             "ssl_verify" : "false",
#             "url" : "http://nas-01.prjx.uk:8009/notify",
#              "key" : "telegram01",
#              "json" : '{"body":"test message"}',
#     }
# }

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

def validate(config):
    required_fields = ["url", "key", "json"]
    for key,value in config.items():
        eprint(key + " " + value)
    for field in required_fields:
        if field not in config:
            eprint("Error no "+field+" value specified")
            return False

    if "ssl_verify" in config:
        if config['ssl_verify'].upper() in ["TRUE"]:
            config["ssl_verify"] = True
        else:
            config["ssl_verify"] = False
    else:
        config["ssl_verify"] = False

    if not is_json(config["json"]):
        eprint("Error the json field is invalid")
        return False

    return True

eprint("Running...")
#if len(sys.argv) > 1 and sys.argv[1] == "--execute":
eprint(sys.stdin)
alert = json.load(sys.stdin)
if validate(alert['configuration']):
    config = alert['configuration']
    ## Headers
    headers = {'Content-Type': 'application/json'}

    ## URL generation
    url = config['url']
    if url[-1] != "/":
        url = url + "/"
    url += config["key"]
    eprint("Sending too: " + url)
    ## Send ...
    r = requests.post(url, headers=headers, data=config["json"], verify=False)
    if r.status_code == 200:
        eprint("HTTP Code 200: Success sending message")
    else:
        eprint("Error HTTP Code " + str(r.status_code) + ": " + r.text)
else:
    eprint("Error Invalid configuration detected. Stopped.")
#else:
#    eprint("FATAL No execute flag given")