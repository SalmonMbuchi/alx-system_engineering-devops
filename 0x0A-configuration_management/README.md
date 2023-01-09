# Configuration Management

This is the process of systemically handling changes to a system in a way that it maintains integrity over time.

Automation plays an essential role in server configuration management. It is the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool's specific language and features.

## Benefits of Configuration Management for Servers
The benefits include:

1. Quick provisioning of new servers
2. Quick recovery from critical events
3. Facilitates version control for the server environment
4. Replicated environments

In this particular project, I worked with Puppet, a popular configuration management tool. Puppet is capable of managing complex infrastructure in a transparent way using a master server to orchestrate the configuration of the nodes.

## Tasks :page_with_curl:

* **0. Create a file**
  * [0-create_a_file.pp](./0-create_a_file.pp): Puppet manifest file that
  creates a file `holberton` in the `/tmp` directory.
    * File permissions: `0744`.
    * File group: `www-data`.
    * File owner: `www-data`.
    * File content: `I love Puppet`.

* **1. Install a package**
  * [1-install_a_package.pp](./1-install_a_package.pp): Puppet manifest file
  that install puppet-lint version 2.1.1.

* **2. Execute a command**
  * [2-execute_a_command.pp](./2-execute_a_command.pp): Puppet manifest file
  that kills the process `killmenow`.
