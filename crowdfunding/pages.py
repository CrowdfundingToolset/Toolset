# Von oTree automatisch erstellte Importe
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# Import, um Datum und Zeit zu erhalten
from datetime import datetime


# Instruktionsseite mit Erklärung des Spielablaufes
class Instructions(Page):

    # Definiert, wann die Seite aufgerufen werden soll (Hier: nur in Runde 1)
    def is_displayed(self):

        # Legt fest, dass die Seite nur in Runde 1 aufgerufen werden soll
        return self.round_number == 1

    # Übergibt bestimmte Variablen an die Seite, da von dort aus nicht direkt auf diese zugegriffen werden kann
    def vars_for_template(self):

        # Legt fest, welche Variablen übergeben werden sollen
        return{

            # Gibt an, ob es möglich sein soll, aus Projekten auszusteigen (True oder False)
            "Enable_Backout": self.session.config['Enable_Backout'],

            # Kosten für den Ausstieg aus einem Projekt
            "Backout_Fees": self.session.config['Backout_Fees'],

            # Gibt an, ob die Anzahl der Spieler, welche ein Projekt unterstützen, angezeigt werden soll (True oder False)
            "Show_Backers": self.session.config['Show_Backers'],

            # Gibt an, ob die "Alles oder Nichts"-Regel aktiviert ist (True oder False)
            "All_Or_Nothing": self.session.config['All_Or_Nothing'],

            # Gibt an, ob die Projekte öffentliche Güter sein sollen (True oder False)
            "Public_Goods": self.session.config['Public_Goods'],

            # Dauer einer Crowdfunding Runde in Sekunden
            "Round_Duration": self.session.config['Round_Duration'],

            # Gibt an, ob Rückzahlungs-Boni aktiviert sind (True oder False)
            "Refund_Bonus_Boolean": self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0,

            # Faktor für den Rückzahlungs-Bonus multipliziert mit 100 => Rückzahlungs-Bonus in Prozent
            "Refund_Bonus_Percentage": self.session.config['Refund_Bonus'] * 100,

            # Gibt an, ob Early-Bird-Boni aktiviert sind (True oder False)
            "Early_Bird_Bonus_Boolean": self.session.config['Early_Bird_Bonus'] > 0,

            # Faktor für den Early-Bird-Bonus multipliziert mit 100 => Early-Bird-Bonus in Prozent
            "Early_Bird_Bonus_Percentage": self.session.config['Early_Bird_Bonus'] * 100,

            # Zeitraum, in welchem Boni gewährt werden, in Sekunden
            "Bonus_Duration": self.session.config['Bonus_Duration'],

            # Gibt die Anzahl an Projekten an
            "Num_Projects": self.session.config['Num_Projects'],

            # Gibt an, wie viel Eurocent die Spieler pro Punkt erhalten
            "Cent_Per_Point": self.session.config['real_world_currency_per_point'] * 100,

            # Teilnahmevergütung in Euro
            "Participation_Fee": self.session.config['participation_fee'],

            # Anzahl der Mitspieler eines Spielers (in der Gruppe)
            "Players": Constants.players_per_group - 1,
        }


# Warteseite vor der Crowdfunding Seite
# Hinsweis: Dient vor Allem dazu, dass alle Spieler der Gruppe gleichzeitig mit dem Crowdfunding beginnen
class CrowdfundingWaitPage(WaitPage):

    # Wird aufgerufen, wenn alle Spieler der Gruppe auf der Seite angekommen sind
    # Speichert für die Gruppe den Zeitpunkt, an dem das Crowdfunding beginnt
    def after_all_players_arrive(self):

        # Der Variable start_time (in Group Klasse in models.py) wird folgender Wert zugewiesen: Aktuelles Datum und Uhrzeit als String
        self.group.start_time = str(datetime.now())


