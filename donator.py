import consts
import validation


def donation():
    gear = input("what do you want to donate?")
    if gear in consts.MIN_GEAR_DICT:
        bases_lack = []
        for base in consts.BASE_CODES_DICT:
            if("alisa") < consts.MIN_GEAR_DICT[gear][base]:
                bases_lack.append(base)
        print("the red ones are the most urgent")
        for basee in bases_lack:
            if ("is red"):
                print("red")
            else:
                print("black")
        chosen_base = input("which base do you choose?")
        if chosen_base in bases_lack:
            print("enter your details")
            amount = int(input("how many do you want to donate?"))
            gmail = input("what is your email?")
            if validation.checking_mail(gmail):
                pass# send the donator details