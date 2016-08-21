Docker Fabric
===

An image for running [Fabric](http://www.fabfile.org/) commands.

Example:

```docker run -it --rm -v $PWD:/app sebestyen/python-fabric fab .```

Given the following fabfile.py in your current directory
```python
def hello():
    print "hello world"
```
will print > hello world

You man also ask for help from fabric like this:

```docker run -it --rm -v $PWD:/app sebestyen/python-fabric fab --help```


Note that this container has [cuisine](https://pypi.python.org/pypi/cuisine) installed.  These are a number of fabric extensions for common
actions. 

How to run cuisine
=====

Open up a python shell and type:

```import cuisine```

Cuisine is designed to be a flat-file module, where all functions are prefixed by the type of functionality they offer (e.g., file for file operations, user for user operations). The available groups are:

```
text_*    Text-processing functions
file_*    File operations
dir_*     Directory operations
package_* Package management operations
command_* Shell commands availability
user_*    User creation commands
group*    Group creation commands
mode_*    Configures cuisine’s behaviour within the current session.
select_*  Selects a specific option, such as package back-end (apt, yum, zypper, or pacman)
```

If you’re using an interactive Python shell such as IPython you can easily browse the available functions by using tab-completion.

As the functions are prefixed by they type of functionality, it is very easy to get started using an interactive shell.

If you would like to use cuisine without using a fabfile, you can call the mode_local() function.

```
import cuisine
cuisine.mode_local()
print cuisine.run("echo Hello")
```

alternatively, you can also directly connect to a server

```
import cuisine
cuisine.connect("my.server.com")
print cuisine.run("echo Hello")
```

If you want to use cuisine within a fabfile, simply create a fabfile with the following content:

```
from cuisine import *

def setup():
    group_ensure("remote_admin")
    user_ensure("admin")
    group_user_ensure("remote_admin", "admin")
```

You may run Ipython for interactive python with tab completion
====

Example:

```docker run -it --rm -v $PWD:/app sebestyen/python-fabric ipython```

You may also run bash to get into the container via bash:
====

Example:

```docker run -it --rm -v $PWD:/app sebestyen/python-fabric bash```
