today = '08/09/2024'

class Person:
    #Função inicial
    def __init__(self, name:str, age:int, contact:str) -> None:
        self.name = name
        self.age = age
        self.contact = contact

    #Função para imprimir
    def __str__(self) -> str:
        return f"\nNome: {self.name}\nIdade: {self.age}\nContato: {self.contact}"

class Student(Person):
    #Função inicial
    def __init__(self, name:str, age:int, contact:str, student_id:int, year_entry:int, materials:list = []) -> None:
        super().__init__(name, age, contact)
        self.student_id = student_id
        self.year_entry = year_entry
        self.materials = materials

    #Função para imprimir
    def __str__(self) -> str:
        return super().__str__() + f"\nID: {self.student_id}\nAno de entrada: {self.year_entry}\nMateriais: {self.materials}"

    #Função para adicionar materiais
    def add_materials(self, material) -> None:
        self.materials.append(material)

class Lecturer(Person):
    #Função inicial
    def __init__(self, name:str, age:int, contact:str, room:int, materials:list = [], students:list = []) -> None:
        super().__init__(name, age, contact)
        self.room = room
        self.materials = materials
        self._students = students

    #Função para imprimir
    def __str__(self) -> str:
        return super().__str__() + f"\nSala: {self.room}\nMateriais: {self.materials}"

    #Função para adicionar materiais
    def add_material(self, material:list) -> None:
        self.material.extend(material)
        print(f'\nMatéria(s) {material} adicionada(is).')

    #Getter e Setter
    @property
    def students(self) -> list:
        return self._students
    
    @students.setter
    def students(self, student_list: list) -> None:
        students = []
        for student in student_list:
            if student in PostGraduate:
                students.append(student)
        self._students = students

    #Função para adicionar estudantes   
    def add_students(self, student) -> None:
        if student in self._students:
            print(f"\nO estudante {student.name} já é um estudante desse professor.")
        elif isinstance(student, PostGraduate):
            self._students.append(student)
            print(f'\nEstudante {student.name} adicionado.')
        else:
            print(f"\nO estudante {student.name} não é um estudante de Pós-Graduação.")

class PostGraduate(Student):
    #Função inicial
    def __init__(self, name:str, age:int, contact:str, student_id:int, year_entry:int, lab:list = [], articles:list = []) -> None:
        super().__init__(name, age, contact, student_id, year_entry)
        self.lab = lab
        self.articles = articles

    #Função para imprimir
    def __str__(self) -> str:
        return super().__str__() + f"\nLaboratórios: {self.lab}\nArtigos: {self.articles}"

    #Função para adicionar laboratórios
    def add_lab(self, lab) -> None:
        self.lab.append(lab)
        print(f'\nLaboratório {lab} adicionado.')

    #Função para adicionar artigos
    def add_articles(self, article) -> None:
        self.articles.append(article)
        print(f'\nArtigo {article} adicionado.')

class Graduate(Student):
    #Função inicial
    def __init__(self, name:str, age:int, contact:str, student_id:int, year_entry:int, diploma:str, borrowed_books = []) -> None:
        super().__init__(name, age, contact, student_id, year_entry)
        self._diploma = diploma
        self.borrowed_books = borrowed_books

    #Função para imprimir
    def __str__(self) -> str:
        return super().__str__() + f"\nDiploma: {self.diploma}"

    #Função para imprimir livros emprestados pelo estudante
    def print_borrowed_books(self, name = None) -> None:   
        if not name:
            for book in self.borrowed_books:
                print(book)
        else:
            for book in self.borrowed_books:
                if book.name == name:
                    print(book)

    #Getter e Setter
    @property
    def diploma(self) -> str:
        return self._diploma
    
    @diploma.setter
    #Função para adicionar diploma
    def diploma(self, diploma) -> None:
        degrees = ["BEng", "MEng"]
        if self._diploma == diploma:
            print(f"\nO estudante {self.name} já tem esse diploma.")
        elif diploma in degrees:
            self._diploma = diploma
            print(f"\nO estudante {self.name} tem o diploma {diploma}.")
        else:
            raise ValueError(f"O diploma {diploma} não existe.")

    #Função para adicionar livros
    def borrow_book(self, book) -> None:
        return_date = today[:3] + str(int(today[3:5]) + 1) + today[5:]
        if book.status:
            book.status = False
            book.reader = self.name
            book.return_date = return_date
            self.borrowed_books.append(book)
            print(f"\nO estudante {self.name} pegou emprestado o livro {book.name}.")
        else:
            print(f"\nO livro {book.name} não está disponível.")

    #Função para devolver livros (/remover do dicionário)   
    def return_book(self, book) -> None:
        def give_back(self, book): #Função interna para realmente devolver livros
            self.borrowed_books.remove(book)
            book.status = True
            book.reader = ''
            book.return_date = ''
            print(f"\nO livro {book.name} foi devolvido com sucesso.")
        
        if book in self.borrowed_books:
            if int(book.return_date[3:5]) > int(today[3:5]):
                give_back(self, book)
            elif int(book.return_date[3:5]) == int(today[3:5]) and int(book.return_date[0:2]) > int(today[0:2]):
                give_back(self, book)
            else:
                print(f"\nO livro {book.name} está atrasado. Multa: 5 reais por dia de atraso.")
                give_back(self, book)
        else:
            print(f"\nO estudante {self.name} não tem esse livro.")

class Library:
    #Função inicial
    def __init__(self, name:str, status:bool = True, reader = '', return_date:str = '') -> None:
        self.name = name
        self.status = status
        self.reader = reader
        self.return_date = return_date

    #Função para mostrar
    def __str__(self) -> str:
        return f"\nLivro: {self.name}\nStatus: {'Disponível' if self.status else 'Não disponível'}\nLeitor: {self.reader}\nData de devolução: {self.return_date}"

#Exemplo
fisica1 = Library("Fisica 1")
fisica2 = Library("Fisica 2")
calculo1 = Library("Calculo 1")
algebra_linear = Library("Algebra Linear")

kaua = Graduate("Kaua", 20, "999999999", 123456, 2023, "MEng")
yuri = Graduate("Yuri", 20, "999999999", 123466, 2023, "MEng")
queiroz = PostGraduate("Queiroz", 23, "999999999", 123457, 2020, ["Lab Rockets"])
geovana = PostGraduate("Geovaná", 23, "999999999", 123458, 2020)
daniel = Lecturer("Daniel", 30, "999999999", 3, ["Cálculo 1"], [queiroz])

kaua.diploma = "MEng"
yuri.diploma = "BEng"
queiroz.add_articles("Artigo 1")
geovana.add_lab("Lab Rockets")
daniel.add_students(yuri)
daniel.add_students(geovana)

kaua.borrow_book(fisica1)
kaua.borrow_book(fisica2)
yuri.borrow_book(calculo1)
kaua.borrow_book(calculo1)

kaua.print_borrowed_books()
kaua.return_book(fisica1)