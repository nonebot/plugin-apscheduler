import logging

from nonebot import get_driver, get_bots, export
from nonebot.log import logger, LoguruHandler
from apscheduler.schedulers.base import undefined
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .config import Config

driver = get_driver()
global_config = driver.config
plugin_config = Config(**global_config.dict())

class Scheduler(AsyncIOScheduler):
    def scheduled_nonebot_job(self, trigger, args=None, kwargs=None, id=None, name=None,
                      misfire_grace_time=undefined, coalesce=undefined, max_instances=undefined,
                      next_run_time=undefined, jobstore='default', executor='default',
                      **trigger_args):
        def inner(func):
            async def func_():
                for bot in get_bots().values():
                    await func(bot)
            self.add_job(func_, trigger, args, kwargs, id, name, misfire_grace_time, coalesce,
                         max_instances, next_run_time, jobstore, executor, True, **trigger_args)
            return func
        return inner

scheduler = Scheduler()
export().scheduler = scheduler


async def _start_scheduler():
    if not scheduler.running:
        scheduler.configure(plugin_config.apscheduler_config)
        scheduler.start()
        logger.opt(colors=True).info("<y>Scheduler Started</y>")


if plugin_config.apscheduler_autostart:
    driver.on_startup(_start_scheduler)

aps_logger = logging.getLogger("apscheduler")
aps_logger.setLevel(plugin_config.apscheduler_log_level)
aps_logger.handlers.clear()
aps_logger.addHandler(LoguruHandler())
