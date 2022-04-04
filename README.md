# argo-probe-eudat-b2find

This script performs checks to test the fucntionality of B2FIND.

The checks return the appropriate messages and codes.

## Usage

### NAME

```
      checkB2FIND.py - B2FIND check functionality metrics 
```

### DESCRIPTION

	B2FIND is an interdisciplinary discovery portal for research output. 
  In this repo you will find the metrics used to check the functionalities of the service.
	The plugin checks the health, and some functionalities of B2FIND service.

### SYNOPSIS

```
      checkB2FIND.py [--version] [--verbose] [--help] [--action <action name>]
                   [--timeout <threshold> ] --hostname <host> [--port <port>]
```

      Options:
       --help,-h         : Display this help.
       --timeout,-t      : Time threshold to wait before timeout (in second).
       --hostname,-H     : URL of the B2FIND service, to which probes are submitted (default is b2find.eudat.eu)
       --port, -p        : The B2FIND server port.
       --version,-e      : Prints the B2FIND and CKAN version and exits.
       --action,-a       : Action which has to be excecuted and checked. Supported actions are URLcheck, ListDatasets, ListCommunities, ShowGroupENES or all 
       


### OPTIONS

    --version
         Display plugins version.
         
    --verbose 
         Same as debug option.
         
    --action 
         Action which has to be excecuted and checked. Supported actions are URLcheck, ListDatasets, ListCommunities, ShowGroupENES or all.
         
    --help
         Display this help.

    --timeout
         Time threshold in second to wait before timeout (default to 30).

    --hostname <host>
         The B2FIND server host. It can be a DNS name or an IP address.

    --port <port>
         The B2FIND server port (default to 80).


### EXAMPLES
      Using  script:

```
   ./checkB2FIND.py -H b2find.eudat.eu -p 443 -a all
```
