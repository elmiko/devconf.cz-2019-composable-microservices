# number generator
A Python source-to-image application for emitting random numbers to a Kafka
topic.

## Launching on OpenShift

```
oc new-app centos/python-36-centos7~https://github.com/elmiko/devconf.cz-2019-composable-microservices \
  --context-dir=number-generator \
  -e KAFKA_BROKERS=kafka:9092 \
  -e KAFKA_TOPIC=bones-brigade \
  --name=generator
```

You will need to adjust the `KAFKA_BROKERS` and `KAFKA_TOPICS` variables to
match your configured Kafka deployment and desired topic. By default this
application will generate integers in the range of 0-1000000, you can change
this behavior by setting the environment variables `LOWER` and `UPPER`.
