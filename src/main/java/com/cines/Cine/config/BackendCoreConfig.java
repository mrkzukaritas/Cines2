package com.cines.Cine.config;

import co.edu.cinematch.core.CineMatchBackend;
import co.edu.cinematch.core.model.Rol;
import co.edu.cinematch.core.model.Usuario;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/** Connects the HTTP API to the independent CineMatch domain module. */
@Configuration
public class BackendCoreConfig {
    @Bean
    CineMatchBackend cineMatchBackend() {
        CineMatchBackend backend = new CineMatchBackend();
        backend.auth.registrar(new Usuario("Administrador", "admin@cinematch.com", "admin123", "3000000000", Rol.ADMINISTRADOR));
        return backend;
    }
}
