# -*- coding: utf-8 -*-
import requests
import json
import argparse


def build_parser():
    """
    define param command line
    :return: parser config
    """
    parser =   argparse.ArgumentParser(add_help=True)
    parser.add_argument("--host", dest="host", help="host ")
    parser.add_argument("--notificationtype", dest="notif", help="warning, critical...")
    parser.add_argument("--ip", dest="ip", help="host ip")
    parser.add_argument("--date", dest="date", help="date")
    parser.add_argument("--state", dest="state", help="status service")
    parser.add_argument("--output", dest="output", help="service info detail")
    return parser


def slack_notif(host, notif, ip, date_status, state, output):

    debug = False
    webhook_url = 'https://hooks.slack.com/services/......'
    if debug:
        to = ['@user1']
    else:
        to = ['#channelName', '@user1','@user2']

    msg = "Notification Type: *{}* \n host: *{}* \n ip: *{}* \n State: {} \n date: {} \n Info: {}".format(notif, host, ip, state, date_status, output)
    
    try:
        icone = ""
        username = ""
        if "critical" in notif.lower():
            icone = ':red_circle:'
            username = "critical"
        elif "warning" in notif.lower():
            icone = ":large_orange_diamond:"
            username = "warning"
        elif "ok" in notif.lower() or "recovery" in notif.lower():
            icone = ':white_check_mark:'
            username = "ok"
        else:
            icone = ":red_circle:"
            username = "unknown"
        

        for user in to:
            data = {
                'channel': user,
                'username': username,
                'text': msg, 
                'icon_emoji': icone
                }

            if not debug:
                try:
                    requests.post(webhook_url, data=json.dumps(
                        data), headers={'Content-Type': 'application/json'})
                except Exception as e:
                    raise ValueError(e)
            else:
                print(user)
                print(json.dumps(data))

    except Exception as e:
        raise ValueError(e)


if __name__ == '__main__':
    pars = build_parser()
    args = pars.parse_args()
    print(args)
    slack_notif(args.host, args.notif, args.ip, args.date, args.state, args.output)
