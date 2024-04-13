class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        try:
            # 숫자가 아닌 값이 입력되었을때 프로그램 동작하도록 예외 처리 구문 추가함
            #연산자에 따라 각각 다른 함수를 사용하여 결과를 리턴함
            num1 = float(self.view.le1.text())
            num2 = float(self.view.le2.text())
            operator = self.view.cb.currentText()

            if operator == '+':
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == '-':
                return f'{num1} - {num2} = {self.sub(num1, num2)}'
            elif operator == '*':
                return f'{num1} * {num2} = {self.mul(num1, num2)}'
            elif operator == '/':
                return f'{num1} / {num2} = {self.div(num1, num2)}'

            else:
                return "Calculation Error"
        except:
            return "Caculation Error"

    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda:\
                                       self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):
        return a+b
    
    def sub(self, a, b):
        return a-b
    
    def mul(self, a, b):
        return a*b
    
    def div(self, a, b):
        try:
            if(b==0):
                raise Exception("Division Error")
        except Exception as e:
            return e
        
        return a/b