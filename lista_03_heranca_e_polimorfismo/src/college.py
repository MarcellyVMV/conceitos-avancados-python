from __future__ import annotations
from datetime import date, timedelta


# 3.I. Crie uma classe, Person, que no construtor instancia os detalhes básicos da pessoa, como nome, idade e detalhes de contato.
class Person:
    """
    Representa uma pessoa.

    Attributes:
        name (str): Nome da pessoa.
        age (int): Idade da pessoa.
        contact (str): Contato da pessoa.
    """

    def __init__(self, name: str, age: int, contact: str) -> None:
        """
        Inicializa uma nova pessoa com suas características básicas.

        Args:
            name (str): Nome da pessoa.
            age (int): Idade da pessoa.
            contact (str): Contato da pessoa.
        """
        self.name = name
        self.age = age
        self.contact = contact

    def __str__(self) -> str:
        """
        Retorna uma representação textual da pessoa.

        Returns:
            str: Informações formatadas da pessoa.
        """
        return (
            f"Nome: {self.name}\n"
            + f"Idade: {self.age}\n"
            + f"Contato: {self.contact}\n"
        )


# 3.II. Crie outra classe, Student, que herda de Person, mas também instancia no construtor: número de matrícula e ano de entrada. Crie um método para Student que adiciona à uma lista as matérias em que o aluno se matriculou.
class Student(Person):
    """
    Representa um estudante, herdando características de 'Person'.

    Attributes:
        student_id (int): ID do estudante.
        year_entry (int): Ano de entrada do estudante.
        courses (list[str]): Lista de matérias do estudante.
    """

    def __init__(
        self,
        name: str,
        age: int,
        contact: str,
        student_id: int,
        year_entry: int,
        courses: list[str] | None = None,
    ) -> None:
        """
        Inicializa um novo estudante com suas características.

        Args:
            name (str): Nome do estudante.
            age (int): Idade do estudante.
            contact (str): Contato do estudante.
            student_id (int): ID do estudante.
            year_entry (int): Ano de entrada do estudante.
            courses (list[str]): Lista de matérias do estudante.
        """
        super().__init__(name, age, contact)
        self.student_id = student_id
        self.year_entry = year_entry
        self.courses = courses if courses is not None else []

    def __str__(self) -> str:
        """
        Retorna uma representação textual do estudante.

        Returns:
            str: Informações formatadas do estudante.
        """
        return (
            super().__str__()
            + f"ID: {self.student_id}\n"
            + f"Ano de entrada: {self.year_entry}\n"
            + f"Matérias: {', '.join(self.courses)}\n"
        )

    def add_course(self, course: str) -> None:
        """
        Adiciona uma matéria à lista de matérias do estudante.

        Args:
            course (str): Matéria a ser adicionada.
        """
        self.courses.append(course)
        print(f"\033[1mMatéria '{course}' adicionada.\033[0m\n")


