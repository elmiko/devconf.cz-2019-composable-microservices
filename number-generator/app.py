import argparse
import logging
import os
import random
import time
import urllib.request as urllib

from kafka import KafkaProducer


def main(args):
    logging.info('brokers={}'.format(args.brokers))
    logging.info('topic={}'.format(args.topic))
    logging.info('rate={}'.format(args.rate))

    logging.info('creating kafka producer')
    producer = KafkaProducer(bootstrap_servers=args.brokers)

    logging.info('sending numbers')
    while True:
        line = str(random.randint(args.lower, args.upper))
        producer.send(args.topic, line.encode())
        time.sleep(1.0 / args.rate)
    logging.info('finished sending source')


def get_arg(env, default):
    return os.getenv(env) if os.getenv(env, '') is not '' else default


def parse_args(parser):
    args = parser.parse_args()
    args.brokers = get_arg('KAFKA_BROKERS', args.brokers)
    args.topic = get_arg('KAFKA_TOPIC', args.topic)
    args.rate = get_arg('RATE', args.rate)
    args.source = get_arg('LOWER', args.lower)
    args.source = get_arg('UPPER', args.upper)
    return args


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('starting number generator')
    parser = argparse.ArgumentParser(description='emit some stuff on kafka')
    parser.add_argument(
            '--brokers',
            help='The bootstrap servers, env variable KAFKA_BROKERS',
            default='localhost:9092')
    parser.add_argument(
            '--topic',
            help='Topic to publish to, env variable KAFKA_TOPIC',
            default='bones-brigade')
    parser.add_argument(
            '--rate',
            type=int,
            help='Lines per second, env variable RATE',
            default=3)
    parser.add_argument(
            '--lower',
            type=int,
            default=0,
            help='The lower bound of random integers, env variable LOWER')
    parser.add_argument(
            '--upper',
            type=int,
            default=1000000,
            help='The lower bound of random integers, env variable UPPER')
    args = parse_args(parser)
    main(args)
    logging.info('exiting')
