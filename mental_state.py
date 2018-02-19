# Description of solution:
# https://regex101.com/r/ZtN9jl/1
# When you get anxious:
import re


class MentalState(object):

    def __init__(self, stimuli, thought):
        self.thought = thought
        self.stimuli = stimuli

    def update(self, new_thought):
        self.thought = new_thought

    def speak(self):
        print("{} makes me think that {}.".format(self.stimuli, self.thought))

    def quality(self):
        pattern = re.compile(
            r'already (?:s\w*|d\w*)|(?:N|n)othing .*|regular|ordinary|normal|natura.*|simpl.*|more of the same|not supris.*|bor[a-z]*|tr[a-z]*.*(?:scary|terrifying|threatening)|i\w* [a]?[ ]?(?:dumb|stupid|joke)+')
        if len(pattern.findall(self.thought)) > 0:
            print('This is a healthy way to think about {} because you included the following words:\n'.format(self.stimuli) + '\n'.join(
                ['"{}"'.format(x) for x in pattern.findall(self.thought)]))
        else:
            print("This is an unhealthy thought because you are taking the stimuli a bit too seriously.\n\
If you rephrase it to make the stimuli more as something dumb then you'll likely pass this condition")


state = MentalState('demo', 'is this going to work?')
state.quality()

state.update('There is nothing here to really worry about')
