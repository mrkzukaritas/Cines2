package com.cines.Cine.config;

import co.edu.cinematch.core.CineMatchBackend;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/** Connects the HTTP API to the independent CineMatch domain module. */
@Configuration
public class BackendCoreConfig {
    @Bean
    CineMatchBackend cineMatchBackend() {
        return new CineMatchBackend();
    }
}
