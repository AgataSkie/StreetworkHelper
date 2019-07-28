from django_webtest import WebTest


class HomepageTestCase(WebTest):

    def test_homepage_runs(self):
        resp = self.app.get('/places/')
        assert resp.status == '200 OK'
        resp.mustcontain('<title>StreetWork</title>')


# map is present on a page


# if new place is added, a point marker appears in js script (test-db)