﻿# -*- coding: utf-8 -*-
"""
Django settings for StuMan project.
Generated by 'django-admin startproject' using Django 2.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
 
import os
import sys
 
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 文件目录导入到搜索路径中
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'mysite'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dhk*7sui0s4wdi6!m0&s90$8z*$fqgf04c2+#alwxk^hel0@0v'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#允许所有host访问
ALLOWED_HOSTS = ['*']

 
 
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'crispy_forms',
    'reversion',
    "program",
]
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
ROOT_URLCONF = 'uxin_test.urls'
#模板：HTML代码＋逻辑控制代码
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],#加载html模板路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
 
WSGI_APPLICATION = 'uxin_test.wsgi.application'
 
 
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
#配置mysql数据库的配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uxin_test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
 
 
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
 
 
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
 
LANGUAGE_CODE = 'zh-hans' #修改语言为汉语
 
TIME_ZONE = 'Asia/Shanghai'
 
USE_I18N = True
 
USE_L10N = True
 
USE_TZ = False
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
#静态文件根目录加载
STATIC_URL = '/static/'
#html、css中加载css路径、图片路径时，需要映射路径
STATIC_ROOT = os.path.join(BASE_DIR, "static").replace('\\', '/')
STATICFILES_DIRS =(
    ("css",    os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ("js",    os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ("imgs",    os.path.join(STATIC_ROOT, 'imgs').replace('\\', '/')),
 )