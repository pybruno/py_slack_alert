#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
from optparse import OptionParser
import argparse


def build_parser():
    """
    define param command line
    :return: parser config
    """
    parser =   argparse.ArgumentParser(add_help=True)
    parser.add_argument("--host", dest="host", help="host ", default=False)
    parser.add_argument("--notificationtype", dest="notif", help="warning, critical...")
    parser.add_argument("--service", dest="service", help="service probleme")
    parser.add_argument("--ip", dest="ip", help="host ip")
    parser.add_argument("--date", dest="date", help="date")
    parser.add_argument("--state", dest="state", help="status service")
    parser.add_argument("--output", dest="output", help="service info detail")
    return parser


def slack_notif(host,notif,service,ip,date_status,state, output):

    debug = False
    webhook_url = 'https://hooks.slack.com/services/.....'
    if debug:
        to = ['@user1']
    else:
        to = ['#channelname1', '@user1','@user2']

    msg = "Notification Type: *{}* \n service: *{}* \n host: *{}* \n ip: *{}* \n State: {} \n date: {} \n Additional Info: {}".format(notif, service, host, ip, state, date_status, output)
    try:
        icone = ""
        username = ""
        print(notif.lower())
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
    slack_notif(args.host, args.notif, args.service, args.ip, args.date, args.state, args.output)
