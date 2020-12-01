<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://raw.githubusercontent.com/nonebot/nonebot2/master/docs/.vuepress/public/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot-plugin-docs

_✨ NoneBot APScheduler 定时任务插件 ✨_

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/nonebot/plugin-apscheduler/master/LICENSE">
    <img src="https://img.shields.io/github/license/nonebot/plugin-apscheduler.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-apscheduler">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-apscheduler.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
</p>

## 使用方式

加载插件后使用 `require` 获取 `scheduler` 对象（请注意插件加载顺序）

```python
from nonebot import require

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job("cron", hour="*/2", id="xxx", args=[1], kwargs={arg2: 2})
async def run_every_2_hour(arg1, arg2):
    pass

scheduler.add_job(run_every_day_from_program_start, "interval", days=1, id="xxx")
```

## 配置项
