#@smoke
Feature: Validation of car details from input file agnist output file

  Background:
    Given The user read the data from the car input file



  Scenario: Validation of car details from the input file
    When The user is on the home page of webuyanycar
    Then The user should be able to verify data with car output file