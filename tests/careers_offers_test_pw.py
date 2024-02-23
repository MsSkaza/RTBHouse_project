from pytest_bdd import scenario, given, when, then
from pages.careers_offers_page_pw import CareersPage


@scenario('features/careers_site.feature', 'Filter Remote Jobs')
def test_status():
    pass


@given("User is on the RTBhouse site")
def site_check(page):
    C = CareersPage(page)
    C.site_verification()


@when("User is filtering jobs by Remote option")
def filtering(page):
    C = CareersPage(page)
    C.confirm_cookies()
    C.change_filter_to_remote()
    C.click_see_more_until_disappear()


@then("Counter (X positions in all locations) should equals number of currently displayed offers")
def comparing(page):
    C = CareersPage(page)
    C.compare_numbers()


@then("Save information about the first 15 offers and save them to JSON")
def saving_json(page):
    C = CareersPage(page)
    C.scrape_job_offers()
    C.print_job_offers()
    C.publishing()
