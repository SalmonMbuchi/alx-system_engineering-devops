# HTPPS SSL

In this project, I installed an SSL certificate on my subdomain. This encrypts all communication between the website and the server.

## Tasks

**0. World wide web**: [0-world_wide_web](./0-world_wide_web)

Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

**1.  HAproxy SSL termination**: [1-haproxy_ssl_termination](./1-haproxy_ssl_termination)

Requirements:

- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic
- HAproxy must serve encrypted traffic that will return the / of your web server
- When querying the root of your domain name, the page returned must contain Holberton School
- Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)


**2. No loophole in your website traffic**: [100-redirect_http_to_https](./100-redirect_http_to_https)

Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
