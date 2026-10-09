package com.cines.Cine.controller;

import java.util.List;

import co.edu.cinematch.core.CineMatchBackend;
import co.edu.cinematch.core.model.Pelicula;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/peliculas")
public class PeliculaController {
    private final CineMatchBackend backend;
    public PeliculaController(CineMatchBackend backend) { this.backend = backend; }
    @GetMapping public List<Pelicula> listar() { return backend.peliculas.listar(); }
    @GetMapping("/{id}") public Pelicula consultar(@PathVariable String id) { return backend.peliculas.buscar(id); }
    @PostMapping @ResponseStatus(HttpStatus.CREATED) public Pelicula crear(@RequestBody Pelicula pelicula) { return backend.peliculas.crear(pelicula); }
    @PutMapping("/{id}") public Pelicula actualizar(@PathVariable String id, @RequestBody Pelicula pelicula) { return backend.peliculas.actualizar(id, pelicula); }
    @DeleteMapping("/{id}") @ResponseStatus(HttpStatus.NO_CONTENT) public void eliminar(@PathVariable String id) { backend.peliculas.eliminar(id); }
}
