# Web Stack Debugging

Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.

## Tasks

**0. Run software as another user**: [0-iamsomeoneelse] (./0-iamsomeoneelse)

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

Requirements:

- write a Bash script that accepts one argument
- the script should run the whoami command under the user passed as an argument
- make sure to try your script by passing different users

**1.Run Nginx as Nginx**: [1-run_nginx_as_nginx] (./1-run_nginx_as_nginx)

Fix this container so that Nginx is running as the nginx user.

Requirements:

- nginx must be running as nginx user
- nginx must be listening on all active IPs on port 8080
- You cannot use apt-get remove
- Write a Bash script that configures the container to fit the above requirements

**100-fix_in_7_lines_or_less**: [100-fix_in_7_lines_or_less] (./100-fix_in_7_lines_or_less)

Using what you did for task #1, make your fix short and sweet.

Requirements:

- Your Bash script must be 7 lines long or less
- There must be a new line at the end of the file
- You respect Bash script requirements
- You cannot use ;
- You cannot use &&
- You cannot use wget
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
