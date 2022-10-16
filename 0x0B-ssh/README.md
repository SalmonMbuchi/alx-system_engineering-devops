# SSH

SSH is a secure protocol used as the primary means of connecting to Linux servers remotely.
SSH stands for **Secure Shell** and provides a safe and secure way of executing commands, making changes, and configuring services remotely.

## Tasks

0. **Use a private key**:
[0-use_a_private_key](./0-use_a_private_key) 

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

1. **Create an SSH Key pair**:
[1-create_ssh_key_pair](./1-create_ssh_key_pair)

Write a Bash script that creates an RSA key pair.

2. **Client configuration file**:
[2-ssh_config](./2-ssh_config)

Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

3. **Let me in**:

Add the SSH public key below to your server so that we can connect using the ubuntu user.

4. **Client configuration with Puppet**:
[100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp)

Set up your client SSH configuration file so that you can connect to a server without typing a password using Puppet.