# Seite, auf der das Crowdfunding stattfindet
class Crowdfunding(Page):

    # Dient der Echtzeit-Interaktion
    # Stellt Verbindung zwischen den Methoden live_method() (in Group Klasse in models.py) und liveSend(), sowie liveRecv() (in Crowdfunding.html) her
    live_method = 'live_method'

    # Definiert die Dauer des Crowdfundings
    def get_timeout_seconds(self):

        # Legt fest, dass die Zeitdauer dem Wert von "Round_Duration" (in settings.py) entsprechen soll
        return self.session.config['Round_Duration']

    # Übergibt bestimmte Variablen an die Seite, da von dort aus nicht direkt auf diese zugegriffen werden kann
    def vars_for_template(self):

        # Legt fest, welche Variablen übergeben werden sollen
        return{

            # Hinweis: x ∈ {a, b, c, d}

            # Gibt an, ob es möglich sein soll, aus Projekten auszusteigen (True oder False)
            "Enable_Backout": self.session.config['Enable_Backout'],

            # Kosten für den Ausstieg aus einem Projekt
            "Backout_Fees": self.session.config['Backout_Fees'],

            # Gibt an, ob die Anzahl der Spieler, welche ein Projekt unterstützen, angezeigt werden soll (True oder False)
            "Show_Backers": self.session.config['Show_Backers'],

            # Gibt an, ob die Projekte öffentliche Güter sein sollen (True oder False)
            "Public_Goods": self.session.config['Public_Goods'],

            # Nur relevant, wenn die Projekte keine öffentlichen Güter sein sollen ("Public_Goods" in settings.py ist deaktiviert)
            # x_minimum: Minimaler Betrag, welchen ein Spieler an das Projekt X spenden muss, um seine zugehörige Auszahlung (im Falle des Projekterfolges) zu erhalten
            # x_minimum = Min_Factor multipliziert mit dem Spendenziel von Projekt X
            "a_minimum": self.session.config['Min_Factor'] * self.session.config['Project_A_Goal'],
            "b_minimum": self.session.config['Min_Factor'] * self.session.config['Project_B_Goal'],
            "c_minimum": self.session.config['Min_Factor'] * self.session.config['Project_C_Goal'],
            "d_minimum": self.session.config['Min_Factor'] * self.session.config['Project_D_Goal'],

            # project_x_goal: Spendenziel von Projekt X
            "Project_A_Goal": self.session.config['Project_A_Goal'],
            "Project_B_Goal": self.session.config['Project_B_Goal'],
            "Project_C_Goal": self.session.config['Project_C_Goal'],
            "Project_D_Goal": self.session.config['Project_D_Goal'],

            # Gibt an, ob Rückzahlungs-Boni aktiviert sind (True oder False)
            "Refund_Bonus_Boolean": self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0,

            # Gibt an, ob Early-Bird-Boni aktiviert sind (True oder False)
            "Early_Bird_Bonus_Boolean": self.session.config['Early_Bird_Bonus'] > 0,

            # Gibt die aktuelle Rundenzahl reduziert um 1 an (Es sollen nur die gewerteten Runden gezählt werden, nicht die Übungsrunde)
            "round_now": self.round_number - 1,

            # Gibt die maximale Rundenzahl reduziert um 1 an (Es sollen nur die gewerteten Runden gezählt werden, nicht die Übungsrunde)
            "round_max": Constants.num_rounds - 1,

            # Gibt die Anzahl an Projekten an
            "Num_Projects": self.session.config['Num_Projects'],
        }


