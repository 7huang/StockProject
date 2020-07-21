import requests
from aiocqhttp import CQHttp, Event

qq_num = 1004759662
qq_pwd = 'a123456789'
at_me = '[CQ:at,qq={0}]'.format(1004759662)

bot = CQHttp(api_root='http://127.0.0.1:5700')

@bot.on_message('private')
async def _(event: Event):
    await bot.send(event, '你发了：')
    return {'reply': event.message}

@bot.on_message('group')
async def _(event: Event):
    if at_me in event.message:
        # await bot.send(event, '你发了：')
        return {'reply': event.message.replace(at_me,'')}
    return

bot.run(host='127.0.0.1', port=5701)

data = {
    'group_id':1034738058,
    'message':'我是一个小机器人~',
    'auto_escape':False
}

api_url = 'http://127.0.0.1:5700/send_private_msg'
#酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700

r = requests.post(api_url,data=data)
print(r.text)