import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget

class MarketApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Mercado")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.tab_buttons = QHBoxLayout()
        self.tab_buttons.addWidget(self.create_tab_button("Cadastro", self.show_cadastro))
        self.tab_buttons.addWidget(self.create_tab_button("Estoque", self.show_estoque))
        self.tab_buttons.addWidget(self.create_tab_button("Vendas", self.show_vendas))

        self.layout.addLayout(self.tab_buttons)

        self.cadastro_widget = self.create_cadastro_widget()
        self.estoque_widget = self.create_estoque_widget()
        self.vendas_widget = self.create_vendas_widget()

        self.stacked_widget = self.create_stacked_widget()
        self.layout.addWidget(self.stacked_widget)

        self.central_widget.setLayout(self.layout)

    def create_tab_button(self, text, slot):
        button = QPushButton(text)
        button.clicked.connect(slot)
        return button

    def create_cadastro_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.product_name_input = QLineEdit()
        self.product_price_input = QLineEdit()
        self.product_quantity_input = QLineEdit()
        self.add_product_button = QPushButton("Adicionar Produto")

        layout.addWidget(QLabel("Nome do Produto:"))
        layout.addWidget(self.product_name_input)
        layout.addWidget(QLabel("Preço Unitário:"))
        layout.addWidget(self.product_price_input)
        layout.addWidget(QLabel("Quantidade em Estoque:"))
        layout.addWidget(self.product_quantity_input)
        layout.addWidget(self.add_product_button)

        self.add_product_button.clicked.connect(self.add_product)

        return widget

    def create_estoque_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.product_list = QListWidget()
        layout.addWidget(self.product_list)

        return widget

    def create_vendas_widget(self):
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.sale_list = QListWidget()
        self.total_label = QLabel("Total: R$ 0.00")
        self.checkout_button = QPushButton("Finalizar Venda")

        layout.addWidget(self.sale_list)
        layout.addWidget(self.total_label)
        layout.addWidget(self.checkout_button)

        self.checkout_button.clicked.connect(self.finalizar_venda)

        return widget

    def create_stacked_widget(self):
        stacked_widget = QWidget()

        self.stacked_layout = QVBoxLayout()
        stacked_widget.setLayout(self.stacked_layout)

        self.stacked_layout.addWidget(self.cadastro_widget)
        self.stacked_layout.addWidget(self.estoque_widget)
        self.stacked_layout.addWidget(self.vendas_widget)

        return stacked_widget

    def show_cadastro(self):
        self.stacked_layout.setCurrentIndex(0)

    def show_estoque(self):
        self.stacked_layout.setCurrentIndex(1)
        self.update_estoque_list()

    def show_vendas(self):
        self.stacked_layout.setCurrentIndex(2)
        self.update_sale_list()

    def add_product(self):
        name = self.product_name_input.text()
        price = self.product_price_input.text()
        quantity = self.product_quantity_input.text()

        if name and price and quantity:
            product_info = f"{name} - Preço: R$ {price} - Estoque: {quantity}"
            self.product_list.addItem(product_info)
            self.product_name_input.clear()
            self.product_price_input.clear()
            self.product_quantity_input.clear()

    def update_estoque_list(self):
        # Implemente a atualização da lista de estoque aqui.
        pass

    def update_sale_list(self):
        # Implemente a atualização da lista de vendas aqui.
        pass

    def finalizar_venda(self):
        # Implemente a finalização da venda e atualização de estoque aqui.
        pass

def main():
    app = QApplication(sys.argv)
    window = MarketApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
