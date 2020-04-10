"""
Watch first
https://www.youtube.com/watch?v=IZmlkoOO8Mg&t=397s




"""

# from flask import Flask
# from flask_testing import TestCase
#
#
# class MyTest(TestCase):
#
#     def create_app(self):
#         app = Flask(__name__)
#         app.config['TESTING'] = True
#         # Default port is 5000
#         app.config['LIVESERVER_PORT'] = 8943
#         # Default timeout is 5 seconds
#         app.config['LIVESERVER_TIMEOUT'] = 10
#         return app
#
#     def test_server_is_up_and_running(self):
#         response = urllib2.urlopen(self.get_server_url())
#         self.assertEqual(response.code, 200)
#
#
#     @app.route("/ajax/")
#     def some_json():
#         return jsonify(success=True)
#
#     class TestViews(TestCase):
#         def test_some_json(self):
#             response = self.client.get("/ajax/")
#             self.assertEquals(response.json, dict(success=True))
