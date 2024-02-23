from playwright.sync_api import Page, expect
import json


class CareersPage:

    def __init__(self, page: Page):
        self.page = page

    def site_verification(self):
        self.page.goto("https://www.rtbhouse.com/careers-offers")
        expect(self.page.get_by_text("All departments")).to_be_visible()

    def confirm_cookies(self):
        self.page.get_by_role("button", name="Reject all").click()

    def change_filter_to_remote(self):
        self.page.get_by_placeholder("On-site/remote/hybrid").click()
        self.page.get_by_role("option", name="Remote").click()

    def click_see_more_until_disappear(self):
        while self.page.query_selector("button:has-text('See more')"):
            self.page.wait_for_selector("button:has-text('See more')", timeout=5000).click()

    def compare_numbers(self):
        number_of_jobs = len(self.page.query_selector_all('.evPsTq'))

        #  "X positions in all locations"
        positions_text = self.page.inner_text('.eRErXB')
        positions_number = int(positions_text.split()[0])

        if number_of_jobs == positions_number:
            print("The number of records is equal to each item.")
        else:
            print("The number of records is not equal to each item")

    def scrape_job_offers(self):
        job_offers = self.page.query_selector_all('div.evPsTq')[:15]

        data = []
        for offer in job_offers:
            role_name = offer.query_selector('span.dzXsku').inner_text()
            work_mode = offer.query_selector('p.bjhSiT').inner_text()
            location = offer.query_selector('div.bFVbjq span').inner_text()
            offer_url = "https://www.rtbhouse.com/careers-offers" + offer.query_selector('.fscAr').get_attribute('href')

            data.append({
                'role_name': role_name,
                'work_mode': work_mode,
                'location': location,
                'offer_url': offer_url
            })

        return data

    def print_job_offers(self):
        job_offers = self.scrape_job_offers()
        for idx, offer in enumerate(job_offers, start=1):
            print(f"Offer {idx}:")
            print(f"Role: {offer['role_name']}")
            print(f"Work Mode: {offer['work_mode']}")
            print(f"Location: {offer['location']}")
            print(f"Offer URL: {offer['offer_url']}")
            print()

    def publishing(self, filename='job_offers.json'):
        job_offers = self.scrape_job_offers()

        with open(filename, 'w') as f:
            json.dump(job_offers, f, indent=4)

        print(f"Job offers have been exported to {filename} file.")
