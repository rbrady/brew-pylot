#!/usr/bin/env python

# There are two primary types of devices that compose
# the brewing system.  Publisher and Subscriber.
#
# A thermometer sensor publishes it's id and temperature at a
# an interval defined in the .conf file.  A thermometer is a 
# device that is always on.

# A heating element is a device that receives messages like
# turn on / turn off / set power.  It may publish a status
# to let the system know if it's on or off and what power it
# is currently at.

# A pump is a device that receives messages like turn on or turn
# off.  It may publish a status of whether it is on of off.

# The heating element and pump may issue an ack message instead
# of publishing at an interval.

# A conductor service will monitor all of the systems and issue
# messages according to user input.

# An external application will communicate with the conductor
# service to monitor all systems and issue user input messages.

# An external application may monitor the message bus to provide
# a history log of the brewing session.  This will likely not sit
# on the raspberry pi platform due to storage constraints

# The conf file for each service will allow the administrator to set
# a value for the interval and to select a messaging backend driver.

# the initial MVP of the system will choose a specific AMQP product,
# but multiple products will be supported in the future.


