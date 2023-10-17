package br.com.layscorrea.todolist.user;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Tipos de modificadores 
 * public
 * privete 
 * protected
 */
@RestController
@RequestMapping("/users")
public class UserController { /*o nome da classe tem que ser a mesma do nome do arquivo e classe tem que começar com letra maiuscula  */


/*
 * Body
 */
    @PostMapping("/")
    public void create(@RequestBody UserModel userModel) {
        System.out.println(userModel.getUsername());
        
    }
}