# Warteseite vor der Results Seite
class ResultsWaitPage(WaitPage):

    # Wird aufgerufen, wenn alle Spieler der Gruppe auf der Seite angekommen sind
    # Ruft für jeden Spieler der Gruppe die set_payoff() Methode (in Player Klasse in models.py) auf
    def after_all_players_arrive(self):

        # Für jeden Spieler in der Gruppe:
        for p in self.group.get_players():

            # Ruft die set_payoff() Methode (in Player Klasse in models.py) für den aktuellen Spieler auf
            # Diese berechnet die in der aktuellen Runde erreichte Auszahlung des Spielers
            p.set_payoff()

            # Öffnet die CSV Datei, in welcher die Rundenergebnisse gespeichert werden
            # Hinweis: Die CSV Datei wird im "Anhängen"-Modus geöffnet, wodurch der vorherige Inhalt nicht überschrieben wird
            with open(self.session.vars['csv_file'] + ".csv", "a") as file:

                # Falls die aktuelle Runde die erste Runde ist:
                if p.round_number == 1:

                    # Erstellt Variable round_number mit dem Wert: "Übungsrunde"
                    round_number = "Übungsrunde"

                # Andernfalls (Aktuelle Runde ist nicht die erste Runde):
                else:

                    # Erstellt Variable round_number mit dem Wert: Aktuelle Rundennummer reduziert um 1
                    round_number = p.round_number - 1
                
                # Im Folgenden werden die tatsächlich erreichten Auszahlungen und Rückzahlungen des Spielers für die Projekte definiert
                # Falls Projekt A das Spendenziel erreicht hat:
                if p.group.a_funded:

                    # Falls die Projekte öffentliche Güter sind:
                    if self.session.config['Public_Goods']:

                        # Erstellt Variable a_payoff mit dem Wert: Mögliche Auszahlung des Spielers für Projekt A + Early-Bird-Bonus des Spielers für Projekt A
                        a_payoff = p.a_payoff + p.a_early_bird

                        # Erstellt Variable a_refund mit dem Wert: 0
                        a_refund = 0

                    # Andernfalls (Projekte sind keine öffentliche Güter)
                    else:

                        # Falls der Spieler mindestens den Betrag an das (erfolgreiche) Projekt A gespendet hat, welcher nötig ist, um die zugehörige Auszahlung zu erhalten:
                        if p.a_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_A_Goal']:

                            # Erstellt Variable a_payoff mit dem Wert: Mögliche Auszahlung des Spielers für Projekt A + Early-Bird-Bonus des Spielers für Projekt A
                            a_payoff = p.a_payoff + p.a_early_bird

                            # Erstellt Variable a_refund mit dem Wert: 0
                            a_refund = 0

                        # Andernfalls (Der Spieler hat den minimal benötigten Betrag nicht gespendet)
                        else:

                            # Erstellt Variable a_payoff mit dem Wert: 0
                            a_payoff = 0

                            # Erstellt Variable a_refund mit dem Wert: 0
                            a_refund = 0

                # Andernfalls (Projekt A hat das Spendenziel nicht erreicht)
                else:

                    # Falls die "Alles oder Nichts"-Regel aktiviert ist:
                    if self.session.config['All_Or_Nothing']:

                        # Erstellt Variable a_payoff mit dem Wert: 0
                        a_payoff = 0

                        # Erstellt Variable a_refund mit dem Wert: Betrag, welchen der Spieler an Projekt A gespendet hat + Rückzahlungs-Bonus des Spielers für Projekt A
                        a_refund = p.a_contribution + p.a_refund_bonus

                    # Andernfalls ("Alles oder Nichts"-Regel ist nicht aktiviert):
                    else:

                        # Erstellt Variable a_payoff mit dem Wert: 0
                        a_payoff = 0

                        # Erstellt Variable a_refund mit dem Wert: 0
                        a_refund = 0

                if p.group.b_funded:
                    if self.session.config['Public_Goods']:
                        b_payoff = p.b_payoff + p.b_early_bird
                        b_refund = 0
                    else:
                        if p.b_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_B_Goal']:
                            b_payoff = p.b_payoff + p.b_early_bird
                            b_refund = 0
                        else:
                            b_payoff = 0
                            b_refund = 0
                else:
                    if self.session.config['All_Or_Nothing']:
                        b_payoff = 0
                        b_refund = p.b_contribution + p.b_refund_bonus
                    else:
                        b_payoff = 0
                        b_refund = 0

                if p.group.c_funded:
                    if self.session.config['Public_Goods']:
                        c_payoff = p.c_payoff + p.c_early_bird
                        c_refund = 0
                    else:
                        if p.c_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_C_Goal']:
                            c_payoff = p.c_payoff + p.c_early_bird
                            c_refund = 0
                        else:
                            c_payoff = 0
                            c_refund = 0
                else:
                    if self.session.config['All_Or_Nothing']:
                        c_payoff = 0
                        c_refund = p.b_contribution + p.c_refund_bonus
                    else:
                        c_payoff = 0
                        c_refund = 0

                if p.group.d_funded:
                    if self.session.config['Public_Goods']:
                        d_payoff = p.d_payoff + p.d_early_bird
                        d_refund = 0
                    else:
                        if p.d_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_D_Goal']:
                            d_payoff = p.d_payoff + p.d_early_bird
                            d_refund = 0
                        else:
                            d_payoff = 0
                            d_refund = 0
                else:
                    if self.session.config['All_Or_Nothing']:
                        d_payoff = 0
                        d_refund = p.d_contribution + p.d_refund_bonus
                    else:
                        d_payoff = 0
                        d_refund = 0

                # Schreibt Folgendes in die CSV Datei (Inhalte werden durch ein Semikolon getrennt):
                file.write(

                    # Wert der Variable round_number (Entweder "Übungsrunde" oder die tatsächliche Rundennummer reduziert um 1)
                    str(round_number) + ";" +

                    # ID der Gruppe, in welcher sich der Spieler befindet
                    str(p.group.group_id) + ";" +

                    # ID des Spielers innerhalb seiner Gruppe
                    str(p.id_in_group) + ";" +

                    # Höhe der Auszahlung des Spielers in der aktuellen Runde
                    str(p.payoff) + ";" +

                    # Höhe der TATSÄCHLICHEN Auszahlung, welche der Spieler für Projekt A erhält
                    str(a_payoff) + ";" +

                    # Höhe der TATSÄCHLICHEN Auszahlung, welche der Spieler für Projekt B erhält
                    str(b_payoff) + ";" +

                    # Höhe der TATSÄCHLICHEN Auszahlung, welche der Spieler für Projekt C erhält
                    str(c_payoff) + ";" +

                    # Höhe der TATSÄCHLICHEN Auszahlung, welche der Spieler für Projekt D erhält
                    str(d_payoff) + ";" +

                    # Höhe der Rückzahlung, welche der Spieler für Projekt A erhält
                    str(a_refund) + ";" +

                    # Höhe der Rückzahlung, welche der Spieler für Projekt B erhält
                    str(b_refund) + ";" +

                    # Höhe der Rückzahlung, welche der Spieler für Projekt C erhält
                    str(c_refund) + ";" +

                    # Höhe der Rückzahlung, welche der Spieler für Projekt D erhält
                    str(d_refund) + ";" +

                    # Höhe des Rückzahlungs-Bonus, welchen der Spieler für Projekt A erhält
                    str(p.a_refund_bonus) + ";" +

                    # Höhe des Rückzahlungs-Bonus, welchen der Spieler für Projekt B erhält
                    str(p.b_refund_bonus) + ";" +

                    # Höhe des Rückzahlungs-Bonus, welchen der Spieler für Projekt C erhält
                    str(p.c_refund_bonus) + ";" +

                    # Höhe des Rückzahlungs-Bonus, welchen der Spieler für Projekt D erhält
                    str(p.d_refund_bonus) + ";" +

                    # Höhe des Early-Bird-Bonus, welchen der Spieler für Projekt A erhält
                    str(p.a_early_bird) + ";" +

                    # Höhe des Early-Bird-Bonus, welchen der Spieler für Projekt B erhält
                    str(p.b_early_bird) + ";" +

                    # Höhe des Early-Bird-Bonus, welchen der Spieler für Projekt C erhält
                    str(p.c_early_bird) + ";" +

                    # Höhe des Early-Bird-Bonus, welchen der Spieler für Projekt D erhält
                    str(p.d_early_bird) + ";" +

                    # Höhe der MÖGLICHEN Auszahlung, welche der Spieler für Projekt A hätte erhalten können
                    str(p.a_payoff) + ";" +

                    # Höhe der MÖGLICHEN Auszahlung, welche der Spieler für Projekt B hätte erhalten können
                    str(p.b_payoff) + ";" +

                    # Höhe der MÖGLICHEN Auszahlung, welche der Spieler für Projekt C hätte erhalten können
                    str(p.c_payoff) + ";" +

                    # Höhe der MÖGLICHEN Auszahlung, welche der Spieler für Projekt D hätte erhalten können
                    str(p.d_payoff) + ";" +

                    # Restliches Kapital des Spielers
                    str(p.money) + ";" +

                    # Betrag, welchen der Spieler an Projekt A gespendet hat
                    str(p.a_contribution) + ";" +

                    # Betrag, welchen der Spieler an Projekt B gespendet hat
                    str(p.b_contribution) + ";" +

                    # Betrag, welchen der Spieler an Projekt C gespendet hat
                    str(p.c_contribution) + ";" +

                    # Betrag, welchen der Spieler an Projekt D gespendet hat
                    str(p.d_contribution) + ";" +

                    # Information, ob Projekt A das Spendenziel erreicht hat (True oder False)
                    str(p.group.a_funded) + ";" +

                    # Information, ob Projekt B das Spendenziel erreicht hat (True oder False)
                    str(p.group.b_funded) + ";" +

                    # Information, ob Projekt C das Spendenziel erreicht hat (True oder False)
                    str(p.group.c_funded) + ";" +

                    # Information, ob Projekt D das Spendenziel erreicht hat (True oder False)
                    str(p.group.d_funded) + ";" +

                    # Summe der Spenden aller Spieler an Projekt A
                    str(p.group.a_total) + ";" +

                    # Summe der Spenden aller Spieler an Projekt B
                    str(p.group.b_total) + ";" +

                    # Summe der Spenden aller Spieler an Projekt C
                    str(p.group.c_total) + ";" +

                    # Summe der Spenden aller Spieler an Projekt D
                    str(p.group.d_total) + ";" +

                    # Anzahl der Spieler, welche das Projekt A unterstützen
                    str(p.group.a_backers) + ";" +

                    # Anzahl der Spieler, welche das Projekt B unterstützen
                    str(p.group.b_backers) + ";" +

                    # Anzahl der Spieler, welche das Projekt C unterstützen
                    str(p.group.c_backers) + ";" +

                    # Anzahl der Spieler, welche das Projekt D unterstützen
                    str(p.group.d_backers) + ";" +

                    # Zeilenumbruch
                    "\n")


