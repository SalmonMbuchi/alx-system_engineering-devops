# Load Balancer

In this project, I learnt about load balancing. Load balancer will distribute the work-load of your system to multiple individual systems, or group of systems to to reduce the amount of load on an individual system, which in turn increases the reliability, efficiency and availability of your enterprise application or website.

I interacted with **HAProxy** which stands for High Availability Proxy as the load balancer for my web infrastructure. It is used in many high profile environments e.g. GitHub, Imgur and Twitter.

### Benefits

The following are advantages of load balancing your application:
1. Reduced the work-load on an individual server.
2. Large amount of work done in same time due to concurrency.
3. Increased performance of your application because of faster response.
4. No single point of failure. In a load balanced environment, if a server crashes the application is sti   ll up and served by the other servers in the cluster.
5. When appropriate load balancing algorithm is used, it brings optimal and efficient utilization of the    resources, as it eliminates the scenario of some server’s resources are getting used than others.
6. Scalability: We can increase or decrease the number of servers on the fly without bringing down the ap   plication
7. Load balancing increases the reliability of your enterprise application
8. Increased security as the physical servers and IPs are abstract in certain cases.

## Tasks

**0. Double the number of webservers**: [0-custom_http_response_header](./0-custom_http_response_header)

Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02):
- The name of the custom HTTP header must be X-Served-By
- The value of the custom HTTP header must be the hostname of the server Nginx is running on.

**1. Install your load balancer**: [1-install_load_balancer](./1-install_load_balancer)

- Install and configure HAproxy on your lb-01 server.

