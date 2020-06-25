1. **How long did it take to finish the test?**<br>
It took me around 5 hours before I finished everything and delivered it.

2. **If you had more time, how could you improve your solution?**<br>
With more time, I will parametrize the app and specify this parameters in the docker-compose (like the host and the port the app is running on). Also if I have to continue developing this app, I will create a Makefile or something similar as a helper for rebuilding, start and stop the containers.

3. **What changes would you do to your solution to be deployed in a production environment?**<br>
To make this service production ready I will do at least those changes:
- Do not use docker-compose and use kubernetes or other container orchestration system to deploy the app and the reverse proxy.
- If this app will be publicly accessible I will add some security in the nginx or some protection in front of the web-server, like a WAF.
- A mandatory thing that for sure I will implement, and here was optional, is https.
- Another thing will be to change the application server. Flask is not a production-ready application server. It is thought for development purposes.

4. **Why did you choose this language over others?**<br>
I chose python to write the app because by default it provides a lot of helpers and with few lines I could achieve what you were asking for. Also, it's the language I'm more familiar with when developing this kind of apps.

5. **What was the most challenging part and why?**<br>
For me the most challenging part of the test was to link both containers with the nginx proxy_pass. I thought I could link it with just the proxy_pass directive but because the container don't have a valid FQDN, nginx wasn't able to proxy the request without creating an nginx upstream.
