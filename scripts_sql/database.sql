
USE EVENTOS;


CREATE TABLE IF NOT EXISTS FUNCIONARIO(
	idFuncionario INT NOT NULL AUTO_INCREMENT,
    cpfFuncionario VARCHAR(13) NOT NULL,
    nomeFuncionario VARCHAR(60) NOT NULL,
	cargo VARCHAR(50) NOT NULL,
	salarioMensal DECIMAL(7,2) NOT NULL,
    CONSTRAINT FUNCIONARIO_PK PRIMARY KEY(idFuncionario)
);


CREATE TABLE IF NOT EXISTS SALAO(
	idSalao INT NOT NULL AUTO_INCREMENT,
    nomeSalao VARCHAR(50) NOT NULL,
    CONSTRAINT SALAO_PK PRIMARY KEY(idSalao)
);

 
CREATE TABLE IF NOT EXISTS EVENTO(
	idEvento INT NOT NULL  AUTO_INCREMENT,
    tipoEvento VARCHAR(50) NOT NULL,
    dataHora DATETIME NOT NULL,
    idSalao INT NOT NULL,
    CONSTRAINT EVENTO_PK PRIMARY KEY(idEvento),
    CONSTRAINT SALAO_FK FOREIGN KEY(idSalao)
		REFERENCES SALAO(idSalao)
);


CREATE TABLE IF NOT EXISTS CLIENTE(
	idCliente INT NOT NULL AUTO_INCREMENT,
    cpfCliente VARCHAR(13) NOT NULL,
    nomeCliente VARCHAR(60) NOT NULL,
	emailCliente VARCHAR(50) NOT NULL,
	CONSTRAINT CLIENTE_PK PRIMARY KEY(idCliente)
);

CREATE TABLE IF NOT EXISTS CONTRATO(
	idContrato INT NOT NULL AUTO_INCREMENT,
    valorEvento INT NOT NULL,
    qtdPessoa INT NOT NULL,
    idEvento INT NOT NULL,
    idCliente INT NOT NULL,
    CONSTRAINT CONTRATO_PK PRIMARY KEY(idContrato),
    CONSTRAINT EVENTO_FK FOREIGN KEY(idEvento)
		REFERENCES EVENTO(idEvento),
	CONSTRAINT CLIENTE_FK FOREIGN KEY(idCliente)
		REFERENCES CLIENTE(idCliente)
);

CREATE TABLE IF NOT EXISTS TRABALHA(
	idFuncionario INT NOT NULL,
    idEvento INT NOT NULL,
    CONSTRAINT FUNCIONARIO_FK FOREIGN KEY(idFuncionario)
		REFERENCES FUNCIONARIO(idFuncionario),
	CONSTRAINT EVENTO_FK_2 FOREIGN KEY(idEvento)
		REFERENCES EVENTO(idEvento)
);

CREATE TABLE IF NOT EXISTS USUARIO(
	nomeUsuario VARCHAR(50) NOT NULL,
    senhaUsuario VARCHAR(30) NOT NULL
);


INSERT INTO USUARIO(nomeUsuario, senhaUsuario) VALUES('admin', 'admin123');
INSERT INTO USUARIO(nomeUsuario, senhaUsuario) VALUES('paulocerq', 'laranjamecanica123');

 INSERT INTO SALAO(idSalao, nomeSalao) 
 VALUES 	
	(1, 'Salao Alfa'),
    (2, 'Salao Delta'),
    (3, 'Salao Charle');

