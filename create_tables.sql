

create table cliente(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100),
Apellidos char(200),
Dni char(9),
Direccion char(200),
Telefono char(13))

create table viajero(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100),
Apellidos char(200),
Dni char(9),
Direccion char(200),
Telefono char(13))

create table comercial(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100),
Apellidos char(200),
Dni char(9),
Direccion char(200),
Telefono char(13))

create table guia(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100),
Apellidos char(200),
Dni char(9),
Direccion char(200),
Telefono char(13))

create table responsable(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100),
Apellidos char(200),
Dni char(9),
Direccion char(200),
Telefono char(13))


create table pais(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100))


create table actividades(
Id Int NOT NULL IDENTITY(1,1) primary key,
Nombre char(100),
Precio decimal(5,2))

create table viaje(
Id Int NOT NULL IDENTITY(1,1) primary key,
Aforo integer,
Destino char(100),
Pais_id integer references pais(id),
Comercial_id integer references comercial(id),
Responsable_id integer references responsable(id),
Cliente_id integer references cliente(id),
Importe float,
Fecha date
)

create table viaje_actividad(
Id Int NOT NULL IDENTITY(1,1) primary key,
Actividad_id int references actividades(id),
Viaje_id int references viaje(id),
Guia_id int references guia(id),
Fecha date
)

create table viaje_viajero(
Id Int NOT NULL IDENTITY(1,1) primary key,
Viajero_id int references viajero(id),
Viaje_id int references viaje(id),

)