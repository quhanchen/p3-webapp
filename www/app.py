#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-24 15:47:14
# @Author  : Kyle Liu (${email})
# @Link    : ${link}
# @Version : $Id$

import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web
import logging
logging.basicConfig(level=logging.INFO)

body_index = b'<h1 align="center">Awesome<h1>'


def index(request):
    return web.Response(body=body_index,
                        content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_get('/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
