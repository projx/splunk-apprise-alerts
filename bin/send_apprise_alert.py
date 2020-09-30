import os, datetime, sys, requests, json, re

# For testing only...
# alert = {
#     "configuration" : {
#             "ssl_verify" : "false",
#             "url" : "http://nas-01.prjx.uk:8009/notify",
#              "key" : "telegram01",
#              "json" : '{"body":"test message"}',
#     }
# }

def log_to_file(msg):
    message = str(datetime.datetime.now().isoformat()) + " " + str(msg)
    filehandle = open(os.path.join(os.environ["SPLUNK_HOME"],  "var", "log", "splunk", "apprise.log"), "a")
    filehandle.write(message + '\n')
    filehandle.close()

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

def validate(config):
    ## mandatory keys needs to execute the message
    required_fields = ["url", "key", "json"]

    for field in required_fields:
        if field not in config:
            log_to_file("Error no "+field+" value specified")
            return False

    if "ssl_verify" in config:
        if config['ssl_verify'].upper() in ["TRUE"]:
            config["ssl_verify"] = True
        else:
            config["ssl_verify"] = False
    else:
        config["ssl_verify"] = False

    ## validate the payload is valid json
    if not is_json(config["json"]):
        log_to_file("Error the json field is invalid")
        return False

    return True

def main():
    alert = json.loads(sys.stdin.read())
    if validate(alert['configuration']):
        config = alert['configuration']
        ## Headers
        headers = {'Content-Type': 'application/json'}

        ## URL generation
        url = config['url']
        if url[-1] != "/":
            url = url + "/"
        url += config["key"]

        log_to_file("Sending too: " + url + " Payload: " + config["json"])
        
        ## Send ...
        r = requests.post(url, headers=headers, data=config["json"], verify=False)
        if r.status_code == 200:
            log_to_file("HTTP Code 200: Success sending message")
        else:
            log_to_file("Error HTTP Code " + str(r.status_code) + ": " + r.text)
    else:
        log_to_file("Error Invalid configuration detected. Stopped.")


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "--execute":
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit()

    main()