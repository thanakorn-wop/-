import random
from random import randrange, uniform
import time


def card():
    sym = ["♣", "♦", "♥", "♠"]
    card = {}
    all_card = []
    for i in range(len(sym)):
        for y in range(1, 14):
            if y == 11:
                card["J"] = sym[i]
            elif y == 12:
                card["Q"] = sym[i]
            elif y == 13:
                card["K"] = sym[i]
            else:
                card[str(y)] = sym[i]
        # no_sym.append(card)
        all_card.append(card)
        card = {}
    return all_card


def player(amount_card,all_card):
    # all_card = card()
    player_card = []
    card1 = {}
    while True:
        random = randrange(1, 14)
        no_sym = randrange(0, 4)
        # print("check random = ",random)
        if random == 11:
            if "J" in all_card[no_sym].keys():
                card1["J"] = all_card[no_sym]["J"]
                player_card.append(card1)
                all_card[no_sym].pop("J")
            
        elif random == 12:
            if "Q" in all_card[no_sym].keys():
                card1["Q"] = all_card[no_sym]["Q"]
                player_card.append(card1)
                all_card[no_sym].pop("Q")
        elif random == 13:
            if "K" in all_card[no_sym].keys():
                card1["K"] = all_card[no_sym]["K"]

                player_card.append(card1)
                all_card[no_sym].pop("K")
        else:
            if str(random) in all_card[no_sym].keys():
                card1[random] = all_card[no_sym][str(random)]
                player_card.append(card1)
                # print(card1)
                all_card[no_sym].pop(str(random))
        
        # print("check1 = ", card1)
        card1 = {}
        # print("check2 = ", player_card)
        # print("check = ",card1)
        # print("check3 = ", all_card)
        # print("aaa = ",all_card[no_sym]["K"])
        if len(player_card) == amount_card:
            break
    # print("Player card = ", player_card)
    return player_card,all_card


def broker(amount_card,all_card):
    broker_card = []
    card1 = {}
    while True:
        random = randrange(1, 14)
        no_sym = randrange(0, 4)
        # print("check random = ",random)
        if random == 11:
            if "J" in all_card[no_sym].keys():
                card1["J"] = all_card[no_sym]["J"]
                broker_card.append(card1)
                all_card[no_sym].pop("J")
            
        elif random == 12:
            if "Q" in all_card[no_sym].keys():
                card1["Q"] = all_card[no_sym]["Q"]
                broker_card.append(card1)
                all_card[no_sym].pop("Q")
        elif random == 13:
            if "K" in all_card[no_sym].keys():
                card1["K"] = all_card[no_sym]["K"]

                broker_card.append(card1)
                all_card[no_sym].pop("K")
        else:
            if str(random) in all_card[no_sym].keys():
                card1[random] = all_card[no_sym][str(random)]
                broker_card.append(card1)
                # print(card1)
                all_card[no_sym].pop(str(random))
        
        # print("check1 = ", card1)
        card1 = {}
        # print("check2 = ", player_card)
        # print("check = ",card1)
        # print("check3 = ", all_card)
        # print("aaa = ",all_card[no_sym]["K"])
        if len(broker_card) == amount_card:
            break
    # print("Player card = ", player_card)
    return broker_card,all_card

