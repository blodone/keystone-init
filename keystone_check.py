#!/usr/bin/env python
import sys

from keystone_init import parse_config

from keystoneclient.v2_0 import client


def check_keystone(config):
    keystone = client.Client(token=config['token'],
                             endpoint=config['endpoint'])

    print '{1}-{0}-{1}'.format('URL', '-'*10)
    print keystone.management_url
    print

    print '{1}-{0}-{1}'.format('Endpoints', '-'*10)
    print keystone.endpoints.list()
    print

    print '{1}-{0}-{1}'.format('Services', '-'*10)
    print keystone.services.list()
    print

    print '{1}-{0}-{1}'.format('Users', '-'*10)
    print keystone.users.list()
    print 
    return keystone

def return_keystone(config_file='config.yml'):
    config = parse_config(config_file)
    return check_keystone(config)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: keystone-check.py config-file.yml"
	print 'using default config.yml'
        config_file = 'config.yml'
    else:
	config_file = sys.argv[1]
    config = parse_config(config_file)
    check_keystone(config)