INSERT INTO FUNCIONARIO (cpfFuncionario, nomeFuncionario, cargo, salarioMensal) VALUES
('12345678901', 'João Silva', 'Cozinheiro', 2500.00),
('23456789012', 'Maria Oliveira', 'Gerente', 5500.00),
('34567890123', 'Carlos Souza', 'Garçon', 1800.00),
('45678901234', 'Ana Pereira', 'Chefe de cozinha', 6000.00),
('56789012345', 'Pedro Santos', 'Motorista', 2200.00),
('67890123456', 'Lucas Lima', 'Manobrador', 2000.00),
('78901234567', 'Fernanda Costa', 'Contador', 4800.00),
('89012345678', 'Juliana Almeida', 'Tecnico de TI', 4000.00),
('90123456789', 'Rafael Rodrigues', 'Copeiro', 1500.00),
('01234567890', 'Bruna Martins', 'Cozinheiro', 2600.00),
('11234567890', 'Ricardo Ferreira', 'Gerente', 5300.00),
('21234567890', 'Patrícia Lima', 'Garçon', 1700.00),
('31234567890', 'Gustavo Alves', 'Chefe de cozinha', 5900.00),
('41234567890', 'Renata Barbosa', 'Motorista', 2300.00),
('51234567890', 'Marcos Ribeiro', 'Manobrador', 2100.00),
('61234567890', 'Camila Fernandes', 'Contador', 4700.00),
('71234567890', 'Thiago Gomes', 'Tecnico de TI', 4100.00),
('81234567890', 'Larissa Pinto', 'Copeiro', 1600.00),
('91234567890', 'Felipe Azevedo', 'Cozinheiro', 2700.00),
('10123456789', 'Aline Carvalho', 'Gerente', 5400.00),
('11123456789', 'Eduardo Rocha', 'Garçon', 1900.00),
('12123456789', 'Vanessa Melo', 'Chefe de cozinha', 5800.00),
('13123456789', 'Rodrigo Teixeira', 'Motorista', 2400.00),
('14123456789', 'Beatriz Nunes', 'Manobrador', 2200.00),
('15123456789', 'André Vieira', 'Contador', 4600.00),
('16123456789', 'Isabela Castro', 'Tecnico de TI', 4200.00),
('17123456789', 'Bruno Mendes', 'Copeiro', 1700.00),
('18123456789', 'Débora Silva', 'Cozinheiro', 2800.00),
('19123456789', 'Fábio Santos', 'Gerente', 5600.00),
('20123456789', 'Tatiana Souza', 'Garçon', 2000.00);


INSERT INTO EVENTO (tipoEvento, dataHora, idSalao) VALUES
('Casamento', '2024-09-01 18:00:00', 1),
('Aniversario', '2024-09-02 15:00:00', 2),
('Cha de Frauda', '2024-09-03 10:00:00', 3),
('Cha de Revelação', '2024-09-04 14:00:00', 1),
('Evento Empresarial', '2024-09-05 09:00:00', 2),
('Evento Comunitario', '2024-09-06 16:00:00', 3),
('Festa de Formatura', '2024-09-07 19:00:00', 1),
('Casamento', '2024-09-08 18:00:00', 2),
('Aniversario', '2024-09-09 15:00:00', 3),
('Cha de Frauda', '2024-09-10 10:00:00', 1),
('Cha de Revelação', '2024-09-11 14:00:00', 2),
('Evento Empresarial', '2024-09-12 09:00:00', 3),
('Evento Comunitario', '2024-09-13 16:00:00', 1),
('Festa de Formatura', '2024-09-14 19:00:00', 2),
('Casamento', '2024-09-15 18:00:00', 3),
('Aniversario', '2024-09-16 15:00:00', 1),
('Cha de Frauda', '2024-09-17 10:00:00', 2),
('Cha de Revelação', '2024-09-18 14:00:00', 3),
('Evento Empresarial', '2024-09-19 09:00:00', 1),
('Evento Comunitario', '2024-09-20 16:00:00', 2),
('Festa de Formatura', '2024-09-21 19:00:00', 3),
('Casamento', '2024-09-22 18:00:00', 1),
('Aniversario', '2024-09-23 15:00:00', 2),
('Cha de Frauda', '2024-09-24 10:00:00', 3),
('Cha de Revelação', '2024-09-25 14:00:00', 1),
('Evento Empresarial', '2024-09-26 09:00:00', 2),
('Evento Comunitario', '2024-09-27 16:00:00', 3),
('Festa de Formatura', '2024-09-28 19:00:00', 1),
('Casamento', '2024-09-29 18:00:00', 2),
('Aniversario', '2024-09-30 15:00:00', 3);


