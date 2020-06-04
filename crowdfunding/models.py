# Von oTree automatisch erstellte Importe
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

# Import, um Datum und Zeit zu erhalten
from datetime import datetime

# Name des Autors
author = 'Marcel Mahdavian'

# Beschreibung des Projektes
doc = """
Crowdfunding Experiment
"""


class Constants(BaseConstants):

    # Legt die Bezeichnung der App in URLs fest
    name_in_url = 'Crowdfunding'

    # Legt die Anzahl der Spieler pro Gruppe fest
    players_per_group = 6

    # Legt fest, wie viele Runden das Experiment haben soll, wobei in jeder Runde ein mal gespielt wird
    # Hinweis: Die erste Runde ist immer eine ungewertete Übungsrunde (falls das Experiment z.B. aus 12 gewerteten Runden bestehen soll, muss der Wert von num_rounds auf 13 gesetzt werden)
    # Hinweis: Die Anzahl der Runden sollte stets folgende Formel erfüllen: Runden = n * Anzahl Spieler + 1, mit n ∈ N
    num_rounds = 3


class Subsession(BaseSubsession):

    # Wird beim Erstellen der Sitzung aufgerufen und für jede Runde ein Mal ausgeführt
    def creating_session(self):

        # Erstellt (Sitzungs-)Variable group_counter mit dem Wert: 0 (wird in der EndWaitPage Klasse in pages.py genutzt)
        self.session.vars['group_counter'] = 0

        # Erstellt (Sitzungs-)Variable last_group mit dem Wert: 0 (wird in der EndWaitPage Klasse in pages.py genutzt)
        self.session.vars['last_group'] = 0

        # Variable group_id mit dem Wert 1. Wird später der ersten Gruppe zugewiesen und anschließend erhöht
        group_id = 1

        # Erstellt (Sitzungs-)Variable csv_file, die folgenden Wert zugewiesen bekommt: Aktuelles Datum und Uhrzeit als String (z.B. "20.04.2020_14.09")
        self.session.vars['csv_file'] = datetime.now().strftime("%d.%m.%Y_%H.%M")

        # Für jede Gruppe:
        for g in self.get_groups():

            # Der Spendenstand von Projekt A wird auf folgenden Wert gesetzt: In settings.py gewähltes Startkapital für Projekt A
            g.a_total = self.session.config['Project_A_Seed']

            # Falls es mehr als ein Projekt geben soll (Anzahl wird in settings.py festgelegt):
            if self.session.config['Num_Projects'] > 1:

                # Der Spendenstand von Projekt B wird auf folgenden Wert gesetzt: In settings.py gewähltes Startkapital für Projekt B
                g.b_total = self.session.config['Project_B_Seed']

            # Falls es mehr als zwei Projekte geben soll (Anzahl wird in settings.py festgelegt):
            if self.session.config['Num_Projects'] > 2:

                # Der Spendenstand von Projekt C wird auf folgenden Wert gesetzt: In settings.py gewähltes Startkapital für Projekt C
                g.c_total = self.session.config['Project_C_Seed']

            # Falls es mehr als drei Projekte geben soll (Anzahl wird in settings.py festgelegt):
            if self.session.config['Num_Projects'] > 3:

                # Der Spendenstand von Projekt D wird auf folgenden Wert gesetzt: In settings.py gewähltes Startkapital für Projekt D
                g.d_total = self.session.config['Project_D_Seed']

            # Erhöht den Wert der (Sitzungs-)Variable last_group um 1
            self.session.vars['last_group'] += 1

            # Der aktuellen Gruppe wird der Wert der Variable group_id zugewiesen
            g.group_id  = group_id

            # Erhöht den Wert der Variable group_id um 1
            group_id += 1

            # Erstellt eine CSV-Datei mit dem aktuellen Datum und Uhrzeit + "_Group" + ID der aktuellen Gruppe als Namen und öffnet die Datei zum schreiben
            with open(self.session.vars['csv_file'] + "_Group" + str(g.group_id) + ".csv", "w") as file:

                # Schreibt Folgendes in die CSV-Datei: NAMEN der Variablen in SESSION_CONFIGS (in settings.py) + "num_rounds" + "players_per_group" + neuer Absatz (Inhalte getrennt durch Semikolons)
                file.write("All_Or_Nothing;Refund_Bonus;Early_Bird_Bonus;Enable_Backout;Backout_Fees;Show_Backers;Public_Goods;Min_Factor;Round_Duration;Bonus_Duration;Num_Projects;Endowment;Project_A_Goal;Project_B_Goal;Project_C_Goal;Project_D_Goal;Project_A_Seed;Project_B_Seed;Project_C_Seed;Project_D_Seed;real_world_currency_per_point;participation_fee;num_rounds;players_per_group" + "\n")

                # Schreibt Folgendes in die CSV-Datei: WERTE der Variablen in settings.py, die der Admin beim Erstellen der Sitzung festlegt + Anzahl Runden + Anzahl Spieler pro Gruppe + zwei neue Absätze (Inhalte getrennt durch Semikolons)
                # Hinweis: Für Erklärungen der Variablen siehe SESSION_CONFIGS in settings.py
                file.write(str(self.session.config['All_Or_Nothing']) + ";" +
                           str(self.session.config['Refund_Bonus']) + ";" +
                           str(self.session.config['Early_Bird_Bonus']) + ";" +
                           str(self.session.config['Enable_Backout']) + ";" +
                           str(self.session.config['Backout_Fees']) + ";" +
                           str(self.session.config['Show_Backers']) + ";" +
                           str(self.session.config['Public_Goods']) + ";" +
                           str(self.session.config['Min_Factor']) + ";" +
                           str(self.session.config['Round_Duration']) + ";" +
                           str(self.session.config['Bonus_Duration']) + ";" +
                           str(self.session.config['Num_Projects']) + ";" +
                           str(self.session.config['Endowment']) + ";" +
                           str(self.session.config['Project_A_Goal']) + ";" +
                           str(self.session.config['Project_B_Goal']) + ";" +
                           str(self.session.config['Project_C_Goal']) + ";" +
                           str(self.session.config['Project_D_Goal']) + ";" +
                           str(self.session.config['Project_A_Seed']) + ";" +
                           str(self.session.config['Project_B_Seed']) + ";" +
                           str(self.session.config['Project_C_Seed']) + ";" +
                           str(self.session.config['Project_D_Seed']) + ";" +
                           str(self.session.config['real_world_currency_per_point']) + ";" +
                           str(self.session.config['participation_fee']) + ";" +
                           str(Constants.num_rounds) + ";" +
                           str(Constants.players_per_group) + ";" +
                           2*"\n")

                # Schreibt Folgendes in die CSV-Datei (Inhalte getrennt durch Semikolons):
                # - "Runde"
                # - "seconds_since_start"
                # - "player_id"
                # - "action_type"
                # - "action_value"
                # - "player_money"
                # - "project"
                # - "player_project_contribution"
                # - "player_project_refund_bonus"
                # - "player_project_early_bird_bonus"
                # - "possible_payoff"
                # - "project_total"
                # - "project_percentage_founded"
                # - "project_backers"
                # - 2 * "\n" (zwei neue Absätze)
                # Hinweis: Siehe your_live_method() Methode in Group Klasse für weitere Erläuterungen
                file.write("round;seconds_since_start;player_id;action_type;action_value;player_money;project;player_project_contribution;player_project_refund_bonus;player_project_early_bird_bonus;possible_payoff;project_total;project_percentage_founded;project_backers" + "\n")


            # Erstellt eine CSV-Datei mit dem aktuellen Datum und Uhrzeit als Namen und öffnet die Datei zum Schreiben
            with open(self.session.vars['csv_file'] + ".csv", "w") as file:

                # Schreibt Folgendes in die CSV-Datei: NAMEN der Variablen in settings.py, die der Admin beim Erstellen der Sitzung festlegt + "num_rounds" + "players_per_group" (Inhalte getrennt durch Semikolons)
                file.write(
                    "All_Or_Nothing;Refund_Bonus;Early_Bird_Bonus;Enable_Backout;Backout_Fees;Show_Backers;Public_Goods;Min_Factor;Round_Duration;Bonus_Duration;Num_Projects;Endowment;Project_A_Goal;Project_B_Goal;Project_C_Goal;Project_D_Goal;Project_A_Seed;Project_B_Seed;Project_C_Seed;Project_D_Seed;real_world_currency_per_point;participation_fee;num_rounds;players_per_group" + "\n")

                # Schreibt Folgendes in die CSV-Datei: WERTE der Variablen in settings.py, die der Admin beim Erstellen der Sitzung festlegt + Anzahl der Runden + Anzahl der Spieler pro Gruppe + zwei neue Absätze (Inhalte getrennt durch Semikolons)
                # Hinweis: Für Erklärungen der Variablen siehe SESSION_CONFIGS in settings.py
                file.write(str(self.session.config['All_Or_Nothing']) + ";" +
                           str(self.session.config['Refund_Bonus']) + ";" +
                           str(self.session.config['Early_Bird_Bonus']) + ";" +
                           str(self.session.config['Enable_Backout']) + ";" +
                           str(self.session.config['Backout_Fees']) + ";" +
                           str(self.session.config['Show_Backers']) + ";" +
                           str(self.session.config['Public_Goods']) + ";" +
                           str(self.session.config['Min_Factor']) + ";" +
                           str(self.session.config['Round_Duration']) + ";" +
                           str(self.session.config['Bonus_Duration']) + ";" +
                           str(self.session.config['Num_Projects']) + ";" +
                           str(self.session.config['Endowment']) + ";" +
                           str(self.session.config['Project_A_Goal']) + ";" +
                           str(self.session.config['Project_B_Goal']) + ";" +
                           str(self.session.config['Project_C_Goal']) + ";" +
                           str(self.session.config['Project_D_Goal']) + ";" +
                           str(self.session.config['Project_A_Seed']) + ";" +
                           str(self.session.config['Project_B_Seed']) + ";" +
                           str(self.session.config['Project_C_Seed']) + ";" +
                           str(self.session.config['Project_D_Seed']) + ";" +
                           str(self.session.config['real_world_currency_per_point']) + ";" +
                           str(self.session.config['participation_fee']) + ";" +
                           str(Constants.num_rounds) + ";" +
                           str(Constants.players_per_group) + ";" +
                           2 * "\n")

                # Schreibt Folgendes in die CSV-Datei (Inhalte getrennt durch Semikolons):
                # - "round"
                # - "group_id"
                # - "player_id"
                # - "payoff"
                # - "a_payoff"
                # - "b_payoff"
                # - "c_payoff"
                # - "d_payoff"
                # - "a_refund"
                # - "b_refund"
                # - "c_refund"
                # - "d_refund"
                # - "a_refund_bonus"
                # - "b_refund_bonus"
                # - "c_refund_bonus"
                # - "d_refund_bonus"
                # - "a_early_bird"
                # - "b_early_bird"
                # - "c_early_bird"
                # - "d_early_bird"
                # - "a_possible_payoff"
                # - "b_possible_payoff"
                # - "c_possible_payoff"
                # - "d_possible_payoff"
                # - "money"
                # - "a_contribution"
                # - "b_contribution"
                # - "c_contribution"
                # - "d_contribution"
                # - "a_funded"
                # - "b_funded"
                # - "c_funded"
                # - "d_funded"
                # - "a_total"
                # - "b_total"
                # - "c_total"
                # - "d_total"
                # - "a_backers"
                # - "b_backers"
                # - "c_backers"
                # - "d_backers"
                # - 2 * "\n" (zwei neue Absätze)
                # Hinweis:
                file.write("round;group_id;player_id;payoff;a_payoff;b_payoff;c_payoff;d_payoff;a_refund;b_refund;c_refund;d_refund;a_refund_bonus;b_refund_bonus;c_refund_bonus;d_refund_bonus;a_early_bird;b_early_bird;c_early_bird;d_early_bird;a_possible_payoff;b_possible_payoff;c_possible_payoff;d_possible_payoff;money;a_contribution;b_contribution;c_contribution;d_contribution;a_funded;b_funded;c_funded;d_funded;a_total;b_total;c_total;d_total;a_backers;b_backers;c_backers;d_backers;" + "\n")

            # 6 verschiedene Präferenztypen als Listen
            # Präferenzen werden durch unterschiedliche Höhe der möglichen Auszahlungen ausgedrückt
            # type_y = [a_payoff, b_payoff, c_payoff, d_payoff] mit y ∈ [1, 2, 3, 4, 5, 6]
            type_1 = [200, 150, 100, 50]
            type_2 = [50, 200, 150, 100]
            type_3 = [100, 50, 200, 150]
            type_4 = [150, 100, 50, 200]
            type_5 = [200, 100, 150, 50]
            type_6 = [50, 150, 100, 200]

            # Liste, die alle Präferenztypen enthält
            # Hinweis: Jeder Eintrag in der Liste types ist selbst eine Liste
            types = [type_1, type_2, type_3, type_4, type_5, type_6]

            # Erstellt Variable index mit dem Wert: aktuelle Rudnennummer reduziert um 1 (da Rundennummern bei 1 beginnen, aber der Index einer Liste bei 0)
            # Wird genutzt, um den Spielern ihren Präferenztypen zuzuweisen
            index = self.round_number - 1

            # Verteilt die Präferenztypen auf die Spieler einer Gruppe
            # Jeder Typ kommt nur ein mal pro Gruppe vor
            # Für jeden Spieler der aktuellen Gruppe:
            for p in g.get_players():

                # Falls der Wert der Variable index größer ist als die Länge der Liste types reduziert um 1 (Index liegt außerhalb der Liste types):
                # Hinweis: Wert von index wird am Ende jedes Schleifendurchlaufs erhöht
                if index > len(types) - 1:

                    # Reduziert den Wert von index um die Länge der Liste types (Index liegt dadurch wieder innerhalb der Liste types)
                    index -= len(types)

                # Erstellt Liste type_y mit folgendem Wert: Präferenztyp, der sich in der Liste types an der Stelle mit dem Index index befindet
                type_y = types[index]

                # Die mögliche Auszahlung des Spielers für das Projekt A wird auf folgenden Wert gesetzt: Wert, der sich in der Liste type_y an der Stelle mit Index 0 befindet
                p.a_payoff = type_y[0]

                # Die mögliche Auszahlung des Spielers für das Projekt B wird auf folgenden Wert gesetzt: Wert, der sich in der Liste type_y an der Stelle mit Index 1 befindet
                p.b_payoff = type_y[1]

                # Die mögliche Auszahlung des Spielers für das Projekt C wird auf folgenden Wert gesetzt: Wert, der sich in der Liste type_y an der Stelle mit Index 2 befindet
                p.c_payoff = type_y[2]

                # Die mögliche Auszahlung des Spielers für das Projekt D wird auf folgenden Wert gesetzt: Wert, der sich in der Liste type_y an der Stelle mit Index 3 befindet
                p.d_payoff = type_y[3]

                index += 1

        # Für jeden Spieler:
        for p in self.get_players():

            # Setzt die Höhe des Startkapitals des Spielers auf den vom Admin gewählten Wert
            p.money = self.session.config['Endowment']




