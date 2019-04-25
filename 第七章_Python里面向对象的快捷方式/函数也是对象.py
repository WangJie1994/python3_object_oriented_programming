# def my_function():
#     print('the function was called')
#
#
# my_function.description = 'a silly function'
#
#
# def second_function():
#     print('the second was called')
#
#
# second_function.description = 'a siller function'
#
#
# def another_function(function):
#     print('the description:', end=' ')
#     print(function.description)
#     print('the name:', end=' ')
#     print(function.__name__)
#     print('the class:', end=' ')
#     print(function.__class__)
#     print('now call function')
#     function()
#
#
# another_function(my_function)
# another_function(second_function)

import datetime
import time


class TimeEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime < datetime.datetime.now()


class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        self.events.append(TimeEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)


def format_time(message, *args):
    now = datetime.datetime.now().strftime("%I:%M:%S")
    print(message.format(*args, now=now))


def one(timer):
    format_time("{now}: called one")


def two(timer):
    format_time("{now}: called two")


def three(timer):
    format_time("{now}: called three")


def four(timer):
    format_time("{now}: called four")


def five(timer):
    format_time("{now}: called five")


class Repeater:
    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        self.count += 1
        format_time("{now}: repeat {0}", self.count)
        timer.call_after(5, self.repeater)


timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, repeater.repeater)
format_time("{now}: starting")
timer.run()
