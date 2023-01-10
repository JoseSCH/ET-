import time;
import os;
import random;

#List of verbs in spanish.
SVS = [["Responder", "Contestar"], ["Preguntar", "Pedir"], ["Ser", "Estar"], "Llamar", "Limpiar", "Cerrar", ["Venir", "Llegar"], "Copiar", "Hacer", "Dibujar", ["Beber", "Tomar"], ["Comer", "Consumir"], "Borrar", "Explicar", ["Terminar", "Finalizar"], "Olvidar", ["Obtener", "Conseguir"], "Dar", "Ir", ["Crecer", "Desarrollarse"], "Tener", "Ayudar", ["Saber", "Conocer"], "Reir", "Aprender", "Gustar", "Escuchar", "vivir", "Mirar", "Necesitar", "Abrir", ["Jugar", "Tocar"], "Practicar", "Pronunciar", ["Poner", "Colocar"]];

#List of verbs in english (Simple present).
EVSP = ["Answer", "Ask", "Be", "Call", "Clean", "Close", "Come", "Copy", "Do", "Draw", "Drink", "Eat", "Erase", "Explain", "Finish", "forget", "Get", "Give", "Go", "Grow", "Have", "Help", "Know", "Laugh", "Learn", "Like", "Listen", "Live", "Look", "Need", "Open", "Play", "Practice", "Pronounce", "Put"];

#list of verbs in english (Simple past).
EVSPst = ["Answered", "Asked", "Was", "Called", "Cleaned", "Closed", "Came", "Copied", "Did", "Drew", "Drank", "Ate", "Erased", "Explained", "Finished", "Forgot", "Got", "Gave", "Went", "Grew", "Had", "Helped", "Knew", "Laughed", "Learned", "Liked", "Listened", "Lived", "Looked", "Needed", "Opened", "Played", "Practiced", "Pronounced", "Put"];

#list of verbs in english (Participle past).
EVPT = ["Answered", "Asked", "Been", "Called", "Cleaned", "Closed", "Come", "Copied", "Done", "Drawn", "Drunk", "Eaten", "Erased", "Explained", "Finished", "Forgotten", "Gotten", "Given", "Gone", "Grown", "Had", "Helped", "Known", "Laughed", "Learned", "Liked", "Listened", "Lived", "Looked", "Needed", "Opened", "Played", "Practiced", "Pronounced", "Put"];

#Lives
Lives = 5;
Score = 0;



class ET:
    def __init__(me, SVS, EVSP, EVSPst, EVPT):
        me.SVS = SVS;
        me.EVSP = EVSP;
        me.EVSPst = EVSPst;
        me.EVPT = EVPT;

    def intro(me):
        print("Welcome to this....");
        time.sleep(1);
        print("TRIVIA");
        time.sleep(1);
        print("ENGLISH");
        time.sleep(1);
        print("GAME!!!!!!");
        time.sleep(1);
        print("Enjoy the game!!!!, You only have 5 lives!!!");
        time.sleep(3);
        os.system("cls");

def out():
    global Lives;
    Lives -= 1;

def add():
    global Score;
    Score += 1;

def game(L1, L2, L3, L4):
    while(True):
        Index = random.choice(range(len(L1)));
        print("***************Lives*************** | ***************Score***************");
        print("_________________" + str(Lives) + "_________________ | " + "_________________" + str(Score) + "__________________\n\n");

        if(Score >= 10):
            print("Hoorayyyy!!!, you made it....");
            print("Here is your trophy\n\n");
            print("  __   __  _______  ______   _______  _______  _______  _______  _______ ")
            print(" |  | |  ||       ||    _ | |       ||       ||       ||       ||       |")
            print(" |  |_|  ||   _   ||   | || |_     _||    ___||_     _||   _   ||  _____|")
            print(" |       ||  | |  ||   |_||_   |   |  |   |___   |   |  |  | |  || |_____ ")
            print(" |_     _||  |_|  ||    __  |  |   |  |    ___|  |   |  |  |_|  ||_____  |")
            print("   |   |  |       ||   |  | |  |   |  |   |___   |   |  |       | _____| |")
            print("   |___|  |_______||___|  |_|  |___|  |_______|  |___|  |_______||_______|")
            time.sleep(5);
            quit();

        if(Lives == 0):
                print("You have 0 lives, good bye!!!");
                time.sleep(1);
                print("You have been eaten by sharks!!!");
                time.sleep(5);
                quit();

        if(type(L1[Index]) == list):
            print("The word is: ");
            for x in L1[Index]:
                print(x + "\n");
        else:
            print("The word is: " + L1[Index]);

        print("What is the translation in english of it?");
        answer = input("> ");
        amay = answer.lower();
        amayl2 = L2[Index].lower();
        time.sleep(1);

        if(amay == amayl2):
            print("That is correct!!!");
            add();

            print("Now give me the simple past tense for that word :)");
            answer = input("> ");
            amay = answer.lower();
            amayl3 = L3[Index].lower();
            time.sleep(1);

            if(amay == amayl3):
                print("That is correct!!!");
                add();

                print("Now give me the past participle tense for that word :)");
                answer = input("> ");
                amay = answer.lower();
                amayl4 = L4[Index].lower();
                time.sleep(1);

                if(amay == amayl4):
                    print("That is correct!!!");
                    add();
                else:
                    print("Wrong!!!");
                    out();
                    time.sleep(2);
                    os.system("cls");
                    continue;

            else:
                print("Wrong!!!");
                out();
                time.sleep(2);
                os.system("cls");
                continue;

        else:
            print("Wrong!!!");
            out();
            time.sleep(2);

        os.system("cls");
        
caller = ET(SVS, EVSP, EVSPst, EVPT);
caller.intro();

game(caller.SVS, caller.EVSP, caller.EVSPst, caller.EVPT);