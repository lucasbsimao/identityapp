package br.com.benchmark.api;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value="/api")
public class RestAPI {
	
	@GetMapping(value="/user/{id}")
	public String getId(@PathVariable(name="id") String id) {
		return id;
	}
	
	@PostMapping(value="/user")
	public String postId() {
		return "";
	}
}
