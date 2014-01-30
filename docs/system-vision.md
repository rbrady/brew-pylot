Vision
=======

The heart of the brew-pylot system contains a raspberry pi connected to sensors
and running the core software that will monitor temperature and manage an AC
power outlet as nedded.  The system will also control pumps and can be expanded
to control other devices.

The first version of the software will provide the building blocks to use for the brewing process or for the fermentation process.  It intial version goals are:
- a python module to monitor temperature
- a python module to manage 240v solid state relay(s)
- a python module to manage 120v solid state relay(s)
- a daemon to continously operate and execute the above monitoring tools
- a REST-based api to allow applications to control the daemon
- a simple application to demonstrate the api functionality


