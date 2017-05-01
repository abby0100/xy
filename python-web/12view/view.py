# coding = utf-8

from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__, template_folder='../templates')

class BasicView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'

        context = {
                'users': self.get_users()
                }
        return self.render_template(context)

class UserView(BasicView):
    def get_template_name(self):
        return '../templates/users.html'

    def get_users(self):
        return [{
            'username': 'fake',
            'avatar': 'http://localhost:1027/'
            }]

app.add_url_rule('/users', view_func=UserView.as_view('userview'))

if __name__ == '__main__':
    app.run(host='localhost', port=1027)