# Seite, welche dem Spieler die Ergebnisse der aktuellen Runde anzeigt
class Results(Page):

    # Übergibt bestimmte Variablen an die Seite, da von dort aus nicht direkt auf diese zugegriffen werden kann
    def vars_for_template(self):

        # Im Folgenden werden die tatsächlich erreichten Auszahlungen bzw. Rückzahlungen des Spielers für die Projekte definiert
        # Falls Projekt A das Spendenziel erreicht hat:
        if self.group.a_funded:

            # Falls die Projekte öffentliche Güter sind:
            if self.session.config['Public_Goods']:

                # Erstellt Variable a_payoff mit dem Wert: Auszahlung + Early-Bird-Bonus des Spielers für Projekt A
                a_payoff = self.player.a_payoff + self.player.a_early_bird

            # Andernfalls (Projekte sind keine öffentliche Güter)
            else:

                # Falls der Spieler mindestens den Betrag an das (erfolgreiche) Projekt A gespendet hat, welcher nötig ist, um die zugehörige Auszahlung zu erhalten:
                if self.player.a_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_A_Goal']:

                    # Erstellt Variable a_payoff mit dem Wert: Auszahlung + Early-Bird-Bonus des Spielers für Projekt A
                    a_payoff = self.player.a_payoff + self.player.a_early_bird

                # Andernfalls (Der Spieler hat den minimal benötigten Betrag nicht gespendet)
                else:

                    # Erstellt Variable a_payoff mit dem Wert: 0
                    a_payoff = 0

        # Andernfalls (Projekt A hat das Spendenziel nicht erreicht)
        else:

            # Falls die "Alles oder Nichts"-Regel aktiviert ist:
            if self.session.config['All_Or_Nothing']:

                # Erstellt Variable a_payoff mit dem Wert: Betrag, welchen der Spieler an Projekt A gespendet hat + Rückzahlungs-Bonus für Projekt A
                a_payoff = self.player.a_contribution + self.player.a_refund_bonus

            # Andernfalls ("Alles oder Nichts"-Regel ist nicht aktiviert):
            else:

                # Erstellt Variable a_payoff mit dem Wert: 0
                a_payoff = 0

        if self.group.b_funded:
            if self.session.config['Public_Goods']:
                b_payoff = self.player.b_payoff + self.player.b_early_bird
            else:
                if self.player.b_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_B_Goal']:
                    b_payoff = self.player.b_payoff + self.player.b_early_bird
                else:
                    b_payoff = 0
        else:
            if self.session.config['All_Or_Nothing']:
                b_payoff = self.player.b_contribution + self.player.b_refund_bonus
            else:
                b_payoff = 0

        if self.group.c_funded:
            if self.session.config['Public_Goods']:
                c_payoff = self.player.c_payoff + self.player.c_early_bird
            else:
                if self.player.c_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_C_Goal']:
                    c_payoff = self.player.c_payoff + self.player.c_early_bird
                else:
                    c_payoff = 0
        else:
            if self.session.config['All_Or_Nothing']:
                c_payoff = self.player.c_contribution + self.player.c_refund_bonus
            else:
                c_payoff = 0

        if self.group.d_funded:
            if self.session.config['Public_Goods']:
                d_payoff = self.player.d_payoff + self.player.d_early_bird
            else:
                if self.player.d_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_D_Goal']:
                    d_payoff = self.player.d_payoff + self.player.d_early_bird
                else:
                    d_payoff = 0
        else:
            if self.session.config['All_Or_Nothing']:
                d_payoff = self.player.d_contribution + self.player.d_refund_bonus
            else:
                d_payoff = 0

        # Legt fest, welche Variablen übergeben werden sollen
        return{

            # Nur relevant, wenn die Projekte keine öffentlichen Güter sein sollen ("Public_Goods" in settings.py ist deaktiviert)
            # x_min_boolean: Gibt an, ob der Spieler mindestens den Betrag an das Projekt X gespendet hat, welcher nötig ist, um die zugehörige Auszahlung (im Falle des Projekterfolges) zu erhalten (True oder False)
            # Hinweis: x ∈ {a, b, c, d}
            "a_min_boolean": self.player.a_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_A_Goal'],
            "b_min_boolean": self.player.b_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_B_Goal'],
            "c_min_boolean": self.player.c_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_C_Goal'],
            "d_min_boolean": self.player.d_contribution >= self.session.config['Min_Factor'] * self.session.config['Project_D_Goal'],

            # Gibt an, ob die Projekte öffentliche Güter sein sollen (True oder False)
            "Public_Goods": self.session.config['Public_Goods'],

            # Gibt an, ob die "Alles oder Nichts"-Regel aktiviert ist (True oder False)
            "All_Or_Nothing": self.session.config['All_Or_Nothing'],

            # Gibt an, ob Rückzahlungs-Boni aktiviert sind (True oder False)
            "Refund_Bonus_Boolean": self.session.config['All_Or_Nothing'] and self.session.config['Refund_Bonus'] > 0,

            # Gibt an, ob Early-Bird-Boni aktiviert sind (True oder False)
            "Early_Bird_Bonus_Boolean": self.session.config['Early_Bird_Bonus'] > 0,

            # Auszahlung/Rückzahlung des Spielers für das Projekt x
            # Hinweis: x ∈ {a, b, c, d}
            "a_payoff": a_payoff,
            "b_payoff": b_payoff,
            "c_payoff": c_payoff,
            "d_payoff": d_payoff,

            # Gibt die Anzahl an Projekten an
            "Num_Projects": self.session.config['Num_Projects'],
        }


