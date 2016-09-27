import web
import os
import sys
import requests

urls = (
        '/right', 'right',
        '/left', 'left',
        '/up', 'up',
        '/down', 'down',
        '/stop', 'stop',
        '/snomcam', 'snom_cam'
        )

TIMEOUT=0.5

if 'CAM_USERNAME' in os.environ.keys():
    CAM_USERNAME = os.environ['CAM_USERNAME']
else:
    print("ERROR: Environment variable CAM_USERNAME not defined")
    sys.exit(-1)

if 'CAM_PASSWORD' in os.environ.keys():
    CAM_PASSWORD = os.environ['CAM_PASSWORD']
else:
    print("ERROR: Environment variable CAM_PASSWORD not defined")
    sys.exit(-1)

if 'CAM_ADDR' in os.environ.keys():
    CAM_ADDR = os.environ['CAM_ADDR']
else:
    print("ERROR: Environment variable CAM_ADDR not defined")
    sys.exit(-1)

template_globals = {
                'app_path': lambda p: web.ctx.homedomain + '/' + web.ctx.homepath + p,
            }

render = web.template.render('templates/', globals=template_globals)

class right:
    def GET(self):
        r = requests.get(
            '{URL}/cgi-bin/CGIProxy.fcgi?cmd=ptzMoveRight&usr={USER}&pwd={PWD}'.format(
                URL=CAM_ADDR,
                USER=CAM_USERNAME,
                PWD=CAM_PASSWORD
                ),
            timeout=TIMEOUT
            )
        web.header('Content-Type', 'text/xml')
        return render.snom_cam({
            'CAM_ADDR': CAM_ADDR,
            'CAM_USERNAME': CAM_USERNAME,
            'CAM_PASSWORD': CAM_PASSWORD
                })
          
class left:
    def GET(self):
        r = requests.get(
            '{URL}/cgi-bin/CGIProxy.fcgi?cmd=ptzMoveLeft&usr={USER}&pwd={PWD}'.format(
                URL=CAM_ADDR,
                USER=CAM_USERNAME,
                PWD=CAM_PASSWORD
                ),
            timeout=TIMEOUT
            )
        web.header('Content-Type', 'text/xml')
        return render.snom_cam({
            'CAM_ADDR': CAM_ADDR,
            'CAM_USERNAME': CAM_USERNAME,
            'CAM_PASSWORD': CAM_PASSWORD
                })

class up:
    def GET(self):
        r = requests.get(
            '{URL}/cgi-bin/CGIProxy.fcgi?cmd=ptzMoveUp&usr={USER}&pwd={PWD}'.format(
                URL=CAM_ADDR,
                USER=CAM_USERNAME,
                PWD=CAM_PASSWORD
                ),
            timeout=TIMEOUT
            )
        web.header('Content-Type', 'text/xml')
        return render.snom_cam({
            'CAM_ADDR': CAM_ADDR,
            'CAM_USERNAME': CAM_USERNAME,
            'CAM_PASSWORD': CAM_PASSWORD
                })

class down:
    def GET(self):
        r = requests.get(
            '{URL}/cgi-bin/CGIProxy.fcgi?cmd=ptzMoveDown&usr={USER}&pwd={PWD}'.format(
                URL=CAM_ADDR,
                USER=CAM_USERNAME,
                PWD=CAM_PASSWORD
                ),
            timeout=TIMEOUT
            )
        return ""

class stop:
    def GET(self):
        r = requests.get(
            '{URL}/cgi-bin/CGIProxy.fcgi?cmd=ptzStopRun&usr={USER}&pwd={PWD}'.format(
                URL=CAM_ADDR,
                USER=CAM_USERNAME,
                PWD=CAM_PASSWORD
                ),
            timeout=TIMEOUT
            )
        web.header('Content-Type', 'text/xml')
        return render.snom_cam({
            'CAM_ADDR': CAM_ADDR,
            'CAM_USERNAME': CAM_USERNAME,
            'CAM_PASSWORD': CAM_PASSWORD
                })

class snom_cam:
    def GET(self):
        web.header('Content-Type', 'text/xml')
        return render.snom_cam({
            'CAM_ADDR': CAM_ADDR,
            'CAM_USERNAME': CAM_USERNAME,
            'CAM_PASSWORD': CAM_PASSWORD
                })

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
