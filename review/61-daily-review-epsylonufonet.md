# 🚀 epsylon/ufonet

- https://ufonet.03c8.net/  

A disruptive tool for DoS and DDos attacks, working on layers 3 and 7.

- **layer 3 (Network)**: Abuses network protocols to act as a botnet
- **layer 7 (APP/HTTP)**: Exploits web vulnerabilities (open redirects) to use third-party websites as botnet nodes 

## What is an Open Redirect Leak?

> An open redirect is a website that accepts a URL as a parameter and redirects the user to that URL without any validation. Which means that the attacker can use the open redirect to redirect the user to a malicious website.

### When to use redirect on your own website

- Log in to your website, then redirect to the previous page  

### How to use it to perform an attack

```shell
https://yourdomain.com/redirect?url=https://phishing.com
```