# Warteseite vor der End Seite
# Wird nur in der LETZTEN Runde aufgerufen
class EndWaitPage(WaitPage):

    # Definiert, wann die Seite aufgerufen werden soll (Hier: nur in der letzten Runde)
    def is_displayed(self):

        # Legt fest, dass die Seite nur in der letzten Runde aufgerufen werden soll
        return self.round_number == Constants.num_rounds

    # Wird aufgerufen, wenn alle Spieler der Gruppe auf der Seite angekommen sind
    # Berechnet die im gesamten Experiment erreichten Auszahlungen aller Spieler der Gruppe
    def after_all_players_arrive(self):

        # Für jeden Spieler in der Gruppe:
        for p in self.group.get_players():

            # Für jeden Eintrag in p.in_all_rounds():
            # Hinweis: p.in_all_rounds() erstellt eine Liste für den Spieler, wobei jeder Eintrag in der Liste den Spieler selbst in einer der Runden repräsentiert
            for entry in p.in_all_rounds():

                # Falls der Eintrag den Spieler NICHT in der ersten Runde repräsentiert (Erste Runde dient nur zur Übung)
                if entry.round_number != 1:

                    # Erhöht die insgesamt erreichte Auszahlung des Spielers um die Auszahlung aus der Runde, welche aktuell repräsentiert wird
                    p.total_payoff += entry.payoff

        # Erhöht den Wert der (Sitzungs-)Variable group_counter um 1
        self.session.vars['group_counter'] += 1

        # Falls die aktuelle Gruppe die letzte Gruppe ist (Folgender Code soll erst ausgeführt werden, nachdem ALLE Gruppen das Experiment abgeschlossen haben):
        if self.session.vars['group_counter'] == self.session.vars['last_group']:

            # Öffnet die CSV Datei, in welcher die Rundenergebnisse gespeichert werden
            # Hinweis: Die CSV Datei wird im "Anhängen"-Modus geöffnet, wodurch der vorherige Inhalt nicht überschrieben wird
            with open(self.session.vars['csv_file'] + ".csv", "a") as file:

                # Schreibt Folgendes in die CSV Datei:
                file.write(

                    # Zwei neue Absätze
                    2*"\n" +

                    # "group_id;player_id;total_payoff;real_life_payoff"
                    "group_id;player_id;total_payoff;real_life_payoff" +

                    # Neuer Absatz
                    "\n")

                # Für jede Gruppe:
                for g in self.subsession.get_groups():

                    # Für jeden Spieler in der aktuellen Gruppe:
                    for p in g.get_players():

                        # Schreibt Folgendes in die CSV Datei:
                        file.write(

                            # ID der Gruppe, in welcher sich der Spieler befindet
                            str(p.group.group_id) + ";" +

                            # ID des Spielers innerhalb seiner Gruppe
                            str(p.id_in_group) + ";" +

                            # Auszahlung, welche der Spieler im gesamten Experiment erreicht hat (ohne Übungsrunde)
                            str(p.total_payoff) + ";" +

                            # Gesamtauszahlung des Spielers in Euro (inklusive Teilnahmevergütung)
                            # Hinweis: Gesamtauszahlung in Punkten * Umrechnungsfaktor + Teilnahmevergütung
                            str(p.total_payoff*self.session.config['real_world_currency_per_point']+self.session.config['participation_fee'])[:-6] + "€;" +

                            # Neuer Absatz
                            "\n")


