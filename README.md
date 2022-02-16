# slack notifications for nagios/centreon...
send alert to slack channel and users

* Create a slack webhook.

* change url

* change channelName and users you want

* define a contact in nagios

```sh
define contact {

    contact_name            slack             ; Short name of user
    use                     generic-contact         ; Inherit default values from generic-contact template (defined above)
    alias                   slack            ; Full name of user
    service_notification_commands	notify-service-by-slack
    host_notification_commands		notify-host-by-slack
}
```

```sh
* define a new command in nagios

define command {
        command_name                notify-service-by-slack
		command_line                /usr/lib/nagios/plugins/py_slack_service.py --notificationtype "$NOTIFICATIONTYPE$"  --host "$HOSTNAME$" --ip "$HOSTADDRESS$" --service "$SERVICEDESC$" --state "$SERVICESTATE$" --output "$SERVICEOUTPUT$" --date "$LONGDATETIME$"
}

define command {
		command_name			     notify-host-by-slack
		command_line			     $USER1$/py_slack_host.py --notificationtype "$NOTIFICATIONTYPE$" --host "$HOSTNAME$" --ip "$HOSTADDRESS$" --state "$HOSTSTATE$" --ouput "$HOSTOUTPUT$" --date "$LONGDATETIME$"
}
```