def Start_game():
    time.sleep(2)
    print("--------------- Start Game in -------------")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    amount_card = 2
    time.sleep(1)

    all_card = card()
    while True:
        broker_start = randrange(0, 2)
        player_start = randrange(0, 2)
        no = 1
        player_score = 0
        broker_score = 0
        if broker_start > player_start:
            broker_card,all_card = broker(amount_card,all_card)
            player_card,all_card = player(amount_card,all_card)
            for i in range(len(broker_card)):
                for k,v in broker_card[i].items():
                    print("BROKER_CARD ",no, " = ",k,v)
                    check_value = isinstance(k, int)
                    if check_value == True:
                        broker_score+=k
                    else:
                        broker_score +=0
                    time.sleep(1)
                    no+=1
            if broker_score == 10:
                broker_score = 0
            elif broker_score > 10:
                broker_score = abs(broker_score-10)
            
            no =1
            print("\n")
            for i in range(len(player_card )):
                for k,v in player_card[i].items():
                    print("PLAYER_CARD ",no, " = ",k,v)
                    check_value = isinstance(k, int)
                    if check_value == True:
                        player_score+=k
                    else:
                        player_score+=0
                    time.sleep(1)
                    no+=1
            if player_score == 10:
                player_score = 0
            elif player_score > 10:
                player_score = abs(player_score-10)
            print("\n")
            print("Point_BROKER = ",broker_score," Point_PLAYER = ",player_score)
            if broker_score > player_score:
                print("\n")
                print("----- WINER is BROKER -----")
                        
            elif player_score > broker_score:
                print("\n")
                print("----- WINER is PLAYER -----")
            else:
                print("\n")

                count = 0
                sym_score_broker= 0
                for i in range(len(broker_card)):
                    for k,v in broker_card[i].items():
                    
                        if k == "♣":
                            count+=1
                            ssym_score_broker += count
                            count = 0
                        elif k =="♦":
                            count +=1
                            sym_score_broker += count
                            count = 0
                        elif k =="♥":
                            count+=1
                            sym_score_broker += count
                            count = 0
                        elif k == "♠":
                            count+=1
                            sym_score_broker += count
                            count = 0
                count = 0
                
                sym_score_player = 0
                for i in range(len(player_card)):
                    for k,v in player_card[i].items():
                    
                        if k == "♣":
                            count+=1
                            sym_score_player += count
                            count = 0
                        elif k =="♦":
                            count +=1
                            sym_score_player += count
                            count = 0
                        elif k =="♥":
                            count+=1
                            sym_score_player += count
                            count = 0
                        elif k == "♠":
                            count+=1
                            sym_score_player += count
                            count = 0
                if sym_score_player == 2:
                    print("----- WINER is PLAYER -----")
                elif sym_score_broker == 2:
                    print("----- WINER is BROKER -----")
                else:
                    print("----- Result is EQUAL -----")
            break
        else:
            player_card,all_card = player(amount_card,all_card)
            broker_card,all_card = broker(amount_card,all_card)
            # print("playera_card = ",player_card)
            # print("broker_card = ",broker_card)
            # print("card = ",all_card)
            for i in range(len(player_card)):
                for k,v in player_card[i].items():
                    print("PLAYER_CARD ",no, " = ",k,v)
                    check_value = isinstance(k, int)
                    if check_value == True:
                        player_score +=k
                    else:
                        player_score +=0
                    time.sleep(1)
                    no+=1
            if player_score == 10:
                player_score = 0
            elif player_score > 10:
                player_score = abs(player_score-10)
            
            no =1
            print("\n")
            for i in range(len(broker_card)):
                for k,v in broker_card[i].items():
                    print("BROKER_CARD ",no, " = ",k,v)
                    check_value = isinstance(k, int)
                    if check_value == True:
                        broker_score+=k
                    else:
                        broker_score+=0
                    time.sleep(1)
                    no+=1
            if broker_score == 10:
                broker_score = 0
            elif broker_score > 10:
                broker_score = abs(broker_score-10)
            print("\n")
            print("Point_BROKER = ",broker_score," Point_PLAYER = ",player_score)
            if broker_score > player_score:
                print("\n")
                print("----- WINER is BROKER -----")
                        
            elif player_score > broker_score:
                print("\n")
                print("----- WINER is PLAYER -----")
            else:
                
                # score_sym = {"♣":1,"♦":2,"♥":3,"♠":4}
                count = 0
                sym_score_player = 0
                for i in range(len(player_card)):
                    for k,v in player_card[i].items():
                    
                        if k == "♣":
                            count+=1
                            sym_score_player += count
                            count = 0
                        elif k =="♦":
                            count +=1
                            sym_score_player += count
                            count = 0
                        elif k =="♥":
                            count+=1
                            sym_score_player += count
                            count = 0
                        elif k == "♠":
                            count+=1
                            sym_score_player += count
                            count = 0
                count = 0
                sym_score_broker= 0
                for i in range(len(broker_card)):
                    for k,v in broker_card[i].items():
                    
                        if k == "♣":
                            count+=1
                            sym_score_broker+= count
                            count = 0
                        elif k =="♦":
                            count +=1
                            sym_score_broker += count
                            count = 0
                        elif k =="♥":
                            count+=1
                            sym_score_broker += count
                            count = 0
                        elif k == "♠":
                            count+=1
                            sym_score_broker += count
                            count = 0
                if sym_score_player == 2:
                    print("----- WINER is PLAYER -----")
                elif sym_score_broker == 2:
                    print("----- WINER is BROKER -----")
                else:
                    print("----- Result is EQUAL -----")

            break
       


Start_game()