# 3.III.1 Um Lecturer é uma pessoa, que adicionalmente possui um número de sala. O Lecturer também ensina várias matérias, que precisam ser atualizados regularmente. O Lecturer supervisiona estudantes de pós-graduação.
class Lecturer(Person):
    """
    Representa um professor, herdando características de 'Person'.

    Attributes:
        room (int): Sala do professor.
        courses (list[str]): Lista de matérias ensinadas pelo professor.
        students (list[PostGraduate]): Lista de estudantes de pós-graduação do professor.
    """

    def __init__(
        self,
        name: str,
        age: int,
        contact: str,
        room: int,
        courses: list[str] | None = None,
        students: list[PostGraduate] | None = None,
    ) -> None:
        """
        Inicializa um novo professor com suas características.

        Args:
            name (str): Nome do professor.
            age (int): Idade do professor.
            contact (str): Contato do professor.
            room (int): Sala do professor.
            courses (list[str]): Lista de matérias ensinadas pelo professor.
            students (list[PostGraduate]): Lista de estudantes de pós-graduação do professor.
        """
        super().__init__(name, age, contact)
        self.room = room
        self.courses = courses if courses is not None else []
        self.students = students if students is not None else []

    def __str__(self) -> str:
        """
        Retorna uma representação textual do professor.

        Returns:
            str: Informações formatadas do professor.
        """
        return (
            super().__str__()
            + f"Sala: {self.room}\n"
            + f"Matérias: {', '.join(self.courses)}\n"
            + f"Estudantes Supervisionados: {', '.join(student.name for student in self.students)}\n"
        )

    def add_course(self, course: str) -> None:
        """
        Adiciona uma matérias à lista de matérias do professor.

        Args:
            courses (str): Matéria a ser adicionada.
        """
        self.courses.append(course)
        print(f"\033[1mMatéria '{course}' adicionada.\033[0m\n")

    # --- Getter e Setter --- #
    @property
    def students(self) -> list[PostGraduate]:
        """
        Retorna a lista de estudantes do professor.

        Returns:
            list[PostGraduate]: Lista de estudantes do professor.
        """
        return self._students

    @students.setter
    def students(self, student_list: list[PostGraduate]) -> None:
        """
        Define a lista de estudantes do professor, garantindo que sejam apenas estudantes de pós-graduação.

        Args:
            student_list (list[PostGraduate]): Lista de estudantes de pós-graduação.
        """
        students: list[PostGraduate] = []
        for student in student_list:
            if isinstance(student, PostGraduate):
                students.append(student)
                student.supervisor = self
        self._students = students

    def add_student(self, student: Student) -> None:
        """
        Adiciona um estudante de pós-graduação ao professor.

        Args:
            student (Student): Estudante de pós-graduação a ser adicionado.
        """
        if student in self._students:
            print(
                f"\033[1mO estudante {student.name} já é um estudante desse professor.\033[0m\n"
            )
        elif isinstance(student, PostGraduate):
            self._students.append(student)
            student.supervisor = self
            print(
                f"\033[1mO estudante {student.name} adicionado a esse professor.\033[0m\n"
            )
        else:
            print(f"\033[1mO estudante {student.name} não é de Pós-Graduação.\033[0m\n")


# 3.III.2 Estudantes de pós-graduação são estudantes que têm um Lecturer como supervisor. Cada um deles também pertence a um ou mais laboratórios e devem ser capazes de rastrear todos os títulos dos artigos que publicaram.
class PostGraduate(Student):
    """
    Representa um estudante de pós-graduação, herdando características de 'Student'.

    Attributes:
        supervisor (Lecturer): Professor orientador do estudante de pós-graduação.
        lab (list[str]): Lista de laboratórios do estudante de pós-graduação.
        articles (list[str]): Lista de artigos do estudante de pós-graduação.
    """

    def __init__(
        self,
        name: str,
        age: int,
        contact: str,
        student_id: int,
        year_entry: int,
        courses: list[str] | None = None,
        supervisor: Lecturer | None = None,
        lab: list[str] | None = None,
        articles: list[str] | None = None,
    ) -> None:
        """
        Inicializa um novo estudante de pós-graduação com suas características.

        Args:
            name (str): Nome do estudante de pós-graduação.
            age (int): Idade do estudante de pós-graduação.
            contact (str): Contato do estudante de pós-graduação.
            student_id (int): ID do estudante de pós-graduação.
            year_entry (int): Ano de entrada do estudante de pós-graduação.
            courses (list[str]): Lista de matérias do estudante de pós-graduação.
            supervisor (Lecturer): Professor orientador do estudante de pós-graduação.
            lab (list[str]): Lista de laboratórios do estudante de pós-graduação.
            articles (list[str]): Lista de artigos do estudante de pós-graduação.
        """
        super().__init__(name, age, contact, student_id, year_entry, courses)
        self.supervisor = supervisor
        self.lab = lab if lab is not None else []
        self.articles = articles if articles is not None else []

    def __str__(self) -> str:
        """
        Retorna uma representação textual do estudante de pós-graduação.

        Returns:
            str: Informações formatadas do estudante de pós-graduação.
        """
        return (
            super().__str__()
            + f"Professor orientador: {self.supervisor.name if self.supervisor else 'Nenhum'}\n"
            + f"Laboratórios: {', '.join(self.lab)}\n"
            + f"Artigos: {', '.join(self.articles)}\n"
        )

    def add_lab(self, lab: str) -> None:
        """
        Adiciona um laboratório à lista de laboratórios do estudante de pós-graduação.

        Args:
            lab (str): Laboratório a ser adicionado.
        """
        self.lab.append(lab)
        print(f"\033[1mLaboratório {lab} adicionado.\033[0m\n")

    def add_article(self, article: str) -> None:
        """
        Adiciona um artigo à lista de artigos do estudante de pós-graduação.

        Args:
            article (str): Artigo a ser adicionado.
        """
        self.articles.append(article)
        print(f"\033[1mArtigo {article} adicionado.\033[0m\n")


