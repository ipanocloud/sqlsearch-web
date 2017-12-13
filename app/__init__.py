#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/9 21:34
# @author  : zhoubin

from flask import Flask
from flask_bootstrap import Bootstrap

from config import config

bootstrap = Bootstrap()


def create_app(config_name):
    """
        根据不同环境的配置创建APP服务
    :param config_name: 配置文件名称
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
