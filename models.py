

class Usuario(main.db.Model):
    __tablename__ = 'Usuarios'
    id = main.db.Column(main.db.String)
    nome = main.db.Column(main.db.String)
    telefone = main.db.Column(main.db.String)
    rua = main.db.Column(main.db.String)
    filhos = main.db.Column(main.db.String)