# 3.III.3 Estudantes de graduação são estudantes que estão trabalhando para obter um diploma (BEng, MEng). Eles têm um Lecturer como tutor e frequentemente pegam livros emprestados da biblioteca, então precisam rastrear quais livros estão com eles e a data de devolução dos livros.
class UnderGraduate(Student):
    """
    Representa um estudante de graduação, herdando características de 'Student'.

    Attributes:
        diploma (str): Diploma do estudante de graduação.
        tutor (Lecturer): Professor tutor do estudante de graduação.
        borrowed_books (list[Library]): Lista de livros emprestados pelo estudante de graduação.
    """

    def __init__(
        self,
        name: str,
        age: int,
        contact: str,
        student_id: int,
        year_entry: int,
        courses: list[str] | None = None,
        diploma: str | None = None,
        tutor: Lecturer | None = None,
        borrowed_books: list[Library] | None = None,
    ) -> None:
        """
        Inicializa um novo estudante de graduação com suas características.

        Args:
            name (str): Nome do estudante de graduação.
            age (int): Idade do estudante de graduação.
            contact (str): Contato do estudante de graduação.
            student_id (int): ID do estudante de graduação.
            year_entry (int): Ano de entrada do estudante de graduação.
            courses (list[str]): Lista de matérias do estudante de graduação.
            diploma (str): Diploma do estudante de graduação.
            tutor (Lecturer): Professor tutor do estudante de graduação.
            borrowed_books (list[Library]): Lista de livros emprestados pelo estudante de graduação.
        """
        super().__init__(name, age, contact, student_id, year_entry, courses)
        self._diploma = None
        self.diploma = diploma
        self.tutor = tutor
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def __str__(self) -> str:
        """
        Retorna uma representação textual do estudante de graduação.

        Returns:
            str: Informações formatadas do estudante de graduação.
        """
        return (
            super().__str__()
            + f"Diploma: {self.diploma}\n"
            + f"Tutor: {self.tutor.name if self.tutor else 'Nenhum'}\n"
        )

    def print_borrowed_books(self, name: str | None = None) -> None:
        """
        Imprime os livros emprestados pelo estudante de graduação. Se um nome de livro for fornecido, imprime apenas esse livro.

        Args:
            name (str, optional): Nome do livro a ser impresso. Defaults to None.
        """
        if not name:
            for book in self.borrowed_books:
                print(book)
        else:
            for book in self.borrowed_books:
                if book.name == name:
                    print(book.name)

    # --- Getter e Setter --- #
    @property
    def diploma(self) -> str:
        """
        Retorna o diploma do estudante de graduação.

        Returns:
            str: Diploma do estudante de graduação.
        """
        return self._diploma

    @diploma.setter
    def diploma(self, diploma: str) -> None:
        """
        Define o diploma do estudante de graduação.

        Args:
            diploma (str): Novo diploma do estudante de graduação.
        """
        degrees = {"BEng", "MEng"}
        if getattr(self, "_diploma", None) == diploma:
            print(f"\033[1mO estudante {self.name} já tem esse diploma.\033[0m\n")
        elif diploma in degrees:
            self._diploma = diploma
            print(f"\033[1mO estudante {self.name} tem o diploma {diploma}.\033[0m\n")
        else:
            raise ValueError(f"\033[1mO diploma {diploma} não existe.\033[0m\n")


