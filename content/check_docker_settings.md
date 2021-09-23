---
title: Elasticsearch Docker Requirements (for Playing Around)
date: 23 Sep 2021 14:35
tags: docker, enterprise search, kibana
---

Two days later, I'm writing this to remind myself of a few things in my docker playground setup.

## If You Get a Licensing Error in Kibana, Check Docker to See If Elasticsearch Is Still Running

Kibana will default to some imaginary Elasticsearch instance[^1] that it can't reach. I do know that part of this is to check for licensing (even if you are using the free license). This is why you may see the error `{"statusCode":503,"error":"Service Unavailable","message":"License is not available."}`

Elasticsearch containers don't just turn off on their own for no reason so this usually means there is another issue which I will point to in the next step.

## If Your Setup Keeps Crashing, You May Need to Increase the Resources That Docker Can Utilize

Elasticsearch Enterprise Search is a little resources intensive. Sometimes my eyes miss the warning in the [Running Enterprise Search with Docker Compose](https://www.elastic.co/guide/en/enterprise-search/current/docker.html#docker-compose-example) section that you should be allocating at least 4GB RAM.

> Make sure Docker Engine is allotted at least 4GiB of memory. In Docker Desktop, you configure resource usage on the Advanced tab in Preference (macOS) or Settings (Windows).

![Enterprise Search Docker Settings](https://kjaymiller.s3-us-west-2.amazonaws.com/images/docker-ent-search-settings-resources.png)

To adjust via the GUI (macOS):

1. Select _Settings_ gear in the top corner
2. Select _Resources_ menu option
3. Select the _Advanced_ submenu
4. Adjust memory to _at least_ 4GB.

[^1]: TODO: Learn what this default instance is and why it exists. Maybe also figure out how to sound the alarm when Kibana is trying to reach it!
