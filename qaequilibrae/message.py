from qgis.PyQt.QtCore import Qt, QCoreApplication


class messages:
    @property
    def first_message(self):
        a = self.tr("AequilibraE and other dependencies are not not installed")
        b = self.tr("Do you want us to install these missing python packages?")
        c = self.tr("QGIS will be non-responsive for a couple of minutes.")
        return f"{a} {b}\r\n{c}"

    @property
    def second_message(self):
        a = self.tr("Errors may have happened during installation.")
        b = self.tr("Please inspect the messages on your General Log message tab")
        return f"{a} {b}"

    @property
    def third_message(self):
        return self.tr("You will probably need to restart QGIS to make it work")

    @property
    def fourth_message(self):
        return self.tr("Without installing the packages, the plugin will be mostly non-functional")

    def tr(self, text):
        return QCoreApplication.translate("messages", text)
