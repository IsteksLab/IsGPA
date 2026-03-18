from prompt_toolkit.shortcuts import input_dialog, message_dialog, button_dialog
import json, os, sys

if not os.path.exists("config.json"):
  raise FileNotFoundError("main.py - Missing vital component: 'config.json'")
  sys.exit(1)

with open("config.json", "r") as r:
  config = json.load(r)

def ask(number):
  title = "IsGPA - GPA Calculator"
  totalGrades = input_dialog(title=title, text="List All Course Averages (Separated by Commas)").run()
  try:
    totalGrades = [int(grade.strip() for grade in totalGrades.split(","))]
  except:
    raise TypeError("main.py - ask(number): Variable totalGrades expects units separated by commas.")
    sys.exit(1)

  updatedGrades, isWeighted = [], None
  if number == 1:
    isWeighted = "unweighted"
  elif number == 2:
    isWeighted = "weighted"
  for grades in totalGrades:
    if number == 1:
      for scale in config["gpaLevel"]["4"].items():
        if grades in range(scale.get("range")[0], (scale.get("range")[1] + 1)):
          updatedGrades.append(scale.get("score"))
        elif grades in range(0, 60):
          updatesGrades.append(0)
    elif number == 2:
      for scale in config["gpaLevel"]["5"].items():
        if grades in range(scale.get("range")[0], (scale.get("range")[1] + 1)):
          updatedGrades.append(scale.get("score"))
        elif grades in range(0, 60):
          updatesGrades.append(0)
  gpa = sum(updatedGrades) / len(updatedGrades)
  message_dialog(title=title, text=f"Your {isWeighted} GPA (rounded) is: {str(round(gpa))}. And unrounded is: {str(gpa)}").run()
  menu()
  
def menu():
  title = "IsGPA - Menu"
  mOptions = button_dialog(title=title, text="Choose GPA Scale", buttons=[("Unweighted (4.0)", 1), ("Weighted (5.0)", 2), ("Exit", 3)]).run()
  if mOptions == 1 or mOptions == 2:
    ask(mOptions)
  elif mOptions == 3:
    sys.exit(0)

menu()
