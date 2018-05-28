#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zhangliang
# Per-Mail: zhanglianghhh@163.com
# Work-Mail: liang.zhang04@msxf.com
# Create Date: 2018-05-25
# Content: 当前时间平均每核CPU的负载信息

import os
import json
import time


metric_each_cpu_load_1min="each.load.1min"
metric_each_cpu_load_5min="each.load.5min"
metric_each_cpu_load_15min="each.load.15min"

endpointinfo=os.popen("hostname").read().strip();

ts = int(time.time())

stepinfo=60
counterTypeinfo="GAUGE"
tagsinfo="loc=all,type=load"

# 得到负载信息
cpu_num = os.popen("cat /proc/cpuinfo | grep 'processor' | wc -l").read().strip();  # 得到CPU核数
load_info = os.popen("cat /proc/loadavg").read().strip();  # 得到当前负载信息
# print(cpu_num)
# print(load_info)

load_1 = load_info.split(" ")[0];  # 1min 负载信息
load_5 = load_info.split(" ")[1];  # 5min 负载信息
load_15 = load_info.split(" ")[2]; # 15min负载信息

avg_1 = float(load_1) / int(cpu_num);   # 平均每核CPU 1min  负载
avg_5 = float(load_5) / int(cpu_num);   # 平均每核CPU 5min  负载
avg_15 = float(load_15) / int(cpu_num); # 平均每核CPU 15min 负载


data = [
        {
            'metric': metric_each_cpu_load_1min,
            'endpoint': endpointinfo,
            'timestamp': ts,
            'step': stepinfo,
            'value': avg_1,
            'counterType': counterTypeinfo,
            'tags': tagsinfo
        },
        {
            'metric': metric_each_cpu_load_5min,
            'endpoint': endpointinfo,
            'timestamp': ts,
            'step': stepinfo,
            'value': avg_5,
            'counterType': counterTypeinfo,
            'tags': tagsinfo
        },
        {
            'metric': metric_each_cpu_load_15min,
            'endpoint': endpointinfo,
            'timestamp': ts,
            'step': stepinfo,
            'value': avg_15,
            'counterType': counterTypeinfo,
            'tags': tagsinfo
        }
       ]

print(json.dumps(data))