# Seite, welche dem Spieler die Ergebnisse des kompletten Experiments anzeigt
class End(Page):

    # Definiert, wann die Seite aufgerufen werden soll (Hier: nur in der letzten Runde)
    def is_displayed(self):

        # Legt fest, dass die Seite nur in der letzten Runde aufgerufen werden soll (Nummer der letzten Runde: Constants.num_rounds)
        return self.round_number == Constants.num_rounds

    # Übergibt bestimmte Variablen an die Seite, da von dort aus nicht direkt auf diese zugegriffen werden kann
    def vars_for_template(self):

        # Erstellt eine leere Liste mit dem Namen payoff_list
        payoff_list = []

        # Für jeden Eintrag in self.player.in_all_rounds():
        # Hinweis: self.player.in_all_rounds() erstellt eine Liste für den Spieler, wobei jeder Eintrag in der Liste den Spieler selbst in einer der Runden repräsentiert
        for entry in self.player.in_all_rounds():

            # Fügt die Auszahlung aus der Runde, welche aktuell repräsentiert wird, der Liste payoff_list hinzu
            payoff_list.append(entry.payoff)

        # Variable payoff_in_euro wird erstellt mit Wert: Gesamtauszahlung des Spielers in Euro (inklusive Teilnahmevergütung)
        # Hinweis: Gesamtauszahlung in Punkten * Umrechnungsfaktor + Teilnahmevergütung
        payoff_in_euro = str(self.player.total_payoff*self.session.config['real_world_currency_per_point']+self.session.config['participation_fee'])[:-6] + "€"

        # Erstellt ein dictionary mit dem Namen vars_for_templates_dict und fügt diesem die Pärchen "tutorial_payoff": payoff_list[0] und "payoff_in_euro":payoff_in_euro hinzu
        # Somit kann später auf der Seite "End.py" mit dem Befehl {{ tutorial_payoff }} auf die Auszahlung der Übungsrunde zugegriffen werden
        vars_for_templates_dict = {"tutorial_payoff": payoff_list[0],"payoff_in_euro":payoff_in_euro}

        # Falls das Experiment aus mehr als einer Runde besteht:
        if Constants.num_rounds > 1:

            # Fügt dem dictionary vars_for_templates_dict das Pärchen "round_1_payoff": payoff_list[1] hinzu
            # Somit kann später auf der Seite "End.py" mit dem Befehl {{ round_1_payoff }} auf die Auszahlung der ersten (tatsächlichen) Runde zugegriffen werden
            vars_for_templates_dict["round_1_payoff"] = payoff_list[1]

        if Constants.num_rounds > 2:
            vars_for_templates_dict["round_2_payoff"] = payoff_list[2]

        if Constants.num_rounds > 3:
            vars_for_templates_dict["round_3_payoff"] = payoff_list[3]

        if Constants.num_rounds > 4:
            vars_for_templates_dict["round_4_payoff"] = payoff_list[4]

        if Constants.num_rounds > 5:
            vars_for_templates_dict["round_5_payoff"] = payoff_list[5]

        if Constants.num_rounds > 6:
            vars_for_templates_dict["round_6_payoff"] = payoff_list[6]

        if Constants.num_rounds > 7:
            vars_for_templates_dict["round_7_payoff"] = payoff_list[7]

        if Constants.num_rounds > 8:
            vars_for_templates_dict["round_8_payoff"] = payoff_list[8]

        if Constants.num_rounds > 9:
            vars_for_templates_dict["round_9_payoff"] = payoff_list[9]

        if Constants.num_rounds > 10:
            vars_for_templates_dict["round_10_payoff"] = payoff_list[10]

        if Constants.num_rounds > 11:
            vars_for_templates_dict["round_11_payoff"] = payoff_list[11]

        if Constants.num_rounds > 12:
            vars_for_templates_dict["round_12_payoff"] = payoff_list[12]

        if Constants.num_rounds > 13:
            vars_for_templates_dict["round_13_payoff"] = payoff_list[13]

        if Constants.num_rounds > 14:
            vars_for_templates_dict["round_14_payoff"] = payoff_list[14]

        if Constants.num_rounds > 15:
            vars_for_templates_dict["round_15_payoff"] = payoff_list[15]

        if Constants.num_rounds > 16:
            vars_for_templates_dict["round_16_payoff"] = payoff_list[16]

        if Constants.num_rounds > 17:
            vars_for_templates_dict["round_17_payoff"] = payoff_list[17]

        if Constants.num_rounds > 18:
            vars_for_templates_dict["round_18_payoff"] = payoff_list[18]

        if Constants.num_rounds > 19:
            vars_for_templates_dict["round_19_payoff"] = payoff_list[19]

        if Constants.num_rounds > 20:
            vars_for_templates_dict["round_20_payoff"] = payoff_list[20]

        if Constants.num_rounds > 21:
            vars_for_templates_dict["round_21_payoff"] = payoff_list[21]

        if Constants.num_rounds > 22:
            vars_for_templates_dict["round_22_payoff"] = payoff_list[22]

        if Constants.num_rounds > 23:
            vars_for_templates_dict["round_23_payoff"] = payoff_list[23]

        if Constants.num_rounds > 24:
            vars_for_templates_dict["round_19_payoff"] = payoff_list[24]


        # Hinweis: Falls das Experiment mehr als 24 tatsächliche Runden haben soll, muss das Muster an dieser Stelle fortgeführt werden

        # Legt fest, dass der Seite "End.py" das dictionary vars_for_templates_dict übergeben wird, damit von dort aus auf die enthaltenen Variablen zugegriffen werden kann
        return vars_for_templates_dict

# Reihenfolge der Seiten in einer Runde
page_sequence = [Instructions, CrowdfundingWaitPage, Crowdfunding, ResultsWaitPage, Results, EndWaitPage, End]
