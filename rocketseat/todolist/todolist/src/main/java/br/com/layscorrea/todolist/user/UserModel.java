package br.com.layscorrea.todolist.user;

import java.time.LocalDateTime;
import java.util.UUID;

import org.hibernate.annotations.CreationTimestamp;


import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Data;//lombok: lib que facilita e deixa o código mais limpo

@Data // gera os getters e setters 
@Entity(name="tb_users") //cria entidade no banco de dados
public class UserModel {

    @Id // observar se a importação está correta (jakarta.persistence.Id)
    @GeneratedValue(generator = "UUID")// gera o id de forma automáticaSSS
    private UUID id; // gera chave primária com uma estrutura específica que aumenta a segurança
   

    private String username;
    private String name;
    private String password;
    
    @CreationTimestamp // guarda quando o usuário é criado 
    private LocalDateTime createdAt;
    
}
