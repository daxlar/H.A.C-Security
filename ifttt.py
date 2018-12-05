import requests


def email_alert(first, second, third):
    report = {"Value1" : 0, "Value2": 0, "Value3": 0}
    report["Value1"] = first
    report["Value2"] = second
    report["Value3"] = third
    requests.post("https://maker.ifttt.com/trigger/something_is_WRONG/with/key/dCOToeQZzXJRGlzaWT6c5O?value1={}&value2={}&value3={}".format(first, second, third))


email_alert("no problem", 1, 1)

