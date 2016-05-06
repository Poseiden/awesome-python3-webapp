#! /usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'TonyZhu'

'''
JSON API definition
'''

import json ,logging,inspect,functools

class APIError(Exception):
	'''
	the base APIError which contains error(required),data(option) and message(optional).
	'''

	def __init__(self,error,data = '',message=''):
		super(APIValueError,self).__init__('value:invalid',field,message)

class APIResourceNotFoundError(APIError):
	'''
	Indicate the resource was not found . The data specifies the resource name.
	'''

	def __init__(self,field,message=''):
		super(APIResourceNotFoundError,self).__init__('value:notfound',field,message)

class APIPermissionError(APIError):
	super(APIPermissionError,self).__init__('permission:forbidden','permission',message)