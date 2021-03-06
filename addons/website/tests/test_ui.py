import openerp.tests


class TestUi(openerp.tests.HttpCase):
    def test_01_public_homepage(self):
        self.phantom_js("/", "console.log('ok')", "openerp.website.snippet")

    def test_02_admin_homepage(self):
        self.phantom_js("/", "console.log('ok')", "openerp.website.editor", login='admin')

    def test_03_admin_rte(self):
        self.phantom_js("/", "openerp.Tour.run('website_rte', 'test')", "openerp.Tour.tours.website_rte", login='admin')

    def test_04_admin_tour_banner(self):
        self.phantom_js("/", "openerp.Tour.run('banner', 'test')", "openerp.Tour.tours.banner", login='admin')
