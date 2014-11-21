import web
import json
from mimerender import mimerender

# render_xml = lambda message: '<message>%s</message>'%message
# render_json = lambda **args: json.dumps(args)
# render_html = lambda message: '<html><body>%s</body></html>'%message
# render_txt = lambda message: message

urls = (
    '/(.*)', 'delays'
)
app = web.application(urls, globals())

class delays:
    def GET(self, name):
      with open('delays.json') as f
        return f.read()

      return 500

if __name__ == "__main__":
    app.run()