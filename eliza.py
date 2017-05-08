import re
import random

class eliza:
  def __init__(self):
    self.keywords = list(map(lambda x:x[0], conversation_temp))
    self.patterns = list(map(lambda x:re.compile(x[1], re.IGNORECASE),conversation_temp))
    self.outputs = list(map(lambda x:x[2],conversation_temp))


  def translate(self, str, dict):
    words = str.lower().split()
    keys = dict.keys()
    for i in range(0,len(words)):
      if words[i] in keys:
         words[i] = dict[words[i]]
    return " ".join(words)


  def respond(self,str):
    for i in range(0,len(self.keywords)):
      if self.keywords[i] in str:
        match = self.patterns[i].match(str)
        if match:
          resp = random.choice(self.outputs[i])
          pos = resp.find('%')
          while pos > -1:
            num = int(resp[pos + 1:pos + 2])
            resp = resp[:pos] + \
                   self.translate(match.group(num), conv_by_subject) + \
                   resp[pos + 2:]
            pos = resp.find('%')
            # fix munged punctuation at the end
          if resp[-2:] == '?.': resp = resp[:-2] + '.'
          if resp[-2:] == '??': resp = resp[:-2] + '?'
          return resp
    return "Tell me more."




conv_by_subject = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}


conversation_temp = [
  [r'are',
  r'(.*) are all (.*)',
  [ "In what way?"]],

  [r'something',
  r'(.*) about something (.*)',
  ["Can you think of a specific example?"]],

  [r'boyfriend',
  r'(.*) boyfriend (.*)',
  ["Your boyfriend %2"]],

  [r'depressed',
  r"(.*) I'm depressed (.*)",
  ["I'm sorry to hear you are depressed."]],

  [r'unhappy',
  r"(.*) I am unhappy(.*)",
  ['Do you think coming here will help you not to be unhappy?']],

  [r'help',
  r"(.*) need (.*) help(.*)",
  ['What would it mean to you if you got some help?']],

  [r'mother',
  r'(.*)',
  ['Tell me more about your family .',
  'Who else in your family takes care of you?']],

  [r'like',
  r'(.*) father',
  ['%1 father',
  'What resemblance do you see?']],
]


def call_eliza():
  print("Therapist\n---------")
  print("Talk to the program by typing in plain English, using normal upper-")
  print('and lower-case letters and punctuation.  Enter "quit" when done.')
  print('='*72)
  s = ""
  therapist = eliza()
  while s != "quit":
    try: s = input(">")
    except EOFError:
      s = "quit"
      print(s)
    while s[-1] in "!.":
        s = s[:-1]
    print(therapist.respond(s))


if __name__ == "__main__":
  call_eliza()