class Group(BaseGroup):

    # Hinweis: x ∈ {a, b, c, d}

    # x_total: Summe der Spenden aller Spieler für das Projekt X
    # Anfangswert: In settings.py gewählte Werte für das Startkapital (Zuweisung per creating_session() Methode in Subsession Klasse)
    a_total = models.IntegerField()
    b_total = models.IntegerField()
    c_total = models.IntegerField()
    d_total = models.IntegerField()

    # x_funded: Information, ob das Spendenziel von Projekt X erreicht ist (True oder False)
    # Anfangswert: False
    a_funded = models.BooleanField(initial=False)
    b_funded = models.BooleanField(initial=False)
    c_funded = models.BooleanField(initial=False)
    d_funded = models.BooleanField(initial=False)

    # x_backers: Anzahl der Spieler, die das Projekt X unterstützen
    # Anfangswert: 0
    a_backers = models.IntegerField(initial=0)
    b_backers = models.IntegerField(initial=0)
    c_backers = models.IntegerField(initial=0)
    d_backers = models.IntegerField(initial=0)

    # start_time: Zeitpunkt, an dem das Crowdfunding beginnt
    start_time = models.StringField()

    # group_id: ID der Gruppe (Wird benötigt, um für jede Gruppe eine eigene CSV-Datei zu erstellen)
    group_id = models.IntegerField()

    # Methode für Echtzeit-Interaktion (Werte werden live aktualisiert)
    # Empfängt die Daten des JavaScript Codes in Crowdfunding.html, die per liveSend() Methode gesendet werden
    # Definiert, wie sich Variablen der Klassen Group und Player ändern, wenn ein Donate/Backout Button ausgelöst wird
    # Schreibt Daten in die CSV-Dateien der einzelnen Gruppen
    # Sendet die aktualisierten Variablen zurück an das Crowdfunding Template (diese werden dort von der Methode liveRecv() empfangen)
    # Hinweis:  In der Klasse Crowdunding (in pages.py) muss live_method = 'live_method' gesetzt werden, um Echtzeitinteraktion zu ermöglichen
    # id_in_group: ID des Spielers, der einen Button ausgelöst hat, innerhalb seiner Gruppe
    # payload: Enthält Information, der Button ausgelöst wurde ("type") und falls es ein Donate Button war, der Betrag gespendet werden soll ("value")
    def live_method(self, id_in_group, payload):

        # Definiert, was passiert, wenn ein Spieler den Donate Button des Projektes A auslöst
        # Falls der Donate Button des Projektes A ausgelöst wurde:
        if payload["type"] == "donate_A":

            # Erstellt Variable time mit dem folgenden Wert: Datum und Uhrzeit, als der Button ausgelöst wurde
            time = datetime.now()

            # Wählt den Spieler, der den Button ausgelöst hat, anhand seiner ID in der Gruppe
            p = self.get_player_by_id(id_in_group)

            # Falls der Spieler ausreichend Kapital besitzt, um die Spende auszuführen und diese größer als 0 ist:
            if 0 < int(payload["value"]) <= p.money:

                # Verringert das Kapital des Spielers um den gespendeten Betrag
                p.money -= int(payload["value"])

                # Falls der Betrag, den der Spieler bisher an das Projekt A spendet, gleich 0 ist:
                if p.a_contribution == 0:

                    # Erhöht die Anzahl der Spieler, die das Projekt A unterstützen, um 1
                    self.a_backers += 1

                # Erhöht den Betrag, den der Spieler bisher an das Projekt A spendet, um den gewählten Wert
                p.a_contribution += int(payload["value"])

                # Falls die bisherige Rundendauer höchstens so groß ist, wie der Bonus-Zeitraum (d.h. der Bonus-Zeitraum ist noch gültig):
                if (time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds <= self.session.config['Bonus_Duration']:

                    # Falls der Faktor zur Berechnung der Early-Bird-Boni größer als 0 ist (d.h. Early-Bird-Boni sind aktiviert):
                    if self.session.config['Early_Bird_Bonus'] > 0:

                        # Setzt den Early-Bird-Bonus des Spielers für das Projekt A auf den Wert des Produktes aus dem entsprechenden Bonus-Faktor und den Gesamtspenden des Spielers an Projekt A
                        # Hinweis: Wird auf 2 Nachkommastellen gerundet
                        p.a_early_bird = round((self.session.config['Early_Bird_Bonus'] * p.a_contribution),2)

                    # Falls die "Alles oder nichts"-Regel aktiviert ist und der Faktor zur Berechnung der Rückzahlungs-Boni größer als 0 ist (d.h. Rückzahlungs-Boni sind aktiviert):
                    if self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0:

                        # Setzt den Rückzahlungs-Bonus des Spielers für das Projekt A auf den Wert des Produktes aus dem entsprechenden Bonus-Faktor und den Gesamtspenden des Spielers an Projekt A
                        # Hinweis: Wird auf 2 Nachkommastellen gerundet
                        p.a_refund_bonus = round((self.session.config['Refund_Bonus'] * p.a_contribution),2)

                # Erhöht die Summe der Spenden aller Spieler für das Projekt A um den gewählten Wert
                self.a_total += int(payload["value"])

                # Falls die Summe der Spenden aller Spieler für das Projekt A mindestens so groß ist, wie das zugehörige Spendenziel:
                if self.a_total >= self.session.config['Project_A_Goal']:

                    # Setzt den Wert von a_funded auf True (Speichert die Information, dass das Spendenziel von Projekt A erreicht ist)
                    self.a_funded = True

                # Andernfalls (Summe der Spenden aller Spieler für das Projekt A ist kleiner als das zugehörige Spendenziel):
                else:

                    # Setzt den Wert von a_funded auf False (Speichert die Information, dass das Spendenziel von Projekt A nicht erreicht ist)
                    self.a_funded = False

                # Öffnet die CSV-Datei, die zu der Gruppe gehört, in der sich der Spieler befindet
                # Hinweis: Die CSV-Datei wird im "Anhängen"-Modus geöffnet, wodurch der vorherige Inhalt nicht überschrieben wird
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:

                    # Falls die aktuelle Runde die erste Runde ist:
                    if self.round_number == 1:

                        # Erstellt Variable round_number mit dem Wert: "Übungsrunde"
                        round_number = "Übungsrunde"

                    # Andernfalls (Aktuelle Runde ist nicht die erste Runde):
                    else:

                        # Erstellt Variable round_number mit dem Wert: Aktuelle Rundennummer reduziert um 1
                        round_number = self.round_number - 1

                    # Schreibt Folgendes in die CSV-Datei (Inhalte werden durch Semikolons getrennt):
                    file.write(

                               # Wert der Variable round_number (Entweder "Übungsrunde" oder die tatsächliche Rundennummer reduziert um 1)
                               str(round_number) + ";" +

                               # Sekunden, die seit dem Start der aktuellen Crowdfunding Runde vergangen sind
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +

                               # ID des Spielers innerhalb seiner Gruppe
                               str(p.id_in_group) + ";" +

                               # Art der Aktion des Spielers. Hier: Spende an das Projekt A (donate_A)
                               str(payload["type"]) + ";" +

                               # Höhe der aktuellen Spende
                               str(payload["value"]) + ";" +

                               # Restliches Kapital des Spielers (nach der Aktion)
                               str(p.money) + ";" +

                               # Name des Projektes. Hier: "A"
                               str("A") + ";" +

                               # Der vom Spieler insgesamt gespendete Betrag an das Projekt A (nach der Aktion)
                               str(p.a_contribution) + ";" +

                               # Rückzahlungs-Bonus des Spielers für das Projekt A
                               str(p.a_refund_bonus) + ";" +

                               # Early-Bird-Bonus des Spielers für das Projekt A
                               str(p.a_early_bird) + ";" +

                               # Mögliche Auszahlung des Spielers durch das Projekt A
                               str(p.a_payoff) + ";" +

                               # Aktueller Spendenstand des Projektes A (nach der Aktion)
                               str(p.group.a_total) + ";" +

                               # Relativer Spendenstand des Projektes A (nach der Aktion)
                               # Beispiel: 0.3 bedeutet, dass 30% vom Spendenziel erreicht sind
                               str(p.group.a_total / self.session.config['Project_A_Goal']) + ";" +

                               # Anzahl der Unterstützer des Projektes A
                               str(p.group.a_backers) + ";" +

                               # Zeilenumbruch
                               "\n")

            # Legt fest, welche Variablen an die Crowdfunding.html Datei gesendet werden sollen
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}

        # Definiert, was passiert, wenn ein Spieler den Donate Button des Projektes B auslöst
        if payload["type"] == "donate_B":
            time = datetime.now()
            p = self.get_player_by_id(id_in_group)
            if 0 < int(payload["value"]) <= p.money:
                p.money -= int(payload["value"])
                if p.b_contribution == 0:
                    self.b_backers += 1
                p.b_contribution += int(payload["value"])
                if (time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds <= self.session.config['Bonus_Duration']:
                    if self.session.config['Early_Bird_Bonus'] > 0:
                        p.b_early_bird = round((self.session.config['Early_Bird_Bonus'] * p.b_contribution),2)
                    if self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0:
                        p.b_refund_bonus = round((self.session.config['Refund_Bonus'] * p.b_contribution),2)
                self.b_total += int(payload["value"])
                if self.b_total >= self.session.config['Project_B_Goal']:
                    self.b_funded = True
                else:
                    self.b_funded = False
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:
                    if self.round_number == 1:
                        round_number = "Übungsrunde"
                    else:
                        round_number = self.round_number - 1
                    file.write(str(round_number) + ";" +
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +
                               str(p.id_in_group) + ";" +
                               str(payload["type"]) + ";" +
                               str(payload["value"]) + ";" +
                               str(p.money) + ";" +
                               str("B") + ";" +
                               str(p.b_contribution) + ";" +
                               str(p.b_refund_bonus) + ";" +
                               str(p.b_early_bird) + ";" +
                               str(p.b_payoff) + ";" +
                               str(p.group.b_total) + ";" +
                               str(p.group.b_total / self.session.config['Project_B_Goal']) + ";" +
                               str(p.group.b_backers) + ";" +
                               "\n")
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}

        # Definiert, was passiert, wenn ein Spieler den Donate Button des Projektes C auslöst
        if payload["type"] == "donate_C":
            time = datetime.now()
            p = self.get_player_by_id(id_in_group)
            if 0 < int(payload["value"]) <= p.money:
                p.money -= int(payload["value"])
                if p.c_contribution == 0:
                    self.c_backers += 1
                p.c_contribution += int(payload["value"])
                if (time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds <= self.session.config['Bonus_Duration']:
                    if self.session.config['Early_Bird_Bonus'] > 0:
                        p.c_early_bird = round((self.session.config['Early_Bird_Bonus'] * p.c_contribution),2)
                    if self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0:
                        p.c_refund_bonus = round((self.session.config['Refund_Bonus'] * p.c_contribution),2)
                self.c_total += int(payload["value"])
                if self.c_total >= self.session.config['Project_C_Goal']:
                    self.c_funded = True
                else:
                    self.c_funded = False
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:
                    if self.round_number == 1:
                        round_number = "Übungsrunde"
                    else:
                        round_number = self.round_number - 1
                    file.write(str(round_number) + ";" +
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +
                               str(p.id_in_group) + ";" +
                               str(payload["type"]) + ";" +
                               str(payload["value"]) + ";" +
                               str(p.money) + ";" +
                               str("C") + ";" +
                               str(p.c_contribution) + ";" +
                               str(p.c_refund_bonus) + ";" +
                               str(p.c_early_bird) + ";" +
                               str(p.c_payoff) + ";" +
                               str(p.group.c_total) + ";" +
                               str(p.group.c_total / self.session.config['Project_C_Goal']) + ";" +
                               str(p.group.c_backers) + ";" +
                               "\n")
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}

        # Definiert, was passiert, wenn ein Spieler den Donate Button des Projektes D auslöst
        if payload["type"] == "donate_D":
            time = datetime.now()
            p = self.get_player_by_id(id_in_group)
            if 0 < int(payload["value"]) <= p.money:
                p.money -= int(payload["value"])
                if p.d_contribution == 0:
                    self.d_backers += 1
                p.d_contribution += int(payload["value"])
                if (time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds <= self.session.config['Bonus_Duration']:
                    if self.session.config['Early_Bird_Bonus'] > 0:
                        p.d_early_bird = round((self.session.config['Early_Bird_Bonus'] * p.d_contribution),2)
                    if self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0:
                        p.d_refund_bonus = round((self.session.config['Refund_Bonus'] * p.d_contribution),2)
                self.d_total += int(payload["value"])
                if self.d_total >= self.session.config['Project_D_Goal']:
                    self.d_funded = True
                else:
                    self.d_funded = False
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:
                    if self.round_number == 1:
                        round_number = "Übungsrunde"
                    else:
                        round_number = self.round_number - 1
                    file.write(str(round_number) + ";" +
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +
                               str(p.id_in_group) + ";" +
                               str(payload["type"]) + ";" +
                               str(payload["value"]) + ";" +
                               str(p.money) + ";" +
                               str("D") + ";" +
                               str(p.d_contribution) + ";" +
                               str(p.d_refund_bonus) + ";" +
                               str(p.d_early_bird) + ";" +
                               str(p.d_payoff) + ";" +
                               str(p.group.d_total) + ";" +
                               str(p.group.d_total / self.session.config['Project_D_Goal']) + ";" +
                               str(p.group.d_backers) + ";" +
                               "\n")
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}


        # Definiert, was passiert, wenn ein Spieler den Backout Button des Projektes A auslöst
        # Falls der Backout Button des Projektes A ausgelöst wurde:
        if payload["type"] == "backout_A":

            # Erstellt Variable time mit folgendem Wert: Datum und Uhrzeit, als der Button ausgelöst wurde
            time = datetime.now()

            # Wählt den Spieler, der den Button ausgelöst hat, anhand seiner ID in der Gruppe
            p = self.get_player_by_id(id_in_group)

            # Falls der Betrag, den der Spieler bisher an das Projekt A spendet, größer als 0 ist:
            if p.a_contribution > 0 and p.money + p.a_contribution > self.session.config['Backout_Fees']:

                # Erhöht das Kapital des Spielers um den Betrag, den er aktuell an das Projekt A spendet
                p.money += p.a_contribution

                # Verringert das Kapital des Spielers um die Kosten eines Backouts:
                p.money -= self.session.config['Backout_Fees']

                # Verringert die Summe der Spenden aller Spieler für das Projekt A um den Betrag, den der Spieler aktuell an das Projekt A spendet
                self.a_total -= p.a_contribution

                # Verringert die Anzahl der Spieler, die das Projekt A unterstützen, um 1
                self.a_backers -= 1

                # Variable a_contribution_csv wird erstellt und bekommt folgenden Wert zugewiesen: Betrag, den der Spieler aktuell an das Projekt A spendet
                # Hinweis: Dient zum Erstellen der CSV-Dateien der einzelnen Gruppen. Dokumentiert, die Beträge von Spielern zurückgezogen werden
                a_contribution_csv = p.a_contribution

                # Setzt den Betrag, den der Spieler aktuell an das Projekt A spendet, auf 0
                p.a_contribution = 0

                # Setzt den Rückzahlungs-Bonus des Spielers für das Projekt A auf 0
                p.a_refund_bonus = 0

                # Setzt den Early-Bird-Bonus des Spielers für das Projekt A auf 0
                p.a_early_bird = 0

                # Falls die Summe der Spenden aller Spieler für das Projekt A mindestens so groß ist, wie das zugehörige Spendenziel:
                if self.a_total >= self.session.config['Project_A_Goal']:

                    # Setzt den Wert von a_funded auf True (Speichert die Information, dass das Spendenziel von Projekt A erreicht ist)
                    self.a_funded = True

                # Andernfalls (Summe der Spenden aller Spieler für das Projekt A ist kleiner als das zugehörige Spendenziel):
                else:

                    # Setzt den Wert von a_funded auf False (Speichert die Information, dass das Spendenziel von Projekt A nicht erreicht ist)
                    self.a_funded = False

                # Öffnet die CSV-Datei, die zu der Gruppe gehört, in der sich der Spieler befindet
                # Hinweis: Die CSV-Datei wird im "Anhängen"-Modus geöffnet, wodurch der vorherige Inhalt nicht überschrieben wird
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:

                    # Falls die aktuelle Runde die erste Runde ist:
                    if self.round_number == 1:

                        # Erstellt Variable round_number mit dem Wert: "Übungsrunde"
                        round_number = "Übungsrunde"

                    # Andernfalls (Aktuelle Runde ist nicht die erste Runde):
                    else:

                        # Erstellt Variable round_number mit dem Wert: Aktuelle Rundennummer reduziert um 1
                        round_number = self.round_number - 1

                    # Schreibt Folgendes in die CSV-Datei (Inhalte werden durch Semikolons getrennt):
                    file.write(

                        # Wert der Variable round_number (Entweder "Übungsrunde" oder die tatsächliche Rundennummer reduziert um 1)
                        str(round_number) + ";" +

                        # Sekunden, die seit dem Start der aktuellen Crowdfunding Runde vergangen sind
                        str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +

                        # ID des Spielers innerhalb seiner Gruppe
                        str(p.id_in_group) + ";" +

                        # Art der Aktion des Spielers. Hier: Aus dem Projekt A aussteigen (backout_A)
                        str(payload["type"]) + ";" +

                        # Betrag, der zurückgezogen wird (VOR Abzug eventueller Kosten für das Aussteigen)
                        str(-a_contribution_csv) + ";" +

                        # Restliches Kapital des Spielers (nach der Aktion)
                        str(p.money) + ";" +

                        # Name des Projektes. Hier: "A"
                        str("A") + ";" +

                        # Der vom Spieler insgesamt gespendete Betrag an das Projekt A (nach der Aktion => muss nach einem Ausstieg dementsprechend immer 0 sein)
                        str(p.a_contribution) + ";" +

                        # Rückzahlungs-Bonus des Spielers für das Projekt A (nach der Aktion => muss nach einem Ausstieg dementsprechend immer 0 sein)
                        str(p.a_refund_bonus) + ";" +

                        # Early-Bird-Bonus des Spielers für das Projekt A (nach der Aktion => muss nach einem Ausstieg dementsprechend immer 0 sein)
                        str(p.a_early_bird) + ";" +

                        # Mögliche Auszahlung des Spielers durch das Projekt A
                        str(p.a_payoff) + ";" +

                        # Aktueller Spendenstand des Projektes A (nach der Aktion)
                        str(p.group.a_total) + ";" +

                        # Relativer Spendenstand des Projektes A (nach der Aktion)
                        # Beispiel: 0.3 bedeutet, dass 30% vom Spendenziel erreicht sind
                        str(p.group.a_total / self.session.config['Project_A_Goal']) + ";" +

                        # Anzahl der Unterstützer des Projektes A
                        str(p.group.a_backers) + ";" +

                        # Zeilenumbruch
                        "\n")

            # Legt fest, welche Variablen an die Crowdfunding.html Datei gesendet werden sollen
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}

        # Definiert, was passiert, wenn ein Spieler den Backout Button des Projektes B auslöst
        if payload["type"] == "backout_B":
            time = datetime.now()
            p = self.get_player_by_id(id_in_group)
            if p.b_contribution > 0 and p.money + p.b_contribution > self.session.config['Backout_Fees']:
                p.money += p.b_contribution
                p.money -= self.session.config['Backout_Fees']
                self.b_total -= p.b_contribution
                self.b_backers -= 1
                b_contribution_csv = p.b_contribution
                p.b_contribution = 0
                p.b_refund_bonus = 0
                p.b_early_bird = 0
                if self.b_total >= self.session.config['Project_B_Goal']:
                    self.b_funded = True
                else:
                    self.b_funded = False
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:
                    if self.round_number == 1:
                        round_number = "Übungsrunde"
                    else:
                        round_number = self.round_number - 1
                    file.write(str(round_number) + ";" +
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +
                               str(p.id_in_group) + ";" +
                               str(payload["type"]) + ";" +
                               str(-b_contribution_csv) + ";" +
                               str(p.money) + ";" +
                               str("B") + ";" +
                               str(p.b_contribution) + ";" +
                               str(p.b_refund_bonus) + ";" +
                               str(p.b_early_bird) + ";" +
                               str(p.b_payoff) + ";" +
                               str(p.group.b_total) + ";" +
                               str(p.group.b_total / self.session.config['Project_B_Goal']) + ";" +
                               str(p.group.b_backers) + ";" +
                               "\n")
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}

        # Definiert, was passiert, wenn ein Spieler den Backout Button des Projektes C auslöst
        if payload["type"] == "backout_C":
            time = datetime.now()
            p = self.get_player_by_id(id_in_group)
            if p.c_contribution > 0 and p.money + p.c_contribution > self.session.config['Backout_Fees']:
                p.money += p.c_contribution
                p.money -= self.session.config['Backout_Fees']
                self.c_total -= p.c_contribution
                self.c_backers -= 1
                c_contribution_csv = p.c_contribution
                p.c_contribution = 0
                p.c_refund_bonus = 0
                p.c_early_bird = 0
                if self.c_total >= self.session.config['Project_C_Goal']:
                    self.c_funded = True
                else:
                    self.c_funded = False
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:
                    if self.round_number == 1:
                        round_number = "Übungsrunde"
                    else:
                        round_number = self.round_number - 1
                    file.write(str(round_number) + ";" +
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +
                               str(p.id_in_group) + ";" +
                               str(payload["type"]) + ";" +
                               str(-c_contribution_csv) + ";" +
                               str(p.money) + ";" +
                               str("C") + ";" +
                               str(p.c_contribution) + ";" +
                               str(p.c_refund_bonus) + ";" +
                               str(p.c_early_bird) + ";" +
                               str(p.c_payoff) + ";" +
                               str(p.group.c_total) + ";" +
                               str(p.group.c_total / self.session.config['Project_C_Goal']) + ";" +
                               str(p.group.c_backers) + ";" +
                               "\n")
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}

        # Definiert, was passiert, wenn ein Spieler den Backout Button des Projektes D auslöst
        if payload["type"] == "backout_D":
            time = datetime.now()
            p = self.get_player_by_id(id_in_group)
            if p.d_contribution > 0 and p.money + p.d_contribution > self.session.config['Backout_Fees']:
                p.money += p.d_contribution
                p.money -= self.session.config['Backout_Fees']
                self.d_total -= p.d_contribution
                self.d_backers -= 1
                d_contribution_csv = p.d_contribution
                p.d_contribution = 0
                p.d_refund_bonus = 0
                p.d_early_bird = 0
                if self.d_total >= self.session.config['Project_D_Goal']:
                    self.d_funded = True
                else:
                    self.d_funded = False
                with open(self.session.vars['csv_file'] + "_Group" + str(p.group.group_id) + ".csv", "a") as file:
                    if self.round_number == 1:
                        round_number = "Übungsrunde"
                    else:
                        round_number = self.round_number - 1
                    file.write(str(round_number) + ";" +
                               str((time - datetime.strptime(p.group.start_time, '%Y-%m-%d %H:%M:%S.%f')).seconds) + ";" +
                               str(p.id_in_group) + ";" +
                               str(payload["type"]) + ";" +
                               str(-d_contribution_csv) + ";" +
                               str(p.money) + ";" +
                               str("D") + ";" +
                               str(p.d_contribution) + ";" +
                               str(p.d_refund_bonus) + ";" +
                               str(p.d_early_bird) + ";" +
                               str(p.d_payoff) + ";" +
                               str(p.group.d_total) + ";" +
                               str(p.group.d_total / self.session.config['Project_D_Goal']) + ";" +
                               str(p.group.d_backers) + ";" +
                               "\n")
            return {0: [self.a_total, self.b_total, self.c_total, self.d_total, self.a_backers, self.b_backers, self.c_backers, self.d_backers]}


