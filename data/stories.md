## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## happy path
* greet
  - utter_greet
* get_weather
  - utter_send_weather

## get_name
* my_name_is{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_send_name
  - action_help

## get_name2
* my_name_is{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_send_name
  - action_help

## get_name3
* my_name_is{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_send_name
  - action_help

## get_name4
* my_name_is{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_send_name
  - action_help
