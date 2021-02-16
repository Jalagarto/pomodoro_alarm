import os
import time
import argparse
from text_to_speech import say_smth
import sys


# # Disable and enable prints:
# def blockPrint():    # Disable
#     # print('blockPrint activated')
#     sys.stdout = open(os.devnull, 'w')
# def enablePrint():   # Restore
#     sys.stdout = sys.__stdout__
# """ usage  -->  blockPrint()  enablePrint() """


# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')
# Add the arguments
my_parser.add_argument('-n',
        '--pomodoros',
        default=2,
        help='Total number of pomodoros you want to do in a row',
        type=int,
        required=False)
my_parser.add_argument('-pt',
        '--pomodoro_time',
        default=40,
        help='Total number of pomodoros you want to do in a row',
        type=int,
        required=False)
my_parser.add_argument('-t',
        '--small_break_time',
        default=5,
        help='small break time (minutes)',
        type=int,
        required=False)
my_parser.add_argument('-T',
        '--big_break_time',
        default=15,
        help='big break time (minutes)',
        type=int,
        required=False)
my_parser.add_argument('-b',
        '--num_pomdrs_to_have_big_break',
        default=2,
        help='number of pomodoros in a row',
        type=int,
        required=False)
my_parser.add_argument('-print_time',
        '--printing_frequence',
        default=5,
        help='time for printing time reminders',
        type=int,
        required=False)

# Execute the parse_args() method
args = my_parser.parse_args()
pomodoros, pomodoro_time, small_break_time, big_break_time, num_pomdrs_to_have_big_break, print_time = args.pomodoros,\
    args.pomodoro_time,	args.small_break_time, args.big_break_time, args.num_pomdrs_to_have_big_break, args.printing_frequence

# total number of pomodoros cant be smaller than the number of pomodoros to have a break
if pomodoros < num_pomdrs_to_have_big_break:
	num_pomdrs_to_have_big_break = pomodoros

str1 = (f"{pomodoros} Pomodoros of {pomodoro_time} minutes, in Series of {num_pomdrs_to_have_big_break} ")
str2 = (f"& Breaks of {small_break_time} & {big_break_time}")


def say_smth_2(texto, language='en', horn=False):
    """tries using say_smth, if it doesn't work tries os.system(speak)"""
    print('\n', texto, '\n')
    try:
        say_smth(texto, language=language, horn=False)
    except:
        os.system("echo {} | espeak &".format(texto))

say_smth_2(str1+str2)


def main(records):
    ### now the pomodoros timing
    beep_duration = 1  # seconds
    freq = 440  # Hz
    # rest = 5 # minutes
    counter = 0
    for i in range(pomodoros):
        print(f"\nPomodoro nº {i+1}:")
        records.pomodoros = i+1
        for t in range(pomodoro_time*60):
            time.sleep(1)
            if t%(print_time*60)==0:
                records.minutes = t/60
                i# print(f" {t/60} minutes") # ,end="\r")
            if t%(int(60*pomodoro_time*3/5))==0:
                # print("\n{} minutes have gone from Pomodoro nº {}".format(int(t/60), i+1))
                texto = "{} minutes have gone from Pomodoro {}".format(int(t/60), i+1) # "{} minutes have gone".format(int(t/60))
                say_smth_2(texto, language='en', horn=False)
            if t%(int(60*5))==0:
                print("{} minutes - pomodoro {}".format(int(t/60), i+1))

        for i in range(1):
            time.sleep(1)
            try:
                # blockPrint()
                say_smth(horn=True)
                # enablePrint()
            except:
                os.system('play -nq -t alsa synth {} sine {}'.format(beep_duration, freq))

        counter +=1
        print('\n', counter, 'pomodoros')

        if 1 < counter < pomodoros and num_pomdrs_to_have_big_break%counter == 0:
            # print('\nTime for a Big Break. Rest {} minutes'.format(big_break_time))
            texto = "Take a long break. Rest for {} minutes".format(big_break_time)
            say_smth_2(texto, language='en', horn=False)
            time.sleep(big_break_time*60)
            # print("\nbe ready for the next one\n")
            texto = "Be ready for the next pomodoro"
            say_smth_2(texto, language='en', horn=False)
            time.sleep(30)
        elif counter < pomodoros:
            # print('Time for a small break. Rest {} minutes'.format(small_break_time))
            texto = "Take a small break. Rest for {} minutes".format(small_break_time)
            say_smth_2(texto, language='en', horn=False)
            time.sleep(small_break_time*60)
            # print("\nbe ready for the next one\n")
            texto = "Be ready for the next pomodoro"
            say_smth_2(texto, language='en', horn=False)
            time.sleep(30)
        else:
            # os.system('spd-say "BYE!"')
            texto = "Has acabado tu tanda! pégate un homenaje! Chao Bambino"
            say_smth_2(texto, language='es', horn=False)
            print('BYE!')

try:
    class records:
        """save some output  metadata"""
    main(records)
except KeyboardInterrupt:
    print('Interrupted')
    try:
        print(f"[INFO]: Final Pomodoro: {records.pomodoros}  -  Final minutes: {records.minutes}")
        sys.exit(0)
    except SystemExit:
        # print(f"[INFO]: Final Pomodoro: {records.pomodoros}  -  Final minutes: {records.minutes}")
        os._exit(0)


# USAGE:      python3 pomodoro_alarm.py -n 4 -pt 40 -t 5 -T 15 -b 2
# os.system('spd-say "your program has finished"')
