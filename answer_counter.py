from configs import Config
from ui.components.select import Select
from ui.components import resources
from ui.components.primary_btn import PrimaryBtn
from show_result import ShowResult

class AnswerTaker:
    def __init__(self, parent_layout, parent):
        self.parent_layout = parent_layout
        self.parent = parent
        self.config = Config.get_instance()
        self.answers = {}
        self.selects = []
        self.additionally = {}
        self.init()

    def init(self):
        tags = self.config.get('tags')
        add = self.config.get('additionally')
        for tag in tags:
            select = Select(self.parent_layout, tag['alias'])
            select.comboBox.addItem('Не Выбрано', 'none')
            for i in tag['values']:
                select.comboBox.addItem(i['alias'], i['value'])

            select.comboBox.setCurrentIndex(0)
            select.comboBox.currentIndexChanged.connect(self.handle_change(tag['alias'], select.comboBox))
            self.selects.append(select)

        for i in add:
            select = Select(self.parent_layout, i['alias'] + ' (Доп.)')
            select.comboBox.addItem('Не Выбрано', '')
            select.comboBox.setCurrentIndex(0)
            for j in i['values']:
                select.comboBox.addItem(j['alias'], j['value'])
            select.comboBox.currentIndexChanged.connect(self.handle_change_additionalls(i['value'], select.comboBox))


        self.btn = PrimaryBtn(self.parent_layout, 'Найти')
        self.btn.pushButton.clicked.connect(self.handle_click)

    def handle_click(self):
        self.set_state(False)
        show_res = ShowResult(self.answers.values(), ' '.join(self.additionally.values()))
        show_res.onClose.connect(self.set_state)

    def set_state(self, value=True):
        self.btn.pushButton.setEnabled(value)
        for select in self.selects:
            select.comboBox.setEnabled(value)

    def handle_change(self, alias, comboBox):
        def _(i):
            if i == 0:
                self.answers.pop(alias)
                return

            self.answers[alias] = comboBox.currentData()

        return _

    def handle_change_additionalls(self, alias, comboBox):
        def _(i):
            if i == 0:
                self.additionally.pop(alias)
                return

            self.additionally[alias] = comboBox.currentData()

        return _


