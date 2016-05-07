#! /usr/bin/python3
# -*- coding:utf-8 -*-

'''
Default configuration
'''

__author__= 'TonyZhu'

configs = {
	'debug':True,
	'db':{
		'host':'127.0.0.1',
		'port':3306,
		'user':'www-data',
		'password':'www-data',
		'db':'awesome'
	},
	'session':{
		'secret':'Awesome'
	}

}