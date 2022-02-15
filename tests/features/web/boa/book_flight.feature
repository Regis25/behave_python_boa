Feature: Book Flight flow

  Scenario: Verify an adult customer can search its round-trip flight
    Given I navigate to BOA website
    When I set in the Book Flight tab the following data
      | Field          | Value      |
      | from_location  | LA PAZ     |
      | to_location    | TARIJA     |
      | select         | round-trip |
      | departure_date | tomorrow   |
      | return_date    | 2 weeks    |
      | adults         | 1          |
      | child          | 0          |
      | infant         | 0          |
    Then the "departure date and the return date" should be the same as the Book Flight searching
      And the "from and to location" should be the same as the Book Flight searching
      And the "adults" should be the same as the Book Flight searching