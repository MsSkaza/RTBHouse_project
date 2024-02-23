Feature: Careers Site Functionality

    Scenario: Filter Remote Jobs
      Given User is on the RTBhouse site
      When User is filtering jobs by Remote option
      Then Counter (X positions in all locations) should equals number of currently displayed offers
      Then Save information about the first 15 offers and save them to JSON