class Player(BasePlayer):

    # Hinweis: x ∈ {a, b, c, d}

    # money: Startkapital des Spielers
    # Anfangswert: Wert, der beim Erstellen der Sitzung vom Admin gewählt wird (Zuweisung durch creating_session() Methode in Subsession Klasse)
    money = models.IntegerField()

    # x_contribution: Gibt an, wie viel der Spieler momentan insgesamt an Projekt X spendet
    # Anfangswert: 0
    a_contribution = models.IntegerField(initial=0)
    b_contribution = models.IntegerField(initial=0)
    c_contribution = models.IntegerField(initial=0)
    d_contribution = models.IntegerField(initial=0)

    # x_payoff: Mögliche Auszahlung des Spielers für das Projekt X
    # Anfangswert: Zuweisung durch creating_session() Methode in Subsession Klasse
    a_payoff = models.IntegerField()
    b_payoff = models.IntegerField()
    c_payoff = models.IntegerField()
    d_payoff = models.IntegerField()

    # x_early_bird: Early Bird Bonus, den der Spieler für das Projekt x erhält
    # Anfangswert: 0,0
    a_early_bird = models.FloatField(initial=0.0)
    b_early_bird = models.FloatField(initial=0.0)
    c_early_bird = models.FloatField(initial=0.0)
    d_early_bird = models.FloatField(initial=0.0)

    # x_refund_bonus: Refund Bonus, den der Spieler erhält, wenn das Projekt x das Spendenziel nicht erreicht
    # Anfangswert: 0,0
    a_refund_bonus = models.FloatField(initial=0.0)
    b_refund_bonus = models.FloatField(initial=0.0)
    c_refund_bonus = models.FloatField(initial=0.0)
    d_refund_bonus = models.FloatField(initial=0.0)

    # total_payoff: Gibt die Auszahlung an, die der Spieler am Ende des Experimentes insgesamt erreicht hat (Übungsrunde fließt nicht mit ein)
    # Anfangswert: c(0) (O Punkte)
    total_payoff = models.CurrencyField(initial=c(0))

    # Berechnet die Auszahlung des Spielers am Ende einer Runde
    # Wird von der after_all_players_arrive() Methode der ResultsWaitPage Klasse in pages.py aufgerufen
    def set_payoff(self):
        
        # Setzt die Auszahlung des Spielers auf den Betrag seines Kapitals zum Ende der Runde
        self.payoff = self.money

        # Falls bei Projekerfolgen öffentliche Güter entstehen sollen:
        if self.session.config['Public_Goods']:

            # Falls die "Alles oder Nichts"-Regel aktiviert ist:
            if self.session.config['All_Or_Nothing']:

                # Falls das Spendenziel von Projekt A (am Ende der Runde) erreicht ist:
                if self.group.a_funded:

                    # Erhöht die Auszahlung des Spielers um dessen mögliche Auszahlung, sowie den Early-Bird-Bonus, für das Projekt A
                    self.payoff += self.a_payoff + self.a_early_bird

                # Andernfalls (Spendenziel von Projekt A ist nicht erreicht):
                else:

                    # Erhöht die Auszahlung des Spielers um den Betrag, den er an Projekt A gespendet hat, sowie um den zugehörigen Zürückzahlungs-Bonus (Spieler erhält den gespendeten Betrag, aufgrund der "Alles oder Nichts"-Regel zurück)
                    self.payoff += self.a_contribution + self.a_refund_bonus

                if self.group.b_funded:
                    self.payoff += self.b_payoff + self.b_early_bird
                else:
                    self.payoff += self.b_contribution + self.b_refund_bonus
                if self.group.c_funded:
                    self.payoff += self.c_payoff + self.c_early_bird
                else:
                    self.payoff += self.c_contribution + self.c_refund_bonus
                if self.group.d_funded:
                    self.payoff += self.d_payoff + self.d_early_bird
                else:
                    self.payoff += self.d_contribution + self.d_refund_bonus

            # Andernfalls ("Alles oder Nichts"-Regel ist nicht aktiviert)
            else:

                # Falls das Spendenziel von Projekt A (am Ende der Runde) erreicht ist:
                if self.group.a_funded:

                    # Erhöht die Auszahlung des Spielers um dessen mögliche Auszahlung für das Projekt A
                    self.payoff += self.a_payoff + self.a_early_bird

                if self.group.b_funded:
                    self.payoff += self.b_payoff + self.b_early_bird
                if self.group.c_funded:
                    self.payoff += self.c_payoff + self.c_early_bird
                if self.group.d_funded:
                    self.payoff += self.d_payoff + self.d_early_bird

        # Andernfalls (Bei Projekerfolgen entstehen private Güter)
        else:

            # Erstellt Variable factor mit dem Wert von "Min_Factor" (Beim Erstellen der Sitzung vom Admin gewählt)
            factor = self.session.config['Min_Factor']

            # Falls die "Alles oder Nichts"-Regel aktiviert ist:
            if self.session.config['All_Or_Nothing']:

                # Falls das Spendenziel von Projekt A (am Ende der Runde) erreicht ist...
                # ...und der Betrag, den der Spieler an Projekt A gespendet hat, mindestens so groß ist wie das Produkt aus dem Wert der Variable factor und dem Spendenziel von Projekt A:
                if self.group.a_funded and self.a_contribution >= (factor*self.session.config['Project_A_Goal']):

                    # Erhöht die Auszahlung des Spielers um dessen mögliche Auszahlung für das Projekt A
                    self.payoff += self.a_payoff + self.a_early_bird

                # Falls stattdessen das Spendenziel von Projekt A nicht erreicht ist:
                elif self.group.a_funded == False:

                    # Erhöht die Auszahlung des Spielers um den Betrag, den er an Projekt A gespendet hat, sowie um den zugehörigen Zürückzahlungs-Bonus (Spieler erhält den gespendeten Betrag, aufgrund der "Alles oder Nichts"-Regel zurück)
                    self.payoff += self.a_contribution + self.a_refund_bonus

                if self.group.b_funded and self.b_contribution >= (factor*self.session.config['Project_B_Goal']):
                    self.payoff += self.b_payoff + self.b_early_bird
                elif self.group.b_funded == False:
                    self.payoff += self.b_contribution + self.b_refund_bonus
                if self.group.c_funded and self.c_contribution >= (factor*self.session.config['Project_C_Goal']):
                    self.payoff += self.c_payoff + self.c_early_bird
                elif self.group.c_funded == False:
                    self.payoff += self.c_contribution + self.c_refund_bonus
                if self.group.d_funded and self.d_contribution >= (factor*self.session.config['Project_D_Goal']):
                    self.payoff += self.d_payoff + self.d_early_bird
                elif self.group.d_funded == False:
                    self.payoff += self.d_contribution + self.d_refund_bonus

            # Andernfalls ("Alles oder Nichts"-Regel ist nicht aktiviert):
            else:

                # Falls das Spendenziel von Projekt A (am Ende der Runde) erreicht ist...
                # ...und der Betrag, den der Spieler an Projekt A gespendet hat, mindestens so groß ist wie das Produkt aus dem Wert der Variable factor und dem Spendenziel von Projekt A:
                if self.group.a_funded and self.a_contribution >= (factor*self.session.config['Project_A_Goal']):

                    # Erhöht die Auszahlung des Spielers um dessen mögliche Auszahlung, sowie den Early-Bird-Bonus, für das Projekt A
                    self.payoff += self.a_payoff + self.a_early_bird

                if self.group.b_funded and self.b_contribution >= (factor*self.session.config['Project_B_Goal']):
                    self.payoff += self.b_payoff + self.b_early_bird
                if self.group.c_funded and self.c_contribution >= (factor*self.session.config['Project_C_Goal']):
                    self.payoff += self.c_payoff + self.c_early_bird
                if self.group.d_funded and self.d_contribution >= (factor*self.session.config['Project_D_Goal']):
                    self.payoff += self.d_payoff + self.d_early_bird