INSERT INTO CLIENTE (cpfCliente, nomeCliente, emailCliente) VALUES
('12345678901', 'João Silva', 'joao.silva@example.com'),
('23456789012', 'Maria Oliveira', 'maria.oliveira@example.com'),
('34567890123', 'Carlos Souza', 'carlos.souza@example.com'),
('45678901234', 'Ana Pereira', 'ana.pereira@example.com'),
('56789012345', 'Pedro Santos', 'pedro.santos@example.com'),
('67890123456', 'Lucas Lima', 'lucas.lima@example.com'),
('78901234567', 'Fernanda Costa', 'fernanda.costa@example.com'),
('89012345678', 'Juliana Almeida', 'juliana.almeida@example.com'),
('90123456789', 'Rafael Rodrigues', 'rafael.rodrigues@example.com'),
('01234567890', 'Bruna Martins', 'bruna.martins@example.com'),
('11234567890', 'Ricardo Ferreira', 'ricardo.ferreira@example.com'),
('21234567890', 'Patrícia Lima', 'patricia.lima@example.com'),
('31234567890', 'Gustavo Alves', 'gustavo.alves@example.com'),
('41234567890', 'Renata Barbosa', 'renata.barbosa@example.com'),
('51234567890', 'Marcos Ribeiro', 'marcos.ribeiro@example.com'),
('61234567890', 'Camila Fernandes', 'camila.fernandes@example.com'),
('71234567890', 'Thiago Gomes', 'thiago.gomes@example.com'),
('81234567890', 'Larissa Pinto', 'larissa.pinto@example.com'),
('91234567890', 'Felipe Azevedo', 'felipe.azevedo@example.com'),
('10123456789', 'Aline Carvalho', 'aline.carvalho@example.com'),
('11123456789', 'Eduardo Rocha', 'eduardo.rocha@example.com'),
('12123456789', 'Vanessa Melo', 'vanessa.melo@example.com'),
('13123456789', 'Rodrigo Teixeira', 'rodrigo.teixeira@example.com'),
('14123456789', 'Beatriz Nunes', 'beatriz.nunes@example.com'),
('15123456789', 'André Vieira', 'andre.vieira@example.com'),
('16123456789', 'Isabela Castro', 'isabela.castro@example.com'),
('17123456789', 'Bruno Mendes', 'bruno.mendes@example.com'),
('18123456789', 'Débora Silva', 'debora.silva@example.com'),
('19123456789', 'Fábio Santos', 'fabio.santos@example.com'),
('20123456789', 'Tatiana Souza', 'tatiana.souza@example.com');


INSERT INTO CONTRATO (valorEvento, qtdPessoa, idEvento, idCliente) VALUES
(4500, 100, 1, 1),
(12000, 200, 2, 2),
(8000, 150, 3, 3),
(5000, 120, 4, 4),
(3000, 80, 5, 5),
(15000, 250, 6, 6),
(7000, 130, 7, 7),
(20000, 300, 8, 8),
(10000, 180, 9, 9),
(2500, 70, 10, 10),
(3500, 90, 11, 11),
(18000, 270, 12, 12),
(22000, 290, 13, 13),
(4000, 110, 14, 14),
(6000, 140, 15, 15),
(9000, 160, 16, 16),
(50000, 300, 17, 17),
(11000, 190, 18, 18),
(13000, 210, 19, 19),
(14000, 220, 20, 20),
(16000, 230, 21, 21),
(17000, 240, 22, 22),
(19000, 260, 23, 23),
(21000, 280, 24, 24),
(23000, 290, 25, 25),
(25000, 300, 26, 26),
(27000, 300, 27, 27),
(29000, 300, 28, 28),
(31000, 300, 29, 29),
(33000, 300, 30, 30);