class Library:
    """
    Representa uma biblioteca de livros.

    Attributes:
        name (str): Nome do livro.
        status (bool): Status do livro (True para disponível, False para indisponível).
        reader (UnderGraduate): Estudante que pegou o livro emprestado.
        return_date (date): Data de devolução do livro.
    """

    def __init__(
        self,
        name: str,
        status: bool = True,
        reader: UnderGraduate | None = None,
        return_date: date | None = None,
    ) -> None:
        """
        Inicializa um novo livro na biblioteca com suas características.

        Args:
            name (str): Nome do livro.
            status (bool, optional): Status do livro (True para disponível, False para indisponível). Defaults to True.
            reader (UnderGraduate | None, optional): Estudante que pegou o livro emprestado. Defaults to None.
            return_date (date | None, optional): Data de devolução do livro. Defaults to None.
        """
        self.name = name
        self.status = status
        self.reader = reader
        self.return_date = return_date

    def __str__(self) -> str:
        """
        Retorna uma representação textual do livro.

        Returns:
            str: Informações formatadas do livro.
        """
        return (
            f"Livro: {self.name}\n"
            f"Status: {'Disponível' if self.status else 'Não disponível'}\n"
            f"Leitor: {self.reader.name if self.reader else 'Nenhum'}\n"
            f"Data de devolução: {self.return_date.strftime('%d/%m/%Y') if self.return_date else 'Nenhuma'}\n"
        )

    def borrow_book(self, undergraduate: UnderGraduate) -> None:
        """
        Empréstimo de um livro para o estudante de graduação. O livro deve estar disponível para empréstimo.

        Args:
            undergraduate (UnderGraduate): Estudante de graduação que pegou o livro emprestado.
        """
        if self.status:
            self.status = False
            self.reader = undergraduate
            self.return_date = date.today() + timedelta(days=15)
            undergraduate.borrowed_books.append(self)
            print(
                f"\033[1mO estudante {undergraduate.name} pegou emprestado o livro {self.name}.\033[0m\n"
            )
        else:
            print(f"\033[1mO livro {self.name} não está disponível.\033[0m\n")

    def return_book(self, undergraduate: UnderGraduate) -> None:
        """
        Devolução de um livro para o estudante de graduação. O livro deve estar emprestado para o estudante de graduação.

        Args:
            undergraduate (UnderGraduate): Estudante de graduação que pegou o livro emprestado.
        """

        if self in undergraduate.borrowed_books:
            if date.today() > self.return_date:
                print(
                    f"\033[1mO livro {self.name} está atrasado. Multa: 5 reais por dia de atraso.\033[0m\n"
                )
            undergraduate.borrowed_books.remove(self)
            self.status = True
            self.reader = None
            self.return_date = None
            print(f"\033[1mO livro {self.name} foi devolvido com sucesso.\033[0m\n")
        else:
            print(
                f"\033[1mO estudante {undergraduate.name} não tem esse livro.\033[0m\n"
            )


def main() -> int:
    """
    Função principal do programa.

    Returns:
        int: Código de saída do programa.
    """
    # Criando livros
    fisica1 = Library("Física 1")
    fisica2 = Library("Física 2")
    calculo1 = Library("Cálculo 1")

    # Criando estudantes de graduação
    kaua = UnderGraduate(
        "Kaua", 20, "999999999", 123456, 2023, ["Física 1", "Cálculo 2"], diploma="MEng"
    )

    yuri = UnderGraduate(
        "Yuri", 20, "999999999", 123466, 2023, ["Física 2"], diploma="BEng"
    )

    # Criando estudantes de pós-graduação
    queiroz = PostGraduate(
        "Queiroz", 23, "999999999", 123457, 2020, ["Cálculo 2"], lab=["Lab Rockets"]
    )

    geovana = PostGraduate("Geovaná", 23, "999999999", 123458, 2020, ["Álgebra Linear"])

    # Criando professor
    daniel = Lecturer("Daniel", 30, "999999999", 3, ["Cálculo 2"], [queiroz])

    # Testando métodos
    kaua.add_course("Programação")
    daniel.add_course("Física Experimental")

    queiroz.add_article("Artigo sobre Física de Partículas")
    geovana.add_lab("Lab Rockets")

    daniel.add_student(geovana)
    daniel.add_student(yuri)  # Deve informar que não é de pós-graduação

    # Testando biblioteca
    fisica1.borrow_book(kaua)
    fisica2.borrow_book(kaua)
    calculo1.borrow_book(yuri)
    calculo1.borrow_book(kaua)  # Livro indisponível

    print("Livros emprestados para Kaua:")
    kaua.print_borrowed_books()

    fisica1.return_book(kaua)

    print("Livros emprestados para Kaua após devolução:")
    kaua.print_borrowed_books()

    # Exibindo os objetos
    print("\033[1mProfessor:\033[0m")
    print(daniel)

    print("\033[1mEstudante de graduação:\033[0m")
    print(kaua)

    print("\033[1mEstudante de pós-graduação:\033[0m")
    print(queiroz)

    print("\033[1mLivro:\033[0m")
    print(calculo1)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
