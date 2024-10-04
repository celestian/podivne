Feature: ppp

  Scenario: Just ppp
    Given we have ppp installed
    When we run ppp
    Then return code is "1"

  Scenario: Just ppp run
    Given we have ppp installed
    When we run ppp run
    Then return code is "0"
