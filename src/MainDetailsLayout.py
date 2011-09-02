from PyQt4 import QtGui
from BaseFormLayout import BaseFormLayout
from BaseFormLayout import LineEdit, ShortLineEdit, NumberEdit, ValueEdit, MoneyEdit
from BaseFormLayout import FormItem as Item

class MainDetailsLayout(BaseFormLayout):
    def __init__(self, record, parent=None):
        super(MainDetailsLayout, self).__init__(parent)
        self.columnCount = 5
        
        self.items = [ Item('title', "Name", parent), 
            Item('value', "Value", parent), Item('unit', "Unit", parent),
            Item('country', "Country", parent), Item('year', "Year", parent),
            Item('period', "Period", parent), Item('mint', "Mint", parent),
            Item('mintmark', "Mint mark", parent), Item('type', "Type", parent),
            Item('series', "Series", parent) ]

        item = self.items[0]
        item.setWidget(LineEdit(parent))
        btn = QtGui.QPushButton(self.tr("Generate"), parent)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        btn.clicked.connect(self.clickGenerate)
        self.addRow(item, btn)

        item = self.items[3]
        item.setWidget(LineEdit(parent))
        self.addRow(item)

        item = self.items[5]
        item.setWidget(LineEdit(parent))
        self.addRow(item)

        item1 = self.items[1]
        item1.setWidget(MoneyEdit(parent))
        item2 = self.items[2]
        item2.setWidget(LineEdit(parent))
        self.addRow(item1, item2)

        item = self.items[4]
        item.setWidget(NumberEdit(parent))
        self.addRow(item)

        item1 = self.items[7]
        item1.setWidget(ShortLineEdit(parent))
        item2 = self.items[6]
        item2.setWidget(LineEdit(parent))
        self.addRow(item1, item2)

        item = self.items[8]
        item.setWidget(LineEdit(parent))
        self.addRow(item)

        item = self.items[9]
        item.setWidget(LineEdit(parent))
        self.addRow(item)

        if not record.isEmpty():
            for item in self.items:
                if not record.isNull(item.field()):
                    value = record.value(item.field())
                    item.setValue(value)

    def values(self):
        val = {}
        for item in self.items:
            val[item.field()] = item.value()
        return val
    
    def clickGenerate(self):
        titleParts = []
        value = str(self.items[1].value())
        if value:
            titleParts.append(value) 
        value = str(self.items[2].value())
        if value:
            titleParts.append(value)
        value = str(self.items[4].value())
        if value:
            titleParts.append(value)
        value = str(self.items[7].value())
        if value:
            titleParts.append(value)

        title = ' '.join(titleParts)
        self.items[0].widget().setText(title)

if __name__ == '__main__':
    from main import run
    run()
