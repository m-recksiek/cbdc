class Calculator(object):

    def calculateRaw(self, settings: dict):

        if settings["useinputraw"] == "False":
            self.settings = settings
            self.weapon_raw = settings["Raw"]
            self.multi_list = []

            if settings["Attackboost"] > 0:
                if settings["Attackboost"] == 1:
                    self.weapon_raw += 3
                elif settings["Attackboost"] == 2:
                    self.weapon_raw += 6
                elif settings["Attackboost"] == 3:
                    self.weapon_raw += 9
                elif settings["Attackboost"] == 4:
                    self.weapon_raw += 7
                    self.multi_list.append(1.05)
                elif settings["Attackboost"] == 5:
                    self.weapon_raw += 8
                    self.multi_list.append(1.06)
                elif settings["Attackboost"] == 6:
                    self.weapon_raw += 9
                    self.multi_list.append(1.08)
                elif settings["Attackboost"] == 7:
                    self.weapon_raw += 10
                    self.multi_list.append(1.1)

            if settings["Challenger"] > 0:
                self.weapon_raw += ( 4 * settings["Challenger"])

            if settings["Resentment"] > 0:
                self.weapon_raw += ( 5 * settings["Resentment"])

            if settings["Resuscitate"] > 0:
                if settings["Resuscitate"] < 3 :
                    self.weapon_raw += ( 5 * settings["Resuscitate"])
                else:
                    self.weapon_raw += 20

            if settings["Peak Performance"] > 0:
                if settings["Peak Performance"] < 3:
                    self.weapon_raw += (5 * settings["Peak Performance"])
                else:
                    self.weapon_raw += 20

            if settings["Offensive Guard"] > 0:
                if settings["Offensive Guard"] == 1:
                    self.multi_list.append(1.05)
                if settings["Offensive Guard"] == 2:
                    self.multi_list.append(1.10)
                if settings["Offensive Guard"] == 3:
                    self.multi_list.append(1.15)

            if settings["Fortify"] > 0:
                if settings["Fortify"] == 1:
                    self.multi_list.append(1.10)
                if settings["Fortify"] == 2:
                    self.multi_list.append(1.20)

            if settings["Counterstrike"] > 0:
                if settings["Counterstrike"] == 1:
                    self.weapon_raw += 10
                if settings["Counterstrike"] == 2:
                    self.weapon_raw += 20
                if settings["Counterstrike"] == 3:
                    self.weapon_raw += 25

            if settings["Heroics"] > 1:
                if settings["Heroics"] == 2:
                    self.multi_list.append(1.05)
                if settings["Heroics"] == 3:
                    self.multi_list.append(1.05)
                if settings["Heroics"] == 5:
                    self.multi_list.append(1.10)
                if settings["Heroics"] == 5:
                    self.multi_list.append(1.30)

            for item in self.multi_list:
                self.weapon_raw *= item
            print(self.weapon_raw)

        else:
            self.weapon_raw = settings["Raw"]

        return self.weapon_raw

    def calculateCrits(self):
        critical = damage * (1.25 + (cbl * 0.05))
        